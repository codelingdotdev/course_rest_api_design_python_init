from ninja import NinjaAPI
from api.endpoints.bark import router as bark_router

api = NinjaAPI()

api.add_router("/barking", bark_router)
