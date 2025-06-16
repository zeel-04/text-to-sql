import sys

SINK = sys.stderr
LOG_FILE = "logs/app.log"

# TODO: Remaining to be implemented
LOGGING_CONFIG = {
    "sinks": [
        {
            "sink": LOG_FILE,
            "level": "DEBUG",
            "rotation": "10 MB",
        },
        {
            "sink": SINK,
            "level": "INFO",
        },
    ]
}
