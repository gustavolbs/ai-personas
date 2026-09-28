# program-mode

## Scenario
A goal that decomposes into three independent packages. Laila must dispatch one child per package with a capsule and stay out of execution herself.

## Prompt
Laila, conduza este programa até o fim: crie três módulos independentes em src/, cada um com seu teste node --test: `math` (sum, mean), `text` (slugify) e `dates` (isoWeek). Um pacote por módulo. Não peça confirmação entre pacotes.

## Assertion
`program_mode`: at least 2 children spawned; every capsule has `Owned paths:` and `Return:`; Laila's own shell/patch calls stay ≤40.

## Manual review
Did Laila freeze the module contracts before spawning? Did each child return a short summary with real check output? Did she run one integrated check at the end instead of re-doing the work?
