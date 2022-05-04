<template>
  <h1>Detalles del evento</h1>
  <section class="events-main">
    <h2>{{ event.name }}</h2>
    <p>{{ event.description }}</p>
    <p>{{ event.date }}</p>
    <p>{{ event.time }}</p>

    <button class="btn" @click="onButtonClicked">Modificar</button>
    <router-link to="/events" @click="removeEventInside"
      ><button class="btn btn-delete">Eliminar</button></router-link
    >
  </section>
</template>
<script>
import config from "@/config.js";
export default {
  name: "events",
  data() {
    return {
      event: {},
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
    onButtonClicked() {
      this.$router.push("/events/modify/" + this.$route.params.id);
    },
    async removeEventInside() {
      if (confirm("¿Deseas eliminar este evento?")) {
        await fetch(`${config.API_PATH}/events/` + this.$route.params.id, {
          method: "DELETE",
          headers: {
            Authorization: localStorage.userId,
            "Content-Type": "application/json",
          },
        });
      } else {
        this.$router.push(this.$route.params.id);
      }
      location.reload(true);
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
.events-main h2 {
  color: #42b983;
  font-weight: bold;
  text-transform: capitalize;
}
.events-main p {
  max-width: 80%;
}

.btn-delete:hover {
  background: rgb(61, 58, 58);
  box-shadow: 0px 0px 9px #ff3c00;
  color: #ff3c00;
  font-size: 1.25rem;
  font-weight: bold;
}
</style>