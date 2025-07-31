<template>
  <div class="flex min-h-full flex-col justify-center py-12 sm:px-6 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-md">
      <h2 class="mt-6 text-center text-3xl font-bold tracking-tight text-gray-900">
        꼬리표, 같이 붙여볼까요?
      </h2>
      <p class="mt-2 text-center text-sm text-gray-600">나만의 웹 아카이브를 만들어 보세요.</p>
    </div>

    <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
      <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
        <form class="space-y-6" @submit.prevent="handleSignUp">
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700"
              >로그인할 때 쓸 이메일이에요</label
            >
            <div class="mt-1">
              <input
                v-model="email"
                id="email"
                type="email"
                required
                class="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-blue-500 focus:outline-none focus:ring-blue-500 sm:text-sm"
              />
              <p v-if="emailError" class="mt-2 text-sm text-red-600">{{ emailError }}</p>
            </div>
          </div>

          <div>
            <label for="password" class="block text-sm font-medium text-gray-700"
              >비밀번호 (8자 이상이면 좋아요!)</label
            >
            <div class="mt-1">
              <input
                v-model="password"
                id="password"
                type="password"
                required
                class="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-blue-500 focus:outline-none focus:ring-blue-500 sm:text-sm"
              />
            </div>
          </div>

          <div>
            <label for="password-confirm" class="block text-sm font-medium text-gray-700"
              >한 번 더! (혹시 모르니까요)</label
            >
            <div class="mt-1">
              <input
                v-model="passwordConfirm"
                id="password-confirm"
                type="password"
                required
                class="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-blue-500 focus:outline-none focus:ring-blue-500 sm:text-sm"
              />
              <p v-if="passwordError" class="mt-2 text-sm text-red-600">{{ passwordError }}</p>
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
              회원가입
            </button>
          </div>
        </form>
        <div class="mt-6 text-center">
          <router-link to="/login" class="font-medium text-blue-600 hover:text-blue-500"
            >이미 꼬리표가 있으신가요?</router-link
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'

const router = useRouter()
const toast = useToast()

// --- [추가] 폼 상태 관리를 위한 ref ---
const email = ref('')
const password = ref('')
const passwordConfirm = ref('')
const emailError = ref('')
const passwordError = ref('')

// --- [추가] 이메일 유효성 검사 로직 ---
const validateEmail = () => {
  if (email.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
    emailError.value = '앗! 이메일 형식인지 다시 한번 확인해주세요.'
  } else {
    emailError.value = ''
  }
}

// --- [추가] 비밀번호 일치 확인 로직 ---
const checkPasswordMatch = () => {
  if (password.value && passwordConfirm.value && password.value !== passwordConfirm.value) {
    passwordError.value = '휴, 비밀번호가 서로 다른 것 같아요.'
  } else {
    passwordError.value = ''
  }
}

// --- [추가] ref 값이 바뀔 때마다 유효성 검사 실행 ---
watch(email, validateEmail)
watch([password, passwordConfirm], checkPasswordMatch)

// --- [추가] 모든 조건이 만족되었는지 계산하는 computed 속성 ---
const isFormReady = computed(() => {
  return (
    email.value &&
    !emailError.value &&
    password.value &&
    passwordConfirm.value &&
    password.value === passwordConfirm.value
  )
})

const handleSignUp = () => {
  if (!isFormReady.value) {
    // [수정] alert 대신 error 토스트 메시지 사용
    toast.error('입력 내용을 다시 확인해주세요. 🧐')
    return
  }

  // TODO: 실제 회원가입 로직 구현
  // [수정] alert 대신 success 토스트 메시지 사용
  toast.success('회원가입 성공! 대문으로 이동합니다. 🚀')
  router.push('/')
}
</script>
