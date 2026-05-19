<template>
  <section class="section skills">
    <div class="container">
      <FadeInView>
        <h2 class="section-title">{{ isZh ? '技术栈' : 'Skills' }}</h2>
      </FadeInView>
      <div class="skills-grid">
        <FadeInView v-for="(group, idx) in skillList" :key="idx">
          <div class="skill-group card">
            <h3 class="skill-category">{{ group.category }}</h3>
            <div class="skill-items">
              <span v-for="item in group.items" :key="item" class="tag">{{ item }}</span>
            </div>
          </div>
        </FadeInView>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue';
import { skills } from '../data/resume.js';
import { useLanguage } from '../composables/useLanguage.js';
import FadeInView from './FadeInView.vue';

const { isZh } = useLanguage();
const skillList = computed(() => (isZh.value ? skills.zh : skills.en));
</script>

<style scoped>
.skills {
  background: var(--color-bg-soft);
}

.skills-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

.skill-group {
  padding: 20px;
}

.skill-category {
  font-size: 14px;
  font-weight: 600;
  color: var(--color-text);
  margin-bottom: 14px;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--color-border-light);
}

.skill-items {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

@media (max-width: 640px) {
  .skills-grid {
    grid-template-columns: 1fr;
  }
}
</style>
