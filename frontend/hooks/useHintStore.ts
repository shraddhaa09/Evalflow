import { create } from "zustand";

type HintStore = {
  hint: string;
  hintCount: number;
  hints: string[];
  question: string;
  isLoading: boolean;
  error: string | null;
  getNextHint: () => void;
  resetHints: () => void;
  setHint: (hint: string) => void;
  setQuestion: (question: string) => void;
  setLoading: (loading: boolean) => void;
  setError: (error: string | null) => void;
};

const hintSteps = [
  "Focus on the comparison with the middle element. Which half can be safely ignored after that check?",
  "If the target is smaller than arr[mid], move the right boundary. If it is larger, move the left boundary.",
  "Your loop already finds the middle correctly. The missing step is updating left or right so the search space keeps shrinking.",
];

export const useHintStore = create<HintStore>((set, get) => ({
  hint: hintSteps[0],
  hintCount: 1,
  hints: hintSteps,
  question: "",
  isLoading: false,
  error: null,
  getNextHint: () => {
    const { hintCount, hints } = get();
    const nextIndex = Math.min(hintCount, hints.length - 1);

    set({
      hint: hints[nextIndex],
      hintCount: Math.min(hintCount + 1, hints.length),
    });
  },
  resetHints: () =>
    set({
      hint: hintSteps[0],
      hintCount: 1,
    }),
  setHint: (hint: string) => {
    const { hintCount } = get();
    set({
      hint,
      hintCount: hintCount + 1,
    });
  },
  setQuestion: (question: string) => set({ question }),
  setLoading: (isLoading: boolean) => set({ isLoading }),
  setError: (error: string | null) => set({ error }),
}));