import pandas as pd
import subprocess

# Simple in-memory storage of transaction descriptions
# We keep this intentionally simple for now
transactions_memory = []


def process_csv(file):
    """
    Reads a CSV file and asks the local LLM
    to describe spending behavior patterns.
    """
    df = pd.read_csv(file)

    texts = []

    # Convert transactions into natural language
    for _, row in df.iterrows():
        text = f"Spent {row['amount']} on {row['description']} on {row['date']}"
        texts.append(text)
        transactions_memory.append(text)

    prompt = f"""
You are an empathetic financial behavior analyst.

These are spending statements written in natural language:
{texts}

Describe any spending behavior patterns you notice.
Do not judge. Do not give advice. Just explain patterns.
"""

    return call_llm(prompt)


def chat_with_ai(user_message):
    """
    Handles user questions about their spending behavior.
    """
    prompt = f"""
You are an empathetic financial behavior analyst.

User question:
{user_message}

Spending history:
{transactions_memory}

Respond thoughtfully and explain any relevant patterns.
"""

    return call_llm(prompt)


def call_llm(prompt):
    """
    Sends a prompt to the local Ollama model and returns the response.
    """
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout.strip()
