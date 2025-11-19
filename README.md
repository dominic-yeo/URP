# Basic Python Application

This project follows the workflow outlined in [the Basic Python Application Guide](https://urp-ecru.vercel.app/) and provides a tiny command-line app that greets a user by name.

## Prerequisites

- Python 3.11 or later available on your `PATH`
- (Recommended) A virtual environment created with `python -m venv .venv`

## Installation

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

The included `requirements.txt` is empty because this starter does not rely on external libraries yet. Add dependencies as your app grows, then run `pip freeze > requirements.txt` to capture versions.

## Usage

```bash
python app.py --name "Ada"
```

If no `--name` argument is provided, the app defaults to `"Developer"`.

## Deploying to Vercel

- Static files (for example `index.html`) deploy as usual.
- The new `vercel.json` keeps the default filesystem routing but forwards any unknown path to `api/log-404.py`.
- The `api/log-404.py` serverless function prints a structured JSON line for every miss and returns a 404 response. Those lines show up inside the Vercel deployment logs, so you can filter for `http.404` to audit missing routes.
- No extra configuration is required after pushing; every non-existent path will now emit an explicit log entry.

## Testing

Install pytest, then run tests:

```bash
pip install pytest
pytest
```

## Next Steps

- Expand the CLI with additional arguments or subcommands.
- Add logging, configuration files, or richer output formatting.
- Package and share the project via Git, GitHub, or a ZIP archive.


