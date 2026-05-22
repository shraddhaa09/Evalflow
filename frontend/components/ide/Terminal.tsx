import styles from "./Terminal.module.css";

type TerminalProps = {
  output?: string;
  status?: "idle" | "running" | "success" | "error";
};

export default function Terminal({
  output = "Ready.\nRun your code to inspect output, errors, timing, and memory.",
  status = "idle",
}: TerminalProps) {
  return (
    <section className={styles.wrapper} aria-label="Execution terminal">
      <div className={styles.header}>
        <div>
          <p className={styles.eyebrow}>Output</p>
          <h2 className={styles.title}>Execution terminal</h2>
        </div>
        <div className={`${styles.status} ${styles[status]}`}>
          {status === "running" && "Running"}
          {status === "success" && "Completed"}
          {status === "error" && "Error"}
          {status === "idle" && "Ready"}
        </div>
      </div>

      <pre className={styles.output}>{output}</pre>
    </section>
  );
}