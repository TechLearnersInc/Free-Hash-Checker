<template>
  <div class="flex items-center justify-center">
    <img class="mb-10 mt-10 size-48" v-bind:src="appIcon" alt="app_icon" />
  </div>
  <div class="flex items-center justify-center">
    <h1 class="text-center font-lato text-5xl font-semibold text-gray-700">Free Hash Checker</h1>
  </div>
  <div class="flex items-center justify-center">
    <h6 class="text-center font-poppins text-xs font-semibold text-gray-700">v3.0</h6>
  </div>
  <div class="flex items-center justify-center">
    <p class="m-3 text-center font-poppins text-xl text-gray-500">
      A simple and elegant Free Hash Checker for desktop
    </p>
  </div>
  <div class="flex items-center justify-center">
    <a v-bind:href="downloadUrl"
      ><button
        type="button"
        class="mb-2 me-2 mt-2 rounded border border-blue-400 px-5 py-2.5 text-center text-xl font-medium text-blue-400 hover:bg-blue-400 hover:text-white focus:outline-none focus:ring-4 focus:ring-blue-300"
      >
        Download
      </button></a
    >
  </div>
  <div class="flex items-center justify-center">
    <a class="m-0 mt-3 text-xs text-blue-500" v-bind:href="gitRepoUrl">
      Give this project a star on GitHub
    </a>
  </div>
</template>

<script>
import AppIcon from '@/assets/images/icon.png';

export default {
  name: 'AppHeader',
  props: {
    gitRepoUrl: {
      type: String,
      required: true,
    },
    downloadUrl: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      appIcon: AppIcon,
    };
  },
};
</script>
