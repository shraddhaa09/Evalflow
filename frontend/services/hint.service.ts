// services/hint.service.ts
import { api } from "./api";

export type HintRequest = {
  question: string;
  current_code: string;
  language: string;
  problem_statement?: string | null;
};

export type HintResponse = {
  hint: string;
  tokens_used?: number | null;
};

export const hintService = {
  getHint: async (payload: HintRequest): Promise<HintResponse> => {
    try {
      return await api.post<HintResponse>("/hint", payload);
    } catch (error) {
      throw new Error("Hint temporarily unavailable, try again");
    }
  },
};

// Convenience functions
export const getHint = (
  code: string,
  question = "Please help me progress on this solution.",
  problemStatement?: string | null
): Promise<HintResponse> => {
  return hintService.getHint({
    question,
    current_code: code,
    language: "python",
    problem_statement: problemStatement ?? null,
  });
};