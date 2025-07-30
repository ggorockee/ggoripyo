<template>
  <header class="bg-white/80 backdrop-blur-sm shadow-sm sticky top-0 z-10">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center">
          <svg
            class="w-8 h-8 text-blue-600"
            fill="none"
            stroke-width="1.5"
            viewBox="0 0 24 24"
            stroke="currentColor"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M9.568 3H5.25A2.25 2.25 0 003 5.25v4.318c0 .597.237 1.17.659 1.591l9.581 9.581c.699.699 1.78.872 2.607.33a18.095 18.095 0 005.223-5.223c.542-.827.369-1.908-.33-2.607L11.16 3.66A2.25 2.25 0 009.568 3z"
            ></path>
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 6h.008v.008H6V6z"></path>
          </svg>
          <h1 class="text-xl sm:text-2xl font-bold text-slate-800 ml-2 whitespace-nowrap">
            꼬리표
          </h1>
        </div>

        <div v-if="isLoggedIn" class="flex items-center gap-x-4">
          <div class="relative w-40 sm:w-full sm:max-w-xs">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <svg class="h-5 w-5 text-slate-400" fill="currentColor" viewBox="0 0 20 20">
                <path
                  fill-rule="evenodd"
                  d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                  clip-rule="evenodd"
                ></path>
              </svg>
            </div>
            <input
              :value="searchQuery"
              @input="$emit('update:searchQuery', ($event.target as HTMLInputElement).value)"
              type="text"
              placeholder="꼬리표 검색..."
              class="block w-full bg-slate-100 border border-transparent rounded-full py-2 pl-10 pr-3 text-sm placeholder-slate-500 focus:outline-none focus:bg-white focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition"
            />
          </div>

          <div class="relative">
            <button
              @click.stop="toggleUserMenu"
              type="button"
              class="flex items-center text-sm bg-transparent rounded-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
            >
              <span class="sr-only">사용자 메뉴 열기</span>
              <svg
                class="h-8 w-8 text-slate-600 hover:text-blue-600"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M17.982 18.725A7.488 7.488 0 0012 15.75a7.488 7.488 0 00-5.982 2.975m11.963 0a9 9 0 10-11.963 0m11.963 0A8.966 8.966 0 0112 21a8.966 8.966 0 01-5.982-2.275M15 9.75a3 3 0 11-6 0 3 3 0 016 0z"
                />
              </svg>
            </button>
            <transition
              enter-active-class="transition ease-out duration-100"
              enter-from-class="transform opacity-0 scale-95"
              enter-to-class="transform opacity-100 scale-100"
              leave-active-class="transition ease-in duration-75"
              leave-from-class="transform opacity-100 scale-100"
              leave-to-class="transform opacity-0 scale-95"
            >
              <div
                v-if="isUserMenuOpen"
                class="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg py-1 bg-white ring-1 ring-black ring-opacity-5 focus:outline-none z-20"
              >
                <a
                  href="#"
                  @click.prevent.stop="$emit('logout')"
                  class="block px-4 py-2 text-sm text-slate-700 hover:bg-slate-100"
                  >로그아웃</a
                >
              </div>
            </transition>
          </div>
        </div>

        <div v-else class="flex items-center space-x-2">
          <router-link
            to="/login"
            class="px-4 py-2 text-sm font-medium text-slate-600 hover:text-blue-600"
          >
            로그인
          </router-link>
          <router-link
            to="/signup"
            class="px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-full hover:bg-blue-700"
          >
            회원가입
          </router-link>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

defineProps<{
  searchQuery?: string
  isLoggedIn: boolean
}>()

defineEmits<{
  (e: 'update:searchQuery', value: string): void
  (e: 'login'): void
  (e: 'logout'): void
}>()

const isUserMenuOpen = ref(false)

const toggleUserMenu = () => {
  isUserMenuOpen.value = !isUserMenuOpen.value
}

const closeUserMenu = () => {
  isUserMenuOpen.value = false
}

onMounted(() => {
  window.addEventListener('click', closeUserMenu)
})

onUnmounted(() => {
  window.removeEventListener('click', closeUserMenu)
})
</script>
