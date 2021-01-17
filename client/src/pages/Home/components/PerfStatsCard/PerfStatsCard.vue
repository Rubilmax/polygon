<template>
  <v-card class="perf-card" elevation="1">
    <v-card-title>{{ title }}</v-card-title>
    <v-divider />
    <div class="perf-stats">
      <v-progress-circular v-if="loading" indeterminate></v-progress-circular>
      <div class="perf-stat" v-if="!loading">
        <span>Min</span>
        <span class="accent--text">{{ minCompletionTimeDisplay }}</span>
      </div>
      <div class="perf-stat" v-if="!loading">
        <span>Avg</span>
        <span class="accent--text">{{ avgCompletionTimeDisplay }}</span>
      </div>
      <div class="perf-stat" v-if="!loading">
        <span>Max</span>
        <span class="accent--text">{{ maxCompletionTimeDisplay }}</span>
      </div>
    </div>
  </v-card>
</template>

<script lang="ts">
import Vue from 'vue';

import { getTimeDisplay, getPerformances } from '../../../../services/performances';

export default Vue.extend({
  name: 'PerfStatsCard',
  props: {
    title: String,
    timeframeHours: Number,
    displayed: Boolean,
  },
  data: () => ({
    loading: false,
    minCompletionTime: -1,
    avgCompletionTime: -1,
    maxCompletionTime: -1,
  }),
  methods: {
    fetchPerformances() {
      if (this.displayed) {
        this.loading = true;

        getPerformances(this.timeframeHours).then(({ minCompletionTime, avgCompletionTime, maxCompletionTime }) => {
          this.minCompletionTime = minCompletionTime;
          this.avgCompletionTime = avgCompletionTime;
          this.maxCompletionTime = maxCompletionTime;

          this.loading = false;
        });
      }
    },
  },
  computed: {
    minCompletionTimeDisplay: function () {
      return getTimeDisplay(this.minCompletionTime);
    },
    avgCompletionTimeDisplay: function () {
      return getTimeDisplay(this.avgCompletionTime);
    },
    maxCompletionTimeDisplay: function () {
      return getTimeDisplay(this.maxCompletionTime);
    },
  },
  watch: {
    displayed: {
      immediate: true,
      handler() {
        this.fetchPerformances();
      },
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
