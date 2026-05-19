<template>
  <header class="header" :class="{ hidden: !isVisible }">
    <div class="container header-inner">
      <router-link to="/" class="logo">
        <span class="logo-name">{{ isZh ? personal.zh.name : personal.en.name }}</span>
      </router-link>
      <nav class="nav">
        <router-link to="/" class="nav-link" :class="{ active: $route.path === '/' }">
          {{ isZh ? '首页' : 'Home' }}
        </router-link>
        <router-link to="/resume" class="nav-link" :class="{ active: $route.path === '/resume' }">
          {{ isZh ? '简历' : 'Resume' }}
        </router-link>
        <LanguageSwitch />
      </nav>
    </div>
  </header>
</template>

<script setup>
import { personal } from '../data/resume.js';
import { useLanguage } from '../composables/useLanguage.js';
import { useScrollHeader } from '../composables/useScrollHeader.js';
import LanguageSwitch from './LanguageSwitch.vue';

const { isZh } = useLanguage();
const { isVisible } = useScrollHeader();
</script>

<style scoped>
.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--color-border-light);
  transition: transform 0.3s ease, background 0.3s ease;
}

.header.hidden {
  transform: translateY(-100%);
}

.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 60px;
}

.logo {
  text-decoration: none;
  color: var(--color-text);
}

.logo-name {
  font-weight: 700;
  font-size: 16px;
  letter-spacing: -0.01em;
}

.nav {
  display: flex;
  align-items: center;
  gap: 24px;
}

.nav-link {
  font-size: 14px;
  font-weight: 500;
  color: var(--color-text-secondary);
  text-decoration: none;
  transition: color 0.2s ease;
  position: relative;
}

.nav-link:hover,
.nav-link.active {
  color: var(--color-text);
}

.nav-link.active::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--color-accent);
  border-radius: 2px;
}

@media (max-width: 640px) {
  .nav {
    gap: 16px;
  }
  .nav-link {
    font-size: 13px;
  }
}
</style>
