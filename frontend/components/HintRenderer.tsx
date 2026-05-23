// components/HintRenderer.tsx

import styles from './HintRenderer.module.css'

export function HintRenderer({ hint }: { hint: string }) {
  // Split on [term] patterns and render highlights
  const parts = hint.split(/(\[.*?\])/g)

  return (
    <p className={styles.root}>
      {parts.map((part, i) => {
        if (/^\[.*\]$/.test(part)) {
          const term = part.slice(1, -1)
          return <span key={i} className={styles.highlight}>{term}</span>
        }
        return <span key={i}>{part}</span>
      })}
    </p>
  )
}