// components/common/SectionHeading.tsx
import { forwardRef, HTMLAttributes } from "react";
import styles from "./SectionHeading.module.css";

type SectionHeadingAs = "h1" | "h2" | "h3" | "h4" | "h5" | "h6";

type SectionHeadingProps = {
  as?: SectionHeadingAs;
  align?: "left" | "center" | "right";
  size?: "sm" | "md" | "lg" | "xl";
  subtitle?: string;
} & HTMLAttributes<HTMLDivElement>;

const SectionHeading = forwardRef<HTMLDivElement, SectionHeadingProps>(
  (
    {
      as = "h2",
      align = "left",
      size = "lg",
      subtitle,
      className,
      children,
      ...props
    },
    ref
  ) => {
    const Tag: keyof JSX.IntrinsicElements = as;

    const combinedClassName = [
      styles.container,
      styles[align],
      styles[size],
      className || "",
    ]
      .filter(Boolean)
      .join(" ");

    return (
      <div ref={ref} className={combinedClassName} {...props}>
        {subtitle && <div className={styles.subtitle}>{subtitle}</div>}
        <Tag className={styles.title}>{children}</Tag>
      </div>
    );
  }
);

SectionHeading.displayName = "SectionHeading";

export default SectionHeading;