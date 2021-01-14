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
      <v-card>
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
        <div class="container">
          <v-card class="perf-card" elevation="1">
            <v-card-title>Over the last 24 hours</v-card-title>
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
          <v-card class="perf-card" elevation="1">
            <v-card-title>Over the last 7 days</v-card-title>
            <v-divider />
            <div class="perf-stats">
              <div class="perf-stat">
                <span>Min</span>
                <span class="accent--text">0.3s</span>
              </div>
              <div class="perf-stat">
                <span>Avg</span>
                <span class="accent--text">289ms</span>
              </div>
              <div class="perf-stat">
                <span>Max</span>
                <span class="accent--text">0.3s</span>
              </div>
            </div>
          </v-card>
          <v-card class="perf-card" elevation="1">
            <v-card-title>Over the last 28 days</v-card-title>
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
        </div>
      </v-card>
    </v-dialog>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  name: 'Home',
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
</style>
