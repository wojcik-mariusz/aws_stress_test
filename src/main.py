from fastapi import FastAPI


app: FastAPI = FastAPI()


@app.get("/", status_code=200)
def read_root() -> dict[str: str]:
    return {"message": "server running"}
