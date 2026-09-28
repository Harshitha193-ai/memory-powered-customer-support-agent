import streamlit as st
from hindsight_service import store_memory, recall_memory
from agent import generate_response


st.title("🧠 Memory-Powered Customer Support Agent")

st.write(
    "An AI customer support agent that remembers previous customer interactions."
)


# Initialize conversation
if "conversation_active" not in st.session_state:
    st.session_state.conversation_active = True


# New Conversation button
if st.button("🆕 New Conversation"):

    st.session_state.conversation_active = True
    st.success(
        "New conversation started. Previous memories are still available."
    )


# Customer message
customer_message = st.text_area(
    "Customer message:",
    placeholder="Example: My Wi-Fi is not working..."
)


# Send button
if st.button("📨 Send") and customer_message:

    # 1. Recall previous customer information
    memories = recall_memory(customer_message)

    memory_text = "\n".join(memories)

    # 2. Generate personalized response
    response = generate_response(
        customer_message,
        memory_text
    )

    # 3. Store this conversation
    store_memory(
        f"Customer message: {customer_message}\n"
        f"Agent response: {response}"
    )

    # 4. Display response
    st.subheader("🤖 Support Agent")
    st.write(response)

    # 5. Display recalled memory
    st.subheader("🧠 Recalled Memory")

    if memories:
        for memory in memories:
            st.write("•", memory)
    else:
        st.info("No previous memory found. This is a new customer.")
