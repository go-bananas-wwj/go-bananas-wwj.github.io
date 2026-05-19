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
        <router-link to="/notes" class="nav-link" :class="{ active: $route.path.startsWith('/notes') }">
          {{ isZh ? '随记' : 'Notes' }}
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
  backdrop-filter: blur(16px);
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
  height: 64px;
}

.logo {
  text-decoration: none;
  color: var(--color-text);
}

.logo-name {
  font-weight: 800;
  font-size: 16px;
  letter-spacing: -0.02em;
}

.nav {
  display: flex;
  align-items: center;
  gap: 28px;
}

.nav-link {
  font-size: 14px;
  font-weight: 600;
  color: var(--color-text-secondary);
  text-decoration: none;
  transition: color 0.2s ease;
  position: relative;
  padding: 4px 0;
}

.nav-link:hover,
.nav-link.active {
  color: var(--color-text);
}

.nav-link.active::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--color-accent), var(--color-accent-warm));
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
