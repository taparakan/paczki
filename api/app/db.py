from sqlmodel import create_engine

conn_str = "postgresql://izydor:test@localhost:5444/bm_dev_auth"

engine = create_engine(conn_str, echo=True)