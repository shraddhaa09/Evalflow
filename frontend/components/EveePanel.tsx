'use client'

import { useState } from 'react'
import { useEditorStore } from '@/hooks/useEditorStore'
import { useHintStore } from '@/hooks/useHintStore'
import { getHint } from '@/services/api'
import styles from './EveePanel.module.css'

export function EveePanel() {
  const { code, language } = useEditorStore()
  const { question, hint, isLoading, error, setQuestion, setHint, setLoading, setError } =
    useHintStore()

  const handleGetHint = async () => {
    if (!question.trim()) {
      setError('Please ask a question')
      return
    }

    if (!code.trim()) {
      setError('Code cannot be empty')
      return
    }

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

  return (
    <div className={styles.container}>
      <div className={styles.header}>⚡ EVEE — Hint Engine</div>

      <textarea
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="What are you stuck on?"
        className={styles.input}
        maxLength={200}
      />

      <div className={styles.charCount}>{question.length}/200</div>

      <button
        onClick={handleGetHint}
        disabled={isLoading}
        className={styles.hintBtn}
      >
        {isLoading ? 'Thinking...' : 'Get Hint'}
      </button>

      {error && <div className={styles.error}>{error}</div>}

      <div className={styles.hintBox}>
        {hint ? <p>{hint}</p> : <p className={styles.empty}>Ask a question to get a hint</p>}
      </div>
    </div>
  )
}
