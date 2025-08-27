import streamlit as st

# 페이지 설정은 살짝 넓게 가는 게 보기에 편하더라! 🥰
st.set_page_config(layout="wide") 

# 웹앱의 제목을 예쁘게 달아줘 보자! 💖
st.title('🎨 성격 맞춤 색깔 추천기 ✨')

# 따뜻하게 앱을 소개하는 글도 잊지 말고!
st.markdown("""
안녕, **유난이**가 너의 성격에 딱 맞는 색깔을 찾아줄게! 💖
아래에서 너의 성격 유형을 골라봐. 어떤 색이 나올지 벌써부터 기대된다! 두근두근! 🎉
""")

# 성격에 따른 색깔 정보들을 딕셔너리로 만들어볼까? 🤩
# 여기서는 예시로 몇 가지 성격을 넣어봤어! 원한다면 더 추가할 수 있어!
personality_colors = {
    "활발함 🥳": {
        "code": "#FF6347", 
        "name": "토마토 레드", 
        "description": "에너지가 넘치고 밝은 너에게 찰떡궁합! 활기를 더해주고 시선을 사로잡을 거야."
    },
    "차분함 😌": {
        "code": "#6495ED", 
        "name": "콘플라워 블루", 
        "description": "조용하고 사색적인 분위기의 너에게 평온함을 선사하는 색이야. 안정감을 느낄 수 있을 거야."
    },
    "창의적 🎨": {
        "code": "#8A2BE2", 
        "name": "블루 바이올렛", 
        "description": "번뜩이는 아이디어와 독창적인 너의 개성을 표현하기에 아주 좋아! 신비롭고 영감을 주는 색이지."
    },
    "열정적 🔥": {
        "code": "#FF4500", 
        "name": "오렌지 레드", 
        "description": "무엇이든 뜨겁게 해내는 너의 열정을 잘 보여주는 강렬한 색이야. 불타는 에너지를 나타내지!"
    },
    "평온함 ✨": {
        "code": "#90EE90", 
        "name": "라이트 그린", 
        "description": "편안하고 안정적인 너의 성격과 잘 어울리는, 마음을 차분하게 해주는 색이야. 자연의 편안함을 선사해."
    },
    "친근함 🤗": {
        "code": "#FFD700", 
        "name": "골드", 
        "description": "모두에게 따뜻하고 친근하게 다가가는 너에게 딱이야! 포근하고 행복한 기운을 줘."
    },
}

# 드롭다운 메뉴에 표시될 성격 목록을 가져오자!
personalities = list(personality_colors.keys())

# 사용자에게 성격을 선택할 수 있는 selectbox를 만들어줘!
selected_personality = st.selectbox(
    '네 성격은 어떤 쪽에 더 가깝다고 생각해? (선택해 줘! 😊)',
    personalities,
    index=0 # 기본 선택은 첫 번째 항목으로!
)

# 만약 성격이 선택되었다면, 그에 맞는 색깔 정보를 보여주자!
if selected_personality:
    color_info = personality_colors[selected_personality]
    color_code = color_info["code"]
    color_name = color_info["name"]
    description = color_info["description"]

    # 결과가 더 돋보이게 구분선을 넣어주고!
    st.markdown(f"---")
    st.markdown(f"### 짜잔! {selected_personality}에 딱 맞는 너의 색깔은 바로... **'{color_name}'** 이야! 🎉")

    # 선택된 색깔을 시각적으로 보여주는 박스를 만들어줘! HTML/CSS를 살짝쿵 활용!
    st.markdown(
        f"""
        <div style="
            background-color:{color_code}; 
            padding: 25px; 
            border-radius: 12px; 
            text-align: center; 
            color: {'black' if color_code in ['#FFD700', '#90EE90'] else 'white'}; 
            font-weight: bold; 
            font-size: 26px; 
            margin-top: 25px;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
            ">
            {color_name} ({color_code})
        </div>
        """,
        unsafe_allow_html=True # HTML 코드를 안전하게 허용해주는 옵션!
    )
    
    # 색깔에 대한 설명을 아래에 예쁘게 달아주자!
    st.markdown(f"<p style='text-align: center; font-size: 18px; margin-top: 15px;'>{description}</p>", unsafe_allow_html=True)
    st.markdown(f"---")

# 마지막으로 따뜻한 메시지를 건네면서 마무리! 💌
st.markdown("""
어때? 이 색이 네 마음에 쏙 들었으면 좋겠다! 🌈 
혹시 더 추가하고 싶은 성격 유형이나 어울리는 색깔이 있다면 언제든지 유난이한테 말해 줘! 얼마든지 수정할 수 있거든! 😉
""")

# 이 코드를 사용하려면, 파이썬 파일로 저장하고 터미널에서 'streamlit run [파일이름].py' 로 실행하면 돼!
# 예시) streamlit run my_color_app.py
