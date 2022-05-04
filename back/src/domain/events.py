import sqlite3
from datetime import *


class Event:
    def __init__(self, id, user_id, name, description, date, completed, time):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.date = date
        self.completed = completed
        self.time = time

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "description": self.description,
            "date": self.date,
            "completed": self.completed,
            "time": self.time,
        }


class EventsRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists events (
                id varchar PRIMARY KEY,
                user_id varchar,
                name text,
                description text,
                date text,
                completed bool,
                time text
                )
                """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_events(self):
        sql = """select * from events"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()
        result = []
        for item in data:
            event = Event(**item)
            result.append(event)
        return result

    def search_by_user_id(self, user_id):
        sql = """select * from events WHERE user_id=:user_id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"user_id": user_id})

        data = cursor.fetchall()
        result = []
        for item in data:
            event = Event(**item)

            result.append(event)
        return result

    def get_events_by_id(self, id):
        sql = """select * from events where id=:id """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})

        data = cursor.fetchone()
        event = Event(**data)
        return event

    def save(self, event, user_id):
        sql = """insert into events (id,user_id,name,description,date,completed,time) values (
            :id, :user_id, :name, :description, :date, :completed, :time)"""

        conn = self.create_conn()
        cursor = conn.cursor()
        params = event.to_dict()
        params["user_id"] = user_id
        cursor.execute(sql, params)

        conn.commit()

    def delete_event_by_id(self, id, user_id):
        sql = """
            DELETE FROM events
            WHERE events.id = :id AND user_id=:user_id
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id, "user_id": user_id})
        conn.commit()

    def modify_event(self, id, event, user_id):
        sql = """
            UPDATE events
            SET name= :name, description= :description,date= :date, time= :time
            WHERE id = :id and user_id=:user_id
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        params = event.to_dict()
        params["user_id"] = user_id
        params["id"] = id
        cursor.execute(sql, params)

        conn.commit()

    def get_future_events(self, date, user_id):

        sql = """select * from events where user_id=:user_id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"user_id": user_id})

        data = cursor.fetchall()
        result = []
        for item in data:
            if item["date"] >= date:
                event = Event(**item)
                result.append(event)

        return result

    def get_events_ordered_by_date(self, user_id):

        sql = """select * from events WHERE user_id=:user_id ORDER BY date,time ASC"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"user_id": user_id})

        data = cursor.fetchall()
        result = []
        dia_actual = str(datetime.today())
        for item in data:
            if item["date"] >= dia_actual:
                event = Event(**item)
                result.append(event)
        return result
