import Link from "next/link";

export default function NotFound() {
  return (
    <main className="state-screen">
      <div className="state-card">
        <div className="state-eyebrow">404</div>
        <h1 className="state-title">Page not found</h1>
        <p className="state-text">
          The page you are looking for does not exist or may have been moved to
          a different location.
        </p>

        <div className="state-actions">
          <Link href="/" className="btn-primary">
            Back to home
          </Link>
          <Link href="/ide" className="btn-secondary">
            Open IDE
          </Link>
        </div>
      </div>
    </main>
  );
}