from openai import OpenAI
from core.personality import SYSTEM_PROMPT
from config import OPENAI_API_KEY, MODEL_NAME

client = OpenAI(api_key=OPENAI_API_KEY)

# Simple short-term memory
conversation_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]


def think(user_input: str) -> str:
    global conversation_history

    # Add user message to memory
    conversation_history.append(
        {"role": "user", "content": user_input}
    )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=conversation_history,
        temperature=0.7
    )

    reply = response.choices[0].message.content.strip()

    # Add assistant reply to memory
    conversation_history.append(
        {"role": "assistant", "content": reply}
    )

    # Optional: limit memory size (VERY important)
    if len(conversation_history) > 12:
        conversation_history = conversation_history[:1] + \
            conversation_history[-10:]

    return reply
