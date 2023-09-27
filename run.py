from app import init_app
from app.database import DatabaseConnection

app = init_app()
if __name__ == "__main__":
    db=DatabaseConnection.create_if_not_exists()
    app.run()