from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker
import cloudinary

cloudinary.config(
    cloud_name="djtxsnk9c",
    api_key="372171617535646",
    api_secret="2zMo8MA5wgslqPtRwHOVS1AFRks",
)

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgres://bvusmfyncjghur:7e81c3210446ff5a122eaecb846f13711e32f75452ad08ead8e0b97064afbadf@ec2-52-5-247-46.compute-1.amazonaws.com:5432/ddr0d0ukd2ckev"
# "postgresql://fastapi_user:fastapi@localhost/fastapi_db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,  # connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
