from fastapi import FastAPI
from db.init_db import init_db
from api.routes.profile import router as profile_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5175",
    "http://localhost:5173"# Add your frontend URL here
    # you can add more origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    init_db()  # Initialize the database at startup


# Define your API routes here
app.include_router(profile_router)
