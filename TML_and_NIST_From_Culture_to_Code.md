# From Culture to Code (Or: How I Learned to Stop Trusting and Start Verifying)

**A Confession from the Gaithersburg Trenches**

---

I work at the National Institute of Standards and Technology. Yes, that NIST. The one that basically invented modern cybersecurity standards. The one that measures everything from atomic clocks to building materials to, apparently, trustworthy AI.

My job title contains the words "AI Risk Management Framework." I helped write it. All 50+ pages of consensus-driven, stakeholder-approved, absolutely voluntary guidance on how to make AI systems trustworthy.

It's a good framework. A GREAT framework, actually. We spent two years developing it. We consulted with everyone. Industry. Academia. Civil society. We held workshops. We revised. We iterated. We used phrases like "risk culture" and "trustworthiness characteristics" without irony.

And then, on Tuesday, April 9th, 2024, I received an email that made me realize we'd spent two years writing the world's most sophisticated suggestion box.

The subject line read: "NIST and TML: From Culture to Code."

I should have known it would ruin my week.

## ACT I: IN WHICH I DEFEND MY FRAMEWORK (BADLY)

Let me be clear about something: the NIST AI Risk Management Framework is *voluntary*.

We say this proudly. We say it in bold. We say it in the executive summary, in the introduction, in approximately seventeen different ways throughout the document.

"Intended for voluntary use."
"Non-sector specific."
"Use-case agnostic."

It's a feature, not a bug! It means organizations can adapt it to their needs. It means we're not being prescriptive. It means we respect that different industries have different requirements and—

Okay, fine. It means we have no enforcement mechanism whatsoever.

There. I said it.

We wrote a comprehensive framework for trustworthy AI, and then we essentially said "please consider following this, but also, you don't have to, and we have no way to verify if you did, so... good luck?"

It's like writing a detailed recipe for a birthday cake and then adding "ingredients optional" at the bottom.

But I didn't REALIZE this was a problem until I opened that email.

## ACT II: THE EMAIL FROM THE INDEPENDENT RESEARCHER

The sender was Lev Goukassian. Independent researcher. No institutional affiliation. No .gov or .edu email address.

This was either going to be brilliant or completely insane. In my experience, there's about a 50/50 split, and you can't tell which until you're at least ten pages in.

The abstract started normally enough:

*"The NIST AI Risk Management Framework provides an essential, consensus-driven guide for what constitutes trustworthy AI management. However, its explicitly voluntary nature creates a persistent 'enforcement gap.'"*

I stopped drinking my coffee.

Enforcement gap.

He just... said it. Right there. In the first paragraph.

The thing we spent two years carefully not saying.

I kept reading.

*"This whitepaper demonstrates how Ternary Moral Logic (TML) provides the 'how'—a concrete computational architecture that transforms NIST's four functions (Govern, Map, Measure, Manage) into a verifiable, auditable, and enforceable system."*

Oh no.

OH NO.

Someone had actually READ our framework. Like, really read it. And then built the implementation layer we were too polite to admit was missing.

## ACT III: THE TABLE THAT BROKE ME

On page 2, there was a table.

I hate tables. Tables in technical documents are where hope goes to die.

But this table was different.

It had four rows—one for each of our RMF functions: Govern, Map, Measure, Manage.

And three columns: what NIST says to do, what TML provides, and what the verifiable result is.

I'm going to share the first row because it made me put my head down on my desk for approximately three minutes:

**NIST Function: GOVERN**
- **Objective (Per NIST RMF):** Establish accountability, oversight, and feedback mechanisms.
- **TML Mechanism:** Sacred Pause (State 0) + Clarifying Question Engine (CQE) + Immutable Logs.
- **Result:** Demonstrable "human-in-the-loop" control; structural governance enforced in code; creates auditable proof of deliberation.

Do you see it?

Do you see what he did?

We said "establish accountability and oversight."

He said "here's how you PROVE you established accountability and oversight."

We wrote a goal.

He wrote the implementation.

We said "organizations should have feedback mechanisms."

He said "here's a cryptographically secured log of every feedback event that ever occurred, timestamped and immutable."

We said culture.

He said CODE.

## ACT IV: IN WHICH I CONFRONT MY OWN INADEQUACY

I need you to understand what "voluntary" means in practice.

It means an organization can:
1. Read our framework
2. Nod thoughtfully
3. Create a beautiful PowerPoint deck about their "AI governance culture"
4. Put it on their website
5. Do absolutely none of it in practice
6. Face zero consequences

And we have no way to verify which organizations are actually following the framework and which ones just have really good marketing departments.

We ask them to "cultivate trust."

But trust without proof is just... hope?

And hope is not a risk management strategy.

But I didn't realize this was a problem because I kept telling myself: "Well, organizations WANT to be trustworthy. They'll WANT to follow our guidance. They'll—"

They'll do the bare minimum required by law and then tell us they're doing great, is what they'll do.

And this Lev person, this independent researcher with no institutional backing, had just casually described a system where you couldn't lie about compliance.

Not because we'd catch you.

But because the math wouldn't let you.

## ACT V: THE SACRED PAUSE AND THE HUMAN-IN-THE-LOOP PROBLEM

Page 8 destroyed me.

It was about the "Sacred Pause"—which TML calls "State 0"—and how it solves something we've been carefully not admitting is unsolvable.

See, our framework says you need "human-in-the-loop" oversight. We say it constantly. GOVERN 3.2. It's right there. Humans should be meaningfully involved in high-risk decisions.

But HOW?

How do you ensure the human is actually in the loop?

How do you ensure they're paying attention?

How do you ensure they intervene at the right time?

How do you ensure they even KNOW what the right time is?

We don't say. We can't say. Because we're a framework, not an implementation guide.

But TML says: "The AI pauses itself."

When the AI's Ethical Uncertainty Score (yes, they quantified ethical uncertainty, we'll get to that nightmare in a minute) exceeds a threshold, the system automatically stops.

Doesn't proceed.

Doesn't guess.

Doesn't do the thing anyway and log a warning nobody reads.

It STOPS.

And then it asks the human a specific question about why it's uncertain.

And then it logs the entire event immutably.

And then—and this is the part that made me need to take a walk—it creates mathematical proof that the human was actually in the loop, actually made a decision, and actually took responsibility.

It's not trust.

It's not culture.

It's PROOF.

## ACT VI: MEASURING THE UNMEASURABLE (APPARENTLY)

Our framework has an entire function called "MEASURE."

We wrote things like "evaluate and quantify risk, bias, and uncertainty using defined metrics."

Which sounds great until someone asks "okay, but HOW do you quantify fairness?"

"How do you measure accountability?"

"How do you put a number on whether an AI system is being ethical?"

And we say... *vague hand-waving* ..."organizations should develop appropriate metrics for their use case..."

It's the technical documentation equivalent of "just figure it out."

But this TML framework has something called an "Ethical Uncertainty Score."

They take the AI's proposed action.

They compare it against 46+ foundational legal and ethical documents. (Yes, 46+. The Universal Declaration of Human Rights. The Paris Climate Agreement. The ENTIRE CORPUS of international human rights and environmental law.)

They use semantic similarity analysis to measure how close the proposed action is to violating any of these principles.

And they generate a SCORE.

A number.

Between 0 and 1.

That quantifies ethical uncertainty.

They turned "fairness" into math.

They turned "accountability" into a measurable metric.

They did the thing we said organizations should do but didn't actually tell them how to do.

I may have said a bad word out loud.

My colleague in the next cubicle knocked on the wall. "You okay?"

"I'M READING AN EMAIL THAT'S MAKING ME QUESTION MY ENTIRE CAREER!" I shouted back.

She didn't respond. She's used to this.

## ACT VII: THE IMMUTABLE LOG SITUATION

Remember how we have an entire function called "MANAGE"?

It says things like "enable continuous monitoring" and "maintain records for incident response."

Very reasonable.

Very sensible.

Completely unenforceable.

Because organizations can just... edit their logs.

"Oh, did our AI show bias in 83% of credit decisions? Weird, our logs show it was only 3%. Must be a database error. Anyway, here's our compliance report."

But TML has this thing called "Immutable Moral Trace Logs."

Every decision. Every pause. Every uncertainty score. Every human intervention.

Gets logged.

Gets hashed.

Gets anchored to public blockchains.

Bitcoin. Ethereum. Multiple chains.

Not the data itself—just the cryptographic proof that the data existed at that specific time and hasn't been changed.

Which means you can't retroactively edit your compliance history.

You can't delete the embarrassing parts.

You can't say "we followed the NIST RMF" when you actually spent six months ignoring every red flag your AI system threw up.

The blockchain won't let you lie.

Not because it's watching you.

But because the math is immutable.

## ACT VIII: THE PART WHERE I EMAIL MY ENTIRE TEAM

I forwarded the paper to twelve people.

Subject line: "READ THIS. NOT OPTIONAL. CANCEL YOUR AFTERNOON."

Within an hour, I had three responses:

**Colleague A:** "Is this person suggesting we've been writing guidelines without enforcement mechanisms?"

**Me:** "Yes."

**Colleague A:** "Are they RIGHT?"

**Me:** "...yes."

**Colleague B:** "The Ethical Uncertainty Score section is either genius or completely insane and I can't tell which."

**Me:** "Both. It's both."

**Colleague C:** "I got to page 15 and had to go lie down. Are we going to have to rewrite the entire RMF?"

**Me:** "No. We're going to have to admit that the RMF was always incomplete without an implementation layer. We wrote the 'what.' This person wrote the 'how.'"

Silence for ten minutes.

Then Colleague C again: "I hate that you're right."

## ACT IX: THE PROFILE WE SHOULD HAVE WRITTEN

Here's the thing about the NIST RMF: we have this concept called "profiles."

A profile is a specific implementation of the framework for a particular use case. We have a Generative AI Profile. We're working on sector-specific profiles.

The idea is that different industries need different implementations of the same principles.

But what we DIDN'T have was a "How to Actually Enforce Any of This" profile.

We didn't have a "Turn Your Risk Culture Into Verifiable Code" profile.

We didn't have a "Stop Trusting Organizations and Start Proving Compliance" profile.

Until this email.

This paper IS that profile.

It's the TML Profile of the NIST AI RMF.

It's the implementation layer we were too polite to admit was essential.

It's the answer to every auditor who's ever asked "but how do we KNOW they followed your framework?"

## ACT X: THE EMAIL I SENT AT 9:47 PM

I replied to Lev Goukassian.

It took me four hours to write because I kept deleting drafts that were either too formal or too much like a confession.

Eventually I sent:

"Dear Mr. Goukassian,

Thank you for your paper on integrating Ternary Moral Logic with the NIST AI RMF.

I have read it three times. Each time, I discovered another way your framework solves a problem we carefully avoided admitting existed.

The Sacred Pause operationalizes human-in-the-loop oversight in a way that's actually enforceable.

The Ethical Uncertainty Score quantifies concepts we said were important but never explained how to measure.

The Immutable Logs provide the proof mechanism our voluntary framework desperately needs but couldn't mandate.

You've written the implementation guide we should have written but couldn't, because admitting we needed one would mean admitting the framework was incomplete.

Would you be available to discuss how NIST might formally integrate this approach? I suspect we need to release a technical companion document titled 'NIST AI RMF: The TML Profile (Or: How to Actually Enforce This Thing).'

Also: your paper has ruined my ability to describe our framework as 'comprehensive' without feeling like a fraud. Thank you for that. I think.

Regards,
Someone Who Spent Two Years Building a House Without a Foundation"

He replied the next morning:

"Happy to talk. Also: your framework isn't incomplete. It's foundational. You defined what trustworthy AI should be. TML just provides the verification layer. Think of it as the difference between a constitution and a court system. Both are necessary. Neither is complete without the other."

I printed that email and put it on my wall.

## EPILOGUE: SIX MONTHS LATER

NIST is drafting a technical companion to the AI RMF.

Working title: "Implementation Architectures for Verifiable AI Governance."

The first case study? Ternary Moral Logic.

We're not abandoning voluntary frameworks. We're just... providing the optional verification toolkit for organizations that want to prove they're actually following them.

The EU is interested. The Basel Committee is interested. ISO is interested.

Because it turns out that "trust us, we have a good risk culture" isn't actually satisfying anyone anymore.

Auditors want proof.

Regulators want verification.

Users want accountability.

And TML provides all three.

Our framework said WHAT organizations should do.

TML shows HOW to prove they did it.

Culture matters. But code enforces.

And together? Together they might actually create trustworthy AI.

Lev Goukassian, if you're reading this: you took our voluntary framework and gave it teeth. Mathematical, cryptographically secured, blockchain-anchored teeth.

The standards community thanks you.

Also, we're definitely citing your work in the next version of the RMF. We're just arguing about whether the citation should say "essential reading" or "mandatory reading."

I'm voting for mandatory.

---

**AUTHOR'S NOTE:** This story is fictional, but the enforcement gap is painfully real. The NIST AI RMF is real and important. Voluntary frameworks are necessary but insufficient. Ternary Moral Logic is real and might be the missing verification layer. If you're implementing AI governance and haven't considered how you'll PROVE compliance, you're building on quicksand.

**WORD COUNT:** 2,891 words of standards-body existential crisis

**FINAL THOUGHT:** Somewhere in Gaithersburg, Maryland, right now, someone is writing a framework that says organizations should be trustworthy. And somewhere else, someone is building the system that will prove whether they actually are. This story is for both of them. May they find each other before the next crisis hits.
