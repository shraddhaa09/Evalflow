export default function Loading() {
  return (
    <main className="state-screen" aria-busy="true" aria-live="polite">
      <div className="state-card">
        <div className="loading-pulse" aria-hidden="true">
          <span />
          <span />
          <span />
        </div>
        <div className="state-eyebrow">Loading</div>
        <h1 className="state-title">Preparing EvalCode</h1>
        <p className="state-text">
          We are setting up the experience so you can start writing and running
          code without interruption.
        </p>
      </div>
    </main>
  );
}