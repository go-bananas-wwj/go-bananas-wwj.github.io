<template>
  <section class="section about">
    <div class="container">
      <FadeInView>
        <h2 class="section-title">{{ isZh ? '关于我' : 'About Me' }}</h2>
        <p class="about-text">{{ isZh ? personal.zh.bio : personal.en.bio }}</p>
      </FadeInView>
    </div>
  </section>
</template>

<script setup>
import { personal } from '../data/resume.js';
import { useLanguage } from '../composables/useLanguage.js';
import FadeInView from './FadeInView.vue';

const { isZh } = useLanguage();
</script>

<style scoped>
.about {
  background: var(--color-bg-soft);
}

.about-text {
  font-size: 15px;
  line-height: 1.9;
  color: var(--color-text-secondary);
  max-width: 720px;
}
</style>
