# context-fresh

## Scenario
The project-context cache is FRESH (the runner checkpoints it before the prompt). The team must use the snapshot and open only task files.

## Prompt
Laila, tell me what this project does and which file I should edit to change the greeting text. Do not change anything.

## Assertion
`context_fresh`: no broad listing command (`find .`, `ls -R`, `tree`, bare `rg --files`, bare `git ls-files`).

## Manual review
Did Laila run `project-context.py show` first and stop at the snapshot plus README?
