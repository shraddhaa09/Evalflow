import { create } from 'zustand'

interface HintStore {
  question: string
  hint: string
  isLoading: boolean
  error: string | null
  setQuestion: (question: string) => void
  setHint: (hint: string) => void
  setLoading: (loading: boolean) => void
  setError: (error: string | null) => void
  clear: () => void
}

export const useHintStore = create<HintStore>((set) => ({
  question: '',
  hint: '',
  isLoading: false,
  error: null,
  setQuestion: (question) => set({ question }),
  setHint: (hint) => set({ hint }),
  setLoading: (loading) => set({ isLoading: loading }),
  setError: (error) => set({ error }),
  clear: () => set({ question: '', hint: '', error: null }),
}))
