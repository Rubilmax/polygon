<template>
  <v-card class="perf-card" elevation="1">
    <v-card-title>{{ title }}</v-card-title>
    <v-divider />
    <div class="perf-stats">
      <div class="perf-stat">
        <span>Min</span>
        <span class="accent--text">0.3s</span>
      </div>
      <div class="perf-stat">
        <span>Avg</span>
        <span class="accent--text">0.3s</span>
      </div>
      <div class="perf-stat">
        <span>Max</span>
        <span class="accent--text">0.3s</span>
      </div>
    </div>
  </v-card>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  name: 'PerfStatsCard',
  props: {
    title: String,
  },
});
</script>

<style scoped lang="scss">
.perf-card {
  margin: 15px 20px;
  padding: 0 25px;
}

.perf-stats {
  display: flex;
  align-items: center;
  justify-content: space-around;
  padding: 20px 0;
}

.perf-stat {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  font-weight: 600;
}
</style>
