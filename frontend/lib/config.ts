export const appConfig = {
  appName: "EvalCode",
  appDescription: "Write honestly. Learn deeply. Improve with confidence.",
  defaultLanguage: "python",
  apiBaseUrl: process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000",
  pistonBaseUrl: process.env.NEXT_PUBLIC_PISTON_BASE_URL || "https://emkc.org/api/v2/piston",
  maxCodeLength: 20000,
  maxHintRequests: 3,
  plagiarismThresholds: {
    low: 40,
    medium: 70,
  },
} as const;

export type AppConfig = typeof appConfig;