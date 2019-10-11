import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Signin from './views/Signin.vue'
import Signup from './views/Signup.vue'
import Vocabulary from './views/Vocabulary.vue'
import firebase from 'firebase'

Vue.use(Router)

let router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [{
            path: '/',
            name: 'home',
            component: Home,
            meta: { requiresAuth: true }
        },
        {
            path: '/vocabulary',
            name: 'vocabulary',
            component: Vocabulary,
            meta: { requiresAuth: true }
        },
        {
            path: '/signin',
            name: 'signin',
            component: Signin
        },
        {
            path: '/signup',
            name: 'signup',
            component: Signup
        }
    ]
})

router.beforeEach((to, from, next) => {
    const requiresAuth = to.matched.some(record => record.meta.requiresAuth)
    if (requiresAuth) {
        firebase.auth().onAuthStateChanged(function(user) {
            if (user) {
                next()
            } else {
                next({
                    path: '/signin',
                    query: { redirect: to.fullPath }
                })
            }
        })
    } else {
        next()
    }
})

export default router