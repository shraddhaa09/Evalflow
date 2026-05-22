"use client";

import Link from "next/link";
import { useEffect } from "react";

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    console.error(error);
  }, [error]);

  return (
    <main className="state-screen">
      <div className="state-card">
        <div className="state-eyebrow">Unexpected error</div>
        <h1 className="state-title">Something went wrong</h1>
        <p className="state-text">
          An unexpected problem interrupted this page. You can try again or go
          back to the home page.
        </p>

        <div className="state-actions">
          <button type="button" className="btn-primary" onClick={() => reset()}>
            Try again
          </button>
          <Link href="/" className="btn-secondary">
            Go home
          </Link>
        </div>
      </div>
    </main>
  );
}