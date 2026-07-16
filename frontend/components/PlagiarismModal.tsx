'use client'

import { usePlagiarismStore } from '@/hooks/usePlagiarismStore'
import styles from './PlagiarismModal.module.css'

export function PlagiarismModal() {
  const { isOpen, isLoading, result, error, close } = usePlagiarismStore()

  if (!isOpen) return null

  const prob       = result?.ai_probability ?? 0
  const pct        = Math.round(prob * 100)
  const confPct    = Math.round((result?.confidence ?? 0) * 100)
  const circumference = 188.4
  const offset     = circumference - circumference * prob
  const color      = prob > 0.7 ? '#ef4444' : prob > 0.45 ? '#f59e0b' : '#22c55e'

  return (
    <div className={styles.overlay} onClick={close}>
      <div className={styles.modal} onClick={(e) => e.stopPropagation()}>

        <div className={styles.header}>
          <div className={styles.headerLeft}>
            <div className={styles.headerIcon}>⭐</div>
            <div>
              <div className={styles.headerTitle}>AI Similarity Check</div>
              <div className={styles.headerSub}>Powered by ML classifier</div>
            </div>
          </div>
          <button onClick={close} className={styles.closeBtn}>✕</button>
        </div>

        {isLoading && (
          <div className={styles.loading}>
            <div className={styles.loadingSpinner} />
            <div className={styles.loadingText}>Analysing submission patterns…</div>
          </div>
        )}

        {error && (
          <div className={styles.content}>
            <div className={styles.error}>
              <span>⚠</span>
              <span>{error}</span>
            </div>
          </div>
        )}

        {result && (
          <>
            <div className={styles.content}>
              <div className={styles.scoreBox}>
                <div className={styles.ringWrap}>
                  <svg width="72" height="72" viewBox="0 0 72 72">
                    <circle className={styles.ringBg} cx="36" cy="36" r="30" />
                    <circle
                      className={styles.ringFill}
                      cx="36" cy="36" r="30"
                      style={{ stroke: color, strokeDashoffset: offset }}
                    />
                  </svg>
                  <div className={styles.ringText}>
                    <span className={styles.ringPct}>{pct}%</span>
                    <span className={styles.ringPctLabel}>AI</span>
                  </div>
                </div>

                <div className={styles.scoreInfo}>
                  <div className={styles.label}>{result.label}</div>
                  <div className={styles.confidence}>Confidence: {confPct}%</div>
                  <div className={styles.progressBar}>
                    <div
                      className={styles.progressFill}
                      style={{ width: `${pct}%`, background: color }}
                    />
                  </div>
                </div>
              </div>

              {result.signals && (
                <div className={styles.signals}>
                  <div className={styles.signalsLabel}>Signals detected</div>
                  {result.signals.map((signal, idx) => (
                    <div key={idx} className={styles.signalItem}>
                      <span className={styles.signalDot} style={{ background: color }} />
                      {signal}
                    </div>
                  ))}
                </div>
              )}
            </div>

            <div className={styles.footer}>
              <button onClick={close} className={styles.confirmBtn}>
                ✓ Acknowledged — close
              </button>
            </div>
          </>
        )}

      </div>
    </div>
  )
}