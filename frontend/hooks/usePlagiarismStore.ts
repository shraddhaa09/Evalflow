import { create } from "zustand";

type PlagiarismStore = {
  isOpen: boolean;
  score: number;
  openModal: (score?: number) => void;
  closeModal: () => void;
  setScore: (score: number) => void;
};

export const usePlagiarismStore = create<PlagiarismStore>((set) => ({
  isOpen: false,
  score: 24,
  openModal: (score) =>
    set((state) => ({
      isOpen: true,
      score: typeof score === "number" ? score : state.score,
    })),
  closeModal: () => set({ isOpen: false }),
  setScore: (score) => set({ score }),
}));