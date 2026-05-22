import styles from "./PlagiarismModal.module.css";

type PlagiarismModalProps = {
  open: boolean;
  onClose: () => void;
  score?: number;
};

export default function PlagiarismModal({
  open,
  onClose,
  score = 24,
}: PlagiarismModalProps) {
  if (!open) return null;

  const riskLabel =
    score >= 70 ? "High review needed" : score >= 40 ? "Moderate review" : "Low concern";

  return (
    <div className={styles.overlay} role="dialog" aria-modal="true" aria-labelledby="plagiarism-title">
      <div className={styles.modal}>
        <div className={styles.header}>
          <div>
            <p className={styles.eyebrow}>Authenticity review</p>
            <h2 id="plagiarism-title" className={styles.title}>
              Submission analysis
            </h2>
          </div>
          <button type="button" className={styles.closeButton} onClick={onClose} aria-label="Close modal">
            Close
          </button>
        </div>

        <div className={styles.body}>
          <div className={styles.scoreCard}>
            <span className={styles.scoreLabel}>AI assistance score</span>
            <strong className={styles.scoreValue}>{score}%</strong>
            <span className={styles.scoreMeta}>{riskLabel}</span>
          </div>

          <div className={styles.details}>
            <div className={styles.detailItem}>
              <h3>Structural consistency</h3>
              <p>The submission pattern appears mostly natural, with some areas worth a second look.</p>
            </div>
            <div className={styles.detailItem}>
              <h3>Token diversity</h3>
              <p>Vocabulary and implementation flow suggest a student-led attempt rather than direct generation.</p>
            </div>
            <div className={styles.detailItem}>
              <h3>Typing behavior</h3>
              <p>Review session timing and editing rhythm alongside the score before making a final judgment.</p>
            </div>
          </div>
        </div>

        <div className={styles.footer}>
          <button type="button" className={styles.secondaryBtn} onClick={onClose}>
            Dismiss
          </button>
          <button type="button" className={styles.primaryBtn}>
            Mark for review
          </button>
        </div>
      </div>
    </div>
  );
}