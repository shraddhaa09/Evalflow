// components/common/Card.tsx
import { HTMLAttributes, ForwardedRef, forwardRef } from "react";
import styles from "./Card.module.css";

type CardVariant = "default" | "elevated" | "outlined" | "interactive";
type CardSize = "sm" | "md" | "lg";

type CardProps = {
  variant?: CardVariant;
  size?: CardSize;
  interactive?: boolean;
  hoverable?: boolean;
} & HTMLAttributes<HTMLDivElement>;

const Card = forwardRef<HTMLDivElement, CardProps>(
  (
    {
      variant = "default",
      size = "md",
      interactive = false,
      hoverable = false,
      className,
      children,
      ...props
    },
    ref
  ) => {
    const combinedClassName = [
      styles.card,
      styles[variant],
      styles[size],
      interactive && styles.interactive,
      hoverable && styles.hoverable,
      className || "",
    ]
      .filter(Boolean)
      .join(" ");

    return (
      <div ref={ref} className={combinedClassName} {...props}>
        {children}
      </div>
    );
  }
);

Card.displayName = "Card";

export default Card;