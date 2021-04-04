from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
import joblib

model = joblib.load('model.sav')


class Parameters(BaseModel):
    location: float
    bhk: float
    furnishing: float
    area: float
    old: float
    floor: float


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/house_pred")
async def read_item(param: Parameters):
    returnJson = {}
    returnJson['price'] = model.predict(
        [[
            param.location,
            param.bhk,
            param.furnishing,
            param.area,
            param.old,
            param.floor,
        ]]
    )[0]
    return returnJson
