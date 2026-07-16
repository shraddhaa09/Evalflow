// services/plagiarism.service.ts
import { api } from "./api";

export type PlagiarismRequest = {
  code: string;
  language: string;
};

export type PlagiarismResponse = {
  ai_probability: number;
  label: string;
  confidence: number;
  signals: string[];
};

export const plagiarismService = {
  analyze: (payload: PlagiarismRequest): Promise<PlagiarismResponse> =>
    api.post<PlagiarismResponse>("/plagiarism", payload),
};

// Convenience functions
export const checkPlagiarism = (code: string): Promise<PlagiarismResponse> => {
  return plagiarismService.analyze({
    code,
    language: "python",
  });
};