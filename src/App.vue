<template>
  <div class="app-wrapper">
    <MimicFrame>
      <template #view>
        <MusicView />
      </template>
    </MimicFrame>
  </div>
</template>

<script setup lang="ts">
import MimicFrame from './components/MimicFrame.vue'
import MusicView from './components/MusicView.vue'
</script>

<style scoped>
.app-wrapper {
  width: 95%;
  height: 80%;
  grid-column: span 2;
  justify-self: center;
  align-content: center;
  justify-items: center;
}
</style>
