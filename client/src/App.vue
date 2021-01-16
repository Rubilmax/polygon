<template>
  <v-app><AppBar /><Home /></v-app>
</template>

<script lang="ts">
import Vue from 'vue';

import AppBar from './components/AppBar/AppBar.vue';

import Home from './pages/Home/Home.vue';

export default Vue.extend({
  name: 'App',
  components: {
    AppBar,
    Home,
  },
});
</script>
