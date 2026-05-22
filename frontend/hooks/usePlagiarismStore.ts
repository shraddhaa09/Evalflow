import { create } from "zustand";

type PlagiarismStore = {
  isPlagiarismOpen: boolean;
  plagiarismScore: number;
  openPlagiarism: (score?: number) => void;
  closePlagiarism: () => void;
  setPlagiarismScore: (score: number) => void;
  // Keep old names for backwards compatibility
  isOpen: boolean;
  score: number;
  openModal: (score?: number) => void;
  closeModal: () => void;
  setScore: (score: number) => void;
};

export const usePlagiarismStore = create<PlagiarismStore>((set) => ({
  isPlagiarismOpen: false,
  plagiarismScore: 24,
  openPlagiarism: (score) =>
    set((state) => ({
      isPlagiarismOpen: true,
      plagiarismScore: typeof score === "number" ? score : state.plagiarismScore,
      isOpen: true,
      score: typeof score === "number" ? score : state.plagiarismScore,
    })),
  closePlagiarism: () => set({ isPlagiarismOpen: false, isOpen: false }),
  setPlagiarismScore: (score) => set({ plagiarismScore: score, score }),
  // Old methods for backwards compatibility
  isOpen: false,
  score: 24,
  openModal: (score) =>
    set((state) => ({
      isPlagiarismOpen: true,
      plagiarismScore: typeof score === "number" ? score : state.plagiarismScore,
      isOpen: true,
      score: typeof score === "number" ? score : state.plagiarismScore,
    })),
  closeModal: () => set({ isPlagiarismOpen: false, isOpen: false }),
  setScore: (score) => set({ plagiarismScore: score, score }),
}));