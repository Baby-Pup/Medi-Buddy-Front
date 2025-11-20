import streamlit as st
import base64

st.set_page_config(layout="wide")

# Base64 이미지 로더
def img64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

face_img = img64("assets/face_smile.png")
big_buddy = img64("assets/body_flag.png")    # 큰 캐릭터
small_buddy = img64("assets/body_flag.png")  # 지도 위 작은 캐릭터
map_img = img64("assets/map_line.png")

# -------------------------------------------------------
# CSS : 베이지색 전체가 "하나의 네모" + 애니메이션 적용
# -------------------------------------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
* { font-family: "Jua", sans-serif; }

.stApp {
    background-color: #f5f5f5 !important;
}

/* 전체 wrap */
.map-wrapper {
    width: 100%;
    margin: 40px auto;
    display: flex;
    justify-content: center;
}

/* 네이비 큰 박스 */
.map-box {
    width: 92%;
    max-width: 1400px;
    background: #0E2C55;
    padding: 60px;
    border-radius: 25px;
}

/* ⭐ 하나의 통합 베이지 박스 */
.inner-paper {
    background: #F7F3EB;
    width: 100%;
    padding: 60px 50px;
    border-radius: 18px;

    display: grid;
    grid-template-columns: 45% 55%;
    gap: 10px;
}

/* 왼쪽 정보 영역 */
.left-area {
    position: relative;
}

.left-face { width: 140px; }

.left-title { font-size: 40px; margin-top: 10px; }
.left-date { font-size: 24px; margin: 20px 0 25px; }
.order-list { font-size: 24px; line-height: 1.8; }

/* 왼쪽 아래 큰 메디버디 */
.big-buddy {
    width: 180px;
    position: absolute;
    bottom: 0;
    left: 0;
}

/* 오른쪽 지도 */
.right-area {
    position: relative;
}

.map-img {
    width: 100%;
    border-radius: 12px;
}

/* ⭐ 작은 메디버디 이동 애니메이션 (척추센터 → 수납) */
@keyframes moveBuddy {
    0%   { top: 38%; left: 36%; }   /* 척추센터 */
    100% { top: 53%; left: 56%; }   /* 수납 */
}

.small-buddy {
    width: 100px;
    position: absolute;
    animation: moveBuddy 2.4s infinite alternate ease-in-out;
    transform: translate(-50%, -50%);
}

</style>
""", unsafe_allow_html=True)


# -------------------------------------------------------
# HTML : 왼쪽 정보 + 오른쪽 지도 + 애니메이션
# -------------------------------------------------------
st.html(f"""
<div class="map-wrapper">
    <div class="map-box">

        <div class="inner-paper">

            <!-- 왼쪽 정보 -->
            <div class="left-area">
                <img src="data:image/png;base64,{face_img}" class="left-face">

                <div class="left-title">개인 진료 MAP</div>

                <div class="left-date">
                    2025년 11월 12일<br>
                    천연진님 진료 순서표
                </div>

                <div class="order-list">
                    1. 채혈실<br>
                    2. X-ray 실<br>
                    3. 척추센터<br>
                    4. 수납
                </div>

                <img src="data:image/png;base64,{big_buddy}" class="big-buddy">
            </div>

            <!-- 오른쪽 지도 -->
            <div class="right-area">
                <img src="data:image/png;base64,{map_img}" class="map-img">

                <img src="data:image/png;base64,{small_buddy}" class="small-buddy">
            </div>

        </div>

    </div>
</div>
""")
