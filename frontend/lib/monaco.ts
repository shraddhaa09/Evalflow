import type * as Monaco from "monaco-editor";

export function setupMonaco(monaco: typeof Monaco) {
  monaco.editor.defineTheme("evalcode-theme", {
    base: "vs-dark",
    inherit: true,
    rules: [
      { token: "", foreground: "DBEAFE", background: "0F172A" },
      { token: "comment", foreground: "6B7A90", fontStyle: "italic" },
      { token: "keyword", foreground: "93C5FD" },
      { token: "number", foreground: "F4C430" },
      { token: "string", foreground: "86EFAC" },
      { token: "identifier", foreground: "F8FAFC" },
      { token: "delimiter", foreground: "94A3B8" },
    ],
    colors: {
      "editor.background": "#0F172A",
      "editor.foreground": "#DBEAFE",
      "editorLineNumber.foreground": "#64748B",
      "editorLineNumber.activeForeground": "#F8FAFC",
      "editorCursor.foreground": "#F4C430",
      "editor.selectionBackground": "#1D4ED855",
      "editor.inactiveSelectionBackground": "#1E293B",
      "editor.lineHighlightBackground": "#111C31",
      "editorLineNumber.background": "#111C31",
      "editorIndentGuide.background1": "#1E293B",
      "editorIndentGuide.activeBackground1": "#334155",
      "editorSuggestWidget.background": "#111827",
      "editorSuggestWidget.border": "#1F2937",
      "editorSuggestWidget.foreground": "#DBEAFE",
      "editorSuggestWidget.selectedBackground": "#1E3A8A55",
    },
  });

  monaco.languages.typescript.javascriptDefaults.setEagerModelSync(true);
  monaco.languages.typescript.typescriptDefaults.setEagerModelSync(true);
}

export const monacoEditorOptions = {
  fontSize: 15,
  fontFamily: "JetBrains Mono, Fira Code, monospace",
  minimap: { enabled: false },
  scrollBeyondLastLine: false,
  wordWrap: "on" as const,
  automaticLayout: true,
  tabSize: 4,
  insertSpaces: true,
  roundedSelection: true,
  padding: {
    top: 16,
    bottom: 16,
  },
  glyphMargin: false,
  folding: true,
  lineNumbersMinChars: 3,
  renderLineHighlight: "all" as const,
  cursorBlinking: "smooth" as const,
  smoothScrolling: true,
  contextmenu: false,
};