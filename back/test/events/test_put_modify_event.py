from email import header
from wsgiref import headers
from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.events import EventsRepository, Event


def test_put_method_should_modify_event():
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

    concierto_queen = Event(
        id="event-1",
        user_id="user-1",
        name="concierto queen",
        description="un tributo a queen de la ostia",
        date="2022-01-25",
        completed=False,
        time="22:00:00",
    )

    events_repository.modify_event("event-1", concierto_queen, "user-1")

    response_modify = client.put("api/events/event-1")

    response = client.get("api/events/event-1", headers={"Authorization": "user-1"})

    assert response.json == {
        "id": "event-1",
        "user_id": "user-1",
        "name": "concierto queen",
        "description": "un tributo a queen de la ostia",
        "date": "2022-01-25",
        "completed": False,
        "time": "22:00:00",
    }
