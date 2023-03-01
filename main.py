from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def root():
    return {"message": "welcome to my server"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/createpost")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title {payload['title']} conetnt: {payload['content']}"}