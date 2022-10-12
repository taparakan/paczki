from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

paczki = {}

class Paczka(BaseModel):
    id: str
    paczkomat_docelowy: str
    opis: Union[str, None] = None

app = FastAPI()


@app.get("/")
async def app_root():
    return {"paczkomaty": "impost"}

@app.get("/regulamin")
async def app_root():
    return "nie wolno umieszać rzeczy w skrytkach przez klientów odbierających paczki"

@app.get("/paczki")
async def get_paczki():
    return paczki

@app.get("/paczka")
async def get_paczka(id: str):
    if id in paczki:
        return paczki[id]
    return f'brak paczki o id: {id}'

@app.post("/paczka")
async def post_paczki(paczka: Paczka):
    paczki[paczka.id] = paczka
    return paczka

@app.delete("/paczki")
async def delete_paczki(id: str):
    if id in paczki:
        paczki.pop(id)
        return f'usunieto paczkę o id: {id}'
    return f'brak paczki o id: {id}'