import sqlite3
from src.webserver import create_app
from src.domain.events import EventsRepository
from src.domain.users import UsersRepository


database_path = "data/events-list.db"

repositories = {
    "event": EventsRepository(database_path),
    "user": UsersRepository(database_path),
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
