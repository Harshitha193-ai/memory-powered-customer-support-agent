import os
import json
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

HINDSIGHT_API_KEY = os.getenv("HINDSIGHT_API_KEY")
HINDSIGHT_BASE_URL = os.getenv(
    "HINDSIGHT_BASE_URL",
    "https://api.hindsight.vectorize.io"
)

BANK_ID = "customer-support-agent"

MEMORY_FILE = "local_memory.json"


def load_local_memory():
    """Load memories from local JSON file."""
    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_local_memory(memories):
    """Save memories to local JSON file."""
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memories, f, indent=2, ensure_ascii=False)


def get_client():
    return Hindsight(
        base_url=HINDSIGHT_BASE_URL,
        api_key=HINDSIGHT_API_KEY
    )


def store_memory(content):
    try:
        client = get_client()

        try:
            result = client.retain(
                bank_id=BANK_ID,
                content=content
            )
            return result

        finally:
            client.close()

    except Exception as e:
        print("Hindsight unavailable. Using local memory.")
        print("Reason:", e)

        memories = load_local_memory()

        memories.append({
            "text": content
        })

        save_local_memory(memories)

        return {
            "status": "local",
            "message": "Memory stored locally"
        }


def recall_memory(query):
    try:
        client = get_client()

        try:
            result = client.recall(
                bank_id=BANK_ID,
                query=query
            )

            return [memory.text for memory in result.results]

        finally:
            client.close()

    except Exception as e:
        print("Hindsight unavailable. Using local memory.")
        print("Reason:", e)

        memories = load_local_memory()

        query_words = query.lower().split()

        matching_memories = []

        for memory in memories:
            text = memory.get("text", "")
            text_lower = text.lower()

            if any(word in text_lower for word in query_words):
                matching_memories.append(text)

        if not matching_memories:
            matching_memories = [
                memory.get("text", "")
                for memory in memories[-5:]
            ]

        return matching_memories