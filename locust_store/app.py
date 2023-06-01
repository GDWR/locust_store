from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlmodel import Session

from .database import engine
from .models import Product
from .routes import routes

@asynccontextmanager
async def lifespan(_: FastAPI):
    # Populate database, products are random strings...
    import string
    import random

    with Session(engine) as session:
        for _ in range(1000):
            session.add(Product(name=''.join(random.choice(string.ascii_lowercase) for _  in range(10))))

        session.commit()

    yield


app = FastAPI(lifespan=lifespan)

for route in routes:
    app.include_router(route)
