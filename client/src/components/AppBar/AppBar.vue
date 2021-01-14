<template>
  <div class="container py-5">
    <img src="@/assets/logo.svg" height="30" />
    <img src="@/assets/polygon.png" height="60" />
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
}
</style>
