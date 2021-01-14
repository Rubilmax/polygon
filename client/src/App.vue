<template>
  <Home />
</template>

<script lang="ts">
import Vue from 'vue';
import Home from './pages/Home/Home.vue';

export default Vue.extend({
  name: 'App',
  components: {
    Home,
  },
});
</script>

<style lang="scss">
#app {
}
</style>
