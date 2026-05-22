import Link from "next/link";
import styles from "./Footer.module.css";

export default function Footer() {
  return (
    <footer className={styles.footer}>
      <div className={styles.inner}>
        <div className={styles.brandBlock}>
          <Link href="/" className={styles.logo} aria-label="EvalCode home">
            <span className={styles.logoText}>Eval</span>
            <span className={styles.logoAccent}>Code</span>
          </Link>
          <p className={styles.tagline}>
            Write honestly. Learn deeply. Improve with confidence.
          </p>
        </div>

        <div className={styles.linksBlock}>
          <Link href="#features" className={styles.link}>
            Features
          </Link>
          <Link href="#how-it-works" className={styles.link}>
            How it works
          </Link>
          <Link href="/ide" className={styles.link}>
            Start coding
          </Link>
        </div>

        <div className={styles.metaBlock}>
          <p className={styles.meta}>Built for focused coding practice.</p>
          <p className={styles.copy}>© 2026 EvalCode</p>
        </div>
      </div>
    </footer>
  );
}