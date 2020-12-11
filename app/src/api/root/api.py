from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from fastapi import Request

router = InferringRouter()

@cbv(router)
class RootView:
    request: Request

    @router.get('/')
    async def index(self):

        return {
            "status": "OK",
            "version": self.request.app.state.version
        }