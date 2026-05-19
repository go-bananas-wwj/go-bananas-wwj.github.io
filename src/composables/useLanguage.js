import { ref, computed, provide, inject } from 'vue';

const LANGUAGE_KEY = Symbol('language');

export function createLanguageProvider() {
  const stored = typeof localStorage !== 'undefined' ? localStorage.getItem('lang') : null;
  const lang = ref(stored === 'en' ? 'en' : 'zh');

  function toggleLang() {
    lang.value = lang.value === 'zh' ? 'en' : 'zh';
    if (typeof localStorage !== 'undefined') {
      localStorage.setItem('lang', lang.value);
    }
  }

  function setLang(value) {
    lang.value = value;
    if (typeof localStorage !== 'undefined') {
      localStorage.setItem('lang', value);
    }
  }

  const isZh = computed(() => lang.value === 'zh');

  provide(LANGUAGE_KEY, { lang, toggleLang, setLang, isZh });

  return { lang, toggleLang, setLang, isZh };
}

export function useLanguage() {
  const injected = inject(LANGUAGE_KEY, null);
  if (!injected) {
    console.warn('useLanguage must be used within a language provider');
    return {
      lang: ref('zh'),
      toggleLang: () => {},
      setLang: () => {},
      isZh: computed(() => true),
    };
  }
  return injected;
}
