# EvalCode Frontend (Basic)

A minimal Next.js frontend to test the EvalCode backend.

## Setup

```bash
# Install dependencies
npm install

# Copy environment
cp .env.example .env.local

# Start dev server
npm run dev
```

Visit `http://localhost:3000/ide`

## What works

- ✅ Code editor (textarea)
- ✅ Run code via `/execute` endpoint
- ✅ Terminal output display
- ✅ EVEE hint panel - get hints via `/hint` endpoint
- ✅ AI plagiarism check - displays results from `/plagiarism`
- ✅ Language selector (Python, JS, Java, C, C++)
- ✅ Elapsed time counter

## No ML yet

The plagiarism check will display whatever your backend returns. When your ML model is ready, it will automatically show the results.

## Structure

- `app/ide/page.tsx` - Main IDE workspace
- `components/` - UI components (Editor, Terminal, EVEE, TopBar, Modal)
- `hooks/` - Zustand stores for state
- `services/api.ts` - Backend API calls
- `lib/config.ts` - Config (API URL, etc)
