<template>
  <div v-if="bookmarks.length > 0" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
    <BookmarkCard
      v-for="bookmark in bookmarks"
      :key="bookmark.id"
      :bookmark="bookmark"
      @edit="$emit('edit', bookmark)"
      @delete="$emit('delete', bookmark.id)"
    />
  </div>
  <EmptyState v-else @add="$emit('add')" />
</template>

<script setup lang="ts">
import BookmarkCard from './BookmarkCard.vue'
import EmptyState from './EmptyState.vue'
import type { Bookmark } from '@/types'

defineProps<{
  bookmarks: Bookmark[]
}>()

defineEmits<{
  (e: 'edit', bookmark: Bookmark): void
  (e: 'delete', id: number): void
  (e: 'add'): void
}>()
</script>
