from celery import Celery
from celery.result import AsyncResult

from api_request import getting_organization_id, getting_person_object

# for enabling backend uses a sqlite db
app = Celery('tasks', broker='pyamqp://guest@localhost//',
             backend='db+sqlite:///db.sqlite3')


@app.task
def task(name: str, organization_name: str):
    """ Use for calling a APIs """
    org_id = getting_organization_id(organization_name)
    person_obj = getting_person_object(org_id, name)
    return person_obj


@app.task
def getting_task_result(job_id: str):
    """ Use for validating a result"""
    result = AsyncResult(job_id)
    return result
