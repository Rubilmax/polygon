<template>
  <div class="home-container">
    <v-btn class="perf-button text-capitalize px-16 py-8 rounded-lg" elevation="0" color="primary" x-large>
      Performances</v-btn
    >
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  name: 'Home',
  props: {
    msg: String,
  },
});
</script>

<style scoped lang="scss">
.home-container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  background-color: #fbfbff;
}

.perf-button {
  font-size: 1.2em !important;
  letter-spacing: 1px;
}
</style>
