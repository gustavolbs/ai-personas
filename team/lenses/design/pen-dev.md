# pen.dev / Pencil Workflow

pen.dev is Ashley's preferred editable design canvas when available.

Official docs: https://docs.pencil.dev/

## Why Ashley prefers it

- `.pen` files are JSON-based, portable and Git-friendly;
- files can live inside the product repository;
- Codex can connect through the local `pencil` MCP;
- the CLI runs the same editor engine headlessly;
- screenshots and exports support Visual QA;
- the design source can evolve in branches alongside code.

## Important rule

Do **not** edit `.pen` JSON manually.

Use:
- pen.dev MCP tools;
- desktop/IDE canvas;
- `pen interactive`;
- supported CLI operations.

## Recommended project layout

```text
design/
├── product.pen
├── brand.pen
├── campaigns.pen
└── exports/        # optional/generated; gitignore if appropriate
```

Use fewer files when the project is small. Do not fragment design without benefit.

## Live MCP workflow

When `pencil` tools are available:
1. open the intended `.pen` file;
2. include its full path in the task when ambiguity is possible;
3. call/read the tool guidance before unfamiliar operations;
4. inspect app/document state;
5. inspect existing styles/components before editing;
6. make coherent writes;
7. take screenshots of consequential results;
8. visually critique and iterate;
9. save the document.

Common public tools include:
- `read_skill`;
- `get_app_state`;
- `get_style`;
- `execute`.

Exact live tools can vary by installed version.

## Headless resilience path

The CLI requires Node.js 22.19+ and pen.dev authentication.

Install:
```bash
npm install -g @pen.dev/cli
pen version
pen login
pen status
```

Useful commands:
```bash
pen --in design/product.pen --export /tmp/ashley-product.png
pen interactive -i design/product.pen -o design/product.pen --enable-preview --preview-output /tmp/ashley-preview.png
```

In headless interactive mode, use `save()` before exit.

The CLI can create/edit/export without a GUI, which makes it the preferred resilience path when the desktop/IDE MCP host is unavailable.

Avoid invoking a second built-in design agent through `pen --prompt` merely to duplicate Ashley's reasoning. Prefer Ashley controlling the design tools directly when the harness permits it.

## Visual QA

Preferred order:
1. `TakeScreenshot()` from the design engine;
2. `Export()` from the design engine;
3. `pen --in ... --export ...png`;
4. browser/implementation screenshot for design↔code comparison.

Ashley must actually inspect the rendered image before claiming visual QA passed.

## Git

A `.pen` file may be committed with the product.

Before large design changes:
- inspect git status;
- avoid overwriting unrelated user changes;
- use normal branches/commits when the user wants design history preserved.

Generated preview images do not need to be committed unless useful to the project.

## Design ↔ code

Use the repo and `.pen` together:
- code may remain authoritative for behavior/accessibility;
- `.pen` may be authoritative for approved visual direction;
- map tokens/components in HANDOFF.md;
- use browser preview to compare implementation against the approved design.

## Failure handling

If the local MCP is unavailable:
- verify pen.dev is running and the intended file is open if live editing is desired;
- if CLI exists and `pen status` is healthy, use the headless path;
- otherwise fall back according to `design-canvas.md`.


## Strict tool discipline for component libraries

When materializing a design system, do not improvise Pencil operations from memory.

Before the first write in a session:
1. call `read_skill()`;
2. load the current schema guidance such as `pen-schema.md`;
3. load `execute.md`;
4. inspect `get_app_state()`;
5. inspect existing variables/components before inserting anything.

Only use operations documented by the currently loaded tool/schema.

If an operation fails:
- read the returned error;
- re-read the relevant tool/schema guidance;
- correct the smallest failing operation;
- do not invent another API name.

### Bounded writes

For component-library work, prefer one component or one tightly related family per coherent write/batch.

Examples:
- Button + Button states;
- Input + Textarea + Label;
- Checkbox + Radio + Switch;
- Dialog primitives;
- Table family.

Do not attempt dozens of component origins in one `execute` call.

After each batch:
1. inspect structure;
2. `TakeScreenshot()`;
3. visually inspect;
4. fix;
5. save/checkpoint;
6. only then continue.

### Reusable origins, instances and slots

A library must use actual reusable components rather than flattened drawings.

Use component origins/instances and slots when content needs insertion.

For compound components, build from verified primitives instead of redrawing everything independently.

Prefer a `.lib.pen` file for a reusable product design library.
