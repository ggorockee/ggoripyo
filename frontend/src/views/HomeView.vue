<template>
  <div class="min-h-screen bg-slate-50">
    <main class="max-w-5xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
      <BookmarkList
        v-if="isLoggedIn"
        :bookmarks="filteredBookmarks"
        @edit="openEditModal"
        @delete="deleteBookmark"
        @add="openAddModal"
      />
      <LandingPage v-else @login="handleLogin" />
    </main>

    <template v-if="isLoggedIn">
      <BookmarkModal
        :is-open="isModalOpen"
        :mode="modalMode"
        :bookmark="currentBookmark"
        @close="closeModal"
        @save="saveBookmark"
      />
      <button
        @click="openAddModal"
        class="fixed bottom-8 right-8 bg-blue-600 text-white rounded-full p-4 shadow-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-transform hover:scale-110"
      >
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M12 6v6m0 0v6m0-6h6m-6 0H6"
          ></path>
        </svg>
      </button>
    </template>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import BookmarkList from '@/components/BookmarkList.vue'
import BookmarkModal from '@/components/BookmarkModal.vue'
import LandingPage from '@/components/LandingPage.vue' // [추가]
import type { Bookmark } from '@/types'

// --- [추가] 로그인 상태 관리 ---
const isLoggedIn = ref<boolean>(false)

const handleLogin = () => {
  isLoggedIn.value = true
}

// ---

const bookmarks = ref<Bookmark[]>([])
const searchQuery = ref<string>('')
const isModalOpen = ref<boolean>(false)
const modalMode = ref<'add' | 'edit'>('add')
const currentBookmark = ref<Partial<Bookmark>>({})

onMounted(() => {
  const storedBookmarks = localStorage.getItem('bookmarks')
  if (storedBookmarks) {
    bookmarks.value = JSON.parse(storedBookmarks)
  }
})

const filteredBookmarks = computed<Bookmark[]>(() => {
  if (!searchQuery.value) return bookmarks.value
  return bookmarks.value.filter(
    (bookmark) =>
      bookmark.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      bookmark.url.toLowerCase().includes(searchQuery.value.toLowerCase()),
  )
})

const persistBookmarks = (): void => {
  localStorage.setItem('bookmarks', JSON.stringify(bookmarks.value))
}

const openAddModal = (): void => {
  modalMode.value = 'add'
  currentBookmark.value = { name: '', url: '' }
  isModalOpen.value = true
}

const openEditModal = (bookmark: Bookmark): void => {
  modalMode.value = 'edit'
  currentBookmark.value = { ...bookmark }
  isModalOpen.value = true
}

const closeModal = (): void => {
  isModalOpen.value = false
}

const saveBookmark = (bookmarkData: Bookmark): void => {
  if (modalMode.value === 'add') {
    bookmarks.value.unshift({
      id: Date.now(),
      name: bookmarkData.name,
      url: bookmarkData.url,
    })
  } else {
    const index = bookmarks.value.findIndex((b) => b.id === bookmarkData.id)
    if (index !== -1) {
      bookmarks.value[index] = { ...bookmarkData }
    }
  }
  persistBookmarks()
  closeModal()
}

const deleteBookmark = (id: number): void => {
  // [수정] 위트 있는 메시지
  if (confirm('이 링크와 작별인가요? 뒤돌아보지 않으셔도 돼요.')) {
    bookmarks.value = bookmarks.value.filter((b) => b.id !== id)
    persistBookmarks()
  }
}
</script>
