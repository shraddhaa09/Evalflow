// app/loading.tsx
import styles from "./loading.module.css";

export default function Loading() {
  return (
    <div className={styles.container}>
      <div className={styles.wrapper}>
        <div className={styles.logo}>
          <span>E</span>
          <span>v</span>
          <span>a</span>
          <span>l</span>
          <span>C</span>
          <span>o</span>
          <span>d</span>
          <span>e</span>
        </div>

        <div className={styles.spinnerWrapper}>
          <div className={styles.spinner} />
        </div>

        <p className={styles.text}>Loading EvalCode…</p>
      </div>
    </div>
  );
}