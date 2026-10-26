# Project title

## Business question

## Result

## Data

## Method

## Limitations

## How to run

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows Git Bash; use .venv/bin/activate on macOS/Linux
pip install -r requirements.txt
nbstripout --install            # once per clone: strips notebook outputs on commit
```

Before committing:

```bash
ruff check .
ruff format .
pytest
```

## How AI was used
