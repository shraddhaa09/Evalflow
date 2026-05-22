export const APP_NAME = "EvalCode";

export const DEFAULT_LANGUAGE = "python";

export const DEFAULT_CODE = `def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        # update boundaries here
    return -1`;

export const DEFAULT_HINTS = [
  "Focus on what changes after the middle comparison. Which half can be safely ignored?",
  "If the target is smaller than arr[mid], move the right boundary. If it is larger, move the left boundary.",
  "Keep shrinking the search space until the target is found or the boundaries cross.",
] as const;

export const DEFAULT_TERMINAL_OUTPUT =
  "Ready.\nRun your code to inspect output, errors, timing, and memory.";

export const SUPPORTED_LANGUAGES = [
  { label: "Python", value: "python" },
  { label: "JavaScript", value: "javascript" },
  { label: "C++", value: "cpp" },
  { label: "Java", value: "java" },
] as const;

export const TERMINAL_STATUS = {
  IDLE: "idle",
  RUNNING: "running",
  SUCCESS: "success",
  ERROR: "error",
} as const;

export const PLAGIARISM_LABELS = {
  LOW: "Low concern",
  MEDIUM: "Moderate review",
  HIGH: "High review needed",
} as const;