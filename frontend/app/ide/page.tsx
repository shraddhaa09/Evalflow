'use client';

import { useState, useEffect } from "react";
import styles from "./page.module.css";
import TopBar from "@/components/ide/TopBar";
import Editor from "@/components/ide/Editor";
import Terminal from "@/components/ide/Terminal";
import EveePanel from "@/components/ide/EveePanel";
import PlagiarismModal from "@/components/ide/PlagiarismModal";
import { useEditorStore } from "@/hooks/useEditorStore";
import { useTerminalStore } from "@/hooks/useTerminalStore";
import { usePlagiarismStore } from "@/hooks/usePlagiarismStore";
import { useHintStore } from "@/hooks/useHintStore";
import { executeCode } from "@/services/execute.service";
import { checkPlagiarism } from "@/services/plagiarism.service";
import { getHint } from "@/services/hint.service";

export default function IDEPage() {
  const [isRunning, setIsRunning] = useState(false);
  const [isMounted, setIsMounted] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  // Zustand stores
  const { code, setCode } = useEditorStore();
  const { output, status, setOutput, setStatus } = useTerminalStore();
  const { isPlagiarismOpen, plagiarismScore, openPlagiarism, closePlagiarism, setPlagiarismScore } =
    usePlagiarismStore();
  const { hint, setHint } = useHintStore();

  useEffect(() => {
    setIsMounted(true);
  }, []);

  const handleRunCode = async () => {
    if (!code.trim()) {
      setErrorMessage("Please write some code first.");
      setOutput("Error: Please write some code first.");
      setStatus("error");
      return;
    }

    setErrorMessage(null);
    setIsRunning(true);
    setStatus("running");

    try {
      const result = await executeCode(code);
      const outputText = [result.stdout, result.stderr]
        .filter(Boolean)
        .join("");
      setOutput(
        outputText ||
          (result.status === "success"
            ? "Execution completed with no output."
            : `Execution ended with status: ${result.status}`)
      );
      setStatus(result.status === "success" ? "success" : "error");
    } catch (error: any) {
      setErrorMessage(`Unable to run code: ${error.message}`);
      setOutput(`Error: ${error.message}`);
      setStatus("error");
    } finally {
      setIsRunning(false);
    }
  };

  const handleCheckAuthenticity = async () => {
    if (!code.trim()) {
      setErrorMessage("Please write some code first.");
      return;
    }

    setErrorMessage(null);

    try {
      const result = await checkPlagiarism(code);
      const score = Math.round((result.ai_probability || 0) * 100);
      setPlagiarismScore(score);
      openPlagiarism(score);
    } catch (error: any) {
      setErrorMessage(`Unable to check authenticity: ${error.message}`);
    }
  };

  const handleGetHint = async () => {
    setErrorMessage(null);

    try {
      const result = await getHint(code);
      setHint(result.hint || "No hint was returned.");
    } catch (error: any) {
      setErrorMessage("Hint temporarily unavailable, try again.");
      setHint("Hint temporarily unavailable, try again.");
    }
  };

  if (!isMounted) {
    return <div style={{ padding: "2rem", textAlign: "center" }}>Loading IDE...</div>;
  }

  return (
    <>
      <main className={styles.ideContainer}>
        {errorMessage ? (
          <div
            role="alert"
            style={{
              marginBottom: "1rem",
              padding: "0.75rem 1rem",
              border: "1px solid #f87171",
              borderRadius: "0.5rem",
              backgroundColor: "#fee2e2",
              color: "#991b1b",
            }}
          >
            {errorMessage}
          </div>
        ) : null}

        <TopBar
          language="Python"
          title="Binary Search — Practice"
          onRun={handleRunCode}
          onCheck={handleCheckAuthenticity}
        />

        <div className={styles.mainGrid}>
          <div className={styles.editorSection}>
            <Editor code={code} onChange={setCode} />
            <Terminal output={output} status={status as any} />
          </div>

          <aside className={styles.sidePanel}>
            <EveePanel hint={hint} onAskHint={handleGetHint} />
          </aside>
        </div>
      </main>

      <PlagiarismModal
        open={isPlagiarismOpen}
        onClose={closePlagiarism}
        score={plagiarismScore}
      />
    </>
  );
}