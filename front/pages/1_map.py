import streamlit as st
import base64

st.set_page_config(layout="wide")

# Base64 이미지 함수
def img64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

face_img = img64("assets/face_smile.png")
flag_img = img64("assets/body_flag.png")
map_img  = img64("assets/map_line.png")


# =======================================
# CSS 추가 (dot walking + 기존 MAP 디자인)
# =======================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

* { font-family: "Jua", sans-serif; }

.stApp {
    background-color: #f5f5f5 !important;
}

/* 페이지 전체 */
.map-wrapper {
    width: 100%;
    margin: 40px auto;
    display: flex;
    justify-content: center;
}

/* 메인 박스 */
.map-box {
    width: 90%;
    max-width: 1200px;
    background: #0E2C55;
    padding: 40px 60px;
    border-radius: 20px;
    display: flex;
    gap: 40px;
    justify-content: center;
    align-items: stretch;
}

/* 왼쪽 패널 */
.left-panel {
    width: 38%;
    background: #F7F3EB;
    padding: 40px;
    border-radius: 15px;
}

.left-title { font-size: 34px; margin-bottom: 15px; }
.left-date { font-size: 22px; margin-bottom: 20px; }
.order-list { font-size: 22px; line-height: 1.8; margin-top: 20px; }

/* 오른쪽 지도 패널 */
.right-panel {
    width: 58%;
    background: #F7F3EB;
    padding: 20px;
    border-radius: 15px;
    position: relative;
}

/* 지도 */
.map-img {
    width: 100%;
    border-radius: 12px;
}

/* 깃발 아이콘 */
.flag-icon {
    position: absolute;
    width: 80px;
    height: auto;
    top: 57%;      /* 위치 조정 */
    left: 54%;
}

/* =====================================
   Dot Walking (움직이는 점)
   ===================================== */
.dot {
    position: absolute;
    width: 16px;
    height: 16px;
    background-color: #ff6f4f;
    border-radius: 50%;
    animation: moveDot 2s infinite linear;
}

/* ⭐ dot 이동 경로 (예시 좌표)  */
@keyframes moveDot {

    0%   { transform: translate(260px, 350px); }   /* 수납 시작점 */
    25%  { transform: translate(290px, 320px); }
    50%  { transform: translate(320px, 260px); }
    75%  { transform: translate(350px, 200px); }
    100% { transform: translate(380px, 150px); }   /* 채혈실 도착점 */
}

/*
⚠ NOTE:
위 좌표는 map_line.png 크기에 맞추어 "대충" 넣은 값이야.
너가 ‘수납과 채혈실의 정확한 위치 좌표’를 알려주면
딱 맞게 수정해줄게!!
*/

</style>
""", unsafe_allow_html=True)


# =======================================
# HTML
# =======================================
st.html(f"""
<div class="map-wrapper">

    <div class="map-box">

        <!-- 왼 패널 -->
        <div class="left-panel">

            <img src="data:image/png;base64,{face_img}" width="90px">

            <div class="left-title">개인 진료 MAP</div>
            <div class="left-date">2025년 11월 12일<br>천연진님 진료 순서표</div>

            <div class="order-list">
                1. 채혈실<br>
                2. X-ray 실<br>
                3. 척추센터<br>
                4. 수납
            </div>

        </div>

        <!-- 지도 패널 -->
        <div class="right-panel">

            <img src="data:image/png;base64,{map_img}" class="map-img">

            <!-- dot walking -->
            <div class="dot"></div>

            <!-- 위치 깃발 -->
            <img src="data:image/png;base64,{flag_img}" class="flag-icon">

        </div>

    </div>

</div>
""")

