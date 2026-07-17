import { create } from "zustand";

export type PlagiarismResult = {
  probability: number;
  label: string;
  highest_similarity_match?: string;
  features?: Record<string, number>;
  signals?: string[];
};

type PlagiarismStore = {
  isPlagiarismOpen: boolean;
  plagiarismScore: number;
  result: PlagiarismResult | null;
  openPlagiarism: (result: PlagiarismResult) => void;
  closePlagiarism: () => void;
  setPlagiarismScore: (score: number) => void; // kept for compatibility if needed
};

export const usePlagiarismStore = create<PlagiarismStore>((set) => ({
  isPlagiarismOpen: false,
  plagiarismScore: 0,
  result: null,
  openPlagiarism: (result) =>
    set({
      isPlagiarismOpen: true,
      result,
      plagiarismScore: Math.round((result.probability || 0) * 100),
    }),
  closePlagiarism: () => set({ isPlagiarismOpen: false }),
  setPlagiarismScore: (score) => set({ plagiarismScore: score }),
}));