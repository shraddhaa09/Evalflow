'use client'

import { useEffect, useState } from 'react'
import { useEditorStore } from '@/hooks/useEditorStore'
import { useTerminalStore } from '@/hooks/useTerminalStore'
import { usePlagiarismStore } from '@/hooks/usePlagiarismStore'
import { executeCode } from '@/services/execute.service'
import { checkPlagiarism } from '@/services/plagiarism.service'
import styles from './TopBar.module.css'

export function TopBar() {
  const { code, language, setLanguage } = useEditorStore()
  const { setOutput, setRunning } = useTerminalStore()
  const { open: openPlagiarism, setLoading: setPlagLoading, setResult: setPlagResult, setError: setPlagError } =
    usePlagiarismStore()
  const [elapsedTime, setElapsedTime] = useState(0)

  // Timer
  useEffect(() => {
    const interval = setInterval(() => {
      setElapsedTime((t) => t + 1)
    }, 1000)
    return () => clearInterval(interval)
  }, [])

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60)
    const secs = seconds % 60
    return `${mins}:${secs.toString().padStart(2, '0')}`
  }

  const handleRun = async () => {
    if (!code.trim()) {
      setOutput('Error: Code is empty\n')
      return
    }

    setRunning(true)
    setOutput('Running...\n')

    try {
      const result = await executeCode(code)
      setOutput(`${result.stdout}${result.stderr}[Exit code: ${result.exit_code}]\n[Time: ${result.execution_time}s]\n`)
    } catch (error) {
      setOutput(`Error: ${error instanceof Error ? error.message : 'Unknown error'}\n`)
    } finally {
      setRunning(false)
    }
  }

  const handleCheckAI = async () => {
    if (!code.trim()) {
      setPlagError('Code is empty')
      return
    }

    setPlagLoading(true)
    setPlagError(null)

    try {
      const result = await checkPlagiarism(code)
      setPlagResult(result)
      openPlagiarism()
    } catch (error) {
      setPlagError(error instanceof Error ? error.message : 'Failed to check AI')
    } finally {
      setPlagLoading(false)
    }
  }

  return (
  <div className={styles.container}>
    <div className={styles.logo}>
      Eval<span className={styles.logoAccent}>Code</span>
    </div>

    <div className={styles.marqueeWrap}>
      <div className={styles.marquee}>
        {['Write every line yourself', 'Sandboxed execution', 'Hints, not answers', 'AI-detection built in', 'Progress is earned',
          'Write every line yourself', 'Sandboxed execution', 'Hints, not answers', 'AI-detection built in', 'Progress is earned']
          .map((text, i) => (
            <span key={i} className={styles.marqueeItem}>
              <span className={styles.marqueeDot} />
              {text}
            </span>
          ))}
      </div>
    </div>

    <div className={styles.controls}>
      <div className={styles.langBadge}>
        <span className={styles.langDot} />
        Python
      </div>

      <div className={styles.divider} />

      <button onClick={handleRun} className="primary">Run Code</button>
      <button onClick={handleCheckAI} className="secondary">Check AI</button>

      <div className={styles.divider} />

      <div className={styles.timer}>
        <span className={styles.timerPulse} />
        {formatTime(elapsedTime)}
      </div>
    </div>
  </div>
)
}
