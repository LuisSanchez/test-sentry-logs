Attempt at reproducing https://github.com/getsentry/sentry-python/issues/4415.

## Steps to run

This project is managed with `uv`; you must have `uv` installed on your system to run the code. Once you have installed `uv`, proceed as follows:

1. Run `uv sync`.
2. Run `export SENTRY_DSN="<your dsn here>"`.
3. Run `uv run main.py`.
4. Observe that the message "Hello, world!" is logged at log-level debug in Sentry.

## main_logger.py

Run `uv run main_logger.py`.

Uses `logging.Logger(__name__)` that creates a new logger for the same module each time it is called. This is bad practice.

Info and Warning get logged to Sentry

## main_get_logger.py

Run `uv run main_get_logger.py`.

Uses `logging.getLogger(__name__)` uses a singleton patter and returns the same instance every time it is called with the same name.

Info does NOT get logged into Sentry.
Warning does get logged into Sentry.

## Misc

- Downgraded to Python 3.10.11 which is the one I'm currently using.
