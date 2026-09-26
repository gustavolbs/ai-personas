# Interaction Design

## Control semantics

Use controls according to behavior:

- **button**: immediate action;
- **link**: navigation;
- **checkbox**: independent boolean/multi-selection;
- **radio**: one choice from small visible set;
- **select/combobox**: selection from larger set;
- **segmented control**: small mutually exclusive view/state choice;
- **toggle**: immediate persistent binary setting;
- **menu**: secondary/contextual actions.

Visual novelty does not justify semantic mismatch.

## Feedback

After an action users should be able to infer:
- was input received?
- is work happening?
- what changed?
- did it succeed?
- did it fail?
- can it be undone?
- what happens next?

Long-running async operations need durable state, not a transient spinner.

## Optimistic updates

Good when:
- low consequence;
- likely success;
- understandable rollback.

Use caution when:
- financial/legal;
- high-impact;
- concurrent/conflicting;
- server validation matters.

## Destructive action

Match friction to consequence.

Prefer:
- undo for easily reversible actions;
- confirmation for meaningful consequence;
- explicit object/consequence wording;
- recycle/archive when product supports recovery.

Typed confirmation is for unusually destructive actions, not routine friction.

## Forms

Design:
- persistent visible labels;
- logical grouping;
- defaults;
- required/optional clarity;
- validation timing;
- inline errors;
- preservation of entered values;
- keyboard progression;
- submitting state;
- server errors;
- recovery.

Placeholder is not a label.

## Tables and selection

Specify:
- row click vs explicit link;
- checkbox selection;
- select-all scope;
- cross-page selection;
- bulk eligibility;
- mixed states;
- frozen columns;
- horizontal overflow;
- density;
- keyboard behavior;
- long values;
- empty/filter-empty distinction.

## Notifications

Choose channel by urgency and persistence:
- inline;
- toast;
- banner;
- inbox/activity;
- modal only when interruption is justified.

A toast is poor storage for information users may need later.

## Motion

Use motion for:
- causality;
- continuity;
- spatial relationship;
- progress;
- state transition;
- hierarchy.

Avoid:
- motion that slows expert workflows;
- gratuitous entrance choreography;
- dependence on animation for meaning;
- ignoring reduced-motion preference.

## Microcopy

Write consequences, not cheerleading.

Errors should say:
- what happened;
- what remains safe;
- how to recover.

Empty states should distinguish:
- no data exists;
- filtered result is empty;
- user lacks permission;
- content is still loading/syncing.
