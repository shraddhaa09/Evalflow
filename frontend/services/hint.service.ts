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
  getHint: (payload: HintRequest): Promise<HintResponse> =>
    api.post<HintResponse>("/hint", payload),
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