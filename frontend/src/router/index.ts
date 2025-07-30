import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView,
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView,
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUpView,
  },
]
// const router = createRouter({
//   history: createWebHistory(process.env.BASE_URL),
//   routes,
// })
const router = createRouter({
  history: createWebHistory(), // 인자를 비워두세요
  routes,
})
export default router
