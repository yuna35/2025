import streamlit as st

# 페이지 설정은 언제나 넓게! 시원시원해야 좋잖아! 🥰
st.set_page_config(layout="wide") 

# 웹앱 제목은 반짝반짝 예쁘게! ✨
st.title('🎨 성격 테스트 & 색깔 추천기 🌟')

# 따뜻한 환영 메시지! 유난이가 있잖아! 💖
st.markdown("""
안녕, **유난이**가 너의 성격에 딱 맞는 색깔을 찾아줄게! 💖
아래 질문들에 솔직하게 답해보면, 너의 내면의 색깔이 짠! 하고 나타날 거야! 기대되지 않아? 두근두근! 🎉
""")

# 성격에 따른 색깔 정보들을 딕셔너리로! 예쁜 색들이 잔뜩이지? 🤩
# 여기서는 심리 테스트 결과와 매칭될 수 있도록 몇 가지 키워드를 성격 설명에 추가해봤어!
personality_colors = {
    "활발함 🥳": {
        "code": "#FF6347", 
        "name": "토마토 레드", 
        "description": "에너지가 넘치고 밝은 너에게 찰떡궁합! 활기를 더해주고 시선을 사로잡을 거야. **외향적이고 적극적인** 사람에게 잘 어울려."
    },
    "차분함 😌": {
        "code": "#6495ED", 
        "name": "콘플라워 블루", 
        "description": "조용하고 사색적인 분위기의 너에게 평온함을 선사하는 색이야. 안정감을 느낄 수 있을 거야. **내성적이고 사려 깊은** 사람에게 잘 어울려."
    },
    "창의적 🎨": {
        "code": "#8A2BE2", 
        "name": "블루 바이올렛", 
        "description": "번뜩이는 아이디어와 독창적인 너의 개성을 표현하기에 아주 좋아! 신비롭고 영감을 주는 색이지. **상상력이 풍부하고 개성 강한** 사람에게 딱이야!"
    },
    "열정적 🔥": {
        "code": "#FF4500", 
        "name": "오렌지 레드", 
        "description": "무엇이든 뜨겁게 해내는 너의 열정을 잘 보여주는 강렬한 색이야. 불타는 에너지를 나타내지! **진취적이고 목표 지향적인** 사람에게 추천해."
    },
    "평온함 ✨": {
        "code": "#90EE90", 
        "name": "라이트 그린", 
        "description": "편안하고 안정적인 너의 성격과 잘 어울리는, 마음을 차분하게 해주는 색이야. 자연의 편안함을 선사해. **조화롭고 여유로운** 사람에게 좋아."
    },
    "친근함 🤗": {
        "code": "#FFD700", 
        "name": "골드", 
        "description": "모두에게 따뜻하고 친근하게 다가가는 너에게 딱이야! 포근하고 행복한 기운을 줘. **사교적이고 배려심 깊은** 사람에게 잘 어울려."
    },
}

# 이제 심리 테스트 질문들을 만들어 볼까? 📝
# 각 답변에는 어떤 성격 키워드와 얼마나 연결되는지 점수를 부여할 거야!
# key: 질문, value: {options: 답변 목록, traits: 답변별 점수 부여}
quiz_questions = [
    {
        "question": "1. 주말에 주로 무엇을 하고 싶어?",
        "options": [
            "새로운 사람들과 시끌벅적한 모임! 🎉",
            "조용히 집에서 혼자만의 시간을 즐기기 📚",
            "친한 친구들과 맛집 탐방이나 나들이 🍰",
            "미래를 위한 자기계발이나 목표 달성 🚀"
        ],
        "traits": [ # 각 답변이 부여하는 성격 점수 (활발, 차분, 창의, 열정, 평온, 친근)
            {"활발함": 3, "친근함": 1},
            {"차분함": 3, "평온함": 1},
            {"친근함": 3, "활발함": 1},
            {"열정적": 3, "창의적": 1}
        ]
    },
    {
        "question": "2. 예상치 못한 문제가 생겼을 때, 너는 어떤 편이야?",
        "options": [
            "바로 해결책을 찾아 나서는 행동파! 💪",
            "침착하게 상황을 분석하고 계획을 세우는 전략가 🧐",
            "기존 틀에서 벗어나 독특한 아이디어를 내는 창조가 💡"
        ],
        "traits": [
            {"열정적": 3, "활발함": 1},
            {"차분함": 3, "평온함": 1},
            {"창의적": 3, "활발함": 1}
        ]
    },
    {
        "question": "3. 너의 옷장에는 어떤 색깔의 옷이 가장 많아?",
        "options": [
            "강렬하고 눈에 띄는 원색 계열 ❤️💙",
            "부드럽고 편안한 파스텔톤 💚💛",
            "개성 있고 독특한 패턴이나 조합의 옷 💜🧡"
        ],
        "traits": [
            {"활발함": 3, "열정적": 1},
            {"평온함": 3, "차분함": 1},
            {"창의적": 3, "친근함": 1}
        ]
    },
    {
        "question": "4. 친구들이 너를 어떤 사람이라고 많이 말해?",
        "options": [
            "분위기 메이커! 활기차고 에너지가 넘쳐! 😄",
            "고민을 잘 들어주는 차분하고 편안한 사람 🎧",
            "새로운 것을 시도하는 독특하고 아이디어가 넘치는 사람 🌟",
            "한번 시작하면 끝을 보는 끈기 있고 열정적인 사람 🔥"
        ],
        "traits": [
            {"활발함": 3, "친근함": 1},
            {"차분함": 3, "평온함": 1},
            {"창의적": 3, "열정적": 1},
            {"열정적": 3, "활발함": 1}
        ]
    },
]

# 성격별 점수를 저장할 딕셔너리를 초기화하자!
# 모든 점수를 0으로 시작하는 게 좋겠지?
trait_scores = {trait: 0 for trait in personality_colors.keys()}

# 각 질문을 화면에 보여주고 사용자 답변을 받자!
user_answers = []
for i, q in enumerate(quiz_questions):
    st.markdown(f"**{q['question']}**")
    # 라디오 버튼으로 답변을 선택하게 할 거야. 키를 고유하게 줘야 해!
    selected_option = st.radio(
        "", 
        q["options"], 
        key=f"q{i}", 
        index=None # 초기에는 아무것도 선택되지 않도록!
    )
    user_answers.append(selected_option)

# 모든 질문에 답변했는지 확인하는 버튼!
if st.button('결과 보기! 🎁'):
    if None in user_answers:
        st.warning("아직 모든 질문에 답하지 않았어! 모든 질문에 답해줘야 정확한 결과를 알 수 있답니다. 😉")
    else:
        # 모든 답변을 기반으로 성격 점수를 계산하자!
        for i, answer in enumerate(user_answers):
            q_idx = quiz_questions[i]["options"].index(answer) # 선택한 답변의 인덱스
            # 해당 답변이 부여하는 트레잇 점수를 누적!
            for trait, score in quiz_questions[i]["traits"][q_idx].items():
                trait_scores[trait] += score

        # 가장 높은 점수를 받은 성격 찾기!
        # 만약 동점이라면, 딕셔너리 순서상 먼저 나오는 성격이 선택될 거야.
        # 필요하다면 동점 처리 로직을 더 복잡하게 만들 수도 있어!
        recommended_personality = max(trait_scores, key=trait_scores.get)
        
        # 결과가 더 돋보이게 구분선을 넣어주고!
        st.markdown(f"---")
        st.markdown(f"### 🎉 두근두근! 너의 성격은... **{recommended_personality}** 에 가깝게 나왔어! 🎉")
        
        # 이제 이 성격에 맞는 색깔 정보를 가져오자!
        color_info = personality_colors[recommended_personality]
        color_code = color_info["code"]
        color_name = color_info["name"]
        description = color_info["description"]

        # 선택된 색깔을 시각적으로 보여주는 박스!
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
            unsafe_allow_html=True 
        )
        
        # 색깔에 대한 설명을 아래에 예쁘게 달아주자!
        st.markdown(f"<p style='text-align: center; font-size: 18px; margin-top: 15px;'>{description}</p>", unsafe_allow_html=True)
        st.markdown(f"---")

# 마지막으로 따뜻한 메시지를 건네면서 마무리! 💌
st.markdown("""
어때? 이 색이 네 마음에 쏙 들었으면 좋겠다! 🌈 
더 많은 질문을 추가하거나, 답변별 성격 점수 매칭을 정교하게 바꾸면 훨씬 더 정확한 결과를 얻을 수 있을 거야! 😉
""")

# 이 코드를 사용하려면, 파이썬 파일로 저장하고 터미널에서 'streamlit run [파일이름].py' 로 실행하면 돼!
# 예시) streamlit run my_color_quiz_app.py
