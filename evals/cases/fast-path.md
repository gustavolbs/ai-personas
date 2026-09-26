# fast-path

## Scenario
A one-file typo fix in a tiny repository. The team must act directly: one hat, one targeted check, no children, no Sol.

## Prompt
Laila, the greeting in src/app.ts says "Helo". Fix the typo.

## Assertion
`fast_path`: no `spawn_agent`; at most 8 tool events including boot.

## Manual review
Did Laila put on Dave's hat immediately, without a plan or a persona graph? Was only the target file read?
