from fastapi import FastAPI, Body, Header, Response

app = FastAPI()

# Parameters in URL Path
# http localhost:8000/hi/Mom
@app.get("/hi/{who}")
def greetw(who):
    return f"Hello? {who}"


# Parameters in Body
# http -v localhost:8000/hi who=Mom
@app.post("/hi2")
def greet(who: str = Body(embed=True)):
    return f"Hello? {who}"


# Parameters in Header
# http -v localhost:8000/hi3 who:Mom
@app.post("/hi3")
def greet(who: str = Header()):
    return f"Hello? {who}"


@app.get("/header/{name}/{value}")
def header(name: str, value: str, response:Response):
    response.headers[name] = value
    return "normal body"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)