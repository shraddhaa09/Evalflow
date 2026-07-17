import { usePlagiarismStore } from "@/hooks/usePlagiarismStore";
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
  const { result } = usePlagiarismStore();
  
  if (!open) return null;

  const riskLabel =
    score >= 85 ? "High Plagiarism Risk" : score >= 60 ? "Moderate Plagiarism Risk" : "Clean/Low Risk";

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
            <span className={styles.scoreLabel}>AI / Plagiarism match score</span>
            <strong className={styles.scoreValue}>{score}%</strong>
            <span className={styles.scoreMeta}>{riskLabel}</span>
          </div>

          <div className={styles.details}>
            {result?.highest_similarity_match && (
              <div className={styles.detailItem}>
                <h3>Highest Similarity Match</h3>
                <p>Most similar to submission: <strong>{result.highest_similarity_match}</strong></p>
              </div>
            )}
            {result?.signals && result.signals.length > 0 && (
              <div className={styles.detailItem}>
                <h3>Detection Signals</h3>
                <ul>
                  {result.signals.map((sig, i) => (
                    <li key={i}>{sig}</li>
                  ))}
                </ul>
              </div>
            )}
            {result?.features && (
              <div className={styles.detailItem}>
                <h3>Feature Explanations</h3>
                <ul>
                  <li>Semantic Similarity (CodeBERT): {Math.round(result.features.semantic_similarity * 100)}%</li>
                  <li>Token Similarity (Jaccard): {Math.round(result.features.token_similarity * 100)}%</li>
                  <li>Structure Similarity (AST-lite): {Math.round(result.features.structure_similarity * 100)}%</li>
                </ul>
              </div>
            )}
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