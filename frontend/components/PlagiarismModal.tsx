'use client'

import { usePlagiarismStore } from '@/hooks/usePlagiarismStore'
import styles from './PlagiarismModal.module.css'

export function PlagiarismModal() {
  const { isOpen, isLoading, result, error, close } = usePlagiarismStore()

  if (!isOpen) return null

  return (
    <div className={styles.overlay} onClick={close}>
      <div className={styles.modal} onClick={(e) => e.stopPropagation()}>
        <div className={styles.header}>
          <h2>AI Similarity Check</h2>
          <button onClick={close} className={styles.closeBtn}>✕</button>
        </div>

        {isLoading && <div className={styles.loading}>Checking...</div>}

        {error && <div className={styles.error}>{error}</div>}

        {result && (
          <div className={styles.content}>
            <div className={styles.scoreBox}>
              <div className={styles.progressBar}>
                <div
                  className={styles.progressFill}
                  style={{
                    width: `${result.ai_probability * 100}%`,
                    background:
                      result.ai_probability > 0.7
                        ? '#ef4444'
                        : result.ai_probability > 0.45
                          ? '#f59e0b'
                          : '#10b981',
                  }}
                ></div>
              </div>
              <div className={styles.percentage}>{(result.ai_probability * 100).toFixed(0)}%</div>
            </div>

            <div className={styles.label}>{result.label}</div>
            <div className={styles.confidence}>Confidence: {(result.confidence * 100).toFixed(0)}%</div>

            <div className={styles.signals}>
              <strong>Signals:</strong>
              <ul>
                {result.signals.map((signal, idx) => (
                  <li key={idx}>{signal}</li>
                ))}
              </ul>
            </div>

            <button onClick={close} className="primary">
              Close
            </button>
          </div>
        )}
      </div>
    </div>
  )
}
