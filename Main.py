import streamlit as st

def get_job_recommendations(mbti_type):
    """
    MBTI 유형에 따른 직업 추천을 반환하는 함수야!
    이 데이터는 예시라서, 나중에 더 풍부한 데이터로 채워 넣으면 좋을 거야. 😉
    """
    recommendations = {
        "ISTJ": ["회계사", "공무원", "관리자", "감사관", "데이터 분석가"],
        "ISFJ": ["간호사", "교사", "사회복지사", "사서", "행정 보조"],
        "INFJ": ["상담사", "작가", "심리학자", "교육자", "인사 담당자"],
        "INTJ": ["건축가", "연구원", "프로그래머", "전략 기획자", "과학자"],
        "ISTP": ["정비사", "엔지니어", "건축가", "조종사", "컴퓨터 기술자"],
        "ISFP": ["예술가", "음악가", "디자이너", "수의사", "자연과학자"],
        "INFP": ["작가", "심리학자", "편집자", "음악 치료사", "예술 치료사"],
        "INTP": ["과학자", "철학자", "교수", "IT 전문가", "연구 개발자"],
        "ESTP": ["영업 관리자", "경찰관", "소방관", "트레이너", "사업가"],
        "ESFP": ["연예인", "파티 플래너", "유치원 교사", "사회복지사", "여행 가이드"],
        "ENFP": ["크리에이티브 디렉터", "디자이너", "시나리오 작가", "상담사", "마케터"],
        "ENTP": ["사업가", "변호사", "발명가", "전략가", "컨설턴트"],
        "ESTJ": ["경영자", "감독관", "은행원", "세일즈 매니저", "군인"],
        "ESFJ": ["교사", "의사", "영업 사원", "사회 복지사", "상담가"],
        "ENFJ": ["리더", "코치", "강사", "인사 담당자", "사회 운동가"],
        "ENTJ": ["CEO", "변호사", "정치인", "경영 컨설턴트", "프로젝트 매니저"],
    }
    # 만약 해당 MBTI 유형에 대한 추천이 없으면 기본 메시지를 반환해.
    return recommendations.get(mbti_type, ["아직 추천 정보가 없는 MBTI 유형이거나, 새로운 도전을 즐기는 당신은 어떤 직업이든 잘 해낼 거예요!"])

# --- Streamlit 앱의 메인 부분 ---

# 웹 페이지의 제목을 설정해줘. 보기 좋게 이모지도 넣어봤어! 🎨
st.set_page_config(layout="wide") # 웹 앱 레이아웃을 좀 더 넓게 설정해 봤어!

st.title('🌱 MBTI 기반 맞춤 진로 탐색 앱 🌱')
st.markdown("""
<span style="font-size:1.1em;">이 앱은 당신의 MBTI 유형에 맞는 직업 분야를 탐색하는 데 도움을 주기 위해 만들어졌어요. 
자신의 유형을 선택하고, 흥미로운 직업들을 발견해보세요!</span>
""", unsafe_allow_html=True)

st.write("---") # 구분선을 넣어서 더 깔끔하게 보이게!

# 모든 MBTI 유형 리스트를 만들어!
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 사용자가 MBTI 유형을 선택할 수 있는 드롭다운 메뉴를 만들어!
selected_mbti = st.selectbox(
    '✨ 당신의 MBTI 유형을 선택해주세요:',
    mbti_types,
    index=None, # 처음에는 아무것도 선택되지 않도록
    placeholder="MBTI 유형을 선택하세요..." # 사용자에게 안내 메시지 표시
)

# MBTI 유형이 선택되었을 때만 추천 직업을 보여주도록 조건문을 넣어줘!
if selected_mbti:
    st.markdown(f"## 당신의 MBTI 유형은 **<span style='color: #4CAF50;'>{selected_mbti}</span>** 이군요! 정말 멋진 유형이에요! 😊", unsafe_allow_html=True)
    st.write("") # 한 칸 띄우기

    jobs = get_job_recommendations(selected_mbti)

    st.markdown("### <span style='color: #2196F3;'>💫 추천 직업군:</span>", unsafe_allow_html=True)
    # 추천 직업들을 보기 좋게 리스트로 보여줘.
    for job in jobs:
        st.markdown(f"- **{job}**")
    
    st.write("")
    st.info("이 추천은 일반적인 경향을 바탕으로 한 예시예요. 당신의 특별한 재능과 관심사에 따라 무궁무진한 가능성이 열려 있답니다! 당신의 꿈을 향해 나아가세요! 💖")
else:
    st.info("⬆️ 위에 드롭다운 메뉴에서 MBTI 유형을 선택해 주세요! 😊")

st.write("---")
st.markdown("##### 🚀 더 자세한 정보를 원한다면 언제든지 물어보세요!")

# 앱 하단에 간단한 설명이나 링크를 추가해도 좋을 것 같아!
# st.markdown("Made with ❤️ using Streamlit") # 이런 식으로 만들었다고 어필하는 것도 좋지!
