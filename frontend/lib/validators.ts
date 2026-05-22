import { appConfig } from "./config";

export function validateCode(code: string) {
  const trimmed = code.trim();

  if (!trimmed) {
    return {
      valid: false,
      message: "Code cannot be empty.",
    };
  }

  if (code.length > appConfig.maxCodeLength) {
    return {
      valid: false,
      message: `Code exceeds the ${appConfig.maxCodeLength} character limit.`,
    };
  }

  return {
    valid: true,
    message: "",
  };
}

export function validateHintRequest(count: number) {
  if (count >= appConfig.maxHintRequests) {
    return {
      valid: false,
      message: "You have reached the maximum number of hint requests for this session.",
    };
  }

  return {
    valid: true,
    message: "",
  };
}

export function validateLanguage(language: string) {
  const supported = ["python", "javascript", "cpp", "java"];

  if (!supported.includes(language)) {
    return {
      valid: false,
      message: "Unsupported language selected.",
    };
  }

  return {
    valid: true,
    message: "",
  };
}

export function validatePlagiarismScore(score: number) {
  if (Number.isNaN(score) || score < 0 || score > 100) {
    return {
      valid: false,
      message: "Plagiarism score must be between 0 and 100.",
    };
  }

  return {
    valid: true,
    message: "",
  };
}