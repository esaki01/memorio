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
                <a v-if="user.uid" class="navbar-item">
                    <router-link to="/">Home</router-link>
                </a>
                <a v-if="user.uid" class="navbar-item">
                    <router-link to="/library">Library</router-link>
                </a>
                <a v-else class="navbar-item">
                    <router-link to="/">What is PARROT?</router-link>
                </a>
            </div>

            <div class="navbar-end">
                <div class="navbar-item">
                    <div class="buttons">
                        <a v-if="!user.uid" class="button is-primary">
                            <router-link to="/signin">
                                <strong class="has-text-white">
                                    <i class="fa fa-sign-in"></i>&nbsp;Sign in
                                </strong>
                            </router-link>
                        </a>
                        <a v-if="!user.uid" class="button is-danger">
                            <router-link to="/signup">
                                <strong class="has-text-white">
                                    <i class="fa fa-user-plus"></i>&nbsp;Sign up
                                </strong>
                            </router-link>
                        </a>
                    </div>
                </div>
                <div
                    v-if="user.uid"
                    class="navbar-item has-dropdown is-left is-hoverable right-navbar-item"
                >
                    <a class="navbar-link">
                        <img alt="user logo" src="@/assets/avatar.png" class="avatar" />
                        {{ name }}
                    </a>
                    <div class="navbar-dropdown is-right">
                        <a class="navbar-item">My page</a>
                        <a class="navbar-item">
                            <router-link to="/about">About</router-link>
                        </a>
                        <hr class="navbar-divider" />
                        <a class="navbar-item" @click="signout">
                            <router-link to="/signout">Sign out</router-link>
                        </a>
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
            name: null
        };
    },
    created() {
        firebase.auth().onAuthStateChanged(user => {
            this.user = user || {};
            this.name = this.user.email
                ? this.user.email.split("@")[0]
                : this.user.displayName;
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
}
</style>
