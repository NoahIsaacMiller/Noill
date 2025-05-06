<template>
  <video
    class="video-background"
    src="/weather_background/raining.mp4"
    :autoplay="true"
    :muted="true"
    loop
  ></video>
  <div class="mimic-frame-container">
    <div class="emotion">
      <div class="emotion-bar">
        <div class="emotion-bar-item" :style="`top: ${(1 - number / (emojis.length - 1)) * 100}%;`">
          {{ emojis[number] }}
        </div>
      </div>
      <div style="width: 3em; overflow: hidden; margin-top: -0.5em">
        压力: {{ `${parseInt(100 - (1 - number / (emojis.length - 1)) * 100)}%` }}
      </div>
    </div>
    <div class="mimic-frame">
      <slot name="view">
        {{ number }}<br />
        <input type="range" v-model="number" :max="emojis.length - 1" min="0" step="1" />
      </slot>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const number = ref(0)
const emojis = ['🥰', '😃', '🙄', '😐', '😮‍💨', '😐', '😐', '😟', '😰', '🥹']
</script>

<style scoped>
.mimic-frame-container {
  background-color: #e1f0ff22;
  box-shadow:
    0.5em 0.5em 1em 0em #000000aa,
    -0.5em -0.5em 1em 0em #ffffffaa;

  border-radius: 2em;
  padding: 2em;
  display: flex;
  justify-content: space-evenly;
  overflow: hidden;
}

.emtion {
  display: flex;
  flex: 0 0 20%;
}

.emotion-bar {
  width: 2em;
  height: 80%;
  background-image: linear-gradient(to top, skyblue, lightgreen, yellow, deeppink);
  border-radius: 0.8em;
  margin-bottom: 2em;
}

.emotion-bar-item {
  position: relative;
  width: 100%;
  height: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 3em;
  text-shadow: 0.05em 0.05em 0.2em #000000;
}

.mimic-frame {
  padding: 1em;
  flex: 0 0 80%;
  flex-shrink: 0;
  display: flex;
  justify-items: center;
  justify-content: center;
  align-items: center;
}

@media (min-width: 1024px) {
  .mimic-frame-container {
    width: 50%;
    height: 50vh;
  }

  .emotion-bar {
    width: 1.6em;
  }

  video {
    border-radius: 2em;
    position: absolute;
    z-index: -1;
  }
}
</style>
