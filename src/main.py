from fastapi import FastAPI

app = FastAPI()



@app.get('/')
async def foo():
    return 2**20
