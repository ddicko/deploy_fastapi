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
SQLALCHEMY_DATABASE_URL = "postgres://dmgshbpnrymmwi:262dd54c1af68404d1ad96bfc7d61323703e56f967432b51931a3f6a6643ed4d@ec2-34-206-8-52.compute-1.amazonaws.com:5432/d6bnjatookfchk"
# "postgresql://fastapi_user:fastapi@localhost/fastapi_db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,  # connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
