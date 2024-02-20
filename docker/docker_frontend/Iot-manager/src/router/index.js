import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'login',
            component: ()=>import('../views/LoginView.vue')
        },
        {
            path: '/main',
            name: 'main',
            component: ()=>import('../views/MainView.vue')
        },
        {
            path: '/map',
            name: 'map',
            component: ()=>import('../views/MapView.vue')
        },
        {
          path:'/register',
          name:'register',
          component:()=>import('../views/RegisterView.vue')
        }
    ]
})



export default router