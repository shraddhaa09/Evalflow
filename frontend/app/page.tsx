import Navbar from "@/components/layout/Navbar";
import LandingHero from "@/components/landing/LandingHero";
import FeaturesSection from "@/components/landing/FeaturesSection";
import HowItWorksSection from "@/components/landing/HowItWorksSection";
import LandingCTA from "@/components/landing/LandingCTA";
import Footer from "@/components/layout/Footer";

export default function HomePage() {
  return (
    <>
      <Navbar />
      <main>
        <LandingHero />
        <FeaturesSection />
        <HowItWorksSection />
        <LandingCTA />
      </main>
      <Footer />
    </>
  );
}