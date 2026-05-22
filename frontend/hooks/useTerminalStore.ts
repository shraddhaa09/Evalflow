import { create } from 'zustand'

interface TerminalStore {
  output: string
  isRunning: boolean
  setOutput: (output: string) => void
  appendOutput: (text: string) => void
  clear: () => void
  setRunning: (running: boolean) => void
}

export const useTerminalStore = create<TerminalStore>((set) => ({
  output: '> Ready\n',
  isRunning: false,
  setOutput: (output) => set({ output }),
  appendOutput: (text) => set((state) => ({ output: state.output + text + '\n' })),
  clear: () => set({ output: '' }),
  setRunning: (running) => set({ isRunning: running }),
}))
