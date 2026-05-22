export type SupportedLanguage = "python" | "javascript" | "java" | "cpp";

export type TerminalStatus = "idle" | "running" | "success" | "error";

export type PlagiarismLevel = "low" | "medium" | "high";

export interface EditorState {
  language: SupportedLanguage;
  code: string;
}

export interface HintState {
  hint: string;
  hintCount: number;
  hints: string[];
}

export interface TerminalState {
  output: string;
  status: TerminalStatus;
}

export interface PlagiarismSignals {
  repetitionScore: number;
  commentScore: number;
  structureScore: number;
  lengthScore: number;
}

export interface PlagiarismResult {
  success: boolean;
  score: number;
  level: PlagiarismLevel;
  label: string;
  signals: PlagiarismSignals;
  summary: string;
}

export interface PlagiarismRequestBody {
  code: string;
  language: SupportedLanguage;
}

export interface HintRequestBody {
  code: string;
  language: SupportedLanguage;
  hintCount?: number;
}

export interface HintResponse {
  success: boolean;
  hint: string;
  hintCount: number;
}

export interface ExecuteCodeRequestBody {
  code: string;
  language: SupportedLanguage;
  stdin?: string;
}

export interface ExecuteCodeResponse {
  success: boolean;
  output: string;
  error?: string;
  status: TerminalStatus;
  executionTime?: number;
  memoryUsed?: number;
}

export interface ApiErrorResponse {
  success: false;
  message: string;
}

export interface MonacoEditorProps {
  language: SupportedLanguage;
  value: string;
  onChange: (value: string) => void;
}

export interface SelectOption<T = string> {
  label: string;
  value: T;
}

declare module "*.module.css" {
  const classes: Record<string, string>;
  export default classes;
}