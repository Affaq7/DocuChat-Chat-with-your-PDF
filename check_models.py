from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

print("--- EMBEDDING MODELS ---")
for model in genai.list_models():
    if "embedContent" in model.supported_generation_methods:
        print(model.name)

print("\n--- CHAT MODELS ---")
for model in genai.list_models():
    if "generateContent" in model.supported_generation_methods:
        print(model.name)
