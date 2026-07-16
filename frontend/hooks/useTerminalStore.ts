import { create } from "zustand";

type TerminalStatus = "idle" | "running" | "success" | "error";

type TerminalStore = {
  output: string;
  status: TerminalStatus;
  setOutput: (output: string) => void;
  setStatus: (status: TerminalStatus) => void;
  runStart: () => void;
  runSuccess: (output: string) => void;
  runError: (output: string) => void;
  resetTerminal: () => void;
  clear: () => void;
  setRunning: (running: boolean) => void;
};

const initialOutput =
  "Ready.\nRun your code to inspect output, errors, timing, and memory.";

export const useTerminalStore = create<TerminalStore>((set) => ({
  output: initialOutput,
  status: "idle",
  setOutput: (output) => set({ output }),
  setStatus: (status) => set({ status }),
  runStart: () =>
    set({
      status: "running",
      output: "Running your code...\n",
    }),
  runSuccess: (output) =>
    set({
      status: "success",
      output,
    }),
  runError: (output) =>
    set({
      status: "error",
      output,
    }),
  resetTerminal: () =>
    set({
      status: "idle",
      output: initialOutput,
    }),
  clear: () =>
    set({
      status: "idle",
      output: initialOutput,
    }),
  setRunning: (running: boolean) =>
    set({
      status: running ? "running" : "idle",
    }),
}));