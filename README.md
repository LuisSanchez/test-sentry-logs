Attempt at reproducting https://github.com/getsentry/sentry-python/issues/4415.

## Steps to run

This project is managed with `uv`; you must have `uv` installed on your system to run the code. Once you have installed `uv`, proceed as follows:

1. Run `uv sync`.
2. Run `export SENTRY_DSN="<your dsn here>"`.
3. Run `uv run main.py`.
4. Observe that the message "Hello, world!" is logged at log-level debug in Sentry.
