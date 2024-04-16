# EMQX `pre-commit` Hooks

Git([`pre-commit`](https://pre-commit.com/)) hooks helping to work in [EMQX](https://github.com/emqx/emqx) repo.

Sample config (preserving local EMQX hooks):

```yaml
repos:
-   repo: local
    hooks:
    -   id: emqx pre-commit hook
        name: emqx built-in pre-commit hook
        entry: ./scripts/git-hook-pre-commit.sh
        language: system
        stages: [pre-commit]
        always_run: true
        args: ['-c']

    -   id: emqx pre-push hook
        name: emqx built-in pre-push hook
        entry: bash
        language: system
        stages: [pre-push]
        always_run: true
        args:
        - -c
        - |
           ./scripts/git-hook-pre-push.sh $PRE_COMMIT_REMOTE_NAME $PRE_COMMIT_REMOTE_URL

    -   id: emqx post-commit hook
        name: emqx built-in post-commit hook
        entry: ./scripts/git-hook-post-commit.sh
        language: system
        stages: [post-commit]
        always_run: true

-   repo: https://github.com/savonarola/emqx-pre-commit-hooks.git
    rev: main
    hooks:
    -   id: emqx-check-year-updated
```
