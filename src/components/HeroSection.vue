<template>
  <section class="hero">
    <div class="container hero-inner">
      <div class="hero-avatar">
        <img src="/images/avatar.jpg" alt="avatar" class="avatar-img" @error="handleImgError" />
        <div v-if="imgError" class="avatar-placeholder">{{ isZh ? personal.zh.name[0] : personal.en.name[0] }}</div>
      </div>
      <h1 class="hero-name">{{ isZh ? personal.zh.name : personal.en.name }}</h1>
      <p class="hero-title">{{ isZh ? personal.zh.title : personal.en.title }}</p>
      <p class="hero-bio">{{ isZh ? personal.zh.bio : personal.en.bio }}</p>
      <div class="hero-actions">
        <router-link to="/resume" class="btn btn-primary">
          {{ isZh ? '查看完整简历' : 'View Full Resume' }}
        </router-link>
        <a :href="'mailto:' + contact.email" class="btn btn-secondary">
          {{ isZh ? '联系我' : 'Contact Me' }}
        </a>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';
import { personal, contact } from '../data/resume.js';
import { useLanguage } from '../composables/useLanguage.js';

const { isZh } = useLanguage();
const imgError = ref(false);

function handleImgError() {
  imgError.value = true;
}
</script>

<style scoped>
.hero {
  padding: 140px 0 80px;
  text-align: center;
}

.hero-inner {
  max-width: 720px;
}

.hero-avatar {
  width: 120px;
  height: 120px;
  margin: 0 auto 24px;
  border-radius: 50%;
  overflow: hidden;
  border: 3px solid var(--color-accent-soft);
  box-shadow: 0 4px 20px rgba(96, 165, 250, 0.2);
}

.avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.avatar-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--color-accent-soft);
  color: var(--color-accent-hover);
  font-size: 48px;
  font-weight: 700;
}

.hero-name {
  font-size: 36px;
  font-weight: 700;
  margin-bottom: 8px;
  letter-spacing: -0.03em;
  color: var(--color-text);
}

.hero-title {
  font-size: 16px;
  color: var(--color-text-secondary);
  margin-bottom: 20px;
  font-weight: 500;
}

.hero-bio {
  font-size: 15px;
  color: var(--color-text-secondary);
  line-height: 1.8;
  margin-bottom: 28px;
}

.hero-actions {
  display: flex;
  gap: 12px;
  justify-content: center;
  flex-wrap: wrap;
}

.btn {
  display: inline-flex;
  align-items: center;
  padding: 10px 20px;
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
}

.btn-secondary {
  background: var(--color-bg-soft);
  color: var(--color-text);
  border: 1px solid var(--color-border);
}

.btn-secondary:hover {
  background: var(--color-bg-muted);
  border-color: var(--color-accent);
}

@media (max-width: 640px) {
  .hero {
    padding: 120px 0 60px;
  }
  .hero-name {
    font-size: 28px;
  }
  .hero-bio {
    font-size: 14px;
  }
}
</style>
