import styles from "./EveePanel.module.css";

type EveePanelProps = {
  hint?: string;
  onAskHint?: () => void;
};

export default function EveePanel({
  hint = "Focus on what changes after the comparison. When the middle value is too small or too large, decide which half can no longer contain the answer and move your boundaries with confidence.",
  onAskHint,
}: EveePanelProps) {
  return (
    <aside className={styles.panel} aria-label="EVEE hint panel">
      <div className={styles.header}>
        <div>
          <p className={styles.eyebrow}>EVEE</p>
          <h2 className={styles.title}>Guided hint panel</h2>
        </div>
        <div className={styles.chip}>Conceptual only</div>
      </div>

      <div className={styles.card}>
        <p className={styles.label}>Current guidance</p>
        <p className={styles.hint}>{hint}</p>
      </div>

      <button type="button" className={styles.button} onClick={onAskHint}>
        Get another hint
      </button>
    </aside>
  );
}