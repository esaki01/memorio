import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Signin from "./views/Signin.vue";
import Signup from "./views/Signup.vue";
import Library from "./views/Library.vue";
import Lyrics from "./views/Lyrics.vue";
import Description from "./views/Description.vue";
import firebase from "firebase";

Vue.use(Router);

const router = new Router({
    mode: "history",
    base: process.env.BASE_URL,
    routes: [
        {
            path: "/",
            name: "home",
            component: Home
        },
        {
            path: "/description",
            name: "description",
            component: Description
        },
        {
            path: "/library",
            name: "library",
            component: Library,
            meta: { requiresAuth: true }
        },
        {
            path: "/signin",
            name: "signin",
            component: Signin
        },
        {
            path: "/signup",
            name: "signup",
            component: Signup
        },
        {
            path: "/lyrics/:artist/:title/:jacket_image_url/:lyrics",
            name: "lyrics",
            component: Lyrics
        }
    ]
});

router.beforeEach((to, from, next) => {
    const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
    if (requiresAuth) {
        firebase.auth().onAuthStateChanged(function(user) {
            if (user) {
                next();
            } else {
                next({
                    path: "/signin",
                    query: { redirect: to.fullPath }
                });
            }
        });
    } else {
        next();
    }
});

export default router;
