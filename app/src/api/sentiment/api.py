from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from fastapi import Request, Depends
from app.src.preprocess import preprocessing
from app.src.api.dependencies import get_model

router = InferringRouter()

@cbv(router)
class RootView:
    request: Request
    model: object = Depends(get_model)

    @router.get('/')
    async def index(self, text: str):
        vectorizer, classifier = self.model

        preprocessed_text = preprocessing(text)
        vectorized_text = vectorizer.transform([preprocessed_text])
        prediction = classifier.predict(vectorized_text)[0]

        return {
            "prediction": prediction,
            "preprocessed_text": preprocessed_text,
        }