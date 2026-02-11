import streamlit as st
from google import genai
import PIL.Image
import json

# 1. 설정 (본인의 API 키 입력)
client = genai.Client(api_key="AIzaSyDXeWVtHt0Dw0WZeamAWq6VDstjpwBHlx4")

# 페이지 제목 설정
st.set_page_config(page_title="AI 영수증 비서", layout="centered")
st.title("🧾 AI 영수증 데이터 추출기")
st.write("이미지를 업로드하면 AI가 자동으로 내용을 분석합니다.")

# 2. 파일 업로드 섹션
uploaded_file = st.file_uploader("영수증 이미지를 선택하세요 (jpg, png, jpeg)", type=['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    # 화면을 반으로 나누어 왼쪽은 이미지, 오른쪽은 결과 출력
    col1, col2 = st.columns(2)

    # 이미지 열기
    image = PIL.Image.open(uploaded_file)

    with col1:
        st.subheader("🖼️ 업로드된 이미지")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("🔍 분석 결과")
        if st.button("AI 분석 시작"):
            with st.spinner('AI가 영수증을 읽고 있습니다...'):
                try:
                    # 분석 요청
                    prompt = "이 영수증에서 사용일시(use_date), 주소(address), 카드명(card_name), 내역(description), 금액(amount, 숫자만)을 JSON으로 추출해줘."
                    response = client.models.generate_content(
                        model='gemini-1.5-flash',
                        contents=[image, prompt]
                    )
                    
                    # JSON 결과 파싱 및 출력
                    # 결과 텍스트에서 ```json ``` 부분을 제거하는 전처리
                    raw_json = response.text.replace('```json', '').replace('```', '').strip()
                    data = json.loads(raw_json)
                    
                    # 화면에 깔끔하게 표기
                    st.success("데이터 추출 성공!")
                    st.json(data)
                    
                    # 개별 항목 보기 좋게 출력
                    st.info(f"📅 날짜: {data.get('use_date')}")
                    st.info(f"💰 금액: {data.get('amount')}원")

                except Exception as e:
                    st.error(f"분석 중 에러가 발생했습니다: {e}")

