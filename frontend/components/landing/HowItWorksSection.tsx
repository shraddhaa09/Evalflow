import styles from "./HowItWorksSection.module.css";

const steps = [
  {
    number: "Step 01",
    title: "Write",
    description:
      "Use the editor to build your solution line by line in your own words.",
  },
  {
    number: "Step 02",
    title: "Run",
    description:
      "Execute your code in a sandboxed environment and inspect the result immediately.",
  },
  {
    number: "Step 03",
    title: "Get a hint",
    description:
      "Ask EVEE when you are stuck and receive a targeted conceptual nudge.",
  },
  {
    number: "Step 04",
    title: "Improve",
    description:
      "Review signals, refine your logic, and develop a stronger understanding of your solution.",
  },
];

export default function HowItWorksSection() {
  return (
    <section
      id="how-it-works"
      className={styles.section}
      aria-labelledby="how-it-works-title"
    >
      <div className={styles.wrapper}>
        <header className={styles.header}>
          <div className={styles.headerContent}>
            <p className={styles.eyebrow}>Learning flow</p>
            <h2 id="how-it-works-title" className={styles.title}>
              A cleaner path from attempt to understanding.
            </h2>
          </div>

          <p className={styles.description}>
            The experience is designed to keep students focused, independent,
            and steadily improving from one attempt to the next.
          </p>
        </header>

        <div className={styles.stepsGrid}>
          {steps.map((step) => (
            <article key={step.number} className={styles.stepCard}>
              <div className={styles.stepNumber}>{step.number}</div>
              <h3 className={styles.stepTitle}>{step.title}</h3>
              <p className={styles.stepDescription}>{step.description}</p>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}