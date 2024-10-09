<template>
  <div class="grid sm:grid-cols-12 grid-cols-12">
    <app-header-vue v-bind:git-repo-url="gitRepoUrl" v-bind:download-url="downloadUrl" />
    <app-screenshots-vue />
    <app-footer-vue />
  </div>
</template>

<script>
import AppHeaderVue from '@/components/Header.vue';
import AppScreenshotsVue from '@/components/Screenshots.vue';
import AppFooterVue from '@/components/Footer.vue';

export default {
  name: 'App',
  components: {
    AppHeaderVue,
    AppScreenshotsVue,
    AppFooterVue,
  },
  data() {
    return {
      gitRepoUrl: 'https://github.com/TechLearnersInc/Free-Hash-Checker.git',
      downloadUrl: 'https://sourceforge.net/projects/free-hash-checker/files/v3.0/',
    };
  },
};
</script>
