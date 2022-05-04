from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.events import EventsRepository, Event


def test_should_return_event_by_date():

    events_repository = EventsRepository(temp_file())
    app = create_app(repositories={"event": events_repository})
    client = app.test_client()

    concierto_queen = Event(
        id="event-1",
        user_id="user-1",
        name="concierto queen",
        description="un tributo a queen",
        date="2022-03-25",
        completed=False,
        time="22:00:00",
    )

    concierto_camela = Event(
        id="event-2",
        user_id="user-1",
        name="concierto Camela",
        description="un tributo a camela",
        date="2022-03-25",
        completed=False,
        time="20:00:00",
    )
    concierto_joseba = Event(
        id="event-3",
        user_id="user-1",
        name="concierto Camela",
        description="un tributo a camela",
        date="2022-04-28",
        completed=False,
        time="20:00:00",
    )
    events_repository.save(concierto_queen, "user-1")
    events_repository.save(concierto_camela, "user-1")
    events_repository.save(concierto_joseba, "user-1")
    response = client.get("/api/orderedevents", headers={"Authorization": "user-1"})

    assert response.status_code == 200
    assert response.json == [
        {
            "id": "event-2",
            "user_id": "user-1",
            "name": "concierto Camela",
            "description": "un tributo a camela",
            "date": "2022-03-25",
            "completed": False,
            "time": "20:00:00",
        },
        {
            "id": "event-1",
            "user_id": "user-1",
            "name": "concierto queen",
            "description": "un tributo a queen",
            "date": "2022-03-25",
            "completed": False,
            "time": "22:00:00",
        },
        {
            "id": "event-3",
            "user_id": "user-1",
            "name": "concierto Camela",
            "description": "un tributo a camela",
            "date": "2022-04-28",
            "completed": False,
            "time": "20:00:00",
        },
    ]
