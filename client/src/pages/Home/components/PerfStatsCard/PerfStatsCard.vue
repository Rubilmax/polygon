<template>
  <v-card class="perf-card" elevation="1">
    <v-card-title>{{ title }}</v-card-title>
    <v-divider />
    <div class="perf-stats">
      <v-progress-circular v-if="loading" indeterminate></v-progress-circular>
      <div class="perf-stat" v-if="!loading">
        <span>Min</span>
        <span class="accent--text">{{ displayTime(minCompletionTime) }}</span>
      </div>
      <div class="perf-stat" v-if="!loading">
        <span>Avg</span>
        <span class="accent--text">{{ displayTime(avgCompletionTime) }}</span>
      </div>
      <div class="perf-stat" v-if="!loading">
        <span>Max</span>
        <span class="accent--text">{{ displayTime(maxCompletionTime) }}</span>
      </div>
    </div>
  </v-card>
</template>

<script lang="ts">
import Vue from 'vue';

import { getPerformances } from '@/services/performances';

export default Vue.extend({
  name: 'PerfStatsCard',
  props: {
    title: String,
    timeframeHours: Number,
  },
  data: () => ({
    loading: true,
    minCompletionTime: -1,
    avgCompletionTime: -1,
    maxCompletionTime: -1,
  }),
  created: function () {
    getPerformances(Number(this.timeframeHours)).then(({ minCompletionTime, avgCompletionTime, maxCompletionTime }) => {
      this.minCompletionTime = minCompletionTime;
      this.avgCompletionTime = avgCompletionTime;
      this.maxCompletionTime = maxCompletionTime;

      this.loading = false;
    });
  },
  methods: {
    displayTime(time: number) {
      if (time < 0) return 'Unknown';

      if (time >= 1) {
        return Math.round(time * 100) / 100 + 's';
      }

      return Math.round(time * 1000 * 100) / 100 + 'ms';
    },
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
