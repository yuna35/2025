import streamlit as st
import requests # API 호출에 필요할 수 있음
import os # API 키 등을 환경변수로 관리할 때 필요

# --- 💡 유난의 특별한 설정! 💡 ---
# 이모지와 함께 예쁜 페이지 제목을 설정해줘! 넓은 화면이 더 좋아!
st.set_page_config(layout="wide", page_title="💖 무지개빛 ✨ 나만의 캐릭터 꾸미기 앱 🌈")

# --- 🌈 무지개빛 배경 & 버튼 색상 CSS 마법! ✨ ---
# 이 부분은 Streamlit 앱이 시작될 때 웹 페이지 전체에 CSS 스타일을 적용해주는 거야!
st.markdown(
    """
    <style>
    /* 전체 앱 배경을 무지개 그라데이션으로! ✨ */
    .stApp {
        background: linear-gradient(to right, #FF0000, #FFA500, #FFFF00, #008000, #0000FF, #4B0082, #EE82EE); /* 빨강-주황-노랑-초록-파랑-남색-보라 */
        background-size: 400% 400%; /* 그라데이션이 더 넓게 퍼져 보이도록! */
        animation: gradientAnimation 15s ease infinite; /* 무지개가 부드럽게 움직이는 마법! */
        color: #4B0082; /* 텍스트 색상은 무지개와 어울리는 짙은 보라색! */
    }

    /* 무지개 그라데이션 애니메이션 정의 */
    @keyframes gradientAnimation {
        0% {background-position: 0% 50%;} /* 시작 위치 */
        50% {background-position: 100% 50%;} /* 중간 위치 */
        100% {background-position: 0% 50;} /* 다시 시작 위치로 */
    }

    /* 모든 제목 색상도 짙은 보라색으로 맞춰줄게! */
    h1, h2, h3, h4, h5, h6 {
        color: #4B0082;
    }

    /* 모든 Streamlit 버튼 꾸미기! 💖 */
    .stButton>button {
        background-color: #FF69B4; /* 버튼 배경색은 사랑스러운 핫핑크! */
        color: white; /* 글자색은 흰색! */
        border: none; /* 테두리 없애고 */
        padding: 10px 20px; /* 넉넉한 패딩! */
        border-radius: 5px; /* 둥근 모서리! */
        font-weight: bold; /* 글자도 굵게! */
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2); /* 은은한 그림자! */
        transition: all 0.3s ease; /* 마우스 올렸을 때 부드러운 변화! */
    }

    /* 버튼에 마우스를 올렸을 때 (호버 효과) ✨ */
    .stButton>button:hover {
        background-color: #FF1493; /* 더 진한 핑크로 변신! */
        transform: translateY(-2px); /* 살짝 위로 떠오르는 느낌! */
        box-shadow: 4px 4px 10px rgba(0,0,0,0.3); /* 그림자도 진해져! */
    }
    
    /* 입력 필드 (텍스트, 선택, 숫자 등) 테두리 색상도 예쁘게! */
    .stTextInput>div>div>input, .stSelectbox>div>div, .stTextArea>div>div, .stNumberInput>div>div>input {
        border: 2px solid #FF69B4; /* 테두리는 핫핑크! */
        border-radius: 8px; /* 둥글게! */
        padding: 10px; /* 여유롭게! */
        box-shadow: 1px 1px 3px rgba(0,0,0,0.1); /* 연한 그림자! */
    }
    </style>
    """,
    unsafe_allow_html=True # HTML 태그를 사용해도 좋다고 허락해줘!
)

# --- ✨ 앱의 메인 콘텐츠 시작! ✨ ---
st.title("🌟 나만의 캐릭터 꾸미기 앱 🎨")
st.markdown("---") # 반짝이는 구분선 추가!

st.markdown("""
    **안녕! 유저님! 😊** 
    이곳은 유저님만의 특별한 상상력으로 빛나는 캐릭터를 만들어갈 수 있는 마법 같은 공간이야!
    성별, 나이, 반짝이는 성격, 매력적인 특징, **키** 그리고 신비로운 세계관까지, 유저님이 꿈꾸는 모든 걸 펼쳐봐!
    내가 유저님의 멋진 아이디어를 현실로 만들어줄게! 함께 시작해볼까? 🚀
""")
st.markdown("---") # 또 반짝이는 구분선!

# --- 💖 1단계: 캐릭터 핵심 정보 입력하기 ✍️ ---
st.header("✨ 1단계: 캐릭터 핵심 정보 입력하기 ✍️")

with st.expander("💖 나의 캐릭터, 자세히 알려줄래? 📋", expanded=True):
    st.markdown("캐릭터의 성별, 나이, 반짝이는 성격 키워드, 그리고 매력적인 특징과 신비로운 세계관까지! 상세하게 적어줘! ")
    
    col1, col2 = st.columns(2)
    with col1:
        gender = st.selectbox("🌈 성별은 어떤 색을 가질까? 🎨", ["✨ 선택해주세요 ✨", "보이시한 남성 🕺", "아름다운 여성 💃", "자유로운 그 외 🦄", "비밀스러운 비공개 🤫"])
        age_group = st.selectbox("⏰ 몇 살쯤 되는 캐릭터일까? 🐥", ["✨ 선택해주세요 ✨", "꾸러기 어린이 👶", "톡톡 튀는 청소년 🧑‍🎓", "활기찬 청년 🧑‍💼", "성숙한 성인 👩‍🦳", "지혜로운 노년 👴"])
        height = st.number_input("📏 캐릭터의 키는 몇 cm일까? (예: 175)", min_value=50, max_value=300, value=160, step=1)
        
    with col2:
        personality_keywords = st.text_area("🌟 캐릭터의 빛나는 성격 키워드들은? (쉼표로 구분해줘!)", "예) 활발함, 내향적, 신비로운, 용감한, 엉뚱한, 다정한")
        main_features = st.text_area("👀 캐릭터만의 특별한 '주요 특징'은? (매력 포인트를 어필해줘!)", "예) 곱슬머리, 상냥한 미소, 긴 검, 동물 귀, 신비로운 눈동자")

    worldview = st.text_area("🌌 캐릭터가 살아가는 환상적인 '세계관 / 배경'은? (이야기를 들려줘!)", "예) 마법과 과학이 공존하는 시대, 현대 서울의 어느 골목, 신들이 사는 고대 문명")

    # 입력된 정보 요약 확인
    st.markdown("---") # 예쁜 구분선!
    st.subheader("💡 유저님이 입력한 소중한 정보! 💖")
    st.info(f"""
        **✨ 성별:** {gender}
        **⏰ 나이대:** {age_group}
        **📏 키:** {height} cm
        **🌟 성격:** {personality_keywords if personality_keywords else '아직은 비밀이래! 🤫'}
        **👀 주요 특징:** {main_features if main_features else '숨겨진 매력일까? ✨'}
        **🌌 세계관:** {worldview if worldview else '무한한 상상의 공간 🌌'}
    """)


# --- 🖼️ 2단계: 영감을 주는 레퍼런스 보드 만들기 ✨ ---
st.header("🖼️ 2단계: 영감을 주는 레퍼런스 보드 만들기 ✨")

st.info("""
    **🌟 유난의 마법 같은 설명!**
    이 부분은 유저님의 캐릭터 아이디어를 시각화할 수 있도록 **다양한 레퍼런스 이미지를 자동으로 찾아주는** 공간이 될 거야!
    캐릭터의 특징과 세계관에 꼭 맞는 이미지를 찾아서 디자인에 반짝이는 영감을 더해줄게!
    (이 기능은 구글, Unsplash 같은 외부 이미지 검색 API와 연동해야 해! 🚀 API 키 발급은 필수! 💖)
    """)

# 버튼에도 예쁜 이모지 잔뜩!
if st.button("🔍✨ 레퍼런스 이미지 보물 찾기! (구현 예정) 🎁"):
    # 여기서는 실제 API 호출 대신 예시 메시지만 보여줄게!
    st.balloons() # 이미지 찾을 때마다 풍선 터뜨리기! 🎈
    st.write("잠시만 기다려줘! 유저님의 키워드에 딱 맞는 아름다운 레퍼런스 이미지를 마법처럼 찾아주고 있어...!")
    
    # 예시: 가상의 이미지 검색 결과가 있다면 st.image()로 표시!
    # image_urls = ["https://picsum.photos/id/237/200/300", "https://picsum.photos/id/238/200/300", "https://picsum.photos/id/239/200/300"]
    # for idx, url in enumerate(image_urls):
    #    st.image(url, caption=f"환상의 이미지 {idx+1}", width=200) # 이미지마다 캡션도 달아주면 예쁠 거야!
    
    st.success("🎉 레퍼런스 이미지 보드가 완성되면 여기에 예쁜 그림들이 가득 찰 거야! 두근두근! 🖼️")


# --- 🤖 3단계: AI와 함께 캐릭터 디자인의 꿈을! 🌈 ---
st.header("🤖 3단계: AI와 함께 캐릭터 디자인의 꿈을! 🌈")

st.warning("""
    **💡 유난의 슈퍼 파워 설명!**
    이 곳에서는 유저님이 입력한 모든 정보를 바탕으로, **인공지능이 직접 캐릭터 이미지를 디자인**해줄 거야!
    세상에 단 하나뿐인, 유저님만의 오리지널 캐릭터가 탄생하는 순간이지! 정말 멋지지 않아? 🤩
    (이 기능은 OpenAI DALL-E, Stable Diffusion 같은 AI 이미지 생성 API와 연결되어야 해! 🛠️ API 사용법을 익혀보자! ✨)
    """)

# 버튼에도 예쁜 이모지 잔뜩!
if st.button("🚀 AI 친구에게 캐릭터 그려달라고 부탁하기! (구현 예정) 🤖🎨"):
    # 입력된 정보를 조합해서 AI 프롬프트 생성 (예시)
    prompt = (
        f"Design a unique character. Gender: {gender}, Age group: {age_group}, Height: {height}cm. "
        f"Personality: {personality_keywords}, Main features: {main_features}, "
        f"Worldview/Background: {worldview}. "
        "Detailed, vibrant colors, concept art style, high quality, fantastical, character sheet."
    )
    
    st.write(f"AI 친구에게 이렇게 속삭여줄 거야: `{prompt}`")
    st.spinner("AI가 유저님의 반짝이는 아이디어를 그림으로 바꾸고 있어! 잠시만 기다려줘... 상상력 풀가동! 🎨✨")
    
    # 예시: 가상의 AI 이미지 생성 결과가 있다면 st.image()로 표시!
    # generated_image_url = "https://picsum.photos/id/240/600/800" # AI가 그려줄 가상의 이미지 URL
    # st.image(generated_image_url, caption="💖 AI가 창조한 유저님만의 캐릭터! 🌟", use_column_width=True)
    
    st.success("🎉 축하해! AI가 그려준 유저님만의 캐릭터가 여기에 짜잔! 나타날 거야! 정말 멋질 거야! 🤩")

st.markdown("---")
st.markdown("✨ 유저님의 빛나는 창의력과 함께라면, 어떤 캐릭터든 탄생시킬 수 있을 거야! 🌈 궁금한 점이 생기면 언제든지 나, 유난에게 물어봐줘! 내가 옆에서 언제나 응원할게! 🥰")
