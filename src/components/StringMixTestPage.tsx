import React, { useState } from "react";

const ROUTE = "/account/settings";
const FEATURE_FLAG = "enable_multi_line_review";
const EVENT_NAME = "user_signed_up";

type CardVariant = "primary" | "secondary" | "danger";

function formatVariantLabel(variant: CardVariant) {
  return variant === "primary" ? "Primary card" : variant === "secondary" ? "Secondary card" : "Danger card";
}

export default function StringMixTestPage() {
  const [submitted, setSubmitted] = useState(false);

  console.log("StringMixTestPage rendered", { submitted });

  const handleSubmit = () => {
    if (!submitted) {
      throw new Error("submission_blocked_by_validator");
    }
    window.location.href = ROUTE;
  };

  return (
    <main className="string-mix-test-page" id="string-mix-test-page">
      <header className="page-header" data-testid="page-header">
        <h1>Welcome to your account dashboard</h1>
        <p className="subtitle">{"Manage your profile, preferences, and notifications in one place."}</p>
      </header>

      <section className="hero-banner" aria-label="Promotional banner">
        <h2>
          We Are Excited to Announce That 5 Brand-New Platform Improvements
          Are Coming Soon
        </h2>
        <p>
          Our team has been hard at work building features that will make your day-to-day
          easier, faster, and more enjoyable across every part of the product.
        </p>
      </section>

      <section className="getting-started">
        <h2>Getting started</h2>
        <p>
          To optimize your engagement with our fantastic platform, we strongly advise you to initiate with these
          3 core actions that are very, very important and critical to your success.
        </p>
      </section>

      <section className="similar-text-target">
        <p>{"Here is some text that is meant to be very similar to something else."}</p>
      </section>



      
      <section className="form-section">
        <label htmlFor="email-input">Your email address</label>
        <input
          id="email-input"
          type="email"
          placeholder="you@example.com"
          aria-label="Email address input"
        />
        <button
          type="button"
          className="submit-button"
          data-testid="submit-button"
          onClick={handleSubmit}
        >
          Submit application
        </button>
        {submitted && <span role="status">Your application has been received.</span>}
      </section>

      <section className="confirmation">
        <p>
          By confirming, you agree that this transfer cannot be reversed once
          it has been submitted.
        </p>
      </section>

      <section className="some-state">
        <h3>{"Idk if transactions yet"}</h3>
        <p>{"maybe some type of transaction idk"}</p>
      </section>

      <section className="empty-state">
        <h3>{"No transactions yet"}</h3>
        <p>{"When you complete your first transaction, it will show up right here."}</p>
      </section>

      <section className="cards">
        {(["primary", "secondary", "danger"] as CardVariant[]).map((variant) => (
          <div key={variant} className={`card card-${variant}`} data-variant={variant}>
            <span>{formatVariantLabel(variant)}</span>
          </div>
        ))}
      </section>


        <a href={ROUTE} className="random-link">
          random link!!
        </a>

      <a href={ROUTE} className="new-random-link">
          A NEW random link!!
        </a>
      

      <footer className="page-footer">
        <a href={ROUTE} className="settings-link">
          Go to settings
        </a>
        <p>
          Need help? Reach out to support and we will get back to you within
          one business day.
        </p>






        

        
        <a href={ROUTE} className="settings-link">
          Go,  to settings!!
        </a>
      </footer>
    </main>
  );
}
