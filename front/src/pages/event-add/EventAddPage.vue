<template>
  <main>
    <h1>Añadir evento</h1>
    <form class="event-add-form">
      <label for="event-name"> Nombre</label>
      <input
        type="text"
        id="event-name"
        placeholder="Escribe el nombre del evento"
        v-model="event.name"
      />
      <label for="event-description"> Descripción</label>
      <input
        type="text"
        id="event-description"
        placeholder="Escribe la descripción del evento"
        v-model="event.description"
      />
      <label for="event-date"> Fecha</label>
      <input type="date" id="event-date" v-model="event.date" />
      <label for="event-time"> Hora</label>
      <input type="time" id="event-time" v-model="event.time" />
      <button class="btn add-event-btn" @click.prevent="addNewEvent">
        Guardar
      </button>
    </form>
  </main>
</template>

<script>
import { v4 as uuidv4 } from "uuid";
import config from "@/config.js";

export default {
  name: "add-event",
  data() {
    return {
      event: {
        name: "",
        description: "",
        date: "",
        time: "",
        completed: false,
      },
    };
  },

  methods: {
    isValidEventForm() {
      if (
        this.name === "" ||
        this.description === "" ||
        this.date === "" ||
        this.time === ""
      ) {
        return false;
      } else {
        return true;
      }
    },

    async addNewEvent() {
      if (!this.isValidEventForm()) {
        alert("Se deben rellaner todos los campos");
        return;
      }
      this.event.id = uuidv4();
      const settings = {
        method: "POST",
        body: JSON.stringify(this.event),
        headers: {
          Authorization: localStorage.userId,
          "Content-Type": "application/json",
        },
      };
      await fetch(`${config.API_PATH}/events`, settings);
      alert("Evento guardado correctamente");
      this.$router.push("/events");
    },
  },
};
</script>

<style scoped>
main {
  padding: 2em;
}
#event-time {
  width: 5em;
}
#event-date {
  width: 10em;
}
.event-add-form {
  display: flex;
  flex-direction: column;
}
.event-add-form label {
  text-align: left;
}

.event-add-form > * {
  margin-bottom: 0.5em;
}
.event-add-form input {
  padding: 0.5em 0;
}
.add-event-btn {
  padding: 0.5em;
  margin-top: 1em;
  width: fit-content;
}
</style>