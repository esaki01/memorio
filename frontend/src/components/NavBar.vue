<template>
    <nav class="navbar" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
            <a class="navbar-item">
                <router-link to="/">
                    <img alt="logo" src="@/assets/logo.svg" />
                </router-link>
            </a>
            <a
                role="button"
                class="navbar-burger burger"
                aria-label="menu"
                aria-expanded="false"
                data-target="navbarBasicExample"
                :class="{ 'is-active': showNav }"
                @click="showNav = !showNav"
            >
                <span aria-hidden="true" />
                <span aria-hidden="true" />
                <span aria-hidden="true" />
            </a>
        </div>

        <div id="navbarBasicExample" class="navbar-menu" :class="{ 'is-active': showNav }">
            <div class="navbar-start">
                <router-link v-if="user.uid" class="navbar-item" to="/">
                    <a>Home</a>
                </router-link>
                <router-link v-if="user.uid" class="navbar-item" to="/library">
                    <a>Library</a>
                </router-link>
                <div
                    v-if="!user.uid"
                    class="navbar-item has-dropdown is-left is-hoverable right-navbar-item"
                >
                    <a class="navbar-link">More info</a>
                    <div class="navbar-dropdown is-right">
                        <router-link to="/description">
                            <a class="navbar-item">What is PARROT?</a>
                        </router-link>
                    </div>
                </div>
            </div>

            <div class="navbar-end">
                <div class="navbar-item">
                    <div class="buttons">
                        <router-link v-if="!user.uid" class="button is-primary" to="/signin">
                            <a>
                                <strong class="has-text-white">
                                    <i class="fa fa-sign-in"></i>&nbsp;Sign in
                                </strong>
                            </a>
                        </router-link>
                        <router-link v-if="!user.uid" class="button is-danger" to="/signup">
                            <a>
                                <strong class="has-text-white">
                                    <i class="fa fa-user-plus"></i>&nbsp;Sign up
                                </strong>
                            </a>
                        </router-link>
                    </div>
                </div>
                <div
                    v-if="user.uid"
                    class="navbar-item has-dropdown is-left is-hoverable right-navbar-item"
                >
                    <a class="navbar-link">
                        <img alt="user logo" :src="imgSrc" class="avatar" />
                        {{ name }}
                    </a>
                    <div class="navbar-dropdown is-right">
                        <a class="navbar-item">My page</a>
                        <router-link class="navbar-item" to="/about">
                            <a>About</a>
                        </router-link>
                        <hr class="navbar-divider" />
                        <router-link to="/signout">
                            <a class="navbar-item" @click="signout">Sign out</a>
                        </router-link>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
import firebase from "firebase";

export default {
    data() {
        return {
            user: {},
            showNav: false,
            name: null,
            imgSrc: null
        };
    },
    created() {
        firebase.auth().onAuthStateChanged(user => {
            this.user = user || {};
            this.name = this.user.email
                ? this.user.email.split("@")[0]
                : this.user.displayName;

            this.imgSrc = this.user.photoURL
                ? this.user.photoURL
                : require("../assets/avatar.png");
        });
    },
    methods: {
        signout: function() {
            firebase
                .auth()
                .signOut()
                .then(() => {
                    this.$router.push("/signin");
                });
        }
    }
};
</script>

<style scoped>
nav {
    padding: 10px;
    border-bottom: 2px solid whitesmoke;
    background-color: #ffffff;
}

a {
    color: #000000;
}

.fa {
    font-size: 18px;
}

.avatar {
    margin-right: 16px;
    border-radius: 100px;
}
</style>
