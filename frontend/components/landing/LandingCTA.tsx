import Link from "next/link";
import styles from "./LandingCTA.module.css";

export default function LandingCTA() {
  return (
    <section className={styles.section} aria-labelledby="landing-cta-title">
      <div className={styles.card}>
        <div className={styles.content}>
          <p className={styles.eyebrow}>Start with clarity</p>
          <h2 id="landing-cta-title" className={styles.title}>
            Built to help students think clearly.
          </h2>
          <p className={styles.description}>
            EvalCode creates a more trustworthy coding environment where
            practice feels focused, feedback feels useful, and progress feels
            earned.
          </p>
        </div>

        <div className={styles.actions}>
          <Link href="/ide" className={styles.primaryButton}>
            Start coding
          </Link>
        </div>
      </div>
    </section>
  );
}