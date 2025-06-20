import sqlalchemy as sa

DB_SERVER = "vm-for-projects\\MSSQLSERVER01"
DB_NAME = "REPO_PROJECTS_DB"

def get_engine():
    conn_str = (
        f"mssql+pyodbc://@{DB_SERVER}/{DB_NAME}"
        "?trusted_connection=yes"
        "&driver=ODBC+Driver+17+for+SQL+Server"
    )
    return sa.create_engine(conn_str)