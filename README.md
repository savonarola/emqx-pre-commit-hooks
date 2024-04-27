# EMQX `pre-commit` Hooks

Git([`pre-commit`](https://pre-commit.com/)) hooks helping to work in [EMQX](https://github.com/emqx/emqx) repo.

Sample config (preserving local EMQX hooks):

```yaml
---
repos:
-   repo: https://github.com/savonarola/emqx-pre-commit-hooks.git
    rev: 1502c90282e66f84ffe73147c34eb47a553d6dd9
    hooks:
    -   id: emqx-check-year-updated
    -   id: emqx-builtin-pre-commit
    -   id: emqx-builtin-pre-push
    -   id: emqx-builtin-post-commit

```
