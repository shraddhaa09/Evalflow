'use client'

import { useEditorStore } from '@/hooks/useEditorStore'
import { useHintStore } from '@/hooks/useHintStore'
import { getHint } from '@/services/api'
import styles from './EveePanel.module.css'

export function EveePanel() {
  const { code, language } = useEditorStore()
  const { question, hint, isLoading, error, setQuestion, setHint, setLoading, setError } =
    useHintStore()

  const handleGetHint = async () => {
    if (!question.trim()) { setError('Please ask a question first'); return }
    if (!code.trim())     { setError('Code cannot be empty'); return }

    setLoading(true)
    setError(null)

    try {
      const result = await getHint(question, code, language)
      setHint(result.hint)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to get hint')
    } finally {
      setLoading(false)
    }
  }

  const isWarn = question.length > 170

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <div className={styles.titleRow}>
          <div className={styles.title}>
            <div className={styles.titleIcon}>✦</div>
            EVEE
          </div>
          <span className={styles.titleBadge}>Hint Engine</span>
        </div>
        <div className={styles.subtitle}>Ask a question — get a nudge, not the answer</div>
      </div>

      <div className={styles.body}>
        <div className={styles.inputSection}>
          <div className={styles.inputLabel}>What are you stuck on?</div>
          <div className={styles.textareaWrap}>
            <textarea
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              placeholder="e.g. Why does my loop go out of bounds?"
              className={styles.input}
              maxLength={200}
            />
            <span className={`${styles.charCount} ${isWarn ? styles.charCountWarn : ''}`}>
              {question.length} / 200
            </span>
          </div>
        </div>

        <div className={styles.btnWrap}>
          <button
            onClick={handleGetHint}
            disabled={isLoading}
            className={styles.hintBtn}
          >
            {isLoading
              ? <><span className="btn-spinner" /> Thinking…</>
              : <><span>✦</span> Get Hint</>
            }
          </button>
        </div>

        <div className={styles.divider} />

        <div className={styles.hintSection}>
          <div className={styles.hintLabel}>Hint</div>

          {!hint && !error && (
            <div className={styles.hintEmpty}>
              <div className={styles.hintEmptyIcon}>💡</div>
              <div className={styles.hintEmptyText}>
                Ask a question above and EVEE will guide your thinking
              </div>
            </div>
          )}

          {hint && (
            <div className={styles.hintBox}>
              <p>{hint}</p>
            </div>
          )}

          {error && (
            <div className={styles.error}>
              <span>⚠</span>
              <span>{error}</span>
            </div>
          )}
        </div>

        <div className={styles.tips}>
          <div className={styles.tip}>
            <span className={styles.tipDot} />
            Be specific about which part confuses you
          </div>
          <div className={styles.tip}>
            <span className={styles.tipDot} />
            EVEE gives nudges, not full solutions
          </div>
        </div>
      </div>
    </div>
  )
}