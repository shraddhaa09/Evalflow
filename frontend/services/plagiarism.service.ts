// services/plagiarism.service.ts
import { api } from "./api";

export type PlagiarismRequest = {
  code: string;
  language: string;
  assignment_id: string;
  typing_speed_wpm: number;
  idle_ratio: number;
  paste_ratio: number;
  tab_switches: number;
  suspicion_score: number;
};

export type PlagiarismResponse = {
  probability: number;
  label: string;
  highest_similarity_match?: string;
  features?: Record<string, number>;
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
    assignment_id: "assignment_001",
    typing_speed_wpm: 45.0,
    idle_ratio: 0.1,
    paste_ratio: 0.05,
    tab_switches: 2,
    suspicion_score: 0.1
  });
};