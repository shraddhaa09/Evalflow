import Link from "next/link";
import styles from "./LandingHero.module.css";

export default function LandingHero() {
  return (
    <section className={styles.hero} aria-labelledby="landing-hero-title">
      <div className={styles.left}>
        <div className={styles.kicker}>
          Built for honest practice and stronger problem solving
        </div>

        <h1 id="landing-hero-title" className={styles.title}>
          Write code with <span>confidence</span>.
        </h1>

        <p className={styles.description}>
          EvalCode gives students a focused environment to write, run, and
          improve their code with clarity. You stay in control of the thinking,
          while the platform supports better learning at every step.
        </p>

        <div className={styles.actions}>
          <Link href="/ide" className={styles.primaryButton}>
            Start coding
          </Link>
          <a href="#how-it-works" className={styles.secondaryButton}>
            See how it works
          </a>
        </div>

        <div className={styles.points}>
          <article className={styles.pointCard}>
            <h2>Real practice</h2>
            <p>
              Write every line yourself and build genuine problem-solving skill.
            </p>
          </article>

          <article className={styles.pointCard}>
            <h2>Instant feedback</h2>
            <p>
              Run code securely and inspect output, errors, timing, and memory
              right away.
            </p>
          </article>

          <article className={styles.pointCard}>
            <h2>Guided support</h2>
            <p>
              Get hints that strengthen your logic without replacing your work.
            </p>
          </article>
        </div>
      </div>

      <div className={styles.right}>
        <div className={styles.screen}>
          <div className={styles.screenTop}>
            <div className={styles.screenLabel}>Python workspace</div>
            <div className={styles.screenChip}>Guided hint available</div>
          </div>

          <div className={styles.codeBody} aria-label="Python code example">
            <div>
              <span className={styles.comment}>
                # binary search — student attempt
              </span>
            </div>
            <div>
              <span className={styles.keyword}>def</span>{" "}
              <span className={styles.functionName}>binary_search</span>(arr,
              target):
            </div>
            <div>
              &nbsp;&nbsp;left, right = <span className={styles.number}>0</span>
              , len(arr) - <span className={styles.number}>1</span>
            </div>
            <div>
              &nbsp;&nbsp;<span className={styles.keyword}>while</span> left
              &lt;= right:
            </div>
            <div>
              &nbsp;&nbsp;&nbsp;&nbsp;mid = (left + right) //{" "}
              <span className={styles.number}>2</span>
            </div>
            <div>
              &nbsp;&nbsp;&nbsp;&nbsp;<span className={styles.keyword}>if</span>{" "}
              arr[mid] == target:
            </div>
            <div>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              <span className={styles.keyword}>return</span> mid
            </div>
            <div>
              &nbsp;&nbsp;&nbsp;&nbsp;
              <span className={styles.comment}>
                # what should update when target is smaller or larger?
              </span>
            </div>
            <div>
              &nbsp;&nbsp;&nbsp;&nbsp;<span className={styles.cursor}>_</span>
            </div>
          </div>

          <aside className={styles.hintCard} aria-label="EVEE hint">
            <div className={styles.hintLabel}>EVEE hint</div>
            <p className={styles.hintText}>
              Focus on what binary search removes each time. Once you compare
              arr[mid] with target, decide which half can no longer contain the
              answer and move the boundaries accordingly.
            </p>
          </aside>
        </div>
      </div>
    </section>
  );
}