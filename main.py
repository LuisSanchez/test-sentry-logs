import sentry_sdk
import sentry_sdk.logger as sentry_logger

def main():
    sentry_sdk.init(
        debug=True,
        environment="development",
        traces_sample_rate=1.0,
        _experiments= {
            "enable_logs": True,
        }
    )
    sentry_logger.debug("Hello, world!")


if __name__ == "__main__":
    main()
