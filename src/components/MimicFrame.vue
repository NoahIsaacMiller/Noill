<template>
  <!-- <video src="/weather_background/raining.mp4"></video> -->

  <div class="mimic-frame-container">
    <div class="emotion">
      <div class="emotion-bar">
        <div class="emotion-bar-item" :style="`top: ${100 - feeling.pressure}%;`">
          {{ feeling.emoji }}
        </div>
      </div>
      <div style="width: 3em; overflow: hidden; margin-top: -0.5em">
        压力: {{ `${feeling.pressure}%` }}
      </div>
    </div>

    <div class="mimic-frame">
      <slot name="view"> </slot>
      <svg
        t="1746613110667"
        class="icon-switch"
        viewBox="0 0 1024 1024"
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        p-id="3455"
        width="32"
        height="32"
      >
        <path
          d="M514.56 962.56C267.776 962.56 66.56 761.344 66.56 514.56S267.776 66.56 514.56 66.56 962.56 267.776 962.56 514.56 761.344 962.56 514.56 962.56z m0-834.56C301.568 128 128 301.568 128 514.56S301.568 901.12 514.56 901.12s386.56-173.568 386.56-386.56S727.552 128 514.56 128z"
          p-id="3456"
          fill="#ffffff"
        ></path>
        <path
          d="M737.28 482.816H291.84c-15.36 0-28.16-12.8-28.16-28.16s12.8-28.16 28.16-28.16h445.44c15.36 0 28.16 12.8 28.16 28.16s-12.8 28.16-28.16 28.16z"
          p-id="3457"
          fill="#ffffff"
        ></path>
        <path
          d="M615.936 293.376l141.312 141.312c10.752 10.752 10.752 28.672 0 39.936-10.752 10.752-28.672 10.752-39.936 0l-141.312-141.312c-10.752-10.752-10.752-28.672 0-39.936 11.264-10.752 29.184-10.752 39.936 0zM311.808 555.008L453.12 696.32c10.752 10.752 10.752 28.672 0 39.936-10.752 10.752-28.672 10.752-39.936 0l-141.312-141.312c-10.752-10.752-10.752-28.672 0-39.936s28.672-11.264 39.936 0z"
          p-id="3458"
          fill="#ffffff"
        ></path>
        <path
          d="M737.28 603.136H291.84c-15.36 0-28.16-12.8-28.16-28.16s12.8-28.16 28.16-28.16h445.44c15.36 0 28.16 12.8 28.16 28.16s-12.8 28.16-28.16 28.16z"
          p-id="3459"
          fill="#ffffff"
        ></path>
      </svg>
    </div>
  </div>
  <div class="data-bar">
    <div class="data-bar-item">
      <svg
        t="1746675492409"
        class="icon"
        viewBox="0 0 1024 1024"
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        p-id="2729"
        width="48"
        height="48"
      >
        <path
          d="M400.5376 350.08l-3.328 0.2048a33.5872 33.5872 0 0 0-27.52 20.864l-40.7296 101.248H142.6688a33.5872 33.5872 0 0 0 0 67.1744h209.024l3.4048-0.1536c12.3136-1.2544 23.0656-9.216 27.776-20.8896l18.8672-46.9504 20.1728 47.5136 1.4336 2.9952c5.8624 10.6752 17.1008 17.4592 29.44 17.4592h41.6l48.2816 38.0928c5.9136 4.6848 13.2608 7.2192 20.8128 7.2192l3.3536-0.1536a33.6128 33.6128 0 0 0 27.648-20.6336l27.9552-67.6608 22.016 29.5936c6.3232 8.4992 16.3072 13.5424 26.9312 13.568h144.2048c18.5344 0 33.5616-15.0528 33.5616-33.5872l-0.1536-3.4304a33.5872 33.5872 0 0 0-33.408-30.1568l-127.36-0.0256-47.2576-63.488a33.5872 33.5872 0 0 0-31.104-13.2608l-3.5328 0.64c-10.4448 2.4576-19.2 9.8048-23.3472 19.8656l-33.5872 81.2544-22.4768-17.7664-3.072-2.1504a33.5872 33.5872 0 0 0-17.7664-5.0688h-31.0784l-43.2128-101.8624a33.2032 33.2032 0 0 0-27.904-20.352l-3.3536-0.1024z"
          fill="#FB553C"
          p-id="2730"
        ></path>
        <path
          d="M207.7184 241.5616c83.9168-83.9168 215.296-92.16 308.5824-23.7824l2.5088 1.8944a238.0288 238.0288 0 0 1 300.9792 12.3136l5.632 5.1456 4.864 4.7616 4.4544 4.608c84.7616 89.7024 86.4512 229.1968 4.8384 321.1776l-5.12 5.5552-4.0192 4.1728-252.7744 252.7488a83.2 83.2 0 0 1-113.9712 3.4816l-3.6864-3.4816-152.3456-152.32a32 32 0 0 1 42.6496-47.616l2.6112 2.3296 152.3456 152.3712a19.2 19.2 0 0 0 24.9856 1.8432l2.176-1.8432 252.3904-252.416 3.4048-3.5072c61.5936-65.2032 63.1552-166.4512 4.9152-233.1648l-4.608-5.0688-3.5072-3.6352-3.8912-3.7888c-64.384-60.8512-164.096-63.232-230.912-6.912l-5.1968 4.5312-4.2752 4.0448a32 32 0 0 1-41.2672 2.1504l-2.7392-2.3552-1.5872-1.5104A173.824 173.824 0 0 0 205.824 373.76a32 32 0 1 1-62.6176-13.1584 236.8 236.8 0 0 1 64.5376-119.04z"
          fill="#FB553C"
          p-id="2731"
        ></path>
      </svg>
      <span>心率</span>
      <span>{{ feeling.heartRate }} BPM</span>
    </div>

    <div class="data-bar-item">
      <svg
        t="1746676646022"
        class="icon"
        viewBox="0 0 1190 1024"
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        p-id="3785"
        width="38"
        height="38"
      >
        <path
          d="M1001.146 1014.082a37.482 37.482 0 0 1-25.492 9.882 37.625 37.625 0 0 1-27.374-11.692 36.375 36.375 0 0 1 1.87-52.044c105.326-96.54 165.693-233.122 165.693-374.633 0-282.296-233.455-511.976-520.442-511.976S74.864 303.3 74.864 585.595c0 141.488 60.439 277.95 165.682 374.537a36.53 36.53 0 0 1 1.857 52.104c-14.11 14.872-37.78 15.574-52.913 1.798C69.101 903.54 0.066 747.336 0.066 585.571 0.066 262.698 267.157 0.011 595.426 0.011c328.255 0 595.275 262.71 595.275 585.56 0 161.908-69.047 318.064-189.555 428.51z m-450.204-510.87l243.492-170.789-104.03 276.938c-1.595 58.32-49.84 105.208-109.481 105.208-60.582 0-109.792-48.353-109.792-107.946 0-49.366 33.85-90.48 79.81-103.41z"
          p-id="3786"
          fill="#83ee5c"
        ></path>
      </svg>
      <span style="margin-top: -0.2em">压力</span>
      <span>{{ feeling.pressure }}%</span>
    </div>

    <div class="data-bar-item">
      <svg
        t="1746677011138"
        class="icon"
        viewBox="0 0 1024 1024"
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        p-id="10101"
        width="36"
        height="36"
      >
        <path
          d="M1006.717435 29.354279l-3.176767-10.483331-10.483331-2.85909C816.11142-31.004292 539.097345 15.694182 304.33427 288.896136c-110.233812-2.541414-199.500962 36.53282-288.768112 127.070677l-15.566158 15.566158 216.655504 145.178248c-28.908579 52.098977-11.754038 129.294413 43.521706 184.252481s132.47118 72.112609 183.617128 44.474736l145.813601 218.561564 15.566158-15.883835c91.808564-91.17321 131.200474-180.122684 127.070677-291.309526C1006.717435 480.137504 1053.733585 206.93555 1006.717435 29.354279zM676.969029 650.729888l-31.767669 26.684842 1.588384 40.980293a254.141353 254.141353 0 0 1-47.969181 164.874203l-127.070676-190.606015-68.618166 36.215143a85.772707 85.772707 0 0 1-83.231293-29.861609 82.278263 82.278263 0 0 1-28.908579-82.59594l37.803527-68.618165-190.606015-127.070677a265.895391 265.895391 0 0 1 162.650466-47.01615h40.34494l26.367165-31.767669c173.76915-202.677729 386.294857-283.049932 563.240774-254.141353 29.861609 177.58127-51.145947 388.518594-253.823677 562.923097zM100.385834 816.239444c-40.980293 40.980293-66.394428 168.05097-66.394428 168.05097s122.305526-20.648985 168.05097-66.394429a81.960586 81.960586 0 0 0 12.707067-114.363609 81.960586 81.960586 0 0 0-114.363609 12.707068z"
          p-id="10102"
          fill="#9eeafc"
        ></path>
        <path
          d="M660.132165 298.10876a63.535338 63.535338 0 1 0 63.535338 63.535338 63.535338 63.535338 0 0 0-63.535338-63.535338z"
          p-id="10103"
          fill="#9eeafc"
        ></path>
      </svg>
      <span style="margin-top: 0.2em">元气值</span>
      <span>{{ feeling.feeling }}%</span>
    </div>

    <div class="data-bar-item">
      <svg
        t="1746679270408"
        class="icon"
        viewBox="0 0 1024 1024"
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        p-id="11244"
        width="36"
        height="36"
      >
        <path
          d="M890.751654 652.62331l-115.563795-217.596386a36.570821 36.570821 0 0 0-32.365177-19.565389H281.298918a36.570821 36.570821 0 0 0-32.365177 19.565389l-115.563795 217.596386a36.570821 36.570821 0 0 0 32.365177 53.759108h692.651354a36.570821 36.570821 0 0 0 32.365177-53.759108zM583.73961 38.233514a86.307138 86.307138 0 0 0-143.357619 0l-152.500325 287.080946a36.570821 36.570821 0 0 0 32.365177 53.576253h383.993623a36.570821 36.570821 0 0 0 32.365177-53.576253zM80.342255 1024h863.43709c59.610439 0 98.375509-54.856232 71.678809-100.021196l-85.941429-161.64303a36.570821 36.570821 0 0 0-32.182323-19.382535H126.787198a36.570821 36.570821 0 0 0-32.182322 19.382535l-85.94143 161.64303C-18.216108 969.143768 20.731817 1024 80.342255 1024z"
          fill="#83ee5c"
          p-id="11245"
        ></path>
      </svg>
      <span style="margin-top: 0.2em">压力等级</span>
      <span>{{ feeling.pressureLevel }}</span>
    </div>
  </div>
</template>

<script setup lang="ts">
import axios from 'axios'
import { ref } from 'vue'

/**
 * {
            # 心率, 血氧, 压力, 元气, 压力等级
            "心率": 0,
            "血氧": 0,
            "压力": 27,
            "元气": 0,
            "压力等级": PressureLevel.MIDDLE.value,
            "emoji": FeelingEmoji.FINE.value
        },
 */
interface Feeling {
  heartRate: number
  bloodOxygen: number
  pressure: number
  feeling: number
  pressureLevel: number
  emoji: string
}

const feeling = ref<Feeling>({
  heartRate: 0,
  bloodOxygen: 0,
  pressure: 0,
  feeling: 0,
  pressureLevel: 1,
  emoji: '🥰',
})
axios
  .get('http://localhost:9999/api/feeling/get_info')
  .then((res) => res.data.data)
  .then((data) => {
    feeling.value = data
    console.log('心情', data)
  })
  .catch((err) => console.log('心情获取失败', err))

// function getPersentage(value: number, max: number) {
//   return (value / max) * 100
// }
</script>

<style scoped>
.mimic-frame-container {
  background-color: #e1f0ff22;
  transition: all 0.5s ease-out;
  &:hover {
    box-shadow: 0.5em 0.5em 0.5em 0em #00000044;
  }

  border-radius: 2em;
  padding: 2em;
  display: flex;
  justify-content: space-evenly;
  overflow: hidden;
  flex-wrap: nowrap;
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

.icon-switch {
  position: relative;
  top: -9.2em;
  right: -2.5em;
  filter: brightness(0.7);
}

.data-bar-item {
  text-align: center;
  align-content: center;
  justify-items: center;
  background-color: #e1f0ff22;
  flex-basis: calc(50% - 10px);

  transition: all 0.5s ease-out;

  padding: 1em 3em;
  border-radius: 1em;

  &:hover {
    background-color: #e1f0ff44;
    box-shadow: 0.5em 0.5em 0.5em 0em #00000044;
  }
  & svg {
    display: block;
  }
  & span {
    margin-top: -0.6em;
    display: block;
    font-weight: bold;
    font-size: 0.8em;
  }
}

.data-bar {
  display: flex;
  justify-content: space-evenly;
  margin-top: 2em;
  flex-wrap: wrap;
  flex-direction: row;
  gap: 10px;
}

@media (min-width: 1024px) {
  .mimic-frame-container {
    width: 50%;
    height: 50vh;
  }

  .emotion-bar {
    width: 1.6em;
  }

  .icon-switch {
    top: -13.8em;
    right: -8.2em;
  }
}
</style>
