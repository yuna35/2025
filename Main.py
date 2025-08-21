import streamlit as st

def get_job_recommendations(mbti_type):
    """
    MBTI 유형에 따른 ✨반짝반짝✨ 직업 추천을 반환하는 마법 같은 함수! 💫
    이 리스트는 당신의 잠재력을 활짝 열어줄 영감의 보물창고야! 💖
    """
    recommendations = {
        "ISTJ": ["📊 꼼꼼한 회계사", "🏛️ 든든한 공무원", "📝 체계적인 관리자", "🔎 정확한 감사관", "📈 명민한 데이터 분석가"],
        "ISFJ": ["👩‍⚕️ 다정한 간호사", "🍎 따뜻한 교사", "🤝 헌신적인 사회복지사", "📚 지적인 사서", "🗂️ 세심한 행정 보조"],
        "INFJ": ["🗣️ 깊이 있는 상담사", "✍️ 감성적인 작가", "🧠 통찰력 있는 심리학자", "👨‍🏫 영향력 있는 교육자", "👥 공정한 인사 담당자"],
        "INTJ": ["🏗️ 창의적인 건축가", "🔬 탐구적인 연구원", "💻 논리적인 프로그래머", "💡 혁신적인 전략 기획자", "🧪 예리한 과학자"],
        "ISTP": ["🛠️ 숙련된 정비사", "⚙️ 실용적인 엔지니어", "📏 정교한 건축가", "✈️ 용감한 조종사", "🖥️ 전문적인 컴퓨터 기술자"],
        "ISFP": ["🎨 감각적인 예술가", "🎶 섬세한 음악가", "👗 독창적인 디자이너", "🐾 생명을 소중히 하는 수의사", "🌳 자연을 사랑하는 과학자"],
        "INFP": ["📖 상상력 풍부한 작가", "💖 공감 능력 좋은 심리학자", "📝 아이디어 넘치는 편집자", "🎵 음악으로 치유하는 음악 치료사", "🎭 예술로 마음을 나누는 예술 치료사"],
        "INTP": ["🔭 호기심 많은 과학자", "🤔 깊은 사색을 즐기는 철학자", "🧑‍🎓 지식을 탐구하는 교수", "💾 첨단 기술의 IT 전문가", "💡 끊임없이 발전하는 연구 개발자"],
        "ESTP": ["🤝 열정적인 영업 관리자", "🚨 용감한 경찰관", "👨‍🚒 든든한 소방관", "💪 활력 넘치는 트레이너", "💼 도전적인 사업가"],
        "ESFP": ["🌟 무대 위의 연예인", "🎉 파티를 빛내는 파티 플래너", "🧸 아이들의 친구 유치원 교사", "🌈 밝은 사회복지사", "🗺️ 모험심 강한 여행 가이드"],
        "ENFP": ["🎨 상상력 폭발! 크리에이티브 디렉터", "✍️ 반짝이는 아이디어의 디자이너", "🎬 매력적인 시나리오 작가", "🗣️ 따뜻한 상담사", "📈 트렌드를 이끄는 마케터"],
        "ENTP": ["🚀 기발한 사업가", "⚖️ 날카로운 변호사", "💡 혁신적인 발명가", "🧠 탁월한 전략가", "🧑‍💼 유연한 컨설턴트"],
        "ESTJ": ["👩‍💼 명확한 경영자", "👮‍♂️ 엄격한 감독관", "💰 신뢰할 수 있는 은행원", "💼 목표 지향적인 세일즈 매니저", "🎖️ 강인한 군인"],
        "ESFJ": ["🧑‍🏫 친근한 교사", "🩺 인정 많은 의사", "📈 성공적인 영업 사원", "🫂 공감하는 사회 복지사", "🤝 마음을 보듬는 상담가"],
        "ENFJ": ["✨ 빛나는 리더", "🏅 영감을 주는 코치", "🧑‍🏫 지혜로운 강사", "🤝 포용력 있는 인사 담당자", "🌍 세상을 바꾸는 사회 운동가"],
        "ENTJ": ["👑 카리스마 넘치는 CEO", "🧑‍⚖️ 논리적인 변호사", "🏛️ 야망 있는 정치인", "📈 전략적인 경영 컨설턴트", "🗓️ 완벽주의자 프로젝트 매니저"],
    }
    # 혹시나 아직 정보가 없는 유형이라면, 이렇게 격려의 메시지를 줘! 💪
    return recommendations.get(mbti_type, ["🎉 당신은 특별하니까 어떤 길이든 개척할 수 있을 거예요! 어떤 직업이든 빛낼 당신의 재능을 응원합니다! ✨"])

# --- Streamlit 앱의 메인 부분 시작! ✨ ---

# 페이지 설정을 ✨화려하게✨ 시작해볼까? 
st.set_page_config(
    page_title="💖 당신의 MBTI 진로 탐색 가이드! 🚀", # 페이지 제목에 이모지 뿜뿜!
    layout="wide", # 넓은 레이아웃으로 시원하게!
    initial_sidebar_state="expanded" # 사이드바도 미리 열어두자!
)

# 커스텀 CSS로 ✨더욱 화려하게✨ 꾸며봐! (배경색, 폰트, 그림자 등)
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap');
    
    body {
        background-color: #f0f8ff; /* 연한 하늘색 배경 */
        font-family: 'Nanum Pen Script', cursive; /* 부드러운 폰트 */
    }
    .stApp {
        background-color: #f0f8ff; /* 앱 전체 배경색 */
        background-image: linear-gradient(to right, #e0ffff, #f0e6fa); /* 살짝 그라데이션 */
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    h1 {
        color: #ff69b4; /* 핑크색 제목 */
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2); /* 그림자 효과 */
        font-size: 3.5em !important;
        text-align: center;
        margin-bottom: 0.8em;
    }
    h2 {
        color: #8a2be2; /* 보라색 부제목 */
        font-size: 2.2em !important;
        text-align: center;
    }
    h3 {
        color: #00bfff; /* 하늘색 소제목 */
        font-size: 1.8em !important;
        border-bottom: 2px solid #00bfff;
        padding-bottom: 0.5em;
        margin-top: 2em;
    }
    .stSelectbox label {
        font-size: 1.5em !important;
        color: #ff4500; /* 오렌지색 라벨 */
        font-weight: bold;
    }
    .st-ea { /* Streamlit Info Box */
        background-color: #ffe0b2 !important; /* 연한 주황색 */
        border-left: 5px solid #ff9800 !important; /* 진한 주황색 테두리 */
        border-radius: 10px;
        padding: 15px;
    }
    .stMarkdown p {
        font-size: 1.2em;
        line-height: 1.6;
        color: #36454F; /* 어두운 회색 글씨 */
    }
    .result-text {
        color: #4CAF50; /* 초록색 결과 텍스트 */
        font-weight: bold;
        font-size: 1.8em;
        text-align: center;
        margin-top: 1.5em;
    }
    .job-item {
        font-size: 1.4em;
        color: #483D8B; /* 어두운 보라색 직업명 */
        margin-bottom: 0.5em;
        list-style-type: '🌟 '; /* 리스트 아이콘도 이모지로! */
    }
    .stSpinner > div {
        color: #ff1493 !important; /* 스피너 색상도 핑크로! */
    }
    .rainbow-text {
        background-image: linear-gradient(to right, violet, indigo, blue, green, yellow, orange, red);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }
    .bottom-info {
        font-size: 1.2em;
        color: #708090;
        text-align: center;
        margin-top: 3em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('💖 당신의 MBTI 진로 탐색 가이드! 🚀')
st.markdown("""
    <h2 class="rainbow-text">✨ MBTI로 찾는, 나에게 딱 맞는 꿈의 직업! ✨</h2>
    <p style='text-align: center; font-size: 1.5em; color: #5F9EA0;'>
        <br>
        🌟 당신의 고유한 매력을 발견하고, <br>
        🌈 가장 빛날 수 있는 진로를 함께 탐험해 봐요! <br>
        💫 한 번의 클릭으로 당신의 미래를 밝혀줄 거예요! <br>
    </p>
    <br>
""", unsafe_allow_html=True)

st.write("---") # 반짝이는 구분선 추가!

# 모든 MBTI 유형 리스트를 예쁘게 만들어!
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 사용자가 MBTI 유형을 선택할 수 있는 ✨마법의✨ 드롭다운 메뉴!
selected_mbti = st.selectbox(
    '✨ 당신의 빛나는 MBTI 유형을 선택해주세요:',
    mbti_types,
    index=None, # 처음에는 설렘 가득한 빈 상태로!
    placeholder="🔮 MBTI 유형을 선택하면 멋진 미래가 펼쳐집니다...", # 안내 메시지도 특별하게!
    key="mbti_selector"
)

st.write("") # 공간을 조금 더 여유롭게!

# MBTI 유형이 선택되었을 때만 ✨찬란한✨ 추천 직업을 보여줘!
if selected_mbti:
    st.markdown(f"<p class='result-text'>🎉 당신의 MBTI 유형은 <span style='color: #FF00FF; font-size:1.2em;'><b>{selected_mbti}</b></span> 이군요! 정말 환상적인 유형이에요! 👑</p>", unsafe_allow_html=True)
    st.write("") 

    # 로딩 스피너로 기대감을 높여봐! 🌀
    with st.spinner('💖 당신을 위한 직업을 신중하게 탐색 중... 잠시만 기다려 주세요! ✨'):
        import time
        time.sleep(2) # 마치 AI가 열심히 생각하는 것처럼 2초 정도 기다려줘!

    jobs = get_job_recommendations(selected_mbti)

    st.markdown("<h3>✨ 당신의 특별함을 빛낼 추천 직업군: ✨</h3>", unsafe_allow_html=True)
    # 추천 직업들을 보기 좋고 ✨예쁘게✨ 리스트로 보여줘.
    for job in jobs:
        st.markdown(f"<p class='job-item'>{job}</p>", unsafe_allow_html=True)
    
    st.write("")
    st.success("🌈 이 추천은 일반적인 경향을 바탕으로 한 영감의 시작일 뿐이에요! 당신의 무한한 재능과 열정이라면 어떤 분야든 눈부시게 성공할 수 있을 거예요. 당신의 꿈을 향해 멋지게 나아가세요! 💖")

else:
    st.info("⬆️ 위에 반짝이는 드롭다운 메뉴에서 MBTI 유형을 선택하면, 당신을 위한 ✨맞춤형 진로 추천✨이 나타날 거예요! 😊")

st.write("---") # 또 하나의 빛나는 구분선!
st.markdown("<p class='bottom-info'>🚀 이 앱은 당신의 빛나는 미래를 응원하기 위해 ❤️으로 만들었어요! 궁금한 점이 있다면 언제든지 문의해주세요! 🌟</p>", unsafe_allow_html=True)
