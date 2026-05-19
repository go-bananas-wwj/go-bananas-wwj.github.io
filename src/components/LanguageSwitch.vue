<template>
  <button class="lang-switch" @click="toggleLang" :title="isZh ? 'Switch to English' : '切换到中文'">
    <span class="lang-icon">🌐</span>
    <span class="lang-label">{{ isZh ? 'EN' : '中' }}</span>
  </button>
</template>

<script setup>
import { useLanguage } from '../composables/useLanguage.js';

const { isZh, toggleLang } = useLanguage();
</script>

<style scoped>
.lang-switch {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 4px 10px;
  border-radius: 6px;
  border: 1px solid var(--color-border);
  background: transparent;
  font-size: 12px;
  font-weight: 600;
  color: var(--color-text-secondary);
  cursor: pointer;
  transition: all 0.2s ease;
  font-family: var(--font-sans);
}

.lang-switch:hover {
  border-color: var(--color-accent);
  color: var(--color-accent-hover);
  background: var(--color-accent-soft);
}

.lang-icon {
  font-size: 13px;
}
</style>
