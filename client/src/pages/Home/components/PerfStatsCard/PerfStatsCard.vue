<template>
  <v-card class="perf-card" elevation="1">
    <v-card-title>{{ title }}</v-card-title>
    <v-divider />
    <div class="perf-stats">
      <div class="perf-stat">
        <span>Min</span>
        <span class="accent--text">{{ displayTime(minCompletionTime) }}</span>
      </div>
      <div class="perf-stat">
        <span>Avg</span>
        <span class="accent--text">{{ displayTime(avgCompletionTime) }}</span>
      </div>
      <div class="perf-stat">
        <span>Max</span>
        <span class="accent--text">{{ displayTime(maxCompletionTime) }}</span>
      </div>
    </div>
  </v-card>
</template>

<script lang="ts">
import Vue from 'vue';
import superagent from 'superagent';

export default Vue.extend({
  name: 'PerfStatsCard',
  props: {
    title: String,
    timeframeHours: String,
  },
  data: () => ({
    minCompletionTime: -1,
    avgCompletionTime: -1,
    maxCompletionTime: -1,
  }),
  created: function () {
    this.fetchPerformances().then(({ minCompletionTime, avgCompletionTime, maxCompletionTime }) => {
      this.minCompletionTime = minCompletionTime;
      this.avgCompletionTime = avgCompletionTime;
      this.maxCompletionTime = maxCompletionTime;
    });
  },
  methods: {
    async fetchPerformances(): Promise<PerfStats> {
      const { body: perfStatsResponse } = await superagent
        .get(`http://127.0.0.1:8000/performances`)
        .query({ timeframeHours: this.timeframeHours });

      return perfStatsResponse;
    },
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
