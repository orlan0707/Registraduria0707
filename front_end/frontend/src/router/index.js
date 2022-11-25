import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Medico from "../components/Medico.vue"
import FamiliarDesignado from "../components/FamiliarDesignado.vue"
import MostrarPacientes from "../components/MostrarPacientes.vue"

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/medico',
    name: 'medico',
    component: Medico
  },
  {
    path: '/FamiliarDesignado',
    name: 'FamiliarDesignado',
    component: FamiliarDesignado
  },
  {
    path: '/mostrarPacientes',
    name: 'MostrarPacientes',
    component: MostrarPacientes
  }
  
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
