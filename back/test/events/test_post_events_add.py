from wsgiref import headers
from src.lib.utils import temp_file
from flask import json, request

from src.webserver import create_app
from src.domain.events import EventsRepository, Event


def test_front_should_post_new_events():

    events_repository = EventsRepository(temp_file())
    app = create_app(repositories={"event": events_repository})
    client = app.test_client()

    body = {
        "id": "event-1",
        "name": "concierto queen",
        "description": "un tributo a queen",
        "date": "2022-01-25",
        "completed": False,
        "time": "22:00:00",
    }

    response = client.post(
        "/api/events", json=body, headers={"Authorization": "user-1"}
    )

    response_get = client.get(
        "/api/events/event-1", headers={"Authorization": "user-1"}
    )

    assert response_get.json == {
        "id": "event-1",
        "user_id": "user-1",
        "name": "concierto queen",
        "description": "un tributo a queen",
        "date": "2022-01-25",
        "completed": False,
        "time": "22:00:00",
    }
