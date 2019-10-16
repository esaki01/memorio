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
        @click="showNav = !showNav"
        :class="{ 'is-active': showNav }"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div id="navbarBasicExample" class="navbar-menu" :class="{ 'is-active': showNav }">
      <div class="navbar-start">
        <a class="navbar-item">
          <router-link to="/">Home</router-link>
        </a>
        <a class="navbar-item">
          <router-link to="/vocabulary">Vocabulary</router-link>
        </a>
      </div>

      <div class="navbar-end">
        <a class="navbar-item" v-if="!user.uid">
          <router-link to="/signin">Sign in</router-link>
        </a>
        <div class="navbar-item">
          <div class="buttons">
            <a class="button" v-if="!user.uid">
              <router-link to="/signup">Sign up</router-link>
            </a>
          </div>
        </div>
        <div
          class="navbar-item has-dropdown is-left is-hoverable right-navbar-item"
          v-if="user.uid"
        >
          <a class="navbar-link">{{ name }}</a>
          <div class="navbar-dropdown is-right">
            <a class="navbar-item">My page</a>
            <a class="navbar-item">
              <router-link to="/about">About</router-link>
            </a>
            <a class="navbar-item">Contact</a>
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
      this.user = user ? user : {};
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
  padding: 10px 0;
  box-shadow: 0 2px whitesmoke;
}

.right-navbar-item {
  padding-right: 20px;
}

a {
  font-weight: 500;
  color: #333333;
}

.navbar-link {
  color: #333333;
}
</style>
