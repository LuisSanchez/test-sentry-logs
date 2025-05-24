import logging
import sentry_sdk

# good practice to set up logging, singleton
# (single logger for the whole module)
log = logging.getLogger(__name__)


def main():
    sentry_sdk.init(
        debug=True,
        environment="development",
        traces_sample_rate=1.0,
        _experiments={
            "enable_logs": True,
        },
    )

    # this does NOT get logged to Sentry
    log.info("Hello, world info from get logger!")
    # this is logged to Sentry
    log.warning("Hello, world warning from get logger!")


if __name__ == "__main__":
    main()
