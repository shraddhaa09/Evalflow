import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'EvalCode',
  description: 'Guided coding environment',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
