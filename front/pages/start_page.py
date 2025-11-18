import streamlit as st
import base64

st.set_page_config(layout="wide")

# Base64 이미지 인코딩
def get_base64_image(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

body_img = get_base64_image("assets/body_stethoscope.png")
bubble_img = get_base64_image("assets/text_bubble.png")

# =============================
# CSS (100vh + 자동반응형 조정)
# =============================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

* { font-family: "Jua", sans-serif !important; }

.stApp { background-color: #102A4C !important; }

/* 🔥 전체 화면 1페이지 높이 고정 */
.page-wrapper {
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* 메인 콘텐츠 */
.main-box {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 60px;
}

/* 캐릭터 이미지 반응형 */
.character-img {
    width: 30vw;      /* 화면 너비의 30% */
    max-width: 350px; /* 너무 커지지 않게 제한 */
    height: auto;
}

/* 말풍선 박스 */
.bubble-wrap {
    position: relative;
    width: 45vw;
    max-width: 650px;
}

/* 말풍선 이미지 */
.bubble-img {
    width: 100%;
    height: auto;
}

/* 말풍선 안 텍스트 */
.bubble-text {
    position: absolute;
    top: 18%;
    left: 12%;
    width: 75%;
    font-size: 1.6vw;   /* 화면 기반 반응형 폰트 */
    max-font-size: 38px;
    line-height: 1.6;
    color: black;
}

/* 음성 안내 텍스트 */
.voice-text {
    margin-top: 20px;
    font-size: 1.2vw;
    color: #EAF4FF;
}

.voice-text b { color: #89D0FF; }

</style>
""", unsafe_allow_html=True)

# =============================
# HTML (100vh 안에 렌더)
# =============================
st.html(f"""
<div class="page-wrapper">

    <div class="main-box">

        <!-- 캐릭터 -->
        <div>
            <img src="data:image/png;base64,{body_img}" class="character-img">
        </div>

        <!-- 말풍선 -->
        <div>
            <div class="bubble-wrap">
                <img src="data:image/png;base64,{bubble_img}" class="bubble-img">

                <div class="bubble-text">
                    안녕하세요!<br>
                    저는 메디버디입니다.<br><br>
                    병원에서 길을 안내해드려요<br>
                    저에게 말을 걸어주세요
                </div>
            </div>

            <div class="voice-text">
                저는 <b>음성으로</b> 말해드릴 수 있어요!<br>
                “메디버디, 약에 대해 궁금한게 있어!”<br>
                “메디버디, 방사선실까지 안내해줘”
            </div>

        </div>

    </div>

</div>
""")
