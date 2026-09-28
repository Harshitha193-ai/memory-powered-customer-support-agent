# 🧠 Memory-Powered Customer Support Agent

An AI-powered customer support agent that uses Hindsight memory to remember previous customer interactions and provide personalized support.

## 🚀 Features

- Remembers previous customer interactions
- Recalls relevant customer history
- Avoids asking customers to repeat information
- Provides personalized support responses
- Uses Groq LLM for response generation
- Uses Hindsight for long-term memory
- Streamlit-based user interface

## 🛠️ Technologies Used

- Python
- Streamlit
- Hindsight
- Groq
- Llama
- python-dotenv

## 🧠 How Memory Works

1. Customer sends a message.
2. The agent recalls relevant previous memories using Hindsight.
3. The recalled information is provided to the AI agent.
4. The agent generates a personalized response.
5. The new interaction is stored in Hindsight.
6. Future conversations can use the stored information.

## 🎯 Demo Flow

### Interaction 1

Customer:

"My Wi-Fi is disconnecting."

### Customer Teaches the Agent

Customer:

"I already restarted my router twice, but the problem continues."

The agent stores this information as memory.

### New Conversation

Customer:

"It is still disconnecting."

The agent recalls the previous customer information and provides a personalized troubleshooting response.

## 📁 Project Structure

```text
memory-powered-customer-support-agent/
│
├── app.py
├── agent.py
├── hindsight_service.py
├── test_hindsight.py
├── local_memory.json
├── .gitignore
└── README.md