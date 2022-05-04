import sys

sys.path.insert(0, "")

from src.domain.events import EventsRepository, Event
from src.domain.users import UsersRepository, User

database_path = "data/events-list.db"


concierto_queen = Event(
    id="event-1",
    user_id="user-1",
    name="concierto queen",
    description="un tributo a queen",
    date="2022-01-25",
    completed=False,
    time="22:00",
)
concierto_iker = Event(
    id="event-2",
    user_id="user-1",
    name="concierto iker",
    description="un tributo a iker",
    date="2022-01-26",
    completed=False,
    time="23:00",
)
concierto_camelia = Event(
    id="event-3",
    user_id="user_2",
    name="concierto camelia",
    description="un tributo a camelia",
    date="2022-01-27",
    completed=False,
    time="21:00",
)
concierto_ainara = Event(
    id="event-4",
    user_id="user-2",
    name="concierto ainara",
    description="un tributo a ainara",
    date="2022-01-28",
    completed=False,
    time="17:00",
)

event_repository = EventsRepository(database_path)
event_repository.save(concierto_queen, "user-1")
event_repository.save(concierto_iker, "user-1")
event_repository.save(concierto_ainara, "user-2")
event_repository.save(concierto_camelia, "user-2")

user_ainara = User(
    id="user-1",
    user_name="Ainara",
)

user_camelia = User(
    id="user-2",
    user_name="Camelia",
)

user_repository = UsersRepository(database_path)
user_repository.save(user_ainara)
user_repository.save(user_camelia)
