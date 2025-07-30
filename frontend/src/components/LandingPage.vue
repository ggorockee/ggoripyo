<template>
  <div class="text-center py-16 sm:py-24 px-4">
    <h1 class="text-4xl sm:text-5xl font-extrabold text-slate-900 tracking-tight">
      웹서핑 중 발견한 보물, <br class="sm:hidden" />
      <span class="text-blue-600">이제 잃어버리지 마세요.</span>
    </h1>
    <p class="mt-6 max-w-2xl mx-auto text-lg text-slate-600">
      '꼬리표'를 톡 붙여두기만 하세요. <br />
      나만 알고 싶은 주소, 나중에 다시 볼 영상, 영감을 주는 모든 페이지를 한 곳에.
    </p>
    <div class="mt-8 flex justify-center gap-x-4">
      <button
        @click="$emit('login')"
        type="button"
        class="inline-flex items-center px-6 py-3 border border-transparent shadow-sm text-base font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
      >
        내 꼬리표 만들러 가기
      </button>
      <a
        href="https://github.com/google/gemini-pro-vision"
        target="_blank"
        class="inline-flex items-center px-6 py-3 border border-slate-300 shadow-sm text-base font-medium rounded-md text-slate-700 bg-white hover:bg-slate-50"
      >
        GitHub 구경하기
      </a>
    </div>
  </div>
</template>

<script setup lang="ts">
defineEmits<{ (e: 'login'): void }>()
</script>
