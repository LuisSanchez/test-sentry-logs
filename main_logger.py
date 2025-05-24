import logging
import sentry_sdk

# bad practice to set up logging
# (multiple loggers for the same module)
log = logging.Logger(__name__)


def main():
    sentry_sdk.init(
        debug=True,
        environment="development",
        traces_sample_rate=1.0,
        _experiments={
            "enable_logs": True,
        },
    )

    # this is logged to Sentry
    log.info("Hello, world info from logger!")
    # this is logged to Sentry
    log.warning("Hello, world warning from logger!")


if __name__ == "__main__":
    main()
