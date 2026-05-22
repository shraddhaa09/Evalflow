import styles from "./Editor.module.css";

type EditorProps = {
  code: string;
  onChange: (value: string) => void;
};

export default function Editor({ code, onChange }: EditorProps) {
  return (
    <section className={styles.wrapper} aria-label="Code editor">
      <div className={styles.header}>
        <div>
          <p className={styles.eyebrow}>Editor</p>
          <h2 className={styles.title}>Write your solution</h2>
        </div>
        <div className={styles.status}>Manual input only</div>
      </div>

      <div className={styles.editorShell}>
        <div className={styles.lineRail} aria-hidden="true">
          {code.split("\n").map((_, index) => (
            <span key={index}>{index + 1}</span>
          ))}
        </div>

        <textarea
          value={code}
          onChange={(e) => onChange(e.target.value)}
          spellCheck={false}
          className={styles.textarea}
          placeholder={`def binary_search(arr, target):\n    left, right = 0, len(arr) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if arr[mid] == target:\n            return mid`}
        />
      </div>
    </section>
  );
}