<template>
  <div class="grid sm:grid-cols-12 grid-cols-12">
    <div class="col-span-12">
      <app-header-vue v-bind:git-repo-url="gitRepoUrl" v-bind:download-url="downloadUrl" />
    </div>
    <div class="col-span-12 row-span-1">
      <app-take-a-look-first-vue />
    </div>
    <div class="col-span-12">
      <app-footer-vue
        v-bind:portfolio="portfolio"
        v-bind:git-repo-url="gitRepoUrl"
        v-bind:license-url="licenseUrl"
      />
    </div>
  </div>
</template>

<script>
import AppHeaderVue from '@/components/Header.vue';
import AppTakeALookFirstVue from '@/components/TakeALookFirst.vue';
import AppFooterVue from '@/components/Footer.vue';

export default {
  name: 'App',
  components: {
    AppHeaderVue,
    AppTakeALookFirstVue,
    AppFooterVue,
  },
  data() {
    return {
      portfolio: 'https://rizwan-hasan.github.io',
      gitRepoUrl: 'https://github.com/TechLearnersInc/Free-Hash-Checker.git',
      downloadUrl: 'https://sourceforge.net/projects/free-hash-checker/files/v3.0/',
      licenseUrl: 'https://github.com/TechLearnersInc/Free-Hash-Checker/blob/main/LICENSE',
    };
  },
};
</script>
