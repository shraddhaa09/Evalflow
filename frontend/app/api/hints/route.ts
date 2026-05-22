// app/api/hint/route.ts
import { NextRequest, NextResponse } from "next/server";

// Request schema
type HintRequest = {
  code: string;
  question?: string;
  problemId?: string;
};

// Response schema
type HintResponse =
  | {
      success: true;
      hint: string;
      level: number; // 1 = very high-level, 2 = more specific, 3 = almost solution
      reasoning?: string;
    }
  | {
      success: false;
      error: string;
    };

// Fallback hint templates (used if no real EVEE backend is connected)
const FALLBACK_HINTS_BY_KEYWORD: Record<string, string[]> = {
  binary: [
    "Think about how binary search halves the search space each iteration.",
    "When arr[mid] doesn't match the target, decide which half can be discarded.",
    "Update your boundaries so the new search space is only the relevant half.",
  ],
  search: [
    "Consider what condition tells you whether the target is to the left or right.",
    "Your loop should keep narrowing the range until it's empty or you find the target.",
  ],
  loop: [
    "Check your loop condition: when should the loop stop?",
    "Make sure your loop moves closer to termination on each iteration.",
  ],
  recursion: [
    "Identify the base case: when should the recursion stop?",
    "Ensure each recursive call works on a strictly smaller problem.",
  ],
  sort: [
    "Think about what order your data should be in for the algorithm to work.",
    "Consider how swapping elements affects the overall ordering.",
  ],
};

const DEFAULT_HINTS = [
  "Read your code line by line and identify where the logic might be breaking.",
  "What is the expected behavior at each step of your algorithm?",
  "Try to trace your code with a small example on paper.",
];

// Simple pattern-based hint selector (fallback)
function getFallbackHint(code: string, question?: string): { hint: string; level: number } {
  const text = `${code} ${question ?? ""}`.toLowerCase();

  for (const [keyword, hints] of Object.entries(FALLBACK_HINTS_BY_KEYWORD)) {
    if (text.includes(keyword)) {
      // Return a progressive hint based on some heuristic (here just random-ish via length)
      const index = Math.min(code.length % hints.length, hints.length - 1);
      return { hint: hints[index], level: 1 + (index % 2) };
    }
  }

  const index = Math.min(code.length % DEFAULT_HINTS.length, DEFAULT_HINTS.length - 1);
  return { hint: DEFAULT_HINTS[index], level: 1 };
}

export async function POST(request: NextRequest) {
  try {
    const body: HintRequest = await request.json();

    const { code, question, problemId } = body;

    // Basic validation
    if (!code || typeof code !== "string") {
      return NextResponse.json(
        {
          success: false,
          error: "Code is required and must be a string.",
        } as HintResponse,
        { status: 400 }
      );
    }

    const MAX_CODE_LENGTH = 30_000;
    if (code.length > MAX_CODE_LENGTH) {
      return NextResponse.json(
        {
          success: false,
          error: `Code exceeds maximum allowed length of ${MAX_CODE_LENGTH} characters.`,
        } as HintResponse,
        { status: 400 }
      );
    }

    if (question !== undefined && question !== null && typeof question !== "string") {
      return NextResponse.json(
        {
          success: false,
          error: "Question must be a string if provided.",
        } as HintResponse,
        { status: 400 }
      );
    }

    // In a real production system, you would:
    // 1. Call your EVEE hint engine (FastAPI, ML model, etc.)
    // 2. Send code, question, and problemId
    // 3. Receive a structured hint response
    //
    // Example (pseudo-code):
    // const eveeResponse = await fetch(`${EVEE_BASE_URL}/hint`, {
    //   method: "POST",
    //   headers: { "Content-Type": "application/json" },
    //   body: JSON.stringify({ code, question, problemId }),
    // });
    // const data = await eveeResponse.json();

    // For now, use fallback hints
    const { hint, level } = getFallbackHint(code, question);

    const response: HintResponse = {
      success: true,
      hint,
      level,
      reasoning:
        "This is a conceptual nudge based on your current code and question. Think through how it applies to your specific case.",
    };

    return NextResponse.json(response, { status: 200 });
  } catch (error) {
    console.error("[hint/api] Unexpected error:", error);

    return NextResponse.json(
      {
        success: false,
        error: "An unexpected error occurred while generating your hint.",
      },
      { status: 500 }
    );
  }
}

// Optional: health check
export async function GET() {
  return NextResponse.json(
    {
      service: "EvalCode EVEE Hint API",
      status: "ok",
      engine: "fallback (replace with EVEE backend in production)",
    },
    { status: 200 }
  );
}