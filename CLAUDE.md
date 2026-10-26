# Project rules

- Code, comments, file names and commit messages are in English.
- Commits follow Conventional Commits: `feat:`, `fix:`, `docs:`, `refactor:`, `data:`, `chore:`.
- Never commit anything in `data/raw/`; keep raw data local and document its source in `data/README.md`.
- Every change goes through a branch and a Pull Request to `main`, even when working alone.
- Run `ruff check .` and `ruff format .` before committing.
