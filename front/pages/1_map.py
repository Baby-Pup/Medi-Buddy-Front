import streamlit as st
import base64
import time
import requests

st.set_page_config(layout="wide")

# =========================================================
# Base64 이미지 로더
# =========================================================
def img64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

face_img = img64("assets/face_smile.png")
big_buddy = img64("assets/body_flag.png")
small_buddy = img64("assets/body_flag.png")
map_img = img64("assets/map_line.png")

# =========================================================
# 병원 지도 좌표 (%)
# =========================================================
map_points = {
    "X-ray실":  {"left": 24.9, "top": 13.9},
    "응급실":   {"left": 61.7, "top": 13.9},
    "화장실":   {"left": 90.2, "top": 26.7},
    "약국":     {"left": 19.3, "top": 47.2},
    "수납":     {"left": 49.7, "top": 48.7},
    "채혈실":   {"left": 65.7, "top": 69.6},
}

# =========================================================
# 🔥 직각 이동을 위한 Waypoints
# =========================================================
waypoints = {
    # 채혈실 → X-ray실
    ("채혈실", "X-ray실"): [
        {"left": 65.7, "top": 40},
        {"left": 24.9, "top": 40},
    ],

    # X-ray실 → 수납
    ("X-ray실", "수납"): [
        {"left": 24.9, "top": 30},
        {"left": 49.7, "top": 30},
    ],

    # 🔥 자연스러운 ㄱ자 이동 (두 번째 waypoint 제거)
    ("채혈실", "수납"): [
        {"left": 65.7, "top": 60},   # 아래로 이동만!
    ],

    ("수납", "채혈실"): [
        {"left": 49.7, "top": 60},
        {"left": 65.7, "top": 60},
    ],

    ("약국", "수납"): [
        {"left": 19.3, "top": 48.7},
        {"left": 49.7, "top": 48.7},
    ],
}

# =========================================================
# QR 기본 정보
# =========================================================
qr_default = {
    "name": "천현진",
    "date": "2025년 11월 28일",
    "route": ["채혈실", "X-ray실", "수납"]
}

# =========================================================
# 상태값 초기화
# =========================================================
session = st.session_state

if "route_original" not in session:
    session["route_original"] = qr_default["route"]

if "route_current" not in session:
    session["route_current"] = qr_default["route"]

if "bathroom_mode" not in session:
    session["bathroom_mode"] = False

if "face_detected" not in session:
    session["face_detected"] = False

if "anim_speed" not in session:
    session["anim_speed"] = 4


# =========================================================
# 🧪 테스트 패널
# =========================================================
st.sidebar.title("🧪 MediBuddy 테스트 패널")

if st.sidebar.button("🔵 기본 경로: 채혈실 → X-ray실 → 수납"):
    session["route_original"] = ["채혈실", "X-ray실", "수납"]
    session["route_current"] = session["route_original"]
    session["bathroom_mode"] = False
    session["face_detected"] = False
    st.rerun()

if st.sidebar.button("🚻 화장실 테스트 (음성 대체)"):
    session["bathroom_mode"] = True
    session["route_current"] = ["화장실"]
    session["face_detected"] = False
    st.rerun()

if st.sidebar.button("🙂 얼굴 인식 성공 트리거"):
    session["face_detected"] = True
    st.rerun()

# 이동 속도
speed_label = st.sidebar.radio(
    "⚡ 이동 속도 선택",
    ["매우 느림 (8s)", "느림 (6s)", "보통 (4s)", "빠름 (2s)"],
    index=2,
)

speed_map = {"매우 느림 (8s)": 8, "느림 (6s)": 6, "보통 (4s)": 4, "빠름 (2s)": 2}
session["anim_speed"] = speed_map[speed_label]


# =========================================================
# 📌 방별 위치 테스트
# =========================================================
st.sidebar.markdown("### 📌 방별 위치 테스트")
for room in map_points:
    if st.sidebar.button(f"📍 {room}"):
        session["route_current"] = [room]
        session["bathroom_mode"] = False
        session["face_detected"] = False
        st.rerun()


# =========================================================
# 🟦 대표 경로 테스트 세트
# =========================================================
st.sidebar.markdown("### 🟦 대표 경로 테스트 세트")

preset_routes = {
    "1) 채혈실 → X-ray실 → 수납": ["채혈실", "X-ray실", "수납"],
    "2) X-ray실 → 수납 → 약국": ["X-ray실", "수납", "약국"],
    "3) 약국 → 수납 → 채혈실": ["약국", "수납", "채혈실"],
    "4) 응급실 → X-ray실 → 수납": ["응급실", "X-ray실", "수납"],
    "5) 응급실 → 수납 → 약국": ["응급실", "수납", "약국"],
    "6) 수납 → 약국": ["수납", "약국"],
    "7) 약국 → 수납": ["약국", "수납"],
    "8) 채혈실 → 수납": ["채혈실", "수납"],
    "9) X-ray실 → 응급실 → 수납": ["X-ray실", "응급실", "수납"],
    "10) 채혈실 → 응급실": ["채혈실", "응급실"],
}

for label, route_list in preset_routes.items():
    if st.sidebar.button(label):
        session["route_original"] = route_list
        session["route_current"] = route_list
        session["bathroom_mode"] = False
        session["face_detected"] = False
        st.rerun()


# =========================================================
# 🔥 FastAPI 얼굴 인식 폴링 (옵션)
# =========================================================
FASTAPI_URL = "http://127.0.0.1:8000/face-status"

try:
    res = requests.get(FASTAPI_URL, timeout=0.2)
    if res.json().get("face_detected"):
        session["face_detected"] = True
except:
    pass


# =========================================================
# 얼굴인식 → 화장실 종료 → 원래 경로로 복귀
# =========================================================
if session["bathroom_mode"] and session["face_detected"]:
    session["bathroom_mode"] = False
    session["route_current"] = session["route_original"]
    session["face_detected"] = False
    st.rerun()


# =========================================================
# 현재 경로
# =========================================================
route = session["route_current"]


# =========================================================
# 🔥 애니메이션 keyframes 생성
# =========================================================
if session["bathroom_mode"]:
    # 화장실 bounce
    pos = map_points["화장실"]

    keyframes = f"""
    @keyframes buddyBounce {{
      0%   {{ top: {pos['top'] - 2}%; left: {pos['left']}%; }}
      50%  {{ top: {pos['top'] + 2}%; left: {pos['left']}%; }}
      100% {{ top: {pos['top'] - 2}%; left: {pos['left']}%; }}
    }}
    """

    animation_css = "animation: buddyBounce 1s infinite ease-in-out;"

else:
    # route + waypoints 합친 전체 이동 경로
    full_path = []

    for i in range(len(route) - 1):
        start = route[i]
        end = route[i + 1]

        full_path.append(map_points[start])

        if (start, end) in waypoints:
            full_path.extend(waypoints[(start, end)])

        full_path.append(map_points[end])

    if len(full_path) == 0:
        full_path = [map_points[route[0]]]

    step = 100 / (len(full_path) - 1) if len(full_path) > 1 else 0

    keyframes = "@keyframes moveBuddy {\n"
    for idx, p in enumerate(full_path):
        percent = round(step * idx, 2)
        keyframes += f"  {percent}% {{ top: {p['top']}%; left: {p['left']}%; }}\n"
    keyframes += "}\n"

    animation_css = f"animation: moveBuddy {session['anim_speed']}s infinite alternate ease-in-out;"


# =========================================================
# CSS 주입
# =========================================================
st.markdown(
    f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

.stApp {{
    background-color: #f5f5f5 !important;
    font-family: "Jua", sans-serif;
}}

{keyframes}

.small-buddy {{
    width: 100px;
    position: absolute;
    transform: translate(-50%, -50%);
    {animation_css}
}}
</style>
""",
    unsafe_allow_html=True,
)

# =========================================================
# 텍스트 박스
# =========================================================
order_html = "".join(
    [f"{i+1}. {r}<br>" for i, r in enumerate(route)]
)

title_text = (
    f"{qr_default['name']}님 화장실 대기 중"
    if session["bathroom_mode"]
    else f"{qr_default['name']}님 진료 순서표"
)

# =========================================================
# 메인 UI
# =========================================================
st.html(
    f"""
<div style="display:flex; justify-content:center; margin-top:40px;">
  <div style="width:92%; max-width:1400px; background:#0E2C55; padding:60px; border-radius:25px;">

    <div style="background:#F7F3EB; padding:60px 50px; border-radius:18px;
                display:grid; grid-template-columns:45% 55%; gap:10px;">

      <!-- 왼쪽 -->
      <div style="position:relative;">
        <img src="data:image/png;base64,{face_img}" style="width:140px;">
        <div style="font-size:40px; margin-top:10px;">개인 진료 MAP</div>

        <div style="font-size:24px; margin:20px 0 25px;">
          {qr_default['date']}<br>
          {title_text}
        </div>

        <div style="font-size:24px; line-height:1.8;">
          {order_html}
        </div>

        <img src="data:image/png;base64,{big_buddy}"
             style="width:180px; position:absolute; bottom:0; left:0;">
      </div>

      <!-- 오른쪽 지도 -->
      <div style="position:relative;">
        <img src="data:image/png;base64,{map_img}" style="width:100%; border-radius:12px;">
        <img src="data:image/png;base64,{small_buddy}" class="small-buddy">
      </div>

    </div>

  </div>
</div>
"""
)
