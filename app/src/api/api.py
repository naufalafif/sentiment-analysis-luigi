from fastapi import APIRouter
from app.src.api.root import api as root
from app.src.api.sentiment import api as sentiment

router = APIRouter()

router.include_router(root.router, prefix='')
router.include_router(sentiment.router, prefix='/sentiment')
