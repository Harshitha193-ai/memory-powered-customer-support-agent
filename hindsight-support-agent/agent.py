
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY is missing. Please add it to your .env file."
    )

client = Groq(api_key=GROQ_API_KEY)


def generate_response(customer_message, memory_text):
    prompt = f"""
You are a helpful and professional customer support agent.

Use the previous customer memory when it is relevant.

Previous customer memory:
{memory_text}

Current customer message:
{customer_message}

Give a helpful, polite, clear, and concise customer support response.

Do not mention the internal memory system.
Do not mention Hindsight.
Do not mention that you are an AI unless necessary.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful, polite, and professional "
                    "customer support agent."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content

