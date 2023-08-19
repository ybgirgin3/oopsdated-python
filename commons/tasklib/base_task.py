import datetime
import logging
from abc import ABC
from celery import Task


class BaseTask(Task, ABC):
    autoretry_for = (
        Exception,
    )
    max_retries = None
    retry_backoff = False
    retry_backoff_max = 1
    retry_jitter = False
    default_retry_delay = 1
    time_limit = 60 * 60 * 24
    soft_time_limit = 60 * 59 * 24
    _seen_loggers = set()

    def __init__(self) -> None:
        super().__init__()

        self.logging_extras = {}

    def before_start(self, task_id, args, kwargs):
        super().before_start(task_id, args, kwargs)

        self.logging_extras['task_name'] = self.name
        self.logging_extras['task_id'] = task_id

    def _patch_logging_extras(self, method):
        def __patch(*args, **kwargs):
            extra = {**self.logging_extras}
            if 'extra' in kwargs and isinstance(kwargs['extra'], dict):
                extra.update(kwargs['extra'])

            kwargs['extra'] = extra

            return method(*args, **kwargs)

        return __patch

    @property
    def logger(self) -> logging.Logger:
        _logger = logging.getLogger(self.name)

        if self.name not in BaseTask._seen_loggers:
            _logger._log = self._patch_logging_extras(_logger._log)

        BaseTask._seen_loggers.add(self.name)

        return _logger

    def set_log_extra(self, name: str, value: any):
        self.logging_extras[name] = value

    def apply_async(self, args=None, kwargs=None, task_id=None, producer=None, link=None,
                    link_error=None, shadow=None, **options):
        expires = options.get('expires', self.expires)
        if expires and isinstance(expires, str):
            try:
                expires = datetime.datetime.fromisoformat(expires)
            except ValueError:
                expires = None

        options['expires'] = expires

        return super().apply_async(
            args, kwargs, task_id, producer, link, link_error, shadow, **options
        )