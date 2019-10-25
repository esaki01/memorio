<template>
  <div class="signin">
    <div class="notification is-danger" v-if="isErrorShow">{{ errorMsg }}</div>
    <progress class="progress is-small is-primary" max="100" v-if="isSuccessShow">15%</progress>
    <div style="height: 12px;" v-else></div>
    <div class="columns level reverse-row-order">
      <div class="column is-6 level-right">
        <div class="form">
          <div class="field">
            <label class="label">Sign in to PARROT</label>

            <div class="field">
              <p class="control">
                <a class="button is-fullwidth is-danger" @click="signinWithGoogle">
                  <span class="icon">
                    <i class="fa fa-google"></i>
                  </span>
                  <span>Sign in with Google</span>
                </a>
              </p>
            </div>

            <div class="field">
              <p class="control">
                <a class="button is-fullwidth is-info" @click="signinWithTwitter">
                  <span class="icon">
                    <i class="fa fa-twitter"></i>
                  </span>
                  <span>Sign in with Twitter</span>
                </a>
              </p>
            </div>

            <div class="is-divider" data-content="OR"></div>
            <div class="control has-icons-left has-icons-right">
              <input class="input" type="email" placeholder="Email" v-model="email" />
              <span class="icon is-left">
                <i class="fa fa-envelope"></i>
              </span>
              <span class="icon is-right">
                <i class="fa fa-check"></i>
              </span>
            </div>
          </div>

          <div class="field">
            <div class="control has-icons-left has-icons-right">
              <input class="input" type="password" placeholder="Password" v-model="password" />
              <span class="icon is-left">
                <i class="fa fa-lock"></i>
              </span>
              <span class="icon is-right">
                <i class="fa fa-check"></i>
              </span>
            </div>
          </div>

          <div class="field">
            <p class="control">
              <a class="button is-fullwidth is-success" @click="signin">Sign in</a>
            </p>
            <p class="not-have">
              <span>New to PARROT? </span>
              <a>
                <router-link to="/signup">Create an account</router-link>
              </a>.
            </p>
          </div>
        </div>
      </div>
      <div class="column is-6 level-left">
        <p class="home-title has-text-danger">Platform for<br/>English learners</p>
        <p class="home-sub">Get started for free!<br/>You will be able to understand how to pronounce the words in the song lyrics 
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import firebase from "firebase";

export default {
  name: "signin",
  data: function() {
    return {
      email: "",
      password: "",
      isSuccessShow: false,
      isErrorShow: false,
      errorMsg: ""
    };
  },
  methods: {
    signin: async function() {
      this.isSuccessShow = true;
      this.isErrorShow = false;
      firebase
        .auth()
        .signInWithEmailAndPassword(this.email, this.password)
        .then(
          () => {
            this.$router.replace("/");
          },
          err => {
            this.isSuccessShow = false;
            this.isErrorShow = true;
            this.errorMsg = err.message;
          }
        );
    },
    signinWithGoogle: function() {
      const provider = new firebase.auth.GoogleAuthProvider();
      firebase
        .auth()
        .signInWithPopup(provider)
        .then(() => {
          this.$router.replace("/");
        })
        .catch(err => {
          this.isErrorShow = true;
          this.errorMsg = err.message;
        });
    },
    signinWithTwitter: function() {
      const provider = new firebase.auth.TwitterAuthProvider();
      firebase
        .auth()
        .signInWithPopup(provider)
        .then(() => {
          this.$router.replace("/");
        })
        .catch(err => {
          this.isErrorShow = true;
          this.errorMsg = err.message;
        });
    }
  }
};
</script>

<style scoped>
@import "~bulma-divider";

.signin {
  text-align: center;
}

.columns {
  margin: 48px auto 0 auto;
}

.form {
  max-width: 400px;
  border-radius: 5px;
  padding: 20px;
  box-shadow: 0 0 3px lightgray;
  margin: auto;
  text-align: center;
  background-color: #ffffff;
}

a {
  font-weight: bolder;
}

.not-have {
  margin-top: 20px;
  font-weight: 500;
}

.not-have a{
  color: #3173DC;
  font-weight: 500;
}

.not-have a:hover{
  text-decoration: underline;
}

.label {
  margin-bottom: 20px;
  font-size: 24px;
  font-weight: 500;
  font-weight: bolder;
}

.home-title {
  font-size: 52px;
  font-weight: bolder;
  text-align: left;
  line-height: 60px;
  margin: 50px auto 0 auto;
  max-width: 400px;
}

.home-sub {
  font-size: 28px;
  font-weight: bolder;
  color: #666666;
  text-align: left;
  line-height: 40px;
  margin: 10px auto 50px auto;
  max-width: 400px;
}

.reverse-row-order {
  flex-direction: row-reverse;
  max-width: 980px;
}
</style>
