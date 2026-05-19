<template>
  <div class="resume-page">
    <!-- Resume Header -->
    <section class="resume-hero">
      <div class="container">
        <div class="resume-hero-inner">
          <h1 class="resume-name">{{ isZh ? personal.zh.name : personal.en.name }}</h1>
          <p class="resume-title">{{ isZh ? personal.zh.title : personal.en.title }}</p>
          <div class="resume-contact-bar">
            <a :href="'mailto:' + contact.email" class="resume-contact-item">{{ contact.email }}</a>
            <span class="resume-contact-sep">·</span>
            <a :href="contact.github" target="_blank" rel="noopener" class="resume-contact-item">GitHub</a>
            <span class="resume-contact-sep">·</span>
            <a :href="contact.modelscope" target="_blank" rel="noopener" class="resume-contact-item">ModelScope</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Education -->
    <section class="section resume-section">
      <div class="container">
        <FadeInView>
          <h2 class="section-title">{{ isZh ? '教育背景' : 'Education' }}</h2>
          <div class="timeline">
            <div v-for="(edu, idx) in eduList" :key="idx" class="timeline-item">
              <div class="timeline-marker"></div>
              <div class="timeline-content card">
                <div class="timeline-header">
                  <h3 class="timeline-title">{{ edu.school }}</h3>
                  <span class="timeline-time">{{ edu.time }}</span>
                </div>
                <p class="timeline-subtitle">{{ edu.degree }}</p>
                <p class="timeline-detail">{{ edu.detail }}</p>
              </div>
            </div>
          </div>
        </FadeInView>
      </div>
    </section>

    <!-- Experience -->
    <section class="section resume-section">
      <div class="container">
        <FadeInView>
          <h2 class="section-title">{{ isZh ? '工作经历' : 'Experience' }}</h2>
          <div class="timeline">
            <div v-for="(exp, idx) in expList" :key="idx" class="timeline-item">
              <div class="timeline-marker"></div>
              <div class="timeline-content card">
                <div class="timeline-header">
                  <div>
                    <h3 class="timeline-title">{{ exp.company }}</h3>
                    <p class="timeline-subtitle">{{ exp.role }} <span v-if="exp.location" class="timeline-location">· {{ exp.location }}</span></p>
                  </div>
                  <span class="timeline-time">{{ exp.time }}</span>
                </div>
                <ul class="timeline-bullets">
                  <li v-for="(b, bidx) in exp.bullets" :key="bidx">{{ b }}</li>
                </ul>
              </div>
            </div>
          </div>
        </FadeInView>
      </div>
    </section>

    <!-- Projects -->
    <section class="section resume-section">
      <div class="container">
        <FadeInView>
          <h2 class="section-title">{{ isZh ? '项目经历' : 'Projects' }}</h2>
          <div class="timeline">
            <div v-for="(proj, idx) in projList" :key="idx" class="timeline-item">
              <div class="timeline-marker"></div>
              <div class="timeline-content card">
                <div class="timeline-header">
                  <div>
                    <h3 class="timeline-title">{{ proj.name }}</h3>
                    <div class="project-meta">
                      <span class="timeline-time">{{ proj.time }}</span>
                      <span v-if="proj.result" class="project-result-tag">{{ proj.result }}</span>
                    </div>
                  </div>
                </div>
                <p class="timeline-detail">{{ proj.desc }}</p>
                <div class="project-tags-row">
                  <span v-for="tag in proj.tags" :key="tag" class="tag">{{ tag }}</span>
                </div>
                <div v-if="proj.links.length" class="project-links-row">
                  <a v-for="link in proj.links" :key="link.url" :href="link.url" target="_blank" rel="noopener" class="project-link">{{ link.label }} →</a>
                </div>
              </div>
            </div>
          </div>
        </FadeInView>
      </div>
    </section>

    <!-- Publications -->
    <section class="section resume-section">
      <div class="container">
        <FadeInView>
          <h2 class="section-title">{{ isZh ? '论文发表' : 'Publications' }}</h2>
          <div class="pub-list">
            <div v-for="(pub, idx) in pubList" :key="idx" class="pub-item card">
              <h3 class="pub-title">{{ pub.title }}</h3>
              <p class="pub-authors">{{ pub.authors }}</p>
              <p class="pub-venue">{{ pub.venue }}</p>
              <div v-if="pub.links.length" class="pub-links">
                <a v-for="link in pub.links" :key="link.url" :href="link.url" target="_blank" rel="noopener" class="project-link">{{ link.label }} →</a>
              </div>
            </div>
          </div>
        </FadeInView>
      </div>
    </section>

    <!-- Patents -->
    <section class="section resume-section">
      <div class="container">
        <FadeInView>
          <h2 class="section-title">{{ isZh ? '专利' : 'Patents' }}</h2>
          <div class="patent-list">
            <div v-for="(pat, idx) in patentList" :key="idx" class="patent-item">
              <span class="patent-name">{{ pat.name }}</span>
              <span class="patent-number">{{ pat.number }}</span>
            </div>
          </div>
        </FadeInView>
      </div>
    </section>

    <!-- Awards -->
    <section class="section resume-section">
      <div class="container">
        <FadeInView>
          <h2 class="section-title">{{ isZh ? '荣誉奖项' : 'Awards' }}</h2>
          <div class="award-list">
            <div v-for="(award, idx) in awardList" :key="idx" class="award-item">
              <span class="award-name">{{ award.name }}</span>
              <span class="award-org">{{ award.org }}</span>
              <span class="award-time">{{ award.time }}</span>
            </div>
          </div>
        </FadeInView>
      </div>
    </section>

    <!-- Skills -->
    <section class="section resume-section">
      <div class="container">
        <FadeInView>
          <h2 class="section-title">{{ isZh ? '技术栈' : 'Skills' }}</h2>
          <div class="resume-skills">
            <div v-for="(group, idx) in skillList" :key="idx" class="resume-skill-group">
              <h3 class="resume-skill-category">{{ group.category }}</h3>
              <div class="resume-skill-items">
                <span v-for="item in group.items" :key="item" class="tag">{{ item }}</span>
              </div>
            </div>
          </div>
        </FadeInView>
      </div>
    </section>

    <!-- Download -->
    <section class="section resume-section resume-download">
      <div class="container">
        <FadeInView>
          <div class="download-card card">
            <p class="download-text">
              {{ isZh ? '如需离线版本，可下载 PDF 简历。' : 'For an offline version, download the PDF resume.' }}
            </p>
            <div class="download-actions">
              <a href="/resume-zh.pdf" target="_blank" class="btn btn-primary">
                {{ isZh ? '下载中文简历 (PDF)' : 'Download Chinese Resume (PDF)' }}
              </a>
              <a href="/resume-en.pdf" target="_blank" class="btn btn-secondary">
                {{ isZh ? '下载英文简历 (PDF)' : 'Download English Resume (PDF)' }}
              </a>
            </div>
          </div>
        </FadeInView>
      </div>
    </section>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { personal, contact, education, experience, projects, publications, patents, awards, skills } from '../data/resume.js';
import { useLanguage } from '../composables/useLanguage.js';
import FadeInView from '../components/FadeInView.vue';

const { isZh } = useLanguage();
const eduList = computed(() => (isZh.value ? education.zh : education.en));
const expList = computed(() => (isZh.value ? experience.zh : experience.en));
const projList = computed(() => (isZh.value ? projects.zh : projects.en));
const pubList = computed(() => (isZh.value ? publications.zh : publications.en));
const patentList = computed(() => (isZh.value ? patents.zh : patents.en));
const awardList = computed(() => (isZh.value ? awards.zh : awards.en));
const skillList = computed(() => (isZh.value ? skills.zh : skills.en));
</script>

<style scoped>
.resume-page {
  padding-top: 80px;
}

.resume-hero {
  padding: 60px 0 40px;
  text-align: center;
  border-bottom: 1px solid var(--color-border-light);
}

.resume-name {
  font-size: 32px;
  font-weight: 700;
  margin-bottom: 8px;
  color: var(--color-text);
}

.resume-title {
  font-size: 15px;
  color: var(--color-text-secondary);
  margin-bottom: 16px;
}

.resume-contact-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  flex-wrap: wrap;
  font-size: 13px;
}

.resume-contact-item {
  color: var(--color-accent-hover);
  text-decoration: none;
}

.resume-contact-item:hover {
  text-decoration: underline;
}

.resume-contact-sep {
  color: var(--color-text-muted);
}

.resume-section {
  padding: 48px 0;
}

.timeline {
  display: flex;
  flex-direction: column;
  gap: 24px;
  position: relative;
}

.timeline-item {
  display: flex;
  gap: 16px;
}

.timeline-marker {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--color-accent);
  margin-top: 8px;
  flex-shrink: 0;
  box-shadow: 0 0 0 4px var(--color-accent-soft);
}

.timeline-content {
  flex: 1;
}

.timeline-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 12px;
  flex-wrap: wrap;
  margin-bottom: 6px;
}

.timeline-title {
  font-size: 16px;
  font-weight: 700;
  color: var(--color-text);
}

.timeline-subtitle {
  font-size: 14px;
  color: var(--color-text-secondary);
  margin-bottom: 4px;
}

.timeline-location {
  color: var(--color-text-muted);
}

.timeline-time {
  font-size: 13px;
  color: var(--color-text-muted);
  font-family: var(--font-mono);
  white-space: nowrap;
}

.timeline-detail {
  font-size: 14px;
  color: var(--color-text-secondary);
  line-height: 1.7;
}

.timeline-bullets {
  margin-top: 8px;
  padding-left: 18px;
  list-style: disc;
}

.timeline-bullets li {
  font-size: 14px;
  color: var(--color-text-secondary);
  line-height: 1.7;
  margin-bottom: 4px;
}

.project-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 2px;
}

.project-result-tag {
  font-size: 11px;
  font-weight: 600;
  color: var(--color-accent-hover);
  background: var(--color-accent-soft);
  padding: 2px 8px;
  border-radius: 999px;
}

.project-tags-row {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 12px;
}

.project-links-row {
  display: flex;
  gap: 12px;
  margin-top: 10px;
}

.pub-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.pub-item {
  padding: 20px;
}

.pub-title {
  font-size: 15px;
  font-weight: 700;
  color: var(--color-text);
  margin-bottom: 6px;
  line-height: 1.4;
}

.pub-authors {
  font-size: 13px;
  color: var(--color-text-secondary);
  margin-bottom: 4px;
}

.pub-venue {
  font-size: 13px;
  color: var(--color-accent-hover);
  font-weight: 600;
  margin-bottom: 8px;
}

.pub-links {
  display: flex;
  gap: 12px;
}

.patent-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.patent-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  background: var(--color-bg-soft);
  border-radius: var(--radius-sm);
  border: 1px solid var(--color-border-light);
}

.patent-name {
  font-size: 14px;
  color: var(--color-text);
}

.patent-number {
  font-size: 12px;
  font-family: var(--font-mono);
  color: var(--color-text-muted);
}

.award-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.award-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  background: var(--color-bg-soft);
  border-radius: var(--radius-sm);
  border: 1px solid var(--color-border-light);
  flex-wrap: wrap;
  gap: 8px;
}

.award-name {
  font-size: 14px;
  color: var(--color-text);
  flex: 1;
}

.award-org {
  font-size: 13px;
  color: var(--color-text-secondary);
}

.award-time {
  font-size: 12px;
  font-family: var(--font-mono);
  color: var(--color-text-muted);
}

.resume-skills {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

.resume-skill-group {
  padding: 16px;
  background: var(--color-bg-soft);
  border-radius: var(--radius-sm);
  border: 1px solid var(--color-border-light);
}

.resume-skill-category {
  font-size: 14px;
  font-weight: 600;
  color: var(--color-text);
  margin-bottom: 10px;
}

.resume-skill-items {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.resume-download {
  padding-bottom: 80px;
}

.download-card {
  text-align: center;
  max-width: 560px;
  margin: 0 auto;
  padding: 32px;
}

.download-text {
  font-size: 15px;
  color: var(--color-text-secondary);
  margin-bottom: 20px;
}

.download-actions {
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
  text-decoration: none;
}

.btn-secondary {
  background: var(--color-bg-soft);
  color: var(--color-text);
  border: 1px solid var(--color-border);
}

.btn-secondary:hover {
  background: var(--color-bg-muted);
  border-color: var(--color-accent);
  text-decoration: none;
}

@media (max-width: 640px) {
  .resume-name {
    font-size: 24px;
  }
  .timeline-header {
    flex-direction: column;
  }
  .resume-skills {
    grid-template-columns: 1fr;
  }
  .award-item {
    flex-direction: column;
    align-items: flex-start;
  }
  .patent-item {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>
