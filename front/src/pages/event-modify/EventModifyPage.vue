<template>
  <h1>Modifica tu evento</h1>
  <section class="events-main">
    <label for="event-name">Nombre</label>
    <input
      type="text"
      id="event-name"
      placeholder="Escribe el nombre del evento"
      v-model="event.name"
    />
    <label for="event-description">Descripcion:</label>
    <input
      type="text"
      id="event-description"
      placeholder="Escribe la descripción del evento"
      v-model="event.description"
    />
    <label for="event-date">Fecha:</label>
    <input type="date" id="event-date" v-model="event.date" />
    <label for="event-time">Hora:</label>
    <input type="time" id="event-time" v-model="event.time" />
    <button class="btn" @click.prevent="addNewEvent">Guardar</button>
    <button class="btn" @click.prevent="cancelModifyEvent">Cancelar</button>
  </section>
</template>

yudsgbcdyu



<script>
import config from "@/config.js";



export default {
  name: "eventsModifyPage",
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
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const settings = {
        methods: "GET",
        headers: {
          Authorization: localStorage.userId,
        },
      };
      let endpoint = `${config.API_PATH}/events/` + this.$route.params.id;
      let response = await fetch(endpoint, settings);
      let loadData = await response.json();

      this.event = loadData;
    },

    // isValidEventForm() {
    //   if (
    //     this.name === "" ||
    //     this.description === "" ||
    //     this.date === "" ||
    //     this.time === ""
    //   ) {
    //     return false;
    //   } else {
    //     return true;
    //   }
    // },

    async addNewEvent() {
      // if (!this.isValidEventForm()) {
      //   alert("Se deben rellenar todos los campos");
      //   return;
      // }
      if (confirm("¿Estas seguro de querer modificar este evento?")) {
        const settings = {
          method: "PUT",
          body: JSON.stringify(this.event),
          headers: {
            Authorization: localStorage.userId,
            "Content-Type": "application/json",
          },
        };
        await fetch(
          `${config.API_PATH}/events/` + this.$route.params.id,
          settings
        );
        alert("Evento guardado correctamente");
        this.$router.push("/events");
      } else {
        this.$router.push("/events/modify/" + this.$route.params.id);
      }
    },
    cancelModifyEvent() {
      this.$router.push("/events/" + this.$route.params.id);
    },
  },
};
</script>

<style scoped>
h1 {
  text-align: center;
}
.events-main {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  background: rgb(61, 58, 58);
  box-shadow: 0px 0px 8px black;
  border-radius: 10px;
  font-size: larger;
  color: white;
  font-family: Montserrat;
  margin: 30px;
  padding: 1em 0;
}
.events-main label {
  margin-bottom: 0.6em;
}
.events-main h2 {
  color: #42b983;
  font-weight: bold;
  text-transform: capitalize;
}

.events-main input {
  padding: 0.4em;
  font-size: 1em;
  margin-bottom: 0.4em;
}

#event-date {
  width: 10em;
  height: 1.5;
}
#event-time {
  width: 6em;
  height: 1.5em;
}

</style> 