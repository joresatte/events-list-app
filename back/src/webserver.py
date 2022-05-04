from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from src.domain.events import Event
from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.errorhandler(403)
    def resource_not_found(e):
        return jsonify(error=str(e)), 403

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/events", methods=["GET"])
    def events_get_by_user_id():
        user_id = request.headers.get("Authorization")
        all_events = repositories["event"].search_by_user_id(user_id)
        return object_to_json(all_events), 200

    @app.route("/api/events", methods=["POST"])
    def events_save_by_user_id():
        user_id = request.headers.get("Authorization")
        data = request.json
        data["user_id"] = user_id
        event = Event(**data)
        repositories["event"].save(event, user_id)
        if user_id == event.user_id:
            return ("", 200)
        else:
            return 403

    @app.route("/api/events/<id>", methods=["GET"])
    def events_get_by_id(id):
        user_id = request.headers.get("Authorization")
        event_by_id = repositories["event"].get_events_by_id(id)
        return object_to_json(event_by_id)

    @app.route("/api/events/<id>", methods=["DELETE"])
    def events_delete_by_id(id):
        user_id = request.headers.get("Authorization")
        asked_event = repositories["event"].get_events_by_id(id)
        event_deleted = repositories["event"].delete_event_by_id(id, user_id)
        if user_id == asked_event.user_id:
            return (event_deleted, 200)
        else:
            return ("", 403)

    @app.route("/api/events/<id>", methods=["PUT"])
    def events_modify(id):
        user_id = request.headers.get("Authorization")
        data = request.json
        data["user_id"] = user_id
        event = Event(**data)
        repositories["event"].modify_event(id, event, user_id)
        if user_id == event.user_id:
            return ("", 200)
        else:
            return ("", 403)

    @app.route("/api/users", methods=["GET"])
    def users_get():
        all_users = repositories["user"].get_users()
        return object_to_json(all_users)

    # @app.route("/api/events/future/<date>", methods=["GET"])
    # def events_get_by_date(date):
    #     user_id = request.headers.get("Authorization")
    #     event_by_date = repositories["event"].get_future_events(date, user_id)
    #     return object_to_json(event_by_date), 200

    @app.route("/api/orderedevents", methods=["GET"])
    def events_get_by_date_ordered():
        user_id = request.headers.get("Authorization")
        all_events = repositories["event"].get_events_ordered_by_date(user_id)
        return object_to_json(all_events), 200

    return app
