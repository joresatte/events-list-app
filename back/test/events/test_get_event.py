from urllib import response
from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.events import EventsRepository, Event


def test_should_return_empty_list_of_events():

    events_repository = EventsRepository(temp_file())
    app = create_app(repositories={"event": events_repository})
    client = app.test_client()

    response = client.get("/api/events")

    assert response.json == []


def test_should_return_event_in_database():

    events_repository = EventsRepository(temp_file())
    app = create_app(repositories={"event": events_repository})
    client = app.test_client()

    concierto_queen = Event(
        id="event-1",
        user_id="user-1",
        name="concierto queen",
        description="un tributo a queen",
        date="2022-01-25",
        completed=False,
        time="22:00:00",
    )
    events_repository.save(concierto_queen, "user-1")

    response = client.get("/api/events", headers={"Authorization": "user-1"})

    assert response.json == [
        {
            "id": "event-1",
            "user_id": "user-1",
            "name": "concierto queen",
            "description": "un tributo a queen",
            "date": "2022-01-25",
            "completed": False,
            "time": "22:00:00",
        }
    ]


def test_should_not_return_event_in_database_not_valid_user():

    events_repository = EventsRepository(temp_file())
    app = create_app(repositories={"event": events_repository})
    client = app.test_client()

    concierto_queen = Event(
        id="event-1",
        user_id="user-1",
        name="concierto queen",
        description="un tributo a queen",
        date="2022-01-25",
        completed=False,
        time="22:00:00",
    )
    concierto_camela = Event(
        id="event-2",
        user_id="user-2",
        name="concierto Camela",
        description="un tributo a camela",
        date="2023-08-15",
        completed=False,
        time="23:00:00",
    )
    events_repository.save(concierto_queen, "user-1")
    events_repository.save(concierto_camela, "user-1")

    response = client.get("/api/events", headers={"Authorization": "user-2"})

    assert response.json == []
