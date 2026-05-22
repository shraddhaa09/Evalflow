import { create } from 'zustand'

interface EditorStore {
  code: string
  language: string
  setCode: (code: string) => void
  setLanguage: (language: string) => void
}

export const useEditorStore = create<EditorStore>((set) => ({
  code: `# Welcome to EvalCode\n\ndef hello():\n    print("Hello World")\n\nif __name__ == "__main__":\n    hello()`,
  language: 'python',
  setCode: (code) => set({ code }),
  setLanguage: (language) => set({ language }),
}))
