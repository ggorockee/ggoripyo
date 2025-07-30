<template>
  <div
    class="bg-white rounded-lg shadow-md hover:shadow-xl transition-shadow duration-300 overflow-hidden group"
  >
    <div class="p-5">
      <div class="flex items-center justify-between">
        <div class="flex items-center min-w-0">
          <img
            :src="faviconUrl"
            @error="onImageError"
            alt="파비콘"
            class="w-8 h-8 rounded-full flex-shrink-0"
          />
          <h3 class="text-lg font-bold text-slate-800 ml-3 truncate" :title="bookmark.name">
            {{ bookmark.name }}
          </h3>
        </div>
        <div class="relative">
          <button
            @click.stop="toggleMenu"
            class="text-slate-400 hover:text-slate-600 focus:outline-none flex-shrink-0"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z"
              ></path>
            </svg>
          </button>
          <!-- 드롭다운 메뉴 -->
          <div
            v-if="isMenuOpen"
            class="absolute right-0 mt-2 w-40 bg-white rounded-md shadow-lg z-20"
          >
            <a
              href="#"
              @click.prevent.stop="$emit('edit')"
              class="block px-4 py-2 text-sm text-slate-700 hover:bg-slate-100"
              >수정하기</a
            >
            <a
              href="#"
              @click.prevent.stop="$emit('delete')"
              class="block px-4 py-2 text-sm text-red-600 hover:bg-slate-100"
              >삭제하기</a
            >
          </div>
        </div>
      </div>
      <a
        :href="bookmark.url"
        target="_blank"
        class="block text-sm text-slate-500 mt-2 truncate hover:text-blue-600"
        :title="bookmark.url"
        >{{ bookmark.url }}</a
      >
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, computed } from 'vue'
import type { Bookmark } from '@/types'

const props = defineProps<{
  bookmark: Bookmark
}>()

defineEmits<{
  (e: 'edit'): void
  (e: 'delete'): void
}>()

const isMenuOpen = ref<boolean>(false)

const faviconUrl = computed(
  () => `https://www.google.com/s2/favicons?domain=${props.bookmark.url}&sz=32`,
)

const toggleMenu = (): void => {
  isMenuOpen.value = !isMenuOpen.value
}

const closeMenu = (): void => {
  isMenuOpen.value = false
}

const onImageError = (event: Event) => {
  ;(event.target as HTMLImageElement).src = 'https://placehold.co/32x32/e2e8f0/64748b?text=B'
}

onMounted(() => {
  window.addEventListener('click', closeMenu)
})

onUnmounted(() => {
  window.removeEventListener('click', closeMenu)
})
</script>
