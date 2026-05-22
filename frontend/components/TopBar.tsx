'use client'

import { useEffect, useState } from 'react'
import { useEditorStore } from '@/hooks/useEditorStore'
import { useTerminalStore } from '@/hooks/useTerminalStore'
import { usePlagiarismStore } from '@/hooks/usePlagiarismStore'
import { executeCode, checkPlagiarism } from '@/services/api'
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
      const result = await executeCode(code, language)
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
      const result = await checkPlagiarism(code, language)
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
      <div className={styles.logo}>EvalCode</div>

      <div className={styles.controls}>
        <select value={language} onChange={(e) => setLanguage(e.target.value)} className={styles.select}>
          <option value="python">Python</option>
          <option value="javascript">JavaScript</option>
          <option value="java">Java</option>
          <option value="c">C</option>
          <option value="cpp">C++</option>
        </select>

        <button onClick={handleRun} className="primary">
          Run ▶
        </button>

        <button onClick={handleCheckAI} className="secondary">
          Check AI
        </button>

        <div className={styles.timer}>{formatTime(elapsedTime)}</div>
      </div>
    </div>
  )
}
