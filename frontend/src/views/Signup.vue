<template>
    <div class="signup">
        <div v-if="isErrorShow" class="notification is-danger">{{ errorMsg }}</div>
        <progress v-if="isSuccessShow" class="progress is-small is-primary" max="100">15%</progress>
        <div v-else style="height: 12px;" />

        <div class="columns">
            <div class="column is-12">
                <div class="form">
                    <div class="field">
                        <label class="label">Sign up for PARROT</label>

                        <div class="control has-icons-left has-icons-right">
                            <input v-model="email" class="input" type="email" placeholder="Email" />
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
                            <a class="button is-fullwidth is-danger" @click="signup">Sign up</a>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
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
                    this.createLibrary();
                    this.$router.push("/");
                })
                .catch(error => {
                    this.isSuccessShow = false;
                    this.isErrorShow = true;
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
    text-align: center;
}

.columns {
    margin: 24px auto 0 auto;
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
    font-weight: bolder;
}
</style>
