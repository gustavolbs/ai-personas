# Dave — Stack Standards

Apply the repository-owned contract in `engineering-standards.md`.

Before implementation, detect the stack from package manifests, lockfiles,
tsconfig, framework config, route structure and scripts. Apply only the
relevant sections:

- TypeScript and React rules for `.ts/.tsx` code;
- Next.js rules for App Router/Pages Router projects;
- Node.js rules for server, worker, CLI and API code;
- Tailwind and shadcn/ui rules when those dependencies/configs exist;
- Expo/React Native rules for Expo projects and native routes.

The external reviewer must report which sections it applied and any rule that
could not be verified. Existing repository conventions win when documented and
coherent; deviations require a local reason and evidence.
