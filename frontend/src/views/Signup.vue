<template>
    <section class="signup section">
        <div class="container">
            <div class="columns">
                <div class="column is-12">
                    <div class="signup-form">
                        <div class="field">
                            <label class="label">Sign up for PARROT</label>

                            <div class="control has-icons-left has-icons-right">
                                <input
                                    v-model="email"
                                    class="input"
                                    type="email"
                                    placeholder="Email"
                                />
                                <span class="icon is-left">
                                    <i class="fa fa-envelope" />
                                </span>
                                <span class="icon is-right">
                                    <i class="fa fa-check" />
                                </span>
                            </div>
                        </div>

                        <div class="field">
                            <div class="control has-icons-left has-icons-right">
                                <input
                                    v-model="password"
                                    class="input"
                                    type="password"
                                    placeholder="Password"
                                />
                                <span class="icon is-left">
                                    <i class="fa fa-lock" />
                                </span>
                                <span class="icon is-right">
                                    <i class="fa fa-check" />
                                </span>
                            </div>
                        </div>

                        <div class="field">
                            <p class="control">
                                <a
                                    class="button is-fullwidth is-danger"
                                    @click="signup"
                                    v-bind:class="{'is-loading':progressShow}"
                                >
                                    <strong>Sign up</strong>
                                </a>
                            </p>
                            <div v-if="errorShow" class="notify">
                                <strong class="has-text-danger">{{ errorMsg }}</strong>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import firebase from "firebase";
import axios from "axios";

export default {
    name: "Signup",
    data() {
        return {
            email: "",
            password: "",
            progressShow: false,
            errorShow: false,
            errorMsg: ""
        };
    },
    methods: {
        signup: async function() {
            this.progressShow = true;
            this.errorShow = false;
            firebase
                .auth()
                .createUserWithEmailAndPassword(this.email, this.password)
                .then(() => {
                    this.createLibrary();
                    this.$router.push("/");
                })
                .catch(error => {
                    this.progressShow = false;
                    this.errorShow = true;
                    this.errorMsg = error.message;
                });
        },
        createLibrary: function() {
            axios
                .post(
                    "https://parrot-api-n2zzz72gsq-uc.a.run.app/library/create",
                    {
                        user_id: firebase.auth().currentUser.uid
                    }
                )
                .then(response => {
                    console.log(response.data.data);
                })
                .catch(error => {
                    console.log(error);
                });
        }
    }
};
</script>

<style scoped>
.signup {
    max-width: 1000px;
    margin: auto;
}

.notify {
    margin-top: 20px;
    text-align: center;
}

.signup-form {
    max-width: 400px;
    text-align: center;
    background-color: #ffffff;
    box-shadow: 0 0 3px lightgray;
    border-radius: 5px;
    padding: 20px;
    margin: auto;
}

.label {
    margin-bottom: 20px;
    font-size: 24px;
    font-weight: bolder;
}
</style>
