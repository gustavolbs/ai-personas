# Review Standards

The persona team uses current primary standards as review anchors. They are
decision aids, not a substitute for repository-specific threat modeling or
runtime evidence.

The stack-specific implementation contract is
`engineering-standards.md`. Reviewers must detect
the repository stack and apply only the relevant sections.

## Security

- [OWASP ASVS 5.0](https://owasp.org/projects/asvs) defines testable
  application-security requirements for architects, developers, testers and
  security reviewers.
- [NIST SP 800-218 SSDF 1.1](https://csrc.nist.gov/pubs/sp/800/218/final)
  supplies secure-development lifecycle practices for preparing, protecting,
  producing and responding to software vulnerabilities.

The implementation gate covers the applicable ASVS areas, especially
encoding/input validation, authentication, session management, access control,
business logic, data protection, secure communications, APIs, configuration,
dependency hygiene and logging/error handling.

## UI and accessibility

- [WCAG 2.2](https://www.w3.org/TR/wcag/) is the current W3C Recommendation
  used for perceivable, operable, understandable and robust interfaces.
- [Playwright visual comparisons](https://playwright.dev/docs/next/test-snapshots)
  provide a deterministic `toHaveScreenshot()` baseline/diff workflow when the
  project uses Playwright.

Visual QA is not complete from a source diff, typecheck or DOM inspection alone:
the affected route/state must be rendered and inspected at the target viewport.
Stabilize fonts, viewport, data and animations before comparing screenshots.

## Anti-slop quality

Review generic or unsupported output only when there is observable evidence:
redundant comments, speculative abstractions, dead code, swallowed failures,
weak tests, generic UI defaults or unsupported claims. Do not infer authorship
from style, remove useful structure to improve a score, or treat AIslop/other
heuristics as a replacement for the stack-specific checks above.

## Independent review

The external reviewer is a read-only child using a different model/provider from
the implementer. It returns findings, evidence and verification steps; it never
edits the worktree or certifies its own fixes. Dave remains the integration
owner and must fix findings, rerun failed checks and collect a terminal review
result before synthesis when the selected execution mode requires independent
review. Small, low-risk FAST work is not blocked on an external reviewer.
