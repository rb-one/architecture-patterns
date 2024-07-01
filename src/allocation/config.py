import os


def get_postgres_uri():
    host = os.environ.get("DB_HOST", "localhost")
    port = 5432 if host == "localhost" else 5432
    db_name = os.environ.get("DB_NAME", "postgres")
    user, db_name = "allocation", "allocation"
    password = os.environ.get("DB_PASSWORD", "postgres")
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


def get_api_url():
    host = os.environ.get("API_HOST", "localhost")
    port = 5005 if host == "localhost" else 80
    return f"http://{host}:{port}"
