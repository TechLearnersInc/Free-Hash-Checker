<template>
  <div class="col-span-12 row-span-1">
    <div class="flex flex-row justify-center items-center">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-x-12 sm:pl-4 sm:pr-4">
        <div class="col-span-1 sm:col-span-2 mt-24 mb-12">
          <h1 class="font-lato text-5xl font-semibold text-gray-700 text-center">
            Take a look first
          </h1>
        </div>
        <div
          class="sm:col-span-1"
          v-for="screenshot in appScreenshots"
          v-bind:key="screenshot.name"
        >
          <div class="flex justify-center items-center drop-shadow-md p-4">
            <img v-bind:src="screenshot.image" v-bind:alt="screenshot.name" />
          </div>
        </div>
      </div>
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
          image: AppStartScrnSht,
        },
        {
          name: 'Finished Window',
          image: AppFinishedScrnSht,
        },
        {
          name: 'Hash Calculation',
          image: AppCalculatingScrnSht,
        },
        {
          name: 'Hash Matching',
          image: AppCheckerScrnSht,
        },
      ],
    };
  },
};
</script>
