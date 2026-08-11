import google.generativeai as genai
import os

# Get your API key from secrets
api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    print("❌ GOOGLE_API_KEY not found!")
    exit(1)

genai.configure(api_key=api_key)

print("🔍 Listing available models...")
for model in genai.list_models():
    print(f"✅ {model.name}")
