// components/common/Loader.tsx
import { HTMLAttributes, ForwardedRef, forwardRef } from "react";
import styles from "./Loader.module.css";

type LoaderVariant = "default" | "primary" | "white";
type LoaderSize = "sm" | "md" | "lg";

type LoaderProps = {
  variant?: LoaderVariant;
  size?: LoaderSize;
  label?: string;
} & HTMLAttributes<HTMLDivElement>;

const Loader = forwardRef<HTMLDivElement, LoaderProps>(
  (
    {
      variant = "default",
      size = "md",
      label,
      className,
      ...props
    },
    ref
  ) => {
    const combinedClassName = [
      styles.loader,
      styles[variant],
      styles[size],
      className || "",
    ]
      .filter(Boolean)
      .join(" ");

    return (
      <div ref={ref} className={combinedClassName} {...props}>
        <div className={styles.spinner} />
        {label && <span className={styles.label}>{label}</span>}
      </div>
    );
  }
);

Loader.displayName = "Loader";

export default Loader;