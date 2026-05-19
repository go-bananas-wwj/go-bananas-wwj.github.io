<template>
  <section class="section projects">
    <div class="container">
      <FadeInView>
        <h2 class="section-title">{{ isZh ? '精选项目' : 'Featured Projects' }}</h2>
      </FadeInView>
      <div class="projects-grid">
        <FadeInView v-for="(project, idx) in featuredProjects" :key="idx">
          <div class="project-card card">
            <div class="project-image">
              <img :src="project.image" :alt="project.name" @error="handleImgError" />
              <div v-if="imgErrors[idx]" class="image-placeholder">
                <span>{{ project.name[0] }}</span>
              </div>
            </div>
            <div class="project-content">
              <div class="project-header">
                <h3 class="project-name">{{ project.name }}</h3>
                <span v-if="project.result" class="project-result">{{ project.result }}</span>
              </div>
              <p class="project-desc">{{ project.desc }}</p>
              <div class="project-tags">
                <span v-for="tag in project.tags" :key="tag" class="tag">{{ tag }}</span>
              </div>
              <div v-if="project.links.length" class="project-links">
                <a v-for="link in project.links" :key="link.url" :href="link.url" target="_blank" rel="noopener" class="project-link">
                  {{ link.label }} →
                </a>
              </div>
            </div>
          </div>
        </FadeInView>
      </div>
      <FadeInView>
        <div class="projects-more">
          <router-link to="/resume" class="btn-link">
            {{ isZh ? '查看全部项目 →' : 'View All Projects →' }}
          </router-link>
        </div>
      </FadeInView>
    </div>
  </section>
</template>

<script setup>
import { computed, reactive } from 'vue';
import { projects } from '../data/resume.js';
import { useLanguage } from '../composables/useLanguage.js';
import FadeInView from './FadeInView.vue';

const { isZh } = useLanguage();

const featuredProjects = computed(() => {
  const list = isZh.value ? projects.zh : projects.en;
  return list.slice(0, 4);
});

const imgErrors = reactive({});

function handleImgError(e, idx) {
  const index = e.target?.dataset?.idx || 0;
  imgErrors[index] = true;
}
</script>

<style scoped>
.projects {
  background: var(--color-bg);
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}

.project-card {
  display: flex;
  flex-direction: column;
  overflow: hidden;
  padding: 0;
}

.project-image {
  width: 100%;
  height: 160px;
  background: var(--color-accent-soft);
  position: relative;
  overflow: hidden;
}

.project-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.image-placeholder {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, var(--color-accent-soft), #eff6ff);
  color: var(--color-accent);
  font-size: 48px;
  font-weight: 700;
}

.project-content {
  padding: 20px;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.project-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  margin-bottom: 8px;
}

.project-name {
  font-size: 16px;
  font-weight: 700;
  color: var(--color-text);
}

.project-result {
  font-size: 11px;
  font-weight: 600;
  color: var(--color-accent-hover);
  background: var(--color-accent-soft);
  padding: 2px 8px;
  border-radius: 999px;
  white-space: nowrap;
}

.project-desc {
  font-size: 13px;
  color: var(--color-text-secondary);
  line-height: 1.6;
  margin-bottom: 12px;
  flex: 1;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 12px;
}

.project-links {
  display: flex;
  gap: 12px;
}

.project-link {
  font-size: 13px;
  font-weight: 600;
  color: var(--color-accent-hover);
  text-decoration: none;
}

.project-link:hover {
  text-decoration: underline;
}

.projects-more {
  text-align: center;
  margin-top: 32px;
}

.btn-link {
  font-size: 14px;
  font-weight: 600;
  color: var(--color-accent-hover);
  text-decoration: none;
}

.btn-link:hover {
  text-decoration: underline;
}

@media (max-width: 640px) {
  .projects-grid {
    grid-template-columns: 1fr;
  }
}
</style>
