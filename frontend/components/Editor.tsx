'use client'

import { useRef, useState, useCallback } from 'react'
import { useEditorStore } from '@/hooks/useEditorStore'
import styles from './Editor.module.css'

export function Editor() {
  const { code, setCode } = useEditorStore()
  const taRef = useRef<HTMLTextAreaElement>(null)
  const lineBoxRef = useRef<HTMLDivElement>(null)
  const [cursorPos, setCursorPos] = useState('Ln 1, Col 1')

  const lineCount = code.split('\n').length
  const charCount = code.length

  const updateMeta = useCallback(() => {
    const ta = taRef.current
    if (!ta) return
    const before = ta.value.substring(0, ta.selectionStart).split('\n')
    const ln = before.length
    const col = before[before.length - 1].length + 1
    setCursorPos(`Ln ${ln}, Col ${col}`)
  }, [])

  const handleChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setCode(e.target.value)
    updateMeta()
    if (lineBoxRef.current && taRef.current) {
      lineBoxRef.current.scrollTop = taRef.current.scrollTop
    }
  }

  const handleScroll = () => {
    if (lineBoxRef.current && taRef.current) {
      lineBoxRef.current.scrollTop = taRef.current.scrollTop
    }
  }

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Tab') {
      e.preventDefault()
      const ta = taRef.current!
      const s = ta.selectionStart
      const newVal = ta.value.substring(0, s) + '    ' + ta.value.substring(ta.selectionEnd)
      setCode(newVal)
      requestAnimationFrame(() => {
        ta.selectionStart = ta.selectionEnd = s + 4
        updateMeta()
      })
    }
  }

  const lines = code.split('\n')
  const activeLine = taRef.current
    ? taRef.current.value.substring(0, taRef.current.selectionStart).split('\n').length
    : 1

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <div className={styles.fileTab}>
          <span className={styles.fileTabDot} />
          solution.py
        </div>
        <div className={styles.headerMeta}>
          <span>{cursorPos}</span>
          <span>UTF-8</span>
          <span className={styles.langBadge}>Python 3.11</span>
        </div>
      </div>

      <div className={styles.body}>
        <div className={styles.lineNumbers} ref={lineBoxRef}>
          {lines.map((_, i) => (
            <span
              key={i}
              className={`${styles.lineNum} ${i + 1 === activeLine ? styles.lineNumActive : ''}`}
            >
              {i + 1}
            </span>
          ))}
        </div>

        <div className={styles.textareaWrap}>
          <textarea
            ref={taRef}
            value={code}
            onChange={handleChange}
            onKeyUp={updateMeta}
            onClick={updateMeta}
            onKeyDown={handleKeyDown}
            onScroll={handleScroll}
            placeholder="# Write your solution here…"
            className={styles.textarea}
            spellCheck={false}
            autoCorrect="off"
            autoCapitalize="off"
          />
        </div>
      </div>

      <div className={styles.footer}>
        <div className={styles.footerLeft}>
          <span>{charCount} chars</span>
          <span>{lineCount} {lineCount === 1 ? 'line' : 'lines'}</span>
        </div>
        <span className={styles.savedBadge}>● saved</span>
      </div>
    </div>
  )
}