import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

EVEE_SYSTEM_PROMPT = """
You are EVEE inside EvalCode.

You help students THINK.

Rules:
- Never provide full code.
- Never provide exact fixes.
- Maximum 4 sentences.
- Mention something from user's current code.
- Explain concept briefly.
- Ask a guiding question.
- Redirect if user asks for complete solution.

Return ONLY the hint.
"""


async def get_evee_hint(
    question: str,
    current_code: str,
    language: str,
    problem_statement: str | None,
):

    prompt = f"""
{EVEE_SYSTEM_PROMPT}

Language:
{language}

Problem:
{problem_statement or "(not provided)"}

Current Code:
{current_code}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    hint = response.text

    try:
        tokens = response.usage_metadata.total_token_count
    except:
        tokens = 0

    return hint, tokens