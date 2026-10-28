# Copilot instructions

## Never
- Do not change AGENTS.md, .github/, pyproject.toml, Docker Compose files, or Alembic files without explicit approval.
- Do not weaken assertions or delete failing tests to make code pass; stop and ask.
- Do not add secrets, tokens, or new dependencies without approval.
- Do not skip validation; run the smallest relevant tests.

## Working
- Start with the failing behavior and add or update the smallest relevant test.
- Read only the files needed for the change; keep patches surgical and consistent with the repo.
- Fix the root cause, not the symptom, and keep the public API and existing behavior intact.
- Verify with the targeted test(s) before finishing.
