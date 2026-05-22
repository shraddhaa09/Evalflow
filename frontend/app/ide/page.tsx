"use client";

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
      setOutput("Error: Please write some code first.");
      setStatus("error");
      return;
    }

    setIsRunning(true);
    setStatus("running");

    try {
      const result = await executeCode(code);
      setOutput(result.output || result.message);
      setStatus(result.success ? "success" : "error");
    } catch (error: any) {
      setOutput(`Error: ${error.message}`);
      setStatus("error");
    } finally {
      setIsRunning(false);
    }
  };

  const handleCheckAuthenticity = async () => {
    if (!code.trim()) {
      alert("Please write some code first.");
      return;
    }

    try {
      const result = await checkPlagiarism(code);
      setPlagiarismScore(result.score || 0);
      openPlagiarism();
    } catch (error: any) {
      alert(`Error checking authenticity: ${error.message}`);
    }
  };

  const handleGetHint = async () => {
    try {
      const result = await getHint(code);
      setHint(result.hint);
    } catch (error: any) {
      setHint("Unable to generate hint at this time.");
    }
  };

  if (!isMounted) {
    return <div style={{ padding: "2rem", textAlign: "center" }}>Loading IDE...</div>;
  }

  return (
    <>
      <main className={styles.ideContainer}>
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