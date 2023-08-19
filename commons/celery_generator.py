import celery.signals
import os
from celery import Celery
from celery.signals import celeryd_after_setup
from commons import celery_settings

from typing import Optional

import logging
from pythonjsonlogger.jsonlogger import JsonFormatter


def _create_celery_logger_handler():
    if os.environ.get('DEBUG', '0') == '1':
        return

    json_formatter = JsonFormatter('%(asctime)s %(name)s %(levelname)s %(message)s')
    logging.basicConfig(level=logging.ERROR, force=True)
    for handler in logging.root.handlers:
        handler.formatter = json_formatter


def create_celery_app(
        name: str = 'oopsdated',
        task_discovery_packages: Optional[list[str]] = None
) -> Celery:
    celery_app = Celery(name)
    celery_app.config_from_object(celery_settings)
    celery_app.autodiscover_tasks(packages=task_discovery_packages)

    @celeryd_after_setup.connect
    def after_setup(sender, instance, **kwargs):
        os.environ['WORKER_NAME'] = '{0}'.format(sender)

    @celery.signals.after_setup_task_logger.connect
    def after_setup_celery_task_logger(logger, **kwargs):
        """ this function sets the 'celery.task' logger handler and formatter """
        _create_celery_logger_handler()

    @celery.signals.after_setup_logger.connect
    def after_setup_celery_logger(logger, **kwargs):
        _create_celery_logger_handler()

    return celery_app

