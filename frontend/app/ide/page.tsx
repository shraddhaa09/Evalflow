'use client'

import { TopBar } from '@/components/TopBar'
import { Editor } from '@/components/Editor'
import { Terminal } from '@/components/Terminal'
import { EveePanel } from '@/components/EveePanel'
import { PlagiarismModal } from '@/components/PlagiarismModal'
import styles from './page.module.css'

export default function IDEPage() {
  return (
    <div className={styles.container}>
      <TopBar />

      <div className={styles.workspace}>
        <Editor />
        <EveePanel />
      </div>

      <Terminal />

      <PlagiarismModal />
    </div>
  )
}
