from google import genai
from google.genai import types
import PIL.Image

# 1. 클라이언트 설정 (최신 방식)
client = genai.Client(api_key="AIzaSyDXeWVtHt0Dw0WZeamAWq6VDstjpwBHlx4")

def extract_receipt_data(image_path):
    # 2. 이미지 로드
    img = PIL.Image.open(image_path)

    # 3. 분석 요청 (모델명을 gemini-2.0-flash로 변경)
    prompt = """
    이 영수증 이미지에서 다음 정보를 추출하여 JSON 형식으로 응답해줘.
    - use_date: 사용일시 (YYYY-MM-DD HH:mm:ss)
    - address: 사업자 주소
    - card_name: 결제 카드명
    - description: 사용 내역
    - amount: 총 금액 (숫자만)
    """

    response = client.models.generate_content(
        model='gemini-flash-latest',
        contents=[img, prompt]
    )
    
    return response.text

if __name__ == "__main__":
    try:
        # 폴더에 receipt.jpg 파일이 있어야 합니다!
        result = extract_receipt_data("receipt.jpg")
        print(result)
    except Exception as e:
        print(f"에러 발생: {e}")