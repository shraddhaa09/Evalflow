// services/execute.service.ts
import { api } from "./api";

export type ExecuteRequest = {
  code: string;
  language: string;
  version?: string;
  stdin?: string;
};

export type ExecuteResponse = {
  success: boolean;
  output: string;
  stdout: string;
  stderr: string;
  signal: string | null;
  exitCode: number;
  time: number | null;
  memory: number | null;
  message?: string;
};

export const executeService = {
  execute: (payload: ExecuteRequest): Promise<ExecuteResponse> =>
    api.post<ExecuteResponse>("/execute", payload),
};

// Convenience functions
export const executeCode = (code: string): Promise<ExecuteResponse> => {
  return executeService.execute({
    code,
    language: "python",
    version: "3.10",
  });
};