from fastapi import FastAPI
from routes.question import questions_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["http://localhost:5173"]
app.add_middleware(CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

app.include_router(questions_router)
