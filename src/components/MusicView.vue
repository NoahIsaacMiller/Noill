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
      <i class="fa fa-heart" aria-hidden="true"></i>
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
    <el-text class="content" :line-clamp="4" type="info">{{ content }}</el-text>
  </div>
</template>

<script setup lang="ts">
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
}

const playList = ref<Music[]>([
  {
    coverUrl:
      'https://p2.music.126.net/E2tigbpOIoDODSr3wGsQAg==/109951166650063350.jpg?imageView&thumbnail=360y360&quality=75&tostatic=0',
    musicUrl: 'music/若生命等候.mp3',
    title: '若生命等候',
    author: '黄凯芹',
  },
  {
    coverUrl:
      'https://p2.music.126.net/E2tigbpOIoDODSr3wGsQAg==/109951166650063350.jpg?imageView&thumbnail=360y360&quality=75&tostatic=0',
    musicUrl: 'music/Style - Taylor Swift.mp3',
    title: 'Style',
    author: 'Taylor Swift',
  },
])

const currentMusicIndex = ref(0)
const currentMusic = computed(() => playList.value[currentMusicIndex.value])
const currentTime = ref(0)
const duration = ref(0)

const togglePlay = () => {
  musicPlaying.value = !musicPlaying.value
  if (audioPlayer.value) {
    musicPlaying.value ? audioPlayer.value.play().catch(console.error) : audioPlayer.value.pause()
  }
}

function playPrev() {
  currentMusicIndex.value =
    currentMusicIndex.value > 0 ? currentMusicIndex.value - 1 : playList.value.length - 1
  loadSong(true)
}

function playNext() {
  currentMusicIndex.value =
    currentMusicIndex.value < playList.value.length - 1 ? currentMusicIndex.value + 1 : 0
  loadSong(true)
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
        audioPlayer.value.play().catch(console.error)
        musicPlaying.value = true
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
    duration.value = audioPlayer.value.duration || 0
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
      duration.value = audioPlayer.value!.duration || 0
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
}
.music-author {
  font-size: 0.9em;
  color: #666;
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
}

.music-progress {
  font-size: 0.8em;
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
}
</style>
