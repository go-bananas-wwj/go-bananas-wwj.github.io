<template>
  <div class="note-detail-page">
    <div class="container note-container">
      <router-link to="/notes" class="note-back">
        ← {{ isZh ? '返回随记列表' : 'Back to notes' }}
      </router-link>

      <article v-if="note" class="note-article">
        <header class="note-header">
          <div class="note-meta">
            <span v-if="note.date" class="note-date">{{ note.date }}</span>
            <div v-if="note.tags.length" class="note-tags">
              <span v-for="tag in note.tags" :key="tag" class="tag">{{ tag }}</span>
            </div>
          </div>
          <h1 class="note-article-title">{{ note.title }}</h1>
        </header>

        <div class="note-body" v-html="renderedBody"></div>
      </article>

      <div v-else class="note-not-found">
        <p>{{ isZh ? '文章不存在。' : 'Note not found.' }}</p>
        <router-link to="/notes" class="btn btn-primary">
          {{ isZh ? '返回随记' : 'Back to notes' }}
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import { marked } from 'marked';
import { getNoteBySlug } from '../data/notes.js';
import { useLanguage } from '../composables/useLanguage.js';

const route = useRoute();
const { isZh } = useLanguage();
const slug = route.params.slug;
const note = getNoteBySlug(slug);

const renderedBody = computed(() => {
  if (!note) return '';
  const body = note.raw.replace(/^---\s*\n[\s\S]*?\n---\s*\n/, '');
  return marked.parse(body);
});
</script>

<style scoped>
.note-detail-page {
  padding-top: 100px;
  padding-bottom: 80px;
}

.note-container {
  max-width: 720px;
}

.note-back {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 14px;
  font-weight: 600;
  color: var(--color-text-secondary);
  margin-bottom: 32px;
  transition: color var(--transition-fast);
}

.note-back:hover {
  color: var(--color-accent-hover);
}

.note-article {
  background: var(--color-bg-soft);
  border: 1px solid var(--color-border-light);
  border-radius: var(--radius-lg);
  padding: 48px;
}

.note-header {
  margin-bottom: 32px;
  padding-bottom: 24px;
  border-bottom: 1px solid var(--color-border);
}

.note-meta {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
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

.note-article-title {
  font-size: 32px;
  font-weight: 800;
  color: var(--color-text);
  letter-spacing: -0.03em;
  line-height: 1.2;
}

.note-body {
  font-size: 15px;
  line-height: 1.8;
  color: var(--color-text-secondary);
}

.note-body :deep(h2) {
  font-size: 22px;
  font-weight: 700;
  color: var(--color-text);
  margin: 32px 0 16px;
  letter-spacing: -0.02em;
}

.note-body :deep(h3) {
  font-size: 18px;
  font-weight: 700;
  color: var(--color-text);
  margin: 24px 0 12px;
}

.note-body :deep(p) {
  margin-bottom: 16px;
}

.note-body :deep(ul),
.note-body :deep(ol) {
  margin-bottom: 16px;
  padding-left: 24px;
}

.note-body :deep(ul) {
  list-style: disc;
}

.note-body :deep(ol) {
  list-style: decimal;
}

.note-body :deep(li) {
  margin-bottom: 6px;
}

.note-body :deep(code) {
  font-family: var(--font-mono);
  font-size: 13px;
  background: var(--color-bg-muted);
  padding: 2px 6px;
  border-radius: 4px;
  color: var(--color-accent-hover);
}

.note-body :deep(pre) {
  background: var(--color-bg-muted);
  padding: 16px;
  border-radius: var(--radius-sm);
  overflow-x: auto;
  margin-bottom: 16px;
}

.note-body :deep(pre code) {
  background: none;
  padding: 0;
}

.note-body :deep(a) {
  color: var(--color-accent-hover);
  text-decoration: underline;
}

.note-body :deep(blockquote) {
  border-left: 3px solid var(--color-accent);
  padding-left: 16px;
  margin-bottom: 16px;
  color: var(--color-text-secondary);
}

.note-not-found {
  text-align: center;
  padding: 80px 0;
}

.note-not-found p {
  font-size: 16px;
  color: var(--color-text-muted);
  margin-bottom: 20px;
}

.btn {
  display: inline-flex;
  align-items: center;
  padding: 10px 20px;
  border-radius: var(--radius-sm);
  font-size: 14px;
  font-weight: 700;
  text-decoration: none;
  border: none;
  cursor: pointer;
}

.btn-primary {
  background: linear-gradient(135deg, var(--color-accent), var(--color-accent-hover));
  color: #fff;
}

@media (max-width: 640px) {
  .note-article {
    padding: 28px;
  }
  .note-article-title {
    font-size: 24px;
  }
}
</style>
