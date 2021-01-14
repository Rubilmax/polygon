<template>
  <div class="container">
    <img src="@/assets/logo.svg" height="50" />
    <img src="@/assets/polygon.png" height="80" />
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  name: 'AppBar',
  props: {
    msg: String,
  },
});
</script>

<style scoped lang="scss">
.container {
  display: flex;
  align-items: center;
  height: 100px;
}
</style>
