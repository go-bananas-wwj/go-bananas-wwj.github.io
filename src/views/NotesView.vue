<template>
  <div class="notes-page">
    <section class="notes-hero">
      <div class="container">
        <h1 class="notes-hero-title">{{ isZh ? '随记' : 'Notes' }}</h1>
        <p class="notes-hero-desc">
          {{ isZh ? '一些研究心得、项目笔记和日常思考。' : 'Research notes, project logs, and random thoughts.' }}
        </p>
      </div>
    </section>

    <section class="section notes-list-section">
      <div class="container">
        <div v-if="noteList.length === 0" class="empty-state">
          <div class="empty-icon">📝</div>
          <p>{{ isZh ? '还没有文章，稍后再来看看。' : 'No notes yet. Check back later.' }}</p>
        </div>
        <div v-else class="notes-grid">
          <FadeInView v-for="note in noteList" :key="note.slug">
            <router-link :to="`/notes/${note.slug}`" class="note-card card">
              <div class="note-meta">
                <span v-if="note.date" class="note-date">{{ note.date }}</span>
                <div v-if="note.tags.length" class="note-tags">
                  <span v-for="tag in note.tags" :key="tag" class="tag">{{ tag }}</span>
                </div>
              </div>
              <h2 class="note-title">{{ note.title }}</h2>
              <p class="note-summary">{{ note.summary }}</p>
              <span class="note-readmore">{{ isZh ? '阅读全文 →' : 'Read more →' }}</span>
            </router-link>
          </FadeInView>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { getAllNotes } from '../data/notes.js';
import { useLanguage } from '../composables/useLanguage.js';
import FadeInView from '../components/FadeInView.vue';

const { isZh } = useLanguage();
const noteList = getAllNotes();
</script>

<style scoped>
.notes-page {
  padding-top: 80px;
}

.notes-hero {
  padding: 80px 0 40px;
  text-align: center;
  background: var(--color-bg-soft);
  position: relative;
  overflow: hidden;
}

.notes-hero::before {
  content: '';
  position: absolute;
  top: -50%;
  left: 50%;
  transform: translateX(-50%);
  width: 800px;
  height: 800px;
  background: radial-gradient(circle, rgba(59, 130, 246, 0.08) 0%, transparent 60%);
  pointer-events: none;
}

.notes-hero-title {
  font-size: 40px;
  font-weight: 800;
  letter-spacing: -0.04em;
  margin-bottom: 12px;
  position: relative;
}

.notes-hero-desc {
  font-size: 16px;
  color: var(--color-text-secondary);
  position: relative;
}

.notes-list-section {
  padding-top: 48px;
}

.notes-grid {
  display: flex;
  flex-direction: column;
  gap: 20px;
  max-width: 720px;
  margin: 0 auto;
}

.note-card {
  display: block;
  text-decoration: none;
  color: inherit;
  padding: 28px;
  border-radius: var(--radius-lg);
  transition: all var(--transition-base);
}

.note-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
  border-color: var(--color-accent-soft);
}

.note-card:hover .note-readmore {
  color: var(--color-accent-hover);
}

.note-meta {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
  flex-wrap: wrap;
}

.note-date {
  font-size: 13px;
  font-family: var(--font-mono);
  color: var(--color-text-muted);
}

.note-tags {
  display: flex;
  gap: 6px;
}

.note-title {
  font-size: 20px;
  font-weight: 700;
  color: var(--color-text);
  margin-bottom: 8px;
  letter-spacing: -0.02em;
}

.note-summary {
  font-size: 14px;
  color: var(--color-text-secondary);
  line-height: 1.7;
  margin-bottom: 16px;
}

.note-readmore {
  font-size: 14px;
  font-weight: 600;
  color: var(--color-accent);
  transition: color var(--transition-fast);
}

.empty-state {
  text-align: center;
  padding: 80px 0;
  color: var(--color-text-muted);
}

.empty-icon {
  font-size: 48px;
  margin-bottom: 16px;
}
</style>
