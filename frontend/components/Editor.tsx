'use client'

import { useEditorStore } from '@/hooks/useEditorStore'
import styles from './Editor.module.css'

export function Editor() {
  const { code, setCode } = useEditorStore()

  return (
    <div className={styles.container}>
      <textarea
        value={code}
        onChange={(e) => setCode(e.target.value)}
        placeholder="Write your code here..."
        className={styles.textarea}
      />
    </div>
  )
}
