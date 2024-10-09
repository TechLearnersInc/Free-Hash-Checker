<template>
  <div class="grid sm:grid-cols-12 grid-cols-12 sm:grid-rows-3 grid-rows-3">
    <app-header-vue v-bind:git-repo-url="gitRepoUrl" v-bind:download-url="downloadUrl" />
    <div class="bg-teal-500 col-span-12 row-span-1"><h1>Contents</h1></div>
    <div class="bg-purple-500 col-span-12 row-span-1"><h1>Footer</h1></div>
  </div>
</template>

<script>
import AppHeaderVue from '@/components/Header.vue';

export default {
  name: 'App',
  components: {
    AppHeaderVue,
  },
  data() {
    return {
      gitRepoUrl: 'https://github.com/TechLearnersInc/Free-Hash-Checker.git',
      downloadUrl: 'https://sourceforge.net/projects/free-hash-checker/files/v3.0/',
    };
  },
};
</script>
