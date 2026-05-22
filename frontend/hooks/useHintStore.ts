import { create } from "zustand";

type HintStore = {
  hint: string;
  hintCount: number;
  hints: string[];
  getNextHint: () => void;
  resetHints: () => void;
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
}));