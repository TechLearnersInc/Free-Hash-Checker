<template>
  <div class="flex flex-row items-center justify-center">
    <div class="grid grid-cols-1 gap-x-12 sm:grid-cols-2 sm:pl-4 sm:pr-4">
      <div class="col-span-1 mb-12 mt-24 sm:col-span-2">
        <h1 class="text-center font-lato text-5xl font-semibold text-gray-700">
          Take a look first
        </h1>
      </div>
      <article
        class="sm:col-span-1"
        v-for="screenshot in appScreenshots"
        v-bind:key="screenshot.name"
      >
        <div class="grid grid-cols-1 text-center">
          <img
            class="p-4 drop-shadow-md"
            v-bind:src="screenshot.img"
            v-bind:alt="screenshot.name"
          />
          <div class="mb-10 mt-4">
            <h1 class="col-span-1 mb-2 font-lato text-2xl font-semibold text-gray-700">
              {{ screenshot.name }}
            </h1>
            <p class="text-md col-span-1 font-poppins text-gray-600">
              {{ screenshot.desc }}
            </p>
          </div>
        </div>
      </article>
    </div>
  </div>
</template>

<script>
import AppCheckerScrnSht from '@/assets/images/screenshots/checker.png';
import AppFinishedScrnSht from '@/assets/images/screenshots/finished.png';
import AppStartScrnSht from '@/assets/images/screenshots/start.png';
import AppCalculatingScrnSht from '@/assets/images/screenshots/calculating.png';

export default {
  name: 'AppTakeALookFirst',
  data() {
    return {
      appScreenshots: [
        {
          name: 'Main Window',
          img: AppStartScrnSht,
          desc: 'Select any file for calcualting hash',
        },
        {
          name: 'Finished Window',
          img: AppFinishedScrnSht,
          desc: 'Hash can be copied to clipboard with a single click',
        },
        {
          name: 'Hash Calculation',
          img: AppCalculatingScrnSht,
          desc: 'Tracking the progress of calculation',
        },
        {
          name: 'Hash Matching',
          img: AppCheckerScrnSht,
          desc: 'Also have the hash matching feature',
        },
      ],
    };
  },
};
</script>
