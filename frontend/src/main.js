import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import firebase from "firebase";
import secrets from "../config/secrets.js";

Vue.config.productionTip = false;

const config = {
    apiKey: secrets.apiKey,
    authDomain: secrets.authDomain,
    databaseURL: secrets.databaseURL,
    projectId: secrets.projectId
};

firebase.initializeApp(config);

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount("#app");
