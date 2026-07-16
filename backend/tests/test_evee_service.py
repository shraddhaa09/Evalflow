import asyncio
from unittest.mock import patch

from app.services import evee_service


def test_returns_fallback_hint_on_provider_exception():
    class FakeClient:
        class models:
            @staticmethod
            def generate_content(*args, **kwargs):
                raise RuntimeError("429 RESOURCE_EXHAUSTED")

    with patch.object(evee_service, "client", FakeClient()):
        hint, tokens = asyncio.run(
            evee_service.get_evee_hint(
                question="How do I fix this?",
                current_code="print('hello')",
                language="python",
                problem_statement="Write a function",
            )
        )

    assert hint == (
        "Focus on the core control flow first: identify the condition that should stop the loop, "
        "and then decide how the search boundaries should shrink after each comparison."
    )
    assert tokens == 0
