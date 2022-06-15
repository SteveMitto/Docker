from typing import Union
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def get_root():
    return {"Hello":"World"}


@app.get('/items/{item_id}')
def get_client_items(item_id: int, price: Union[str, None] = None):
    return {"item_id":item_id, "price":price}



if __name__ == "__main__":
    uvicorn.run(app)