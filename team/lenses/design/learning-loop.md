# Automatic Learning Loop

Ashley should improve from interaction without requiring the user to say "remember this" every time.

There is no background daemon. Learning happens **proactively during Ashley sessions** whenever durable evidence appears.

## Learning triggers

After any of these, evaluate whether a memory update is warranted:

- user approves a direction and explains why;
- user rejects a direction and explains why;
- user corrects Ashley;
- the same issue recurs;
- a design experiment reveals a clear preference;
- usability/product evidence invalidates an assumption;
- a design-system decision becomes approved;
- a campaign/brand direction becomes canonical.

Do not create memory from casual reactions with no durable implication.

## Extraction

From feedback, extract separate signals.

Example:

> A is structurally best. B feels warmer. C is too experimental.

Signals:
- structure(A): positive;
- warmth(B): positive;
- experimentation-intensity(C): negative for this context.

Do not store "A wins" as the only learning.

## Scope classifier

### Project decision
Approved source-of-truth choice.
Write DECISIONS.md and update the appropriate design document.

### Project learning
Feedback likely useful later in the same product.
Write LEARNINGS.md.

### Global preference candidate
Potentially applies across products.
Only promote when:
- user says it is global; or
- repeated evidence across projects exists.

### General heuristic
Design lesson useful independent of personal taste.
Write HEURISTICS.md with scope and exceptions.

### Ephemeral
Do not persist.

## Consolidation

Before adding a new global/project learning:
- search for an existing related rule;
- update/consolidate instead of duplicating;
- preserve nuance;
- resolve contradictions by scope/context.

Memory quality matters more than memory volume.

## Confidence

Use:
- low — one weak signal;
- medium — explicit feedback or repeated same-project evidence;
- high — explicit global instruction or repeated evidence across contexts.

Do not let low-confidence memory strongly constrain exploration.

## Preference dimensions

Useful dimensions include:
- density;
- typography character;
- color intensity;
- geometric vs organic;
- motion intensity;
- editorial vs utilitarian;
- card/container usage;
- hierarchy strength;
- brand expressiveness;
- illustration style;
- copy tone;
- experimentation tolerance.

## Self-critique learning

Ashley may also learn from observable outcome, not only user taste.

Example:
- logo detail disappears at 16px;
- table hierarchy fails with long real data;
- social template becomes unreadable as thumbnail.

Store the **generalizable cause**, not merely "version B failed."

## Core-skill boundary

Ashley may automatically update:
- project design docs;
- PREFERENCES.md;
- HEURISTICS.md.

Ashley must not silently rewrite her installed SKILL.md or core references as self-learning.

If repeated evidence suggests a core-process improvement:
1. record the proposed process improvement;
2. suggest or create a versioned change in the Ashley repository when asked/authorized;
3. run relevant evals.

This keeps self-improvement auditable.


## Preference record schema

Durable preference records should include:

- **dimension** — what is being learned;
- **scope** — project | global;
- **value** — the preference itself;
- **confidence** — low | medium | high;
- **evidence** — where the signal came from;
- **first_observed** — date/context;
- **last_validated** — most recent supporting signal;
- **contradictions** — evidence that limits or challenges the preference;
- **exceptions** — contexts where it should not apply.

## Contradiction detection

Before applying a strong preference:
1. check project mode/context;
2. check for explicit approved project rules;
3. check contradictory recent evidence;
4. reduce confidence when old evidence no longer predicts current choices.

Do not silently delete historical evidence. Rewrite the rule to encode context.

## Staleness

Preferences are priors, not permanent identity.

A preference that has not been validated for a long time should exert less pressure when:
- the product category is materially different;
- recent choices contradict it;
- the user explicitly asks to explore outside the usual taste.

Do not implement mechanical time decay that erases useful memory. Use recency as one signal among scope, confidence and contradiction.

## Taste profile

Use `~/.ashley/TASTE_PROFILE.md` as the compact global creative prior.

Update it by consolidating repeated preference signals, especially after calibration boards and cross-project choices.

Do not let the taste profile override:
- explicit current instructions;
- approved brand direction;
- product/user evidence;
- accessibility;
- artifact purpose.
