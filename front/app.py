import streamlit as st
import time

st.set_page_config(layout="wide")

# 세션 상태 초기화
if "intro_step" not in st.session_state:
    st.session_state.intro_step = 0
    st.session_state.start_time = time.time()

INTRO_DURATION = 1.3

elapsed = time.time() - st.session_state.start_time

# ---------- CSS + 애니메이션 ----------
ANIM_CSS = """
<style>
.face-box {
    background: #102A4C;
    width: 80%;
    margin: auto;
    margin-top: 50px;
    height: 400px;
    border-radius: 10px;
    position: relative;
}

/* 눈 */
.eye {
    width: 25px;
    height: 25px;
    background: #D8D8D8;
    border-radius: 50%;
    position: absolute;
    top: 45%;
    animation: blink 3s infinite;
}
.eye-left { left: 35%; }
.eye-right { right: 35%; }

/* 일자 입 */
.mouth-line {
    width: 40px;
    height: 3px;
    background: white;
    border-radius: 3px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translateX(-50%);
}

/* 미소 입 */
.mouth-smile {
    width: 40px;
    height: 20px;
    border: 3px solid white;
    border-color: transparent transparent white transparent;
    border-radius: 0 0 40px 40px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translateX(-50%);
}

/* 깜빡임 애니메이션 */
@keyframes blink {
    0% { transform: scaleY(1); }
    45% { transform: scaleY(1); }
    50% { transform: scaleY(0.1); }
    55% { transform: scaleY(1); }
    100% { transform: scaleY(1); }
}
</style>
"""
st.markdown(ANIM_CSS, unsafe_allow_html=True)

# ---------- 랜더링 ----------
if elapsed < INTRO_DURATION:
    st.markdown("""
        <div class="face-box">
            <div class="eye eye-left"></div>
            <div class="mouth-line"></div>
            <div class="eye eye-right"></div>
        </div>""",
        unsafe_allow_html=True)

elif elapsed < INTRO_DURATION * 2:
    st.markdown("""
        <div class="face-box">
            <div class="eye eye-left"></div>
            <div class="mouth-smile"></div>
            <div class="eye eye-right"></div>
        </div>""",
        unsafe_allow_html=True)

else:
    st.switch_page("pages/start_page.py")

# ---------- re-render ----------
time.sleep(0.12)
st.rerun()
