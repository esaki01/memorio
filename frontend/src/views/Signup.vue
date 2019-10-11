<template>
  <div class="signup">
    <progress class="progress is-small is-primary" max="100" v-if="isSuccessShow">15%</progress>
    <div class="notification is-danger" v-if="isErrorShow">
      {{ errorMsg }}
    </div>

    <div class="form">
      <div class="field">
        <label class="label">Sign up for memorio</label>

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
          <a class="button is-fullwidth is-success" @click="signup">Sign up</a>
        </p>
        <p class="sign-in-now">
          <a>
            <router-link to="/signin">Sign in now!</router-link>
          </a>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import firebase from "firebase";

export default {
  name: "signup",
  data() {
    return {
      email: "",
      password: "",
      isSuccessShow: false,
      isErrorShow: false,
      errorMsg: ""
    };
  },
  methods: {
    signup: async function() {
      this.isSuccessShow = true;
      this.isErrorShow = false;
      firebase.auth().createUserWithEmailAndPassword(this.email, this.password)
        .then(() => {
          this.$router.push("/");
        })
        .catch(error => {
          this.isSuccessShow = false;
          this.isErrorShow = true;
          this.errorMsg = error.message;
        });
    }
  }
};
</script>

<style scoped>
.form {
  margin: 50px auto 0 auto;
  max-width: 400px;
  border: 1px solid lightgray;
  border-radius: 5px;
  padding: 20px;
  box-shadow: 0 0 3px lightgray;
}

.sign-in-now {
  margin-top: 20px;
}

.sign-in-now a {
  color: #333333;
  text-decoration: underline;
}

.sign-in-now a:hover {
  opacity: 0.8;
}

.label {
  margin-bottom: 20px;
}
</style>