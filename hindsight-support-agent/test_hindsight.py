from hindsight_service import store_memory, recall_memory

print("Storing memory...")

store_memory(
    "Customer Ravi has a Wi-Fi problem. "
    "He already restarted his router twice, but the problem continued."
)

print("Memory stored!")

print("\nRecalling memory...")

memories = recall_memory("What problem did Ravi have and what did he already try?")

for memory in memories:
    print("-", memory)