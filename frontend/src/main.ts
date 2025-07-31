import './assets/main.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import Toast, { type PluginOptions, POSITION } from 'vue-toastification' // [수정] POSITION 추가

import 'vue-toastification/dist/index.css'

const app = createApp(App)

app.use(createPinia())
app.use(router)

const options: PluginOptions = {
  // 알림 위치를 화면 상단 중앙으로 설정
  position: POSITION.TOP_CENTER,
  // 3초 후에 자동으로 사라지도록 설정 (단위: ms)
  timeout: 3000,
  // 알림을 클릭해서 닫을 수 있도록 설정
  closeOnClick: true,
  // 진행 바(progress bar) 숨기기
  hideProgressBar: true,
  // 아이콘 비활성화 (필요 시 true로 변경)
  icon: false,
  // 통통 튀는 듯한 트랜지션 효과 적용
  transition: 'Vue-Toastification__bounce',
}

app.use(Toast, options)
app.mount('#app')
