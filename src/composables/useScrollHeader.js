import { ref, onMounted, onUnmounted } from 'vue';

export function useScrollHeader(threshold = 10) {
  const isVisible = ref(true);
  const lastScrollY = ref(0);

  function handleScroll() {
    const currentY = window.scrollY;
    if (currentY < threshold) {
      isVisible.value = true;
    } else if (currentY > lastScrollY.value) {
      isVisible.value = false;
    } else {
      isVisible.value = true;
    }
    lastScrollY.value = currentY;
  }

  onMounted(() => {
    window.addEventListener('scroll', handleScroll, { passive: true });
  });

  onUnmounted(() => {
    window.removeEventListener('scroll', handleScroll);
  });

  return { isVisible };
}
