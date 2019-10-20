<template>
  <div class="signup">
    <div class="notification is-danger" v-if="isErrorShow">{{ errorMsg }}</div>
    <progress class="progress is-small is-primary" max="100" v-if="isSuccessShow">15%</progress>
    <div style="height: 12px;" v-else></div>

    <div class="columns">
      <div class="column is-12">
        <div class="form">
          <div class="field">
            <label class="label">Sign up for PARROT</label>

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
          </div>
        </div>
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
      firebase
        .auth()
        .createUserWithEmailAndPassword(this.email, this.password)
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
a {
  font-weight: bolder;
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

.label {
  margin-bottom: 20px;
  font-size: 24px;
  font-weight: 500;
}
</style>