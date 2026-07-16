// services/execute.service.ts
import { api } from "./api";

export type ExecuteRequest = {
  code: string;
  language: string;
  version?: string;
  stdin?: string;
};

export type ExecuteResponse = {
  stdout: string;
  stderr: string;
  exit_code: number;
  execution_time: number;
  memory_used: string | null;
  status: string;
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
    version: "3.10.0",
  });
};