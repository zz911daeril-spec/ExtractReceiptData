from google import genai
import PIL.Image

client = genai.Client(api_key="AIzaSyDXeWVtHt0Dw0WZeamAWq6VDstjpwBHlx4")

models_to_test = [
    'gemini-2.0-flash-lite-001',
    'gemini-flash-latest',
    'gemini-2.0-flash'
]

img = PIL.Image.new('RGB', (100, 100))

for model_name in models_to_test:
    print(f"Testing {model_name}...")
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=[img, "Describe this image"]
        )
        print(f"SUCCESS: {model_name}")
        # print(response.text)
        break # Stop after first success to save quota
    except Exception as e:
        print(f"FAILED: {model_name} with error: {e}")
