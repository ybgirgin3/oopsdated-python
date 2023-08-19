from commons.celery_generator import create_celery_app
import logging


celery_app = create_celery_app(
    task_discovery_packages=[
        __name__
    ]
)


loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
for logger in loggers:
    logger.setLevel(logging.ERROR)


__all__ = ('celery_app',)


