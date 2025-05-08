<template>
  <div class="music-view">
    <audio
      ref="audioPlayer"
      :src="currentMusic.musicUrl"
      class="music-player"
      @timeupdate="updateCurrentTime"
      @ended="playNext"
    ></audio>
    <div class="music-info">
      <div class="music-cover">
        <img :src="currentMusic.coverUrl" />
      </div>
      <div class="music-info-detail">
        <div class="music-title">{{ currentMusic.title }}</div>
        <div class="music-author">{{ currentMusic.author }}</div>
      </div>
    </div>
    <div class="music-control">
      <i class="fa fa-step-backward" aria-hidden="true" @click="playPrev"></i>
      <i
        class="fa"
        :class="{ 'fa-play': !musicPlaying, 'fa-pause': musicPlaying }"
        aria-hidden="true"
        @click="togglePlay"
      ></i>
      <i class="fa fa-step-forward" aria-hidden="true" @click="playNext"></i>
    </div>
    <div class="music-progress">
      <div class="current-time">{{ formatTime(currentTime) }}</div>
      <el-slider
        @change="handleTimeChange"
        @input="handleSliderInput"
        :max="duration"
        v-model="currentTime"
        :format-tooltip="formatTime"
      ></el-slider>
      <div class="total-time">{{ formatTime(duration) }}</div>
    </div>
    <el-text class="content" :line-clamp="4" type="info" style="color: white; font-weight: bold">{{
      content
    }}</el-text>
  </div>
</template>

<script setup lang="ts">
import axios from 'axios'
import { ref, onMounted, computed, watch } from 'vue'

const content = ref('')
fetch('https://v1.xqapi.com/v1.php?y=sm&type=json')
  .then((res) => res.json())
  .then((data) => {
    content.value = data.text
  })

const audioPlayer = ref<HTMLAudioElement | null>(null)
const musicPlaying = ref(false)
const isDraggingSlider = ref(false)
const isSwitchingSong = ref(false)
const wasPlayingBeforeDrag = ref(false) // 记录拖动前的播放状态

interface Music {
  coverUrl: string
  musicUrl: string
  title: string
  author: string
  duration: number
}

const playList = ref<Music[]>([])
axios
  .get('http://localhost:9999/api/music/get_info')
  .then((data) => {
    playList.value = data.data.data
    // console.log(data.data)
  })
  .catch((err) => {
    console.log('请求失败')
    console.log(err)
  })

const currentMusic = computed(() => {
  if (playList.value.length) {
    console.log(playList.value[0].musicUrl)
    return playList.value[0]
  } else
    return {
      title: 'Style',
      author: 'Taylor Swift',
      coverUrl: '/music/cover/Style  - Taylor Swift.png',
      musicUrl: '/music/Taylor Swift - Style.mp3',
      duration: 231.0,
    }
})
const currentTime = ref(0)
const duration = ref(0)

const togglePlay = () => {
  musicPlaying.value = !musicPlaying.value
  if (audioPlayer.value) {
    if (musicPlaying.value) {
      audioPlayer.value.play().catch(() => (musicPlaying.value = false))
    } else {
      audioPlayer.value.pause()
    }
  }
}

function playPrev() {
  if (playList.value.length) {
    const _ = playList.value.pop()!
    playList.value.unshift(_)
  }
}

function playNext() {
  if (playList.value.length) {
    const _ = playList.value.shift()!
    playList.value.push(_)
  }
}

function loadSong(shouldPlay: boolean) {
  if (audioPlayer.value) {
    audioPlayer.value.src = currentMusic.value.musicUrl
    currentTime.value = 0
    duration.value = 0
    audioPlayer.value.load()
    audioPlayer.value.onloadeddata = () => {
      isSwitchingSong.value = false
      if (shouldPlay) {
        audioPlayer
          .value!.play()
          .then(() => (musicPlaying.value = true))
          .catch(console.error)
      } else {
        musicPlaying.value = false
      }
    }
    audioPlayer.value.onerror = console.error
  }
}

function handleTimeChange(time: number) {
  if (audioPlayer.value) {
    audioPlayer.value.currentTime = time
    currentTime.value = time
  }
}

function handleSliderInput() {
  isDraggingSlider.value = true
  wasPlayingBeforeDrag.value = musicPlaying.value // 记录拖动前的播放状态
  if (audioPlayer.value && !audioPlayer.value.paused) {
    audioPlayer.value.pause()
  }
}

function updateCurrentTime() {
  if (audioPlayer.value && !isDraggingSlider.value) {
    currentTime.value = audioPlayer.value.currentTime
    duration.value = audioPlayer.value.duration
  }
  isDraggingSlider.value = false
  // 拖动结束后自动播放
  if (audioPlayer.value && wasPlayingBeforeDrag.value && audioPlayer.value.paused) {
    audioPlayer.value.play().catch(console.error)
  }
}

onMounted(() => {
  if (audioPlayer.value) {
    audioPlayer.value.addEventListener('loadedmetadata', () => {
      duration.value = audioPlayer.value!.duration
    })
  }
  loadSong(false)
})

function formatTime(seconds: number): string {
  const minutes = Math.floor(seconds / 60)
  const remainingSeconds = Math.floor(seconds % 60)
  return `${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`
}

watch(currentMusic, () => {
  loadSong(true)
})

watch(currentTime, (newTime) => {
  if (audioPlayer.value && isDraggingSlider.value) {
    audioPlayer.value.currentTime = newTime
  }
})
</script>

<style scoped>
.music-info {
  display: flex;
  align-items: center;
  padding: 1em;
}

.music-cover img {
  width: 4em;
  height: 4em;
  border-radius: 1em;
  margin-right: 1em;
}

.music-info-detail {
  flex-grow: 1;
}

.music-title {
  font-size: 1.1em;
  font-weight: bold;
  margin-bottom: 0.2em;
  color: white;
}
.music-author {
  font-size: 0.9em;
  color: white;
  font-weight: bold;
}

.music-control {
  display: flex;
  align-items: center;
  justify-content: space-around;
  padding: 1em;
}

.music-control i {
  font-size: 1.5em;
  cursor: pointer;
  color: #333;
}

.music-progress {
  padding: 0 1em 1em 1em;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.9em;
  color: white;
  font-weight: bold;
}

.current-time {
  position: relative;
  left: -1em;
}

.total-time {
  position: relative;
  right: -1em;
}

.content {
  margin-top: 1em;
  display: block;
  text-align: center;
}
</style>
