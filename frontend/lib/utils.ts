export function cn(...classes: Array<string | false | null | undefined>) {
  return classes.filter(Boolean).join(" ");
}

export function clamp(value: number, min: number, max: number) {
  return Math.min(Math.max(value, min), max);
}

export function getPlagiarismLabel(score: number) {
  if (score >= 70) return "High review needed";
  if (score >= 40) return "Moderate review";
  return "Low concern";
}

export function formatExecutionMetrics(timeMs?: number, memoryKb?: number) {
  const timeText =
    typeof timeMs === "number" ? `${timeMs.toFixed(2)} ms` : "N/A";
  const memoryText =
    typeof memoryKb === "number" ? `${memoryKb.toFixed(2)} KB` : "N/A";

  return `Time: ${timeText} | Memory: ${memoryText}`;
}

export function normalizeLineEndings(value: string) {
  return value.replace(/\r\n/g, "\n");
}

export function countLines(value: string) {
  if (!value) return 0;
  return normalizeLineEndings(value).split("\n").length;
}

export function truncateText(value: string, maxLength: number) {
  if (value.length <= maxLength) return value;
  return `${value.slice(0, maxLength)}...`;
}

export function safeJsonParse<T>(value: string, fallback: T): T {
  try {
    return JSON.parse(value) as T;
  } catch {
    return fallback;
  }
}