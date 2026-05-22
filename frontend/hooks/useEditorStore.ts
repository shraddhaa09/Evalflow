import { create } from "zustand";

type EditorStore = {
  language: string;
  code: string;
  setLanguage: (language: string) => void;
  setCode: (code: string) => void;
  resetCode: () => void;
};

const defaultCode = `def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        # update boundaries here
    return -1`;

export const useEditorStore = create<EditorStore>((set) => ({
  language: "Python",
  code: defaultCode,
  setLanguage: (language) => set({ language }),
  setCode: (code) => set({ code }),
  resetCode: () => set({ code: defaultCode }),
}));