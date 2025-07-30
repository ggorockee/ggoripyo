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
            <label for="email" class="block text-sm font-medium text-gray-700">이메일 주소</label>
            <div class="mt-1">
              <input
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
            <label for="password" class="block text-sm font-medium text-gray-700">비밀번호</label>
            <div class="mt-1">
              <input
                id="password"
                name="password"
                type="password"
                required
                class="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-blue-500 focus:outline-none focus:ring-blue-500 sm:text-sm"
              />
            </div>
          </div>

          <div>
            <label for="password-confirm" class="block text-sm font-medium text-gray-700"
              >비밀번호 확인</label
            >
            <div class="mt-1">
              <input
                id="password-confirm"
                name="password-confirm"
                type="password"
                required
                class="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-blue-500 focus:outline-none focus:ring-blue-500 sm:text-sm"
              />
            </div>
          </div>

          <div>
            <button
              type="submit"
              class="flex w-full justify-center rounded-md border border-transparent bg-blue-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
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
import { useRouter } from 'vue-router'

const router = useRouter()
const handleSignUp = () => {
  // TODO: 실제 회원가입 로직 구현
  alert('회원가입 성공! 로그인 페이지로 이동합니다. (시뮬레이션)')
  router.push('/login')
}
</script>
