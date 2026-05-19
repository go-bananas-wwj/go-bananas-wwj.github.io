<template>
  <section class="section contact">
    <div class="container">
      <FadeInView>
        <h2 class="section-title">{{ isZh ? '联系我' : 'Get in Touch' }}</h2>
        <div class="contact-card card">
          <p class="contact-desc">
            {{ isZh ? '如果你对我的研究或项目感兴趣，欢迎通过以下方式联系我。' : "If you're interested in my research or projects, feel free to reach out." }}
          </p>
          <div class="contact-links">
            <a :href="'mailto:' + contact.email" class="contact-item">
              <span class="contact-icon">✉️</span>
              <span class="contact-label">{{ contact.email }}</span>
            </a>
            <a :href="contact.github" target="_blank" rel="noopener" class="contact-item">
              <span class="contact-icon">💻</span>
              <span class="contact-label">github.com/go-bananas-wwj</span>
            </a>
            <a :href="contact.modelscope" target="_blank" rel="noopener" class="contact-item">
              <span class="contact-icon">🤖</span>
              <span class="contact-label">modelscope.cn/profile/WeijieWu</span>
            </a>
          </div>
          <div class="contact-actions">
            <router-link to="/resume" class="btn btn-primary">
              {{ isZh ? '下载简历 / 查看完整履历 →' : 'Download Resume / View Full CV →' }}
            </router-link>
          </div>
        </div>
      </FadeInView>
    </div>
  </section>
</template>

<script setup>
import { contact } from '../data/resume.js';
import { useLanguage } from '../composables/useLanguage.js';
import FadeInView from './FadeInView.vue';

const { isZh } = useLanguage();
</script>

<style scoped>
.contact {
  background: var(--color-bg);
}

.contact-card {
  text-align: center;
  max-width: 640px;
  margin: 0 auto;
}

.contact-desc {
  font-size: 15px;
  color: var(--color-text-secondary);
  margin-bottom: 24px;
}

.contact-links {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 28px;
}

.contact-item {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px 16px;
  border-radius: var(--radius-sm);
  background: var(--color-bg-soft);
  border: 1px solid var(--color-border-light);
  color: var(--color-text);
  text-decoration: none;
  font-size: 14px;
  transition: all 0.2s ease;
}

.contact-item:hover {
  border-color: var(--color-accent);
  background: var(--color-accent-soft);
  text-decoration: none;
}

.contact-icon {
  font-size: 16px;
}

.contact-label {
  font-family: var(--font-mono);
  font-size: 13px;
}

.contact-actions {
  display: flex;
  justify-content: center;
}

.btn {
  display: inline-flex;
  align-items: center;
  padding: 12px 24px;
  border-radius: var(--radius-sm);
  font-size: 14px;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.2s ease;
  cursor: pointer;
  border: none;
}

.btn-primary {
  background: var(--color-accent);
  color: #fff;
}

.btn-primary:hover {
  background: var(--color-accent-hover);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
  text-decoration: none;
}
</style>
