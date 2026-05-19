<template>
  <section class="section about">
    <div class="gradient-mesh"></div>
    <div class="container" style="position:relative;z-index:1">
      <FadeInView>
        <h2 class="section-title">{{ isZh ? '关于我' : 'About Me' }}</h2>
      </FadeInView>
      <div class="about-grid">
        <FadeInView class="about-card card">
          <div class="about-icon">🎯</div>
          <h3 class="about-label">{{ isZh ? '研究方向' : 'Research' }}</h3>
          <p class="about-desc">{{ isZh ? '从事地理嵌入研究和遥感智能体研究，目前在读博一。' : 'Working on geo-embedding and remote sensing agents. Currently in my first year of PhD.' }}</p>
        </FadeInView>
        <FadeInView class="about-card card">
          <div class="about-icon">🔧</div>
          <h3 class="about-label">{{ isZh ? '硬件' : 'Hardware' }}</h3>
          <p class="about-desc">{{ isZh ? '喜欢从零开始捣鼓硬件，做过智能制冷衣、雷达建图小车、嵌入式检测设备。' : 'Love tinkering with hardware from scratch. Built cooling suits, LiDAR robots, and embedded devices.' }}</p>
        </FadeInView>
        <FadeInView class="about-card card">
          <div class="about-icon">🤖</div>
          <h3 class="about-label">{{ isZh ? '智能体架构' : 'Agent Architecture' }}</h3>
          <p class="about-desc">{{ isZh ? '折腾各种 Agent 框架和工具，从 Dify 到 LangChain，从 RAG 到多智能体协同。' : 'Experimenting with agent frameworks from Dify to LangChain, from RAG to multi-agent systems.' }}</p>
        </FadeInView>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useLanguage } from '../composables/useLanguage.js';
import FadeInView from './FadeInView.vue';

const { isZh } = useLanguage();
</script>

<style scoped>
.about {
  background: var(--color-bg-soft);
  overflow: hidden;
}

.about-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.about-card {
  text-align: center;
  padding: 36px 24px;
  border-radius: var(--radius-lg);
  background: var(--color-bg);
  border: 1px solid var(--color-border-light);
  transition: all var(--transition-base);
}

.about-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-lg);
  border-color: var(--color-accent-soft);
}

.about-icon {
  font-size: 40px;
  margin-bottom: 16px;
  line-height: 1;
}

.about-label {
  font-size: 16px;
  font-weight: 700;
  color: var(--color-text);
  margin-bottom: 10px;
}

.about-desc {
  font-size: 14px;
  color: var(--color-text-secondary);
  line-height: 1.7;
}

@media (max-width: 768px) {
  .about-grid {
    grid-template-columns: 1fr;
  }
}
</style>
