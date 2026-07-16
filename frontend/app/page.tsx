'use client'

import { useRouter } from 'next/navigation'
import './landing.css'

export default function LandingPage() {
  const router = useRouter()

  return (
    <>
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