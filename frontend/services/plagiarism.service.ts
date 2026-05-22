// services/plagiarism.service.ts
import { api } from "./api";

export type PlagiarismRequest = {
  code: string;
  language: string;
};

export type PlagiarismResponse = {
  success: boolean;
  score: number;
  label: string;
  details?: {
    structuralRegularity: number;
    tokenDiversity: number;
    typingPattern: number;
  };
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