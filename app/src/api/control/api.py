import subprocess
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from fastapi import Request
import os

router = InferringRouter()

START_PIPELINE_SCRIPT_PATH = os.path.join(os.curdir, "scripts", "start_pipeline.sh")

@cbv(router)
class ControlView:
    request: Request

    @router.post('/start-pipeline')
    async def index(self):

        subprocess.Popen(['/bin/bash', START_PIPELINE_SCRIPT_PATH])
        return {
            "status": "on progress",
        }
