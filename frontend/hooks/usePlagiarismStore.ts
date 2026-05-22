import { create } from 'zustand'

interface PlagiarismResult {
  ai_probability: number
  label: string
  confidence: number
  signals: string[]
}

interface PlagiarismStore {
  isOpen: boolean
  isLoading: boolean
  result: PlagiarismResult | null
  error: string | null
  open: () => void
  close: () => void
  setLoading: (loading: boolean) => void
  setResult: (result: PlagiarismResult) => void
  setError: (error: string | null) => void
}

export const usePlagiarismStore = create<PlagiarismStore>((set) => ({
  isOpen: false,
  isLoading: false,
  result: null,
  error: null,
  open: () => set({ isOpen: true }),
  close: () => set({ isOpen: false }),
  setLoading: (loading) => set({ isLoading: loading }),
  setResult: (result) => set({ result }),
  setError: (error) => set({ error }),
}))
