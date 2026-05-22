'use client'

import { useTerminalStore } from '@/hooks/useTerminalStore'
import styles from './Terminal.module.css'

export function Terminal() {
  const { output, clear } = useTerminalStore()

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <span>Terminal Output</span>
        <button onClick={clear} className={styles.clearBtn}>
          Clear
        </button>
      </div>
      <pre className={styles.output}>{output}</pre>
    </div>
  )
}
