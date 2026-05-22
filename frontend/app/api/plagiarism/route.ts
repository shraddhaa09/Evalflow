import { NextRequest, NextResponse } from "next/server";

type PlagiarismLevel = "low" | "medium" | "high";

type PlagiarismResponse = {
  success: boolean;
  score: number;
  level: PlagiarismLevel;
  label: string;
  signals: {
    repetitionScore: number;
    commentScore: number;
    structureScore: number;
    lengthScore: number;
  };
  summary: string;
};

function clamp(value: number, min: number, max: number) {
  return Math.min(Math.max(value, min), max);
}

function getLevel(score: number): {
  level: PlagiarismLevel;
  label: string;
} {
  if (score >= 70) {
    return { level: "high", label: "High review needed" };
  }

  if (score >= 40) {
    return { level: "medium", label: "Moderate review" };
  }

  return { level: "low", label: "Low concern" };
}

function analyzeCode(code: string) {
  const normalized = code.replace(/\r\n/g, "\n").trim();
  const lines = normalized.split("\n").map((line) => line.trim()).filter(Boolean);

  const totalLines = lines.length;
  const uniqueLines = new Set(lines).size;
  const duplicateRatio =
    totalLines > 0 ? (totalLines - uniqueLines) / totalLines : 0;

  const commentLines = lines.filter(
    (line) =>
      line.startsWith("#") ||
      line.startsWith("//") ||
      line.startsWith("/*") ||
      line.startsWith("*")
  ).length;

  const commentRatio = totalLines > 0 ? commentLines / totalLines : 0;

  const repeatedTokens = [
    "optimal",
    "efficient",
    "solution",
    "approach",
    "helper",
    "function",
    "initialize",
    "iterate",
  ];

  const lowerCode = normalized.toLowerCase();
  const matchedTokens = repeatedTokens.filter((token) =>
    lowerCode.includes(token)
  ).length;

  const repeatedPatternRatio =
    repeatedTokens.length > 0 ? matchedTokens / repeatedTokens.length : 0;

  const avgLineLength =
    totalLines > 0
      ? lines.reduce((sum, line) => sum + line.length, 0) / totalLines
      : 0;

  const repetitionScore = clamp(Math.round(duplicateRatio * 100), 0, 100);
  const commentScore = clamp(Math.round((1 - commentRatio) * 35), 0, 35);
  const structureScore = clamp(
    Math.round(repeatedPatternRatio * 45 + (avgLineLength > 60 ? 15 : 0)),
    0,
    100
  );
  const lengthScore = clamp(totalLines < 4 ? 20 : totalLines > 80 ? 30 : 10, 0, 30);

  const finalScore = clamp(
    Math.round(
      repetitionScore * 0.35 +
        commentScore * 0.15 +
        structureScore * 0.35 +
        lengthScore * 0.15
    ),
    0,
    100
  );

  return {
    score: finalScore,
    signals: {
      repetitionScore,
      commentScore,
      structureScore,
      lengthScore,
    },
  };
}

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const code = typeof body?.code === "string" ? body.code : "";
    const language =
      typeof body?.language === "string" ? body.language.toLowerCase() : "python";

    if (!code.trim()) {
      return NextResponse.json(
        {
          success: false,
          message: "Code is required.",
        },
        { status: 400 }
      );
    }

    if (code.length > 20000) {
      return NextResponse.json(
        {
          success: false,
          message: "Code exceeds the allowed size limit.",
        },
        { status: 400 }
      );
    }

    const supportedLanguages = ["python", "javascript", "java", "cpp"];
    if (!supportedLanguages.includes(language)) {
      return NextResponse.json(
        {
          success: false,
          message: "Unsupported language.",
        },
        { status: 400 }
      );
    }

    const analysis = analyzeCode(code);
    const levelData = getLevel(analysis.score);

    const response: PlagiarismResponse = {
      success: true,
      score: analysis.score,
      level: levelData.level,
      label: levelData.label,
      signals: analysis.signals,
      summary:
        analysis.score >= 70
          ? "The submission shows stronger structural regularity and should be reviewed carefully."
          : analysis.score >= 40
          ? "The submission appears mostly natural but includes some patterns worth a second look."
          : "The submission appears reasonably natural based on the current heuristic checks.",
    };

    return NextResponse.json(response, { status: 200 });
  } catch {
    return NextResponse.json(
      {
        success: false,
        message: "Failed to analyze submission.",
      },
      { status: 500 }
    );
  }
}