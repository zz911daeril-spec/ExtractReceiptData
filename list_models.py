from google import genai
import os

# Use the key from the user's file
client = genai.Client(api_key="AIzaSyDXeWVtHt0Dw0WZeamAWq6VDstjpwBHlx4")

print("Listing models:")
try:
    for m in client.models.list():
        print(f"- {m.name}")
except Exception as e:
    print(f"Error listing models: {e}")
