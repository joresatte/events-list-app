<template>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/events">Events</router-link>
    <p class="user">{{ loggedUser }}</p>
  </div>
  <router-view />
</template>

<script>
export default {
  data() {
    return {
      loggedUser: localStorage.userName,
    };
  },
};
</script>
<style scoped>
.user {
  text-decoration: none;
  size: 1.2em;
}
</style>