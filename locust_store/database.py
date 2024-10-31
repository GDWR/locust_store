from sqlmodel import SQLModel, create_engine

# Ensure models are loaded when creating metadata
from .models import *

# engine = create_engine("postgresql://postgres:postgres@localhost:5432")
engine = create_engine("sqlite:///database.db")

SQLModel.metadata.create_all(engine)
