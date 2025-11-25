# Medi-Buddy-Front


병원 내 길안내·약 정보 스캔·진료 안내를 제공하는  
**자연어 기반 길안내 로봇 “Medi-Buddy”의 Streamlit 프론트엔드**입니다.

본 리포지토리는 사용자와 로봇 사이의 UI를 담당하며,  
어르신·보호자 등 의료 취약 계층도 쉽게 사용할 수 있도록  
큰 글씨 · 단순한 UI · 캐릭터 기반 가시성에 중점을 두었습니다.

---

## 📁 프로젝트 구조

front/      
├── app.py # 시작 화면 (눈 깜빡 페이지)       
│         
├── assets/ # 모든 이미지 리소스 (버디 표정, 지도, 아이콘 등)    
│        
└── pages/    
├── 1_map.py # 병원 지도와 길안내 페이지              
│       
├── 2-1_drug_ocr.py # 약 OCR 1단계 (약 정보를 쉽게 설명해드릴까요?)       
├── 2-2_drug_ocr.py # 약 OCR 2단계 (촬영 준비 요청 화면)       
├── 2-3_drug_ocr.py # 약 OCR 3단계 (카메라로 인식)       
├── 2-4_drug_ocr.py # 약 OCR 4단계 (약 이름 결과 출력)       
├── 2-5_drug_ocr.py # 약 OCR 5단계 (요약 결과 출력)       
│       
├── 3-1_follow_stage.py # 건강검진 길 안내를 동행해 드릴까요?       
├── 3-2_follow_stage.py # 카메라로 문진표 qr인식       
│       
├── 4_error_404.py # 비정상 루트 진입 시 표시되는 에러 페이지       
├── 5_loading.py # 로딩 중 애니메이션/대기 페이지       
├── 6_rescan.py # OCR 재스캔 안내 페이지       
├── 7_null.py # 정제가 알지 못하는 정보에!요       
│       
└── start_page.py # 첫 화면       





## ▶ 실행 방법

### 1) 설치
pip install streamlit
pip install opencv-python # 
pip install requests # 


### 2) 실행
streamlit run app.py

