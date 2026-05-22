import styles from "./FeaturesSection.module.css";

const features = [
  {
    number: "01",
    title: "Run code instantly",
    description:
      "Execute Python in a secure sandbox and inspect stdout, stderr, timing, and memory in one focused workspace.",
    tag: "Piston engine",
    featured: true,
  },
  {
    number: "02",
    title: "Review code authenticity",
    description:
      "Use AI-detection signals to identify unusual submission patterns and support more reliable evaluation.",
    tag: "ML classifier",
    featured: false,
  },
  {
    number: "03",
    title: "Learn with EVEE",
    description:
      "EVEE reads your current code and question, then gives a precise conceptual nudge instead of a full answer.",
    tag: "Hint engine",
    featured: false,
  },
];

export default function FeaturesSection() {
  return (
    <section className={styles.section} aria-labelledby="features-title">
      <div className={styles.inner}>
        <div className={styles.headingBlock}>
          <p className={styles.eyebrow}>Core capabilities</p>
          <h2 id="features-title" className={styles.title}>
            Built for focused coding and stronger learning outcomes.
          </h2>
          <p className={styles.subtitle}>
            EvalCode combines execution, review, and guided support in one
            streamlined environment designed for honest student work.
          </p>
        </div>

        <div className={styles.grid}>
          {features.map((feature) => (
            <article
              key={feature.number}
              className={`${styles.card} ${
                feature.featured ? styles.featuredCard : ""
              }`}
            >
              <div className={styles.cardTop}>
                <span className={styles.number}>{feature.number}</span>
                <span className={styles.tag}>{feature.tag}</span>
              </div>

              <h3 className={styles.cardTitle}>{feature.title}</h3>
              <p className={styles.cardDescription}>{feature.description}</p>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}