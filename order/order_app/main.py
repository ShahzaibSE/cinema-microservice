from fastapi import FastAPI

app: FastAPI = FastAPI(
    servers=[
        {
            "url": "http://127.0.0.1:8000", # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        }
    ]
)

app.get("/")
def greeting():
    return {
        "status": True,
        "message": "Hello World"
    }