// app/api/execute/route.ts
import { NextRequest, NextResponse } from "next/server";

// Piston API endpoint
const PISTON_URL = "https://emkc.org/api/v2/piston";

// Request body schema
type ExecuteRequest = {
  code: string;
  language?: string;
  version?: string;
  stdin?: string;
};

// Response schema from Piston
type PistonRunResponse = {
  run: {
    output: string;
    stdout: string;
    stderr: string;
    signal: string | null;
    exit_code: number;
    time: string | null;
    memory: number | null;
  };
};

// Safe default language and version
const DEFAULT_LANGUAGE = "python";
const DEFAULT_VERSION = "3.10.0";

export async function POST(request: NextRequest) {
  try {
    const body: ExecuteRequest = await request.json();

    const { code, language = DEFAULT_LANGUAGE, version = DEFAULT_VERSION, stdin } = body;

    // Basic validation
    if (!code || typeof code !== "string") {
      return NextResponse.json(
        {
          success: false,
          error: "Code is required and must be a string.",
        },
        { status: 400 }
      );
    }

    // Limit code length for safety and cost
    const MAX_CODE_LENGTH = 50_000;
    if (code.length > MAX_CODE_LENGTH) {
      return NextResponse.json(
        {
          success: false,
          error: `Code exceeds maximum allowed length of ${MAX_CODE_LENGTH} characters.`,
        },
        { status: 400 }
      );
    }

    // Limit stdin length if provided
    if (stdin !== undefined && stdin !== null && typeof stdin !== "string") {
      return NextResponse.json(
        {
          success: false,
          error: "stdin must be a string if provided.",
        },
        { status: 400 }
      );
    }

    if (stdin && stdin.length > 5_000) {
      return NextResponse.json(
        {
          success: false,
          error: `stdin exceeds maximum allowed length of 5,000 characters.`,
        },
        { status: 400 }
      );
    }

    // Prepare payload for Piston
    const pistonPayload = {
      language,
      version,
      files: [
        {
          content: code,
          name: "main.py",
        },
      ],
      stdin: stdin || "",
      timeout: 5, // seconds
    };

    // Call Piston API
    const pistonResponse = await fetch(`${PISTON_URL}/run`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify(pistonPayload),
    });

    if (!pistonResponse.ok) {
      const errorText = await pistonResponse.text();
      return NextResponse.json(
        {
          success: false,
          error: "Failed to execute code on Piston.",
          details: errorText,
        },
        { status: pistonResponse.status }
      );
    }

    const pistonData: PistonRunResponse = await pistonResponse.json();

    const { output, stdout, stderr, signal, exit_code, time, memory } = pistonData.run;

    // Build response
    const response = {
      success: true,
      output: output || "",
      stdout: stdout || "",
      stderr: stderr || "",
      signal: signal || null,
      exitCode: exit_code,
      time: time ? parseFloat(time) : null,
      memory: memory,
    };

    return NextResponse.json(response, { status: 200 });
  } catch (error) {
    // Handle JSON parse errors or other unexpected errors
    console.error("[execute/api] Unexpected error:", error);

    return NextResponse.json(
      {
        success: false,
        error: "An unexpected error occurred while executing your code.",
      },
      { status: 500 }
    );
  }
}

// Optional: allow GET for health check or debugging
export async function GET() {
  return NextResponse.json(
    {
      service: "EvalCode Execute API",
      status: "ok",
      language: DEFAULT_LANGUAGE,
      version: DEFAULT_VERSION,
      engine: "Piston",
    },
    { status: 200 }
  );
}