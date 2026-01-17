import subprocess

# Strong system prompt to FORCE good HTML output
SYSTEM_PROMPT = """
You are a senior front-end developer.

STRICT RULES:
- Generate modern, production-ready HTML ONLY
- DO NOT include explanations or markdown
- DO NOT use <style> tags
- DO NOT use inline CSS
- ALWAYS assume an external file called style.css exists
- ALWAYS include: <link rel="stylesheet" href="/static/style.css">
- Use semantic HTML (header, nav, main, section, footer)
- Use reusable class names
- Support complex layouts (e.g. Amazon, dashboards, SaaS, landing pages)
- Output ONLY valid HTML
"""

def generate_html(user_prompt: str) -> str:
    """
    Sends a prompt to Ollama and returns clean HTML output
    """

    full_prompt = SYSTEM_PROMPT + "\n\nUSER REQUEST:\n" + user_prompt

    try:
        result = subprocess.run(
            ["ollama", "run", "llama3"],
            input=full_prompt,
            text=True,
            capture_output=True,
            check=True
        )

        return clean_output(result.stdout)

    except subprocess.CalledProcessError as e:
        return f"<h1>Error generating HTML</h1><pre>{e}</pre>"


def clean_output(text: str) -> str:
    """
    Cleans unwanted terminal escape characters and code fences
    """

    # Remove common terminal control characters
    garbage = [
        "\x1b", "[?25l", "[?25h", "[?2026h", "[?2026l"
    ]

    for g in garbage:
        text = text.replace(g, "")

    # Remove markdown fences if model adds them
    text = text.replace("```html", "")
    text = text.replace("```", "")

    return text.strip()
