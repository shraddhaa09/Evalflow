import Link from "next/link";
import styles from "./Navbar.module.css";

export default function Navbar() {
  return (
    <header className={styles.header}>
      <div className={styles.inner}>
        <Link href="/" className={styles.logo} aria-label="EvalCode home">
          <span className={styles.logoText}>Eval</span>
          <span className={styles.logoAccent}>Code</span>
        </Link>

        <nav className={styles.nav} aria-label="Primary navigation">
          <Link href="#features" className={styles.navLink}>
            Features
          </Link>
          <Link href="#how-it-works" className={styles.navLink}>
            How it works
          </Link>
          <Link href="/ide" className={styles.cta}>
            Start coding
          </Link>
        </nav>
      </div>
    </header>
  );
}