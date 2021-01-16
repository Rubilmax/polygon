<template>
  <div class="home-container">
    <v-btn
      class="perf-button text-capitalize px-16 py-8 rounded-lg"
      elevation="0"
      color="primary"
      x-large
      @click="isDialogOpen = true"
    >
      Performances</v-btn
    >
    <v-dialog v-model="isDialogOpen" width="500">
      <v-card class="dialog-card">
        <v-toolbar color="secondary" flat>
          <v-toolbar-title class="text-h6">Performances</v-toolbar-title><v-spacer /><v-btn
            class="text-h6 text-capitalize"
            elevation="0"
            color="transparent"
            @click="isDialogOpen = false"
          >
            Close <v-icon color="accent">mdi-close</v-icon>
          </v-btn>
        </v-toolbar>
        <div class="container" v-if="isDialogOpen">
          <!-- v-if to unmount following components so that they update their stats next time they are displayed -->
          <PerfStatsCard title="Over the last 24 hours" timeframeHours="24" />
          <PerfStatsCard title="Over the last 7 days" timeframeHours="168" />
          <PerfStatsCard title="Over the last 28 days" timeframeHours="672" />
        </div>
      </v-card>
    </v-dialog>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

import PerfStatsCard from './components/PerfStatsCard/PerfStatsCard.vue';

export default Vue.extend({
  name: 'Home',
  components: {
    PerfStatsCard,
  },
  data: () => ({
    isDialogOpen: false,
  }),
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
  font-size: 1.3em !important;
  letter-spacing: 1px;
}

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

.dialog-card {
  min-height: 500px; // for animation purposes
}
</style>
