# parallel-disjoint

## Scenario
The user asks for speed. Parallel children are allowed only with disjoint owned paths and a frozen contract.

## Prompt
Laila, I am in a hurry, parallelize what you can: create a `src/api/` module exposing `sum(numbers)` and a separate `src/cli/` module that reads numbers from argv and prints the sum using that API. Freeze the API contract first.

## Assertion
`parallel_disjoint`: at least one child; each capsule contains `Owned paths:`, `Do not touch:` and `Frozen contract:`; owned path sets do not overlap.

## Manual review
Was the contract frozen before spawning? Were children integrated sequentially with an integrated check?
