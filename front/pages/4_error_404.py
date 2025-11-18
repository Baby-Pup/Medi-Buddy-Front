import streamlit as st
import base64

st.set_page_config(layout="wide")

# Base64 이미지 인코딩 함수
def get_base64_image(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

lost_img = get_base64_image("assets/body_lost.png")

# ============================
# CSS
# ============================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

* {
    font-family: "Jua", sans-serif !important;
}

.stApp {
    background-color: #102A4C !important;
}

/* 전체 박스 */
.error-box {
    width: 90%;
    max-width: 1100px;
    margin: 60px auto;
    background: #F7F3EB;    /* 아이보리 */
    border: 20px solid #102A4C;
    border-radius: 20px;
    padding: 80px 40px;
    text-align: center;
}

/* 404 텍스트 */
.error-title {
    font-size: 120px;
    font-weight: 700;
    color: #000;
    margin-bottom: 10px;
}

/* 안내 문구 */
.error-text {
    margin-top: 20px;
    font-size: 32px;
    color: #000;
}

/* 버튼 느낌 텍스트 */
.error-btn {
    margin: 40px auto 0;
    padding: 14px 34px;
    background-color: #496A90;
    color: white;
    border-radius: 30px;
    font-size: 22px;
    width: fit-content;
}

</style>
""", unsafe_allow_html=True)

# ============================
# HTML 렌더링
# ============================
st.html(f"""
<div class="error-box">

    <div class="error-title">404</div>

    <!-- 길 잃은 메디버디 이미지 -->
    <div>
        <img src="data:image/png;base64,{lost_img}" width="500px">
    </div>

    <div class="error-text">Medi-Buddy가 길을 잃었어요</div>

    <div class="error-btn">관리자 오는중…</div>

</div>
""")
