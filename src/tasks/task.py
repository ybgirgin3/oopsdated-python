from src.tasks import celery_app
from commons.tasklib.base_task import BaseTask


# plan all
@celery_app.task(
    bind=True,
    name='oopsdated.plan'
)
def plan_repos(self: BaseTask):
    """
    __summary__: get tasks from db and make them ready to scrape
    :param self:
    :return:
    """
    pass





# scan
@celery_app.task(
    bind=True,
    name='oopsdated.scan'
)
def scrape_repo(
        self: BaseTask,
):
    pass


@celery_app.task(
    bind=True,
    name='oopsdated.extract'
)
def extract_repo(self: BaseTask):
    pass


