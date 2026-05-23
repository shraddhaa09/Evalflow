'use client'

import { useRouter } from 'next/navigation'

export default function LandingPage() {
  const router = useRouter()

  return (
    <>
      <style>{`
        :root {
          --bg: #ffffff;
          --surface: #f7f9fc;
          --surface-2: #eef4ff;
          --text: #0f172a;
          --muted: #475569;
          --line: #dbe3f0;
          --blue: #155dfc;
          --blue-dark: #0f3fd1;
          --yellow: #f4c430;
          --yellow-soft: #fff4cc;
          --screen: #0f172a;
          --screen-2: #111827;
          --font-body: 'Inter', sans-serif;
          --font-code: 'JetBrains Mono', monospace;
          --radius-md: 18px;
          --shadow-sm: 0 10px 30px rgba(15, 23, 42, 0.06);
          --shadow-md: 0 20px 60px rgba(21, 93, 252, 0.12);
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        html { scroll-behavior: smooth; }
        .landing-body {
          font-family: var(--font-body);
          background: var(--bg);
          color: var(--text);
          line-height: 1.6;
          overflow-x: hidden;
          min-height: 100vh;
          position: relative;
        }
        a { color: inherit; text-decoration: none; }
        .landing-body::before {
          content: "";
          position: fixed;
          inset: 0;
          pointer-events: none;
          background:
            radial-gradient(circle at top right, rgba(21,93,252,0.08), transparent 28%),
            radial-gradient(circle at 20% 20%, rgba(244,196,48,0.10), transparent 24%);
          z-index: 0;
        }
        nav {
          position: fixed;
          top: 0; left: 0; right: 0;
          z-index: 50;
          display: flex;
          justify-content: space-between;
          align-items: center;
          padding: 18px 40px;
          background: rgba(255,255,255,0.88);
          backdrop-filter: blur(14px);
          border-bottom: 1px solid rgba(15,23,42,0.08);
        }
        .nav-logo { font-size: 1.1rem; font-weight: 800; letter-spacing: -0.03em; }
        .nav-logo span { color: var(--blue); }
        .nav-cta {
          background: var(--blue);
          color: white;
          border: none;
          padding: 12px 22px;
          border-radius: 999px;
          font-size: 0.92rem;
          font-weight: 700;
          cursor: pointer;
          transition: 0.2s ease;
          box-shadow: var(--shadow-sm);
        }
        .nav-cta:hover { background: var(--blue-dark); transform: translateY(-1px); }
        .hero {
          position: relative;
          z-index: 1;
          min-height: 100vh;
          display: grid;
          grid-template-columns: 1.08fr 0.92fr;
          align-items: center;
          padding-top: 82px;
        }
        .hero-left { padding: 72px 56px 72px 40px; }
        .hero-kicker {
          display: inline-flex;
          align-items: center;
          gap: 10px;
          padding: 8px 14px;
          border-radius: 999px;
          background: var(--yellow-soft);
          color: #7a5600;
          font-size: 0.84rem;
          font-weight: 700;
          margin-bottom: 24px;
          border: 1px solid rgba(244,196,48,0.45);
        }
        .hero-h1 {
          font-size: clamp(3rem, 6vw, 5.8rem);
          line-height: 0.95;
          letter-spacing: -0.06em;
          font-weight: 800;
          max-width: 620px;
        }
        .hero-h1 .accent { color: var(--blue); }
        .hero-sub {
          margin-top: 26px;
          max-width: 560px;
          color: var(--muted);
          font-size: 1.06rem;
          line-height: 1.8;
        }
        .hero-actions {
          display: flex;
          flex-wrap: wrap;
          gap: 14px;
          margin-top: 34px;
        }
        .btn-primary, .btn-secondary {
          padding: 15px 24px;
          border-radius: 999px;
          font-weight: 700;
          font-size: 0.96rem;
          cursor: pointer;
          transition: 0.2s ease;
        }
        .btn-primary {
          background: var(--blue);
          color: white;
          border: none;
          box-shadow: var(--shadow-md);
        }
        .btn-primary:hover { background: var(--blue-dark); transform: translateY(-2px); }
        .btn-secondary {
          background: white;
          color: var(--text);
          border: 1px solid var(--line);
        }
        .btn-secondary:hover { border-color: rgba(21,93,252,0.32); color: var(--blue); }
        .hero-points {
          display: grid;
          grid-template-columns: repeat(3, minmax(0,1fr));
          gap: 14px;
          margin-top: 42px;
          max-width: 700px;
        }
        .hero-point {
          background: white;
          border: 1px solid var(--line);
          border-radius: var(--radius-md);
          padding: 18px 16px;
          box-shadow: var(--shadow-sm);
        }
        .hero-point strong { display: block; font-size: 1rem; margin-bottom: 6px; }
        .hero-point span { font-size: 0.92rem; color: var(--muted); }
        .hero-right { padding: 56px 40px 56px 20px; }
        .screen {
          background: linear-gradient(180deg, var(--screen), var(--screen-2));
          border-radius: 30px;
          padding: 22px;
          box-shadow: 0 25px 80px rgba(2, 6, 23, 0.24);
          border: 1px solid rgba(255,255,255,0.06);
        }
        .screen-top {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin-bottom: 18px;
          padding-bottom: 14px;
          border-bottom: 1px solid rgba(255,255,255,0.08);
        }
        .screen-label { color: #cbd5e1; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
        .screen-chip {
          background: rgba(244,196,48,0.14);
          color: #ffe082;
          border: 1px solid rgba(244,196,48,0.25);
          padding: 6px 10px;
          border-radius: 999px;
          font-size: 0.74rem;
          font-weight: 700;
        }
        .code-body {
          font-family: var(--font-code);
          font-size: 0.92rem;
          line-height: 1.85;
          color: #dbeafe;
          padding: 4px 2px 0;
        }
        .c-cm { color: #7c8aa5; }
        .c-kw { color: #93c5fd; }
        .c-fn { color: #f8fafc; }
        .c-num { color: #facc15; }
        .c-var { color: #ffffff; }
        .hint-card {
          margin-top: 18px;
          background: linear-gradient(180deg, #fff8df, #fff2b8);
          border-radius: 22px;
          padding: 20px 22px;
          border: 1px solid rgba(244,196,48,0.45);
        }
        .hint-label { font-size: 0.76rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.12em; color: #8a6200; margin-bottom: 8px; }
        .hint-text { color: #332200; font-size: 0.95rem; line-height: 1.75; }
        .features { position: relative; z-index: 1; padding: 24px 40px 0; }
        .feature-grid { display: grid; grid-template-columns: 1.1fr 1fr 1fr; gap: 18px; }
        .feature-card {
          background: white;
          border: 1px solid var(--line);
          border-radius: 26px;
          padding: 30px;
          box-shadow: var(--shadow-sm);
        }
        .feature-card.primary {
          background: linear-gradient(180deg, #eff5ff, #ffffff);
          border-color: rgba(21,93,252,0.18);
        }
        .feature-number { font-size: 0.82rem; font-weight: 800; color: var(--blue); letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 18px; }
        .feature-title { font-size: 1.45rem; line-height: 1.15; font-weight: 800; letter-spacing: -0.03em; margin-bottom: 12px; }
        .feature-desc { color: var(--muted); font-size: 0.98rem; line-height: 1.75; margin-bottom: 18px; }
        .feature-tag {
          display: inline-flex;
          align-items: center;
          padding: 8px 12px;
          border-radius: 999px;
          background: var(--surface-2);
          color: var(--blue);
          font-size: 0.78rem;
          font-weight: 700;
        }
        .how { position: relative; z-index: 1; padding: 90px 40px; }
        .how-wrap {
          background: linear-gradient(180deg, #0f172a, #111827);
          border-radius: 32px;
          overflow: hidden;
          box-shadow: 0 30px 80px rgba(2, 6, 23, 0.18);
        }
        .how-head {
          display: flex;
          justify-content: space-between;
          align-items: flex-end;
          gap: 20px;
          padding: 34px 34px 24px;
          border-bottom: 1px solid rgba(255,255,255,0.08);
        }
        .how-head h2 { color: white; font-size: clamp(2rem, 4vw, 3.2rem); line-height: 1; letter-spacing: -0.05em; }
        .how-head p { color: #94a3b8; max-width: 520px; font-size: 0.98rem; }
        .how-steps { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1px; background: rgba(255,255,255,0.06); }
        .step { background: rgba(255,255,255,0.02); padding: 28px; min-height: 220px; }
        .step-num { color: #f4c430; font-size: 0.8rem; font-weight: 800; letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 14px; }
        .step-title { color: white; font-size: 1.24rem; font-weight: 800; margin-bottom: 10px; letter-spacing: -0.03em; }
        .step-desc { color: #cbd5e1; font-size: 0.95rem; line-height: 1.75; }
        .cta-strip { position: relative; z-index: 1; padding: 0 40px 90px; }
        .cta-box {
          background: linear-gradient(135deg, #155dfc, #0f3fd1);
          color: white;
          border-radius: 32px;
          padding: 42px 34px;
          display: flex;
          justify-content: space-between;
          align-items: center;
          gap: 22px;
          box-shadow: var(--shadow-md);
        }
        .cta-box h3 { font-size: clamp(2rem, 4vw, 3.1rem); line-height: 1; letter-spacing: -0.05em; margin-bottom: 10px; }
        .cta-box p { color: rgba(255,255,255,0.82); max-width: 560px; }
        .btn-white {
          background: white;
          color: var(--blue);
          white-space: nowrap;
          padding: 15px 24px;
          border-radius: 999px;
          font-weight: 700;
          font-size: 0.96rem;
          cursor: pointer;
          border: none;
          transition: 0.2s ease;
          box-shadow: none;
        }
        .btn-white:hover { transform: translateY(-2px); }
        footer {
          padding: 24px 40px 34px;
          display: flex;
          justify-content: space-between;
          align-items: flex-start;
          gap: 20px;
          flex-wrap: wrap;
          color: var(--muted);
          font-size: 0.9rem;
          border-top: 1px solid rgba(15,23,42,0.08);
          position: relative;
          z-index: 1;
        }
        .footer-links {
          display: flex;
          flex-direction: column;
          gap: 8px;
        }
        .footer-links a {
          display: inline-flex;
          align-items: center;
          gap: 7px;
          color: var(--muted);
          font-size: 0.88rem;
          font-weight: 500;
          transition: color 0.15s ease;
        }
        .footer-links a:hover { color: var(--blue); }
        .footer-links-label {
          font-size: 0.75rem;
          font-weight: 700;
          text-transform: uppercase;
          letter-spacing: 0.1em;
          color: #94a3b8;
          margin-bottom: 4px;
        }
        .footer-love {
          font-size: 0.88rem;
          color: var(--muted);
          text-align: right;
          line-height: 1.7;
        }
        .footer-love span { color: #e74c7a; }
        @media (max-width: 1100px) {
          .hero { grid-template-columns: 1fr; min-height: auto; }
          .feature-grid { grid-template-columns: 1fr; }
          .how-steps { grid-template-columns: 1fr 1fr; }
          .cta-box { flex-direction: column; }
          .hero-left, .hero-right, .features, .how, .cta-strip, footer, nav { padding-left: 20px; padding-right: 20px; }
          .hero-left { padding-top: 48px; padding-bottom: 26px; }
          .hero-right { padding-top: 10px; }
          .hero-points { grid-template-columns: 1fr; }
          .how-head { align-items: flex-start; flex-direction: column; }
        }
        @media (max-width: 720px) {
          .hero-h1 { font-size: 2.8rem; }
          .how-steps { grid-template-columns: 1fr; }
          .feature-card, .step, .screen { border-radius: 22px; }
          .nav-cta, .btn-primary, .btn-secondary, .btn-white { width: 100%; text-align: center; }
          .hero-actions { flex-direction: column; }
        }
      `}</style>

      <link
        rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap"
      />
      <link rel="icon" href="/favicon.ico" type="image/x-icon" />

      <div className="landing-body">
        <nav>
          <div className="nav-logo">Eval<span>Code</span></div>
          <button className="nav-cta" onClick={() => router.push('/ide')}>Start coding</button>
        </nav>

        <section className="hero">
          <div className="hero-left">
            <div className="hero-kicker">Built for honest practice and better problem solving</div>
            <h1 className="hero-h1">
              Write code with <span className="accent">confidence</span>.
            </h1>
            <p className="hero-sub">
              EvalCode gives students a focused environment to write, run, and improve their code with clarity.
              You stay in control of the thinking, while the platform supports better learning at every step.
            </p>
            <div className="hero-actions">
              <button className="btn-primary" onClick={() => router.push('/ide')}>Start coding</button>
              <a href="#how" className="btn-secondary">See how it works</a>
            </div>
            <div className="hero-points">
              <div className="hero-point">
                <strong>Real practice</strong>
                <span>Write every line yourself and build genuine problem-solving skill.</span>
              </div>
              <div className="hero-point">
                <strong>Instant feedback</strong>
                <span>Run code securely and inspect output, errors, timing, and memory right away.</span>
              </div>
              <div className="hero-point">
                <strong>Guided support</strong>
                <span>Get hints that strengthen your logic without replacing your work.</span>
              </div>
            </div>
          </div>

          <div className="hero-right">
            <div className="screen">
              <div className="screen-top">
                <div className="screen-label">Python workspace</div>
                <div className="screen-chip">Guided hint available</div>
              </div>
              <div className="code-body">
                <div><span className="c-cm"># binary search — student attempt</span></div>
                <div><span className="c-kw">def</span> <span className="c-fn">binary_search</span>(arr, target):</div>
                <div>&nbsp;&nbsp;left, right = <span className="c-num">0</span>, len(arr) - <span className="c-num">1</span></div>
                <div>&nbsp;&nbsp;<span className="c-kw">while</span> left &lt;= right:</div>
                <div>&nbsp;&nbsp;&nbsp;&nbsp;mid = (left + right) // <span className="c-num">2</span></div>
                <div>&nbsp;&nbsp;&nbsp;&nbsp;<span className="c-kw">if</span> arr[mid] == target:</div>
                <div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span className="c-kw">return</span> mid</div>
                <div>&nbsp;&nbsp;&nbsp;&nbsp;<span className="c-cm"># what should update when target is smaller or larger?</span></div>
                <div>&nbsp;&nbsp;&nbsp;&nbsp;<span className="c-var">_</span></div>
              </div>
              <div className="hint-card">
                <div className="hint-label">EVEE hint</div>
                <div className="hint-text">
                  Focus on what binary search removes each time. Once you compare arr[mid] with target,
                  decide which half can no longer contain the answer and move the boundaries accordingly.
                </div>
              </div>
            </div>
          </div>
        </section>

        <section className="features">
          <div className="feature-grid">
            <article className="feature-card primary">
              <div className="feature-number">01</div>
              <div className="feature-title">Run code instantly</div>
              <div className="feature-desc">
                Execute Python in a secure sandbox and inspect stdout, stderr, timing, and memory in one focused workspace.
              </div>
              <div className="feature-tag">Piston engine</div>
            </article>
            <article className="feature-card">
              <div className="feature-number">02</div>
              <div className="feature-title">Review code authenticity</div>
              <div className="feature-desc">
                Use AI-detection signals to identify unusual submission patterns and support more reliable evaluation.
              </div>
              <div className="feature-tag">ML classifier</div>
            </article>
            <article className="feature-card">
              <div className="feature-number">03</div>
              <div className="feature-title">Learn with EVEE</div>
              <div className="feature-desc">
                EVEE reads your current code and question, then gives a precise conceptual nudge instead of a full answer.
              </div>
              <div className="feature-tag">Hint engine</div>
            </article>
          </div>
        </section>

        <section className="how" id="how">
          <div className="how-wrap">
            <div className="how-head">
              <div><h2>How it works</h2></div>
              <p>
                The experience is designed to keep students focused, independent, and steadily improving
                from one attempt to the next.
              </p>
            </div>
            <div className="how-steps">
              <div className="step">
                <div className="step-num">Step 01</div>
                <div className="step-title">Write</div>
                <div className="step-desc">Use the editor to build your solution line by line in your own words.</div>
              </div>
              <div className="step">
                <div className="step-num">Step 02</div>
                <div className="step-title">Run</div>
                <div className="step-desc">Execute your code in a sandboxed environment and inspect the result immediately.</div>
              </div>
              <div className="step">
                <div className="step-num">Step 03</div>
                <div className="step-title">Get a hint</div>
                <div className="step-desc">Ask EVEE when you are stuck and receive a targeted conceptual nudge.</div>
              </div>
              <div className="step">
                <div className="step-num">Step 04</div>
                <div className="step-title">Improve</div>
                <div className="step-desc">
                  Review signals, refine your logic, and develop a stronger understanding of your solution.
                </div>
              </div>
            </div>
          </div>
        </section>

        <section className="cta-strip">
          <div className="cta-box">
            <div>
              <h3>Built to help students think clearly.</h3>
              <p>
                EvalCode creates a more trustworthy coding environment where practice feels focused,
                feedback feels useful, and progress feels earned.
              </p>
            </div>
            <button className="btn-white" onClick={() => router.push('/ide')}>Start coding</button>
          </div>
        </section>

        <footer>
          <div>
            <div><strong>EvalCode</strong></div>
            <div style={{ marginTop: '4px', fontSize: '0.88rem' }}>Write honestly. Learn deeply. Improve with confidence.</div>
            <div style={{ marginTop: '2px', fontSize: '0.84rem', color: '#94a3b8' }}>Built with FastAPI and Next.js</div>
          </div>

          <div className="footer-links">
            <div className="footer-links-label">Useful links</div>
            <a href="https://github.com/SharwillKhisti/EvalCode" target="_blank" rel="noopener noreferrer">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                <path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844a9.59 9.59 0 012.504.337c1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/>
              </svg>
              GitHub — EvalCode
            </a>
          </div>

          <div className="footer-love">
            Made with <span>❤️</span> by<br />
            <strong style={{ color: 'var(--text)' }}>SY CS F 16</strong>
          </div>
        </footer>
      </div>
    </>
  )
}