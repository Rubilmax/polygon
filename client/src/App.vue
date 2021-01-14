<template>
  <Home />
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Home from './pages/Home/Home.vue';

@Component({
  components: {
    Home,
  },
})
export default class App extends Vue {}
</script>

<style lang="scss">
</style>
