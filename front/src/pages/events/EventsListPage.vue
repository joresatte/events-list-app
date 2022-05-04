<template>
  <h1>Mis eventos</h1>

  <main class="events-main">
    <button class="btn btn-add-event" @click="addNewEventClicked">
      ➕ Añadir Evento
    </button>

    <!-- <div class="input-container">
      <input type="date" v-model="date" @change="filterEventsByDate(date)" />
    </div> -->
    <section class="events-container">
      <article class="event" v-for="event in eventList" :key="event.id">
        <h2>{{ event.name }}</h2>

        <p>{{ event.date }}</p>
        <button class="btn" @click="openEventDetail(event)">Ver más</button>
        <button class="btn btn-delete" @click="removeEvent(event)">
          Eliminar
        </button>
      </article>
    </section>
  </main>
</template>

<script>
import config from "@/config.js";
export default {
  name: "events",
  data() {
    return {
      eventList: [],
      date: "",
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async filterEventsByDate(date) {
      const settings = {
        methods: "GET",
        headers: {
          Authorization: localStorage.userId,
        },
      };
      let endpoint = `${config.API_PATH}/events/future/${date}`;

      let response = await fetch(endpoint, settings);
      let loadData = await response.json();

      this.eventList = loadData;
    },
    async loadData() {
      const settings = {
        methods: "GET",
        headers: {
          Authorization: localStorage.userId,
        },
      };
      let endpoint = `${config.API_PATH}/orderedevents`;

      let response = await fetch(endpoint, settings);
      let loadData = await response.json();

      this.eventList = loadData;
    },

    async removeEvent(event) {
      if (confirm("¿Deseas eliminar este evento?")) {
        await fetch("http://localhost:5000/api/events/" + event.id, {
          method: "DELETE",
          headers: {
            Authorization: localStorage.userId,
            "Content-Type": "application/json",
          },
        });
      } else {
        return "";
      }
      location.reload(true);
    },
    addNewEventClicked() {
      this.$router.push("/events/add");
    },

    openEventDetail(event) {
      this.$router.push("/events/" + event.id);
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600&display=swap");
.input-container {
  text-align: center;
}
h1 {
  text-align: center;
}
.events-main {
  display: flex;
  flex-direction: column;
}
.events-container {
  color: white;
  font-family: Montserrat;
  display: grid;
  gap: 2em;
  grid-auto-rows: 22rem;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 50rem), 1fr));
  margin: 2em 1.5em;
}

.events-container .event {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  text-align: center;
  background: rgb(61, 58, 58);
  box-shadow: 0px 0px 8px black;
  border-radius: 10px;
  font-size: larger;
}
.events-container .event h2 {
  color: #42b983;
  font-weight: bold;
  text-transform: capitalize;
}
.events-container .event p {
  max-width: 80%;
}

.btn {
  margin-top: 1rem;
  font-size: 1rem;
  border: 2px solid transparent;
  border-radius: 5px;
  background: #42b983;
  box-shadow: 0px 0px 4px black;
  height: 2.5rem;
  width: 13rem;
  transition: 0.1s ease-in;
}
.btn-add-event {
  margin-left: auto;
  margin-right: 1.5em;
}

.btn:hover {
  background: rgb(61, 58, 58);
  box-shadow: 0px 0px 4px #42b983;
  color: #42b983;
  font-size: 1.05rem;
}
.btn-delete:hover {
  background: rgb(61, 58, 58);
  box-shadow: 0px 0px 9px #ff3c00;
  color: #ff3c00;
  font-size: 1.05rem;
  font-weight: bold;
}
</style>
