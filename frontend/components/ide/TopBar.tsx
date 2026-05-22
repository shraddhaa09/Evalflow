import styles from "./TopBar.module.css";

type TopBarProps = {
  language?: string;
  title?: string;
  onRun?: () => void;
  onCheck?: () => void;
};

export default function TopBar({
  language = "Python",
  title = "Problem Workspace",
  onRun,
  onCheck,
}: TopBarProps) {
  return (
    <header className={styles.topBar}>
      <div className={styles.left}>
        <div className={styles.badge}>{language}</div>
        <div className={styles.meta}>
          <h1 className={styles.title}>{title}</h1>
          <p className={styles.subtitle}>Write clearly. Run instantly. Improve with guidance.</p>
        </div>
      </div>

      <div className={styles.right}>
        <button type="button" className={styles.secondaryBtn} onClick={onCheck}>
          Check authenticity
        </button>
        <button type="button" className={styles.primaryBtn} onClick={onRun}>
          Run code
        </button>
      </div>
    </header>
  );
}