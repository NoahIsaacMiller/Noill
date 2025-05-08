<template>
  <div class="app-wrapper">
    <div class="animate-wrapper">
      <div class="happy" v-if="current === 'upset'">
        <!-- <div class="cloud" style="left: 70vw; top: 1vh"></div>
        <div class="cloud" style="left: 20vw; top: -1vh; height: 15em; width: 15em"></div>
        <div class="cloud" style="left: 0vw; top: -15vh"></div>
        <div class="cloud" style="left: 40vw; top: -12vh"></div>
        <div class="cloud" style="left: 60vw; top: 10vh"></div>
        <div class="cloud" style="left: 30vw; top: 12vh; height: 15em; width: 15em"></div> -->
        <!-- <div
          class="cloud"
          style="
            left: 20vw;
            top: 20vh;
            background-image: url('weather_background/cloud2.png');
            transform: rotate(45deg);
            filter: brightness(0.7);
          "
        ></div>
        <div
          class="cloud"
          style="
            left: -10vw;
            top: 0vh;
            background-image: url('weather_background/cloud2.png');
            transform: rotate(45deg);
            filter: brightness(0.7);
          "
        ></div> -->
      </div>
    </div>
    <MimicFrame>
      <template #view>
        <MusicView />
      </template>
    </MimicFrame>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import MimicFrame from './components/MimicFrame.vue'
import MusicView from './components/MusicView.vue'

const current = ref('upset')

// 获取随机数
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

.cloud {
  width: 20em;
  height: 20em;
  position: absolute;
  top: -2em;
  left: 0em;
  background-size: cover;
  background-image: url('weather_background/cloud1.png');
  background-repeat: no-repeat;
  z-index: -1;
  animation: cloud-animation 100s ease-out forwards;
  filter: blur(2px);

  /* background-color: red; */
}
@keyframes cloud-animation {
  100% {
    transform: translateX(50vw);
  }
}
</style>
