import type { Metadata } from "next";
import { Inter, JetBrains_Mono } from "next/font/google";
// @ts-ignore: CSS import handled by Next.js
import "./globals.css";

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-body",
  display: "swap",
});

const jetbrainsMono = JetBrains_Mono({
  subsets: ["latin"],
  variable: "--font-code",
  display: "swap",
});

export const metadata: Metadata = {
  title: "EvalCode — Write with confidence",
  description:
    "EvalCode is a focused coding environment where students write honestly, run code instantly, and improve with guided support.",
  keywords: [
    "EvalCode",
    "coding platform",
    "python sandbox",
    "student coding practice",
    "AI code detection",
    "guided hints",
  ],
  applicationName: "EvalCode",
  authors: [{ name: "EvalCode Team" }],
  creator: "EvalCode",
  metadataBase: new URL("http://localhost:3000"),
  openGraph: {
    title: "EvalCode — Write with confidence",
    description:
      "A focused coding environment for honest practice, instant execution, and guided learning.",
    url: "/",
    siteName: "EvalCode",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "EvalCode — Write with confidence",
    description:
      "A focused coding environment for honest practice, instant execution, and guided learning.",
  },
  robots: {
    index: true,
    follow: true,
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${inter.variable} ${jetbrainsMono.variable}`}>
        {children}
      </body>
    </html>
  );
}