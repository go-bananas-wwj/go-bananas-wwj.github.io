<template>
  <section class="section skills">
    <div class="container">
      <FadeInView>
        <h2 class="section-title">{{ isZh ? '技术方向' : 'Focus Areas' }}</h2>
      </FadeInView>
      <div class="skills-grid">
        <FadeInView v-for="(area, idx) in areas" :key="idx">
          <div class="area-card card">
            <div class="area-number">0{{ idx + 1 }}</div>
            <h3 class="area-name">{{ area.name }}</h3>
            <p class="area-desc">{{ area.desc }}</p>
            <div class="area-tags">
              <span v-for="tag in area.tags" :key="tag" class="tag">{{ tag }}</span>
            </div>
          </div>
        </FadeInView>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue';
import { useLanguage } from '../composables/useLanguage.js';
import FadeInView from './FadeInView.vue';

const { isZh } = useLanguage();

const areas = computed(() => {
  if (isZh.value) {
    return [
      {
        name: '遥感 AI',
        desc: '遥感大模型、地理嵌入、跨模态检索',
        tags: ['PyTorch', 'SAM', 'VLM'],
      },
      {
        name: '智能体系统',
        desc: '多智能体协同、Agent 框架、RAG',
        tags: ['Dify', 'LangChain', 'n8n'],
      },
      {
        name: '前端工程',
        desc: '数据可视化平台、交互式 Web 应用',
        tags: ['Vue.js', 'React', 'Vite'],
      },
      {
        name: '硬件集成',
        desc: '嵌入式开发、传感器融合、原型设计',
        tags: ['ARM', 'ROS', 'Altium'],
      },
    ];
  }
  return [
    {
      name: 'Remote Sensing AI',
      desc: 'Foundation models, geo-embedding, cross-modal retrieval',
      tags: ['PyTorch', 'SAM', 'VLM'],
    },
    {
      name: 'Agent Systems',
      desc: 'Multi-agent coordination, agent frameworks, RAG',
      tags: ['Dify', 'LangChain', 'n8n'],
    },
    {
      name: 'Frontend Engineering',
      desc: 'Data visualization platforms, interactive web apps',
      tags: ['Vue.js', 'React', 'Vite'],
    },
    {
      name: 'Hardware Integration',
      desc: 'Embedded development, sensor fusion, prototyping',
      tags: ['ARM', 'ROS', 'Altium'],
    },
  ];
});
</script>

<style scoped>
.skills {
  background: var(--color-bg);
}

.skills-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

.area-card {
  padding: 32px;
  border-radius: var(--radius-lg);
  position: relative;
  overflow: hidden;
}

.area-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--color-accent), var(--color-accent-warm));
  opacity: 0;
  transition: opacity var(--transition-fast);
}

.area-card:hover::before {
  opacity: 1;
}

.area-number {
  font-family: var(--font-mono);
  font-size: 12px;
  font-weight: 700;
  color: var(--color-accent);
  margin-bottom: 12px;
  letter-spacing: 0.05em;
}

.area-name {
  font-size: 20px;
  font-weight: 800;
  color: var(--color-text);
  margin-bottom: 8px;
  letter-spacing: -0.02em;
}

.area-desc {
  font-size: 14px;
  color: var(--color-text-secondary);
  line-height: 1.6;
  margin-bottom: 16px;
}

.area-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

@media (max-width: 640px) {
  .skills-grid {
    grid-template-columns: 1fr;
  }
}
</style>
