from fastapi import FastAPI
from pydantic import BaseModel

from tasks import task, getting_task_result

app = FastAPI()


class Leads(BaseModel):
    """ Request Body params """
    name: str
    organization_name: str


@app.post('/scrape')
def scrape(leads: Leads):
    result = task.delay(leads.name, leads.organization_name)
    return result.id


@app.get('/scrape_results/{job_id}')
def scrape_results(job_id: str):
    result = getting_task_result.delay(job_id)
    result_obj = result.app.AsyncResult(job_id)
    if result_obj.status == 'SUCCESS':
        return result_obj.result
    return {'status': result_obj.status}
