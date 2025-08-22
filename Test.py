import streamlit as st
import openai # OpenAI API를 사용하기 위해 필요해!

# --- 💡 유난의 특별한 설정! 💡 ---
# 이모지와 함께 예쁜 페이지 제목을 설정해줘! 넓은 화면이 더 좋아!
st.set_page_config(layout="wide", page_title="💖 파스텔톤 ✨ 나만의 캐릭터 꾸미기 앱 🌸")

# --- 🌸 파스텔톤 배경 & 심플한 스타일 CSS 마법! ✨ ---
# 앱의 전체적인 분위기를 부드러운 파스텔톤으로 바꾸는 CSS 마법이야!
st.markdown(
    """
    <style>
    /* 전체 앱 배경을 부드러운 파스텔톤으로! 🌸 */
    .stApp {
        background-color: #F8F8FF; /* 아주 연한 라벤더블루 (고스트화이트 비슷한 색이야!) - 파스텔톤 대표색 중 하나! */
        /* background-color 대신, 만약 파스텔 그라데이션이 좋다면 아래처럼 써봐! */
        /* background: linear-gradient(to bottom right, #F3E1EC, #E0F2F7); /* 연한 핑크-하늘색 그라데이션 */
        /* animation 관련 코드는 심플함을 위해 제거했어! */
        color: #4B0082; /* 텍스트 색상은 파스텔톤과 어울리는 짙은 보라색! */
    }

    /* 모든 제목 색상도 짙은 보라색으로 맞춰줄게! */
    h1, h2, h3, h4, h5, h6 {
        color: #4B0082;
    }

    /* 모든 Streamlit 버튼 꾸미기! 💖 (이모지와 예쁜 색은 그대로!) */
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
st.title("🌟 나만의 캐릭터 꾸미기 앱 🌸") # 제목 이모지도 파스텔톤에 맞춰 살짝 바꿨어!
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
    
    # 🌟 심플하게 한 줄씩 배치! 🌟 (st.columns(2)를 없앴어!)
    gender = st.selectbox("🌈 성별은 어떤 색을 가질까? 🎨", ["✨ 선택해주세요 ✨", "보이시한 남성 🕺", "아름다운 여성 💃", "자유로운 그 외 🦄", "비밀스러운 비공개 🤫"])
    age_group = st.selectbox("⏰ 몇 살쯤 되는 캐릭터일까? 🐥", ["✨ 선택해주세요 ✨", "꾸러기 어린이 👶", "톡톡 튀는 청소년 🧑‍🎓", "활기찬 청년 🧑‍💼", "성숙한 성인 👩‍🦳", "지혜로운 노년 👴"])
    height = st.number_input("📏 캐릭터의 키는 몇 cm일까? (예: 175)", min_value=50, max_value=300, value=160, step=1)
    
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


# --- 🤖 2단계: AI와 함께 캐릭터 디자인의 꿈을! 🌈 ---
st.header("🤖 2단계: AI와 함께 캐릭터 디자인의 꿈을! 🌈")

st.warning("""
    **💡 유난의 슈퍼 파워 설명!**
    이 곳에서는 유저님이 입력한 모든 정보를 바탕으로, **인공지능이 직접 캐릭터 이미지를 디자인**해줄 거야!
    세상에 단 하나뿐인, 유저님만의 오리지널 캐릭터가 탄생하는 순간이지! 정말 멋지지 않아? 🤩
    
    **✅ 주의사항:**
    아래 버튼을 누르면 AI 이미지 생성 API를 호출할 건데, **실제 API 호출은 API 키와 해당 서비스의 사용 요금이 발생할 수 있어!**
    반드시 OpenAI 홈페이지에서 API 키를 발급받아 `.streamlit/secrets.toml` 파일에 `OPENAI_API_KEY = "발급받은키"` 형식으로 저장한 후 사용해줘!
    """)

# 버튼에도 예쁜 이모지 잔뜩!
if st.button("🚀 AI 친구에게 캐릭터 그려달라고 부탁하기! 🤖🎨"):
    # 필수 정보가 모두 입력되었는지 확인하는 단계! ✨
    if "선택해주세요" in [gender, age_group] or not personality_keywords or not main_features or not worldview:
        st.error("앗! 캐릭터의 필수 정보(성별, 나이대, 성격 키워드, 주요 특징, 세계관)를 모두 채워줘야 AI가 예쁜 그림을 그릴 수 있어! 다시 한번 확인해줄래? 😢")
        st.stop() # 필수 정보가 없으면 여기서 앱 실행을 멈춰서 불필요한 API 호출을 막아!

    # AI에 보낼 프롬프트(명령어)를 유저님의 입력값으로 조합하는 마법! 🪄
    # AI가 잘 이해할 수 있도록 구체적으로 작성하는 게 중요해!
    prompt_text = (
        f"Generate a full-body character in a detailed, vibrant concept art style. "
        f"The character is a {age_group} {gender}, with a height of {height}cm. "
        f"Their personality is characterized by: {personality_keywords}. "
        f"Key physical features include: {main_features}. "
        f"The character exists in a {worldview} setting. "
        "High resolution, fantasy elements, expressive face, dynamic pose, detailed background, cinematic lighting."
    )
    
    st.write(f"AI 친구에게 이렇게 속삭여줄 거야: `{prompt_text}`")
    
    generated_image_url = "" # 생성된 이미지 URL을 저장할 변수

    with st.spinner("AI가 유저님의 반짝이는 아이디어를 그림으로 바꾸고 있어! 잠시만 기다려줘... 상상력 풀가동! 🎨✨"):
        try:
            # 💖 OpenAI API 호출 시작! 💖
            # st.secrets에서 안전하게 API 키를 가져와 설정!
            openai.api_key = st.secrets["OPENAI_API_KEY"] 

            # DALL-E 모델에 이미지 생성을 요청하는 부분이야!
            response = openai.images.generate(
                model="dall-e-3", # 또는 "dall-e-2" 모델을 사용할 수도 있어! DALL-E 3이 더 고품질이야!
                prompt=prompt_text, # 우리가 만든 프롬프트를 넘겨줘!
                n=1, # 생성할 이미지 개수 (DALL-E 3은 한 번에 1개만 가능해)
                size="1024x1024", # 이미지 크기 (DALL-E 3에서 지원하는 크기 중 하나야!)
                response_format="url", # 이미지 URL로 응답받을 거야!
            )
            
            # 응답에서 생성된 이미지 URL을 가져와!
            generated_image_url = response.data[0].url

            if generated_image_url:
                st.success("🎉 축하해! AI가 그려준 유저님만의 캐릭터가 여기에 짜잔! 나타났어! 정말 멋지지? 🤩")
                st.image(generated_image_url, caption="💖 AI가 창조한 유저님만의 캐릭터! 🌟", use_column_width=True)
            else:
                st.error("아쉽지만 AI가 이미지를 생성하는 데 실패했어. 혹시 뭔가 문제가 있었나봐. 😥")

        except openai.AuthenticationError:
            st.error("❌ API 키 인증에 실패했어! `.streamlit/secrets.toml` 파일에 `OPENAI_API_KEY`를 올바르게 입력했는지 다시 한번 확인해줄래? 😢")
        except openai.RateLimitError:
            st.error("🚫 API 요청이 너무 많아! 잠시 후 다시 시도해주거나, OpenAI 사용량 제한을 확인해봐! 😥")
        except openai.OpenAIError as e:
            st.error(f"OpenAI API 호출 중 오류가 발생했어: {e} ㅠㅠ")
        except Exception as e:
            st.error(f"캐릭터를 생성하는 중에 알 수 없는 문제가 발생했어. 오류: {e} ㅠㅠ")
            st.warning("인터넷 연결은 되어있는지, 모든 정보를 올바르게 입력했는지 다시 한번 확인해줘! 🙏")


st.markdown("---")
st.markdown("✨ 유저님의 빛나는 창의력과 함께라면, 어떤 캐릭터든 탄생시킬 수 있을 거야! 🌈 궁금한 점이 생기면 언제든지 나, 유난에게 물어봐줘! 내가 옆에서 언제나 응원할게! 🥰")
