// services/hint.service.ts
import { api } from "./api";

export type HintRequest = {
  code: string;
  language: string;
  question?: string;
  problemId?: string;
};

export type HintResponse = {
  success: boolean;
  hint: string;
  level: number;
  reasoning?: string;
};

export const hintService = {
  getHint: (payload: HintRequest): Promise<HintResponse> =>
    api.post<HintResponse>("/hint", payload),
};

// Convenience functions
export const getHint = (code: string): Promise<HintResponse> => {
  return hintService.getHint({
    code,
    language: "python",
  });
};