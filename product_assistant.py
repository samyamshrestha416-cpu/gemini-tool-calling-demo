
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import json
from products import get_product_info,calculate_total_price

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = "You are a product assistant for GlobalJava Roasters. Always use the available tools to look up current product information and pricing. Do not rely on memory."

chat = client.chats.create(
    model="gemini-3.5-flash-lite",
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        tools=[get_product_info,calculate_total_price],
        temperature=0.2,
    ),
)

print("GlobalJava assistant. Type 'quit' to stop.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    if not user_input.strip():
        continue

    try:
        response = chat.send_message(user_input)
        print("Assistant:", response.text)
    except Exception as e:
        print("Something went wrong:", e)