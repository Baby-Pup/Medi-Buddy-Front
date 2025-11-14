import streamlit as st

st.set_page_config(layout="wide")

# -----------------------------
# CSS (배경, 말풍선, 캐릭터 스타일)
# -----------------------------
st.markdown("""
<style>
/* 전체 배경 */
.main {
    background-color: #102A4C;
}

/* 말풍선 스타일 */
.bubble {
    background: white;
    padding: 20px 30px;
    border-radius: 25px;
    font-size: 22px;
    width: fit-content;
    margin-top: 30px;
}

/* MediBuddy 캐릭터 원형(도형 기반으로 표현) */
.bot-face {
    width: 160px;
    height: 160px;
    background: white;
    border-radius: 40px;
    margin-top: 30px;
    position: relative;
}

.eye {
    width: 22px;
    height: 22px;
    background: #102A4C;
    border-radius: 50%;
    position: absolute;
    top: 45%;
}

.eye-left { left: 33%; }
.eye-right { right: 33%; }

.smile {
    width: 50px;
    height: 25px;
    border: 4px solid #102A4C;
    border-color: transparent transparent #102A4C transparent;
    border-radius: 0 0 40px 40px;
    position: absolute;
    top: 60%;
    left: 50%;
    transform: translateX(-50%);
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Layout
# -----------------------------
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

st.markdown("<div class='bot-face'>"
            "<div class='eye eye-left'></div>"
            "<div class='eye eye-right'></div>"
            "<div class='smile'></div>"
            "</div>", unsafe_allow_html=True)

st.markdown("<div class='bubble'>"
            "안녕하세요! 저는 <b>Medi-Buddy</b>예요 🩺<br>"
            "병원에서 길을 안내해드릴게요!"
            "</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# 버튼 → 지도 페이지로 이동
# -----------------------------
st.markdown("<br><br>", unsafe_allow_html=True)

if st.button("➡ 길 안내 시작하기", use_container_width=True):
    st.switch_page("pages/1_Map.py")
