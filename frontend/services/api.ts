import { API_ENDPOINTS } from '@/lib/config'

export async function executeCode(code: string, language: string) {
  const response = await fetch(API_ENDPOINTS.execute, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ code, language }),
  })

  if (!response.ok) {
    const error = await response.json()
    throw new Error(error.detail || 'Execution failed')
  }

  return response.json()
}

export async function getHint(question: string, code: string, language: string) {
  const response = await fetch(API_ENDPOINTS.hint, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question, current_code: code, language }),
  })

  if (!response.ok) {
    const error = await response.json()
    throw new Error(error.detail || 'Hint request failed')
  }

  return response.json()
}

export async function checkPlagiarism(code: string, language: string) {
  const response = await fetch(API_ENDPOINTS.plagiarism, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ code, language }),
  })

  if (!response.ok) {
    const error = await response.json()
    throw new Error(error.detail || 'Plagiarism check failed')
  }

  return response.json()
}
