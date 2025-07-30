<script setup lang="ts">
import { ref } from 'vue'
import TheHeader from '@/components/TheHeader.vue'

// 로그인과 검색어 상태를 최상위 컴포넌트에서 관리
const isLoggedIn = ref(false)
const searchQuery = ref('')

const handleLogin = () => {
  isLoggedIn.value = true
}

const handleLogout = () => {
  isLoggedIn.value = false
}
</script>

<template>
  <div class="min-h-screen bg-slate-50">
    <TheHeader
      :is-logged-in="isLoggedIn"
      :search-query="searchQuery"
      @update:search-query="(newValue) => (searchQuery = newValue)"
      @login="handleLogin"
      @logout="handleLogout"
    />
    <router-view :is-logged-in="isLoggedIn" :search-query="searchQuery" />
  </div>
</template>

<style scoped>
::-webkit-scrollbar {
  width: 8px;
}
::-webkit-scrollbar-track {
  background: #f1f5f9;
}
::-webkit-scrollbar-thumb {
  background: #94a3b8;
  border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover {
  background: #64748b;
}
</style>
