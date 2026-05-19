<template>
  <div ref="el" class="fade-wrapper" :class="{ revealed: isRevealed }">
    <slot />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const el = ref(null);
const isRevealed = ref(false);

onMounted(() => {
  if (!el.value) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          isRevealed.value = true;
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
  );

  observer.observe(el.value);
});
</script>

<style scoped>
.fade-wrapper {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.5s ease-out, transform 0.5s ease-out;
}

.fade-wrapper.revealed {
  opacity: 1;
  transform: translateY(0);
}
</style>
