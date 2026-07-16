import { create } from "zustand";

type PlagiarismStore = {
  isPlagiarismOpen: boolean;
  plagiarismScore: number;
  isLoading: boolean;
  result: { ai_probability?: number; label?: string; confidence?: number; signals?: string[] } | null;
  error: string | null;
  openPlagiarism: (score?: number) => void;
  closePlagiarism: () => void;
  setPlagiarismScore: (score: number) => void;
  setLoading: (loading: boolean) => void;
  setResult: (result: PlagiarismStore['result']) => void;
  setError: (error: string | null) => void;
  close: () => void;
  open: (score?: number) => void;
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
  isLoading: false,
  result: null,
  error: null,
  openPlagiarism: (score) =>
    set((state) => ({
      isPlagiarismOpen: true,
      plagiarismScore: typeof score === "number" ? score : state.plagiarismScore,
      isOpen: true,
      score: typeof score === "number" ? score : state.plagiarismScore,
    })),
  closePlagiarism: () => set({ isPlagiarismOpen: false, isOpen: false }),
  close: () => set({ isPlagiarismOpen: false, isOpen: false }),
  open: (score) =>
    set((state) => ({
      isPlagiarismOpen: true,
      plagiarismScore: typeof score === "number" ? score : state.plagiarismScore,
      isOpen: true,
      score: typeof score === "number" ? score : state.plagiarismScore,
    })),
  setPlagiarismScore: (score) => set({ plagiarismScore: score, score }),
  setLoading: (isLoading: boolean) => set({ isLoading }),
  setResult: (result) => set({ result }),
  setError: (error: string | null) => set({ error }),
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