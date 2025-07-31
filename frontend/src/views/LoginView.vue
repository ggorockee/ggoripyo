<template>
  <div class="flex min-h-full flex-col justify-center py-12 sm:px-6 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-md">
      <h2 class="mt-6 text-center text-3xl font-bold tracking-tight text-gray-900">
        다시 오셨네요! <br />꼬리표가 기다렸어요.
      </h2>
    </div>

    <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
      <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
        <form class="space-y-6" @submit.prevent="handleLogin">
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700"
              >가입하셨던 이메일 주소</label
            >
            <div class="mt-1">
              <input
                v-model="email"
                id="email"
                name="email"
                type="email"
                autocomplete="email"
                required
                class="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-blue-500 focus:outline-none focus:ring-blue-500 sm:text-sm"
              />
            </div>
          </div>

          <div>
            <label for="password" class="block text-sm font-medium text-gray-700"
              >비밀번호도 잊지 않으셨죠?</label
            >
            <div class="mt-1">
              <input
                v-model="password"
                id="password"
                name="password"
                type="password"
                autocomplete="current-password"
                required
                class="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-blue-500 focus:outline-none focus:ring-blue-500 sm:text-sm"
              />
            </div>
          </div>

          <div>
            <button
              type="submit"
              :class="[
                'flex w-full justify-center rounded-md border border-transparent py-2 px-4 text-sm font-medium text-white shadow-sm transition-colors',
                isFormReady
                  ? 'bg-blue-600 hover:bg-blue-700 focus:ring-blue-500'
                  : 'bg-blue-300 cursor-not-allowed',
              ]"
            >
              로그인
            </button>
          </div>
        </form>

        <div class="mt-6">
          <div class="relative">
            <div class="absolute inset-0 flex items-center">
              <div class="w-full border-t border-gray-300" />
            </div>
            <div class="relative flex justify-center text-sm">
              <span class="bg-white px-2 text-gray-500">계정이 없으신가요?</span>
            </div>
          </div>

          <div class="mt-6">
            <router-link
              to="/signup"
              class="flex w-full justify-center rounded-md border border-gray-300 bg-white py-2 px-4 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50"
              >꼬리표 붙이러 가기</router-link
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'

const router = useRouter()
const toast = useToast()

// --- [추가] 폼 상태 관리를 위한 ref ---
const email = ref('')
const password = ref('')

// --- [추가] 폼이 준비되었는지 확인하는 computed 속성 ---
const isFormReady = computed(() => {
  return email.value && password.value
})

const handleLogin = () => {
  // --- [추가] 폼 제출 전 유효성 검사 ---
  if (!isFormReady.value) {
    toast.error('이메일과 비밀번호를 모두 입력해주세요!')
    return
  }

  // TODO: 실제 로그인 로직 구현
  // [수정] alert 대신 success 토스트 사용
  toast.success('다시 오신 것을 환영해요! 🙌')
  router.push('/')
}
</script>
