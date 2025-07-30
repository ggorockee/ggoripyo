<template>
  <div
    v-if="isOpen"
    class="fixed inset-0 z-50 flex items-center justify-center bg-black/30 backdrop-blur-sm"
    @click.self="$emit('close')"
  >
    <div class="bg-white rounded-lg shadow-xl w-full max-w-md mx-4" @click.stop>
      <div class="p-6">
        <h3 class="text-xl font-bold text-slate-800 mb-4">
          {{ mode === 'add' ? '새 북마크 추가' : '북마크 수정' }}
        </h3>
        <form @submit.prevent="handleSubmit">
          <div class="space-y-4">
            <div>
              <label for="name" class="block text-sm font-medium text-slate-700">이름</label>
              <input
                v-model="editableBookmark.name"
                type="text"
                id="name"
                class="mt-1 block w-full border border-slate-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                required
              />
            </div>
            <div>
              <label for="url" class="block text-sm font-medium text-slate-700">URL</label>
              <div class="mt-1 flex rounded-md shadow-sm">
                <input
                  v-model="editableBookmark.url"
                  type="url"
                  id="url"
                  class="block w-full border border-slate-300 rounded-l-md py-2 px-3 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                  placeholder="https://example.com"
                  required
                />
                <button
                  @click="startQrScanner"
                  type="button"
                  class="relative -ml-px inline-flex items-center justify-center rounded-r-md border border-slate-300 bg-slate-50 px-3 py-2 text-sm font-medium text-slate-500 hover:bg-slate-100"
                >
                  <svg
                    class="h-5 w-5"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke-width="1.5"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="M3.75 4.5a.75.75 0 00-.75.75v13.5a.75.75 0 00.75.75h13.5a.75.75 0 00.75-.75V5.25a.75.75 0 00-.75-.75H3.75zM8.25 9.75h.008v.008H8.25v-.008zm0 3h.008v.008H8.25v-.008zm0 3h.008v.008H8.25v-.008zm3-6h.008v.008H11.25v-.008zm0 3h.008v.008H11.25v-.008zm0 3h.008v.008H11.25v-.008zm3-6h.008v.008H14.25v-.008zm0 3h.008v.008H14.25v-.008z"
                    />
                  </svg>
                </button>
              </div>
            </div>

            <div id="qr-reader" class="w-full"></div>
          </div>
          <div class="mt-6 flex justify-end space-x-3">
            <button
              @click="$emit('close')"
              type="button"
              class="bg-white py-2 px-4 border border-slate-300 rounded-md shadow-sm text-sm font-medium text-slate-700 hover:bg-slate-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
            >
              취소
            </button>
            <button
              type="submit"
              class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
            >
              저장
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, onUnmounted } from 'vue'
import { Html5Qrcode, type Html5QrcodeResult } from 'html5-qrcode'
import type { Bookmark } from '@/types'

const props = defineProps<{
  isOpen: boolean
  mode: 'add' | 'edit'
  bookmark: Partial<Bookmark>
}>()

const emit = defineEmits<{
  (e: 'close'): void
  (e: 'save', bookmark: Bookmark): void
}>()

const editableBookmark = ref<Partial<Bookmark>>({})

watch(
  () => props.bookmark,
  (newVal) => {
    editableBookmark.value = { ...newVal }
  },
  { deep: true, immediate: true },
)

const handleSubmit = () => {
  emit('save', editableBookmark.value as Bookmark)
}

// --- QR 코드 스캔 관련 로직 ---

let html5QrCode: Html5Qrcode | null = null

const startQrScanner = () => {
  if (html5QrCode?.isScanning) return
  html5QrCode = new Html5Qrcode('qr-reader')

  // [수정] 사용하지 않는 result 매개변수 앞에 _ 추가
  const onScanSuccess = (decodedText: string, result: Html5QrcodeResult) => {
    console.log(result)
    if (editableBookmark.value) {
      editableBookmark.value.url = decodedText
    }
    stopQrScanner()
  }

  const qrConfig = { fps: 10, qrbox: { width: 250, height: 250 } }

  html5QrCode
    .start({ facingMode: 'environment' }, qrConfig, onScanSuccess, undefined)
    .catch((err) => {
      console.error('QR 스캐너 시작 실패', err)
      alert('앗, 카메라님 수줍으신가봐요. 권한을 확인해주시겠어요?')
    })
}

const stopQrScanner = () => {
  if (html5QrCode && html5QrCode.isScanning) {
    html5QrCode.stop().catch((err) => console.error('QR 스캐너 중지 실패', err))
  }
}

watch(
  () => props.isOpen,
  (newVal) => {
    if (!newVal) {
      stopQrScanner()
    }
  },
)

onUnmounted(() => {
  stopQrScanner()
})
</script>
