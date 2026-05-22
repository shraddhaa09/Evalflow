// app/error.tsx
"use client";

import { useEffect } from "react";
import styles from "./error.module.css";

type ErrorProps = {
  error: Error & { digest?: string };
  reset: () => void;
};

export default function Error({ error, reset }: ErrorProps) {
  useEffect(() => {
    // Log the error to an error reporting service in production
    console.error("App error:", error);
  }, [error]);

  return (
    <div className={styles.container}>
      <div className={styles.wrapper}>
        <div className={styles.iconCircle}>
          <span className={styles.icon}>!</span>
        </div>

        <h1 className={styles.title}>Something went wrong</h1>
        <p className={styles.description}>
          We’re sorry, but an unexpected error occurred while loading this page.
        </p>

        {error.message && (
          <details className={styles.details}>
            <summary>Error details</summary>
            <pre className={styles.errorText}>{error.message}</pre>
          </details>
        )}

        <div className={styles.actions}>
          <button className={styles.buttonPrimary} onClick={reset}>
            Try again
          </button>
          <a href="/" className={styles.buttonSecondary}>
            Go to homepage
          </a>
        </div>
      </div>
    </div>
  );
}