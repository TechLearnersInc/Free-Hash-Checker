<template>
  <div class="col-span-12">
    <div class="flex justify-center items-center">
      <img class="size-48 mt-10 mb-10" v-bind:src="appIcon" alt="app_icon" />
    </div>
    <div class="flex justify-center items-center">
      <h1 class="font-lato text-5xl font-semibold text-gray-700 text-center">Free Hash Checker</h1>
    </div>
    <div class="flex justify-center items-center">
      <h6 class="font-poppins text-xs font-semibold text-gray-700 text-center">v3.0</h6>
    </div>
    <div class="flex justify-center items-center">
      <p class="font-poppins text-xl text-gray-500 text-center m-3">
        A simple and elegant Free Hash Checker for desktop
      </p>
    </div>
    <div class="flex justify-center items-center">
      <a v-bind:href="downloadUrl"
        ><button
          type="button"
          class="text-blue-400 hover:text-white border border-blue-400 hover:bg-blue-400 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded text-xl px-5 py-2.5 text-center me-2 mb-2 mt-2"
        >
          Download
        </button></a
      >
    </div>
    <div class="flex justify-center items-center">
      <a class="text-xs text-blue-500 m-0 mt-3" v-bind:href="gitRepoUrl">
        Give this project a star on GitHub
      </a>
    </div>
  </div>
</template>

<script>
import AppIcon from '@/assets/images/icon.png';
import AppHeaderIcon from '@/assets/images/header.png';

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
      appHeaderIcon: AppHeaderIcon,
    };
  },
};
</script>
