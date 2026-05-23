'use client'

import { useRef, useEffect } from 'react'
import { useTerminalStore } from '@/hooks/useTerminalStore'
import styles from './Terminal.module.css'

export function Terminal() {
  const { output, clear } = useTerminalStore()
  const wrapperRef = useRef<HTMLDivElement>(null)
  const dragging   = useRef(false)
  const startY     = useRef(0)
  const startH     = useRef(0)

  useEffect(() => {
    const onMove = (e: MouseEvent | TouchEvent) => {
      if (!dragging.current) return
      const clientY = 'touches' in e ? e.touches[0].clientY : e.clientY
      const delta   = startY.current - clientY
      const newH    = Math.min(Math.max(startH.current + delta, 80), window.innerHeight * 0.7)
      if (wrapperRef.current) wrapperRef.current.style.height = `${newH}px`
    }
    const onUp = () => {
      dragging.current = false
      document.body.style.userSelect = ''
      document.body.style.cursor = ''
    }
    document.addEventListener('mousemove', onMove)
    document.addEventListener('mouseup', onUp)
    document.addEventListener('touchmove', onMove, { passive: true })
    document.addEventListener('touchend', onUp)
    return () => {
      document.removeEventListener('mousemove', onMove)
      document.removeEventListener('mouseup', onUp)
      document.removeEventListener('touchmove', onMove)
      document.removeEventListener('touchend', onUp)
    }
  }, [])

  const onDragStart = (e: React.MouseEvent | React.TouchEvent) => {
    dragging.current = true
    const clientY = 'touches' in e ? e.touches[0].clientY : e.clientY
    startY.current = clientY
    startH.current = wrapperRef.current?.getBoundingClientRect().height ?? 220
    document.body.style.userSelect = 'none'
    document.body.style.cursor = 'ns-resize'
  }

  return (
    <div className={styles.wrapper} ref={wrapperRef}>
      <div
        className={styles.dragHandle}
        onMouseDown={onDragStart}
        onTouchStart={onDragStart}
      >
        <div className={styles.dragPipRow}>
          <div className={styles.dragPip} />
          <div className={styles.dragPip} />
          <div className={styles.dragPip} />
        </div>
      </div>

      <div className={styles.container}>
        <div className={styles.header}>
          <div className={styles.headerLeft}>
            <div className={styles.dots}>
              <div className={`${styles.dot} ${styles.dotRed}`} />
              <div className={`${styles.dot} ${styles.dotYellow}`} />
              <div className={`${styles.dot} ${styles.dotGreen}`} />
            </div>
            <span className={styles.title}>Output</span>
            <div className={styles.status}>
              <span className={styles.statusDot} />
              python · ready
            </div>
          </div>
          <button onClick={clear} className={styles.clearBtn}>✕ clear</button>
        </div>

        <pre className={styles.output}>{output}</pre>
      </div>
    </div>
  )
}