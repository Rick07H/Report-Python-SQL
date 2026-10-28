import os
import urllib.parse

import sqlalchemy as sa
from dotenv import load_dotenv

load_dotenv()


def get_engine():
    """Build a SQLAlchemy engine for SQL Server from environment variables.

    DB_SERVER and DB_NAME are required. If DB_USER is set, SQL authentication
    is used; otherwise Windows authentication (trusted connection).
    """
    server = os.environ["DB_SERVER"]
    database = os.environ["DB_NAME"]
    driver = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")

    parts = [
        f"DRIVER={{{driver}}}",
        f"SERVER={server}",
        f"DATABASE={database}",
        "TrustServerCertificate=yes",
    ]
    if os.getenv("DB_USER"):
        parts += [f"UID={os.environ['DB_USER']}", f"PWD={os.environ['DB_PASSWORD']}"]
    else:
        parts.append("Trusted_Connection=yes")

    odbc = urllib.parse.quote_plus(";".join(parts))
    return sa.create_engine(f"mssql+pyodbc:///?odbc_connect={odbc}")
