import { createRouter, createWebHashHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import ResumeView from '../views/ResumeView.vue';
import NotesView from '../views/NotesView.vue';
import NoteDetailView from '../views/NoteDetailView.vue';

const routes = [
  { path: '/', name: 'Home', component: HomeView },
  { path: '/resume', name: 'Resume', component: ResumeView },
  { path: '/notes', name: 'Notes', component: NotesView },
  { path: '/notes/:slug', name: 'NoteDetail', component: NoteDetailView },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
  scrollBehavior() {
    return { top: 0 };
  },
});

export default router;
