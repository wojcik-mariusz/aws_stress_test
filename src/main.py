from fastapi import FastAPI


app: FastAPI = FastAPI()


@app.get("/", status_code=200)
def read_root():
    return {"message": "server running"}
