from fastapi import APIRouter
from app.src.api.root import api as root
from app.src.api.sentiment import api as sentiment
from app.src.api.control import api as control

router = APIRouter()

router.include_router(root.router, prefix='')
router.include_router(sentiment.router, prefix='/sentiment')
router.include_router(control.router, prefix='/control')
