from fastapi import FastAPI
from web import explorer

app = FastAPI()
app.include_router(explorer.router)
# app.include_router(creature.router)


@app.get("/")
def top():
    return "Top here!"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
