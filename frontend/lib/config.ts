export const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

export const API_ENDPOINTS = {
  execute: `${API_URL}/execute`,
  hint: `${API_URL}/hint`,
  plagiarism: `${API_URL}/plagiarism`,
  session: `${API_URL}/session`,
}
