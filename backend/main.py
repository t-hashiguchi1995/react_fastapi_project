from fastapi import FastAPI,Request

app = FastAPI()


@app.get("/api")
async def root(request:Request):
    print(request.headers)
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/no-proxy-header")
async def noProxyHeader(request:Request):
    print(request.headers)
    return {"message": "no proxy header"}