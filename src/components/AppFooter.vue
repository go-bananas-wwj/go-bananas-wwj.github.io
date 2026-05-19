<template>
  <footer class="footer">
    <div class="container footer-inner">
      <p class="footer-text">
        © {{ year }} {{ isZh ? personal.zh.name : personal.en.name }}
        <span class="divider">·</span>
        {{ isZh ? '用 ❤️ 和 Vue 构建' : 'Built with ❤️ and Vue' }}
      </p>
      <div class="footer-links">
        <a :href="contact.github" target="_blank" rel="noopener">GitHub</a>
        <a :href="contact.modelscope" target="_blank" rel="noopener">ModelScope</a>
        <a :href="'mailto:' + contact.email">Email</a>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { personal, contact } from '../data/resume.js';
import { useLanguage } from '../composables/useLanguage.js';

const { isZh } = useLanguage();
const year = new Date().getFullYear();
</script>

<style scoped>
.footer {
  border-top: 1px solid var(--color-border-light);
  padding: 32px 0;
  background: var(--color-bg-soft);
}

.footer-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
}

.footer-text {
  font-size: 13px;
  color: var(--color-text-muted);
}

.divider {
  margin: 0 6px;
}

.footer-links {
  display: flex;
  gap: 16px;
}

.footer-links a {
  font-size: 13px;
  color: var(--color-text-secondary);
  text-decoration: none;
  transition: color 0.2s ease;
}

.footer-links a:hover {
  color: var(--color-accent-hover);
}

@media (max-width: 640px) {
  .footer-inner {
    flex-direction: column;
    text-align: center;
  }
}
</style>
