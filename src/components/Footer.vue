<template>
  <footer class="m-4 rounded-lg bg-white">
    <div class="mx-auto w-full max-w-screen-xl p-4 md:py-8">
      <div class="sm:flex sm:items-center sm:justify-between">
        <a
          href="https://free-hash-checker.github.io/"
          class="mb-4 flex items-center space-x-3 sm:mb-0 rtl:space-x-reverse"
        >
          <img v-bind:src="appHeaderIcon" class="h-10" alt="Free Hash Checker Logo" />
        </a>
        <ul class="mb-6 flex flex-wrap items-center text-sm font-medium text-gray-500 sm:mb-0">
          <li>
            <a v-bind:href="gitRepoUrl" target="_blank" class="me-4 hover:underline md:me-6"
              >GitHub</a
            >
          </li>
          <li>
            <a v-bind:href="licenseUrl" target="_blank" class="me-4 hover:underline md:me-6"
              >Licensing</a
            >
          </li>
          <li>
            <a v-bind:href="portfolio" target="_blank" class="me-4 hover:underline md:me-6"
              >Contact</a
            >
          </li>
        </ul>
      </div>
      <hr class="my-6 border-gray-200 sm:mx-auto lg:my-8" />
      <span class="block text-sm text-gray-500 sm:text-center">© 2024, All Rights Reserved.</span>
    </div>
  </footer>
</template>

<script>
import AppHeaderIcon from '@/assets/images/header.png';

export default {
  name: 'AppFooter',
  props: {
    gitRepoUrl: {
      type: String,
      required: true,
    },
    portfolio: {
      type: String,
      required: true,
    },
    licenseUrl: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      appHeaderIcon: AppHeaderIcon,
    };
  },
};
</script>
