<template>
  <section class="hero">
    <div class="gradient-mesh"></div>
    <div class="container hero-inner">
      <div class="hero-left">
        <div class="avatar-wrapper">
          <img src="/images/avatar.jpg" alt="avatar" class="avatar-img" @error="handleImgError" />
          <div v-if="imgError" class="avatar-fallback">{{ isZh ? personal.zh.name[0] : personal.en.name[0] }}</div>
          <div class="avatar-ring"></div>
        </div>
      </div>
      <div class="hero-right">
        <div class="hero-greeting">{{ isZh ? '你好，我是' : "Hi, I'm" }}</div>
        <h1 class="hero-name">{{ isZh ? personal.zh.name : personal.en.name }}</h1>
        <p class="hero-title">{{ isZh ? personal.zh.title : personal.en.title }}</p>
        <p class="hero-bio">{{ isZh ? personal.zh.bio : personal.en.bio }}</p>
        <div class="hero-socials">
          <a :href="contact.github" target="_blank" rel="noopener" class="social-link" title="GitHub">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
          </a>
          <a :href="contact.modelscope" target="_blank" rel="noopener" class="social-link" title="ModelScope">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
          </a>
          <a :href="'mailto:' + contact.email" class="social-link" title="Email">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
          </a>
        </div>
        <div class="hero-actions">
          <router-link to="/resume" class="btn btn-primary">
            {{ isZh ? '查看完整简历' : 'View Full Resume' }}
          </router-link>
          <router-link to="/notes" class="btn btn-secondary">
            {{ isZh ? '阅读随记' : 'Read Notes' }}
          </router-link>
        </div>
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
  padding: 140px 0 100px;
  position: relative;
  overflow: hidden;
}

.hero-inner {
  display: flex;
  align-items: center;
  gap: 64px;
  position: relative;
  z-index: 1;
}

.hero-left {
  flex-shrink: 0;
}

.avatar-wrapper {
  position: relative;
  width: 240px;
  height: 240px;
}

.avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 32px;
  position: relative;
  z-index: 2;
  box-shadow: var(--shadow-lg);
  transition: transform var(--transition-base);
}

.avatar-wrapper:hover .avatar-img {
  transform: scale(1.03) rotate(-2deg);
}

.avatar-fallback {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, var(--color-accent-soft), #eff6ff);
  color: var(--color-accent);
  font-size: 80px;
  font-weight: 800;
  border-radius: 32px;
  position: relative;
  z-index: 2;
}

.avatar-ring {
  position: absolute;
  inset: -12px;
  border: 3px solid var(--color-accent-soft);
  border-radius: 40px;
  z-index: 1;
  animation: pulse-glow 3s ease-in-out infinite;
}

.hero-right {
  flex: 1;
}

.hero-greeting {
  font-size: 14px;
  font-weight: 600;
  color: var(--color-accent-hover);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 8px;
}

.hero-name {
  font-size: 48px;
  font-weight: 800;
  margin-bottom: 12px;
  letter-spacing: -0.04em;
  color: var(--color-text);
  line-height: 1.1;
}

.hero-title {
  font-size: 18px;
  color: var(--color-text-secondary);
  margin-bottom: 20px;
  font-weight: 500;
}

.hero-bio {
  font-size: 15px;
  color: var(--color-text-secondary);
  line-height: 1.8;
  margin-bottom: 24px;
  max-width: 520px;
}

.hero-socials {
  display: flex;
  gap: 12px;
  margin-bottom: 24px;
}

.social-link {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  background: var(--color-bg-soft);
  border: 1px solid var(--color-border);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-text-secondary);
  transition: all var(--transition-fast);
}

.social-link:hover {
  background: var(--color-accent);
  color: #fff;
  border-color: var(--color-accent);
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(59, 130, 246, 0.3);
}

.hero-actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.btn {
  display: inline-flex;
  align-items: center;
  padding: 12px 24px;
  border-radius: var(--radius-sm);
  font-size: 14px;
  font-weight: 700;
  text-decoration: none;
  transition: all var(--transition-fast);
  cursor: pointer;
  border: none;
}

.btn-primary {
  background: linear-gradient(135deg, var(--color-accent), var(--color-accent-hover));
  color: #fff;
  box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(59, 130, 246, 0.4);
}

.btn-secondary {
  background: var(--color-bg-soft);
  color: var(--color-text);
  border: 1px solid var(--color-border);
}

.btn-secondary:hover {
  background: var(--color-bg-muted);
  border-color: var(--color-accent);
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .hero {
    padding: 120px 0 60px;
  }
  .hero-inner {
    flex-direction: column;
    text-align: center;
    gap: 40px;
  }
  .avatar-wrapper {
    width: 180px;
    height: 180px;
  }
  .hero-name {
    font-size: 36px;
  }
  .hero-bio {
    max-width: 100%;
  }
  .hero-socials {
    justify-content: center;
  }
  .hero-actions {
    justify-content: center;
  }
}
</style>
