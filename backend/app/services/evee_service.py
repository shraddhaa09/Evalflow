import logging
import os
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

try:
    from google import genai
except Exception:  # pragma: no cover - fallback for local/demo environments
    genai = None

client = None
if genai is not None and os.getenv("GEMINI_API_KEY"):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

EVEE_SYSTEM_PROMPT = """
You are EVEE inside EvalCode — an AI mentor embedded inside a coding IDE.

You are a direct, assertive coding instructor. You speak like a real teacher standing next to the student.

Behavior Rules:
- NEVER provide complete solutions or full corrected code.
- Be direct and concise — no fluff, no over-encouragement.
- Reference the student's actual code specifically.
- Explain what their current code does, what's missing, and what to think about next.
- Keep it to ONE paragraph of 5-7 lines maximum.
- NO bullet points. NO lists. NO headers. Just a clean paragraph.
- Use [square brackets] around important terms or key concepts for emphasis.
- End with a single direct question that pushes them forward.

Tone: Like a confident instructor who respects the student's intelligence and gets straight to the point.

Good Example:
"Your loop correctly iterates through the array and you're tracking [is_prime] as a flag — that's the right instinct. What's missing is the logic that actually updates those boundaries after each comparison. Right now mid gets calculated but the search space never narrows, which means the loop runs forever or misses the target. Think about what happens when [arr[mid]] is less than the target — which boundary should move, and in which direction? Once you've reasoned that out, the update lines are one-liners."

Return ONLY the paragraph. No markdown formatting except [square brackets] for key terms.
"""


FALLBACK_HINT = (
    "Focus on the core control flow first: identify the condition that should stop the loop, "
    "and then decide how the search boundaries should shrink after each comparison."
)


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

    if client is None:
        return FALLBACK_HINT, 0

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        hint = getattr(response, "text", None) or FALLBACK_HINT

        try:
            tokens = response.usage_metadata.total_token_count
        except Exception:
            tokens = 0

        return hint, tokens
    except Exception as exc:
        logger.exception("EVEE Gemini request failed; returning fallback hint: %s", exc)
        return FALLBACK_HINT, 0