<template>
    <section class="signin section">
        <div class="container">
            <div class="columns level reverse-row-order">
                <div class="column is-6 level-right">
                    <div class="signin-form">
                        <div class="field">
                            <label class="label">Sign in to PARROT</label>
                            <div class="field">
                                <p class="control">
                                    <a
                                        class="button is-fullwidth is-danger"
                                        @click="signinWithGoogle"
                                    >
                                        <span class="icon">
                                            <i class="fa fa-google" />
                                        </span>
                                        <strong>Sign in with Google</strong>
                                    </a>
                                </p>
                            </div>

                            <div class="field">
                                <p class="control">
                                    <a
                                        class="button is-fullwidth is-info"
                                        @click="signinWithTwitter"
                                    >
                                        <span class="icon">
                                            <i class="fa fa-twitter" />
                                        </span>
                                        <strong>Sign in with Twitter</strong>
                                    </a>
                                </p>
                            </div>

                            <div class="is-divider" data-content="OR" />
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
                                    class="button is-fullwidth is-primary"
                                    @click="signin"
                                    v-bind:class="{'is-loading':progressShow}"
                                >
                                    <strong>Sign in</strong>
                                </a>
                            </p>
                            <div v-if="errorShow" class="notify">
                                <strong class="has-text-danger">{{ errorMsg }}</strong>
                            </div>
                            <p class="new-account">
                                <span>New to PARROT?&nbsp;</span>
                                <a>
                                    <router-link to="/signup">Create an account</router-link>
                                </a>.
                            </p>
                        </div>
                    </div>
                </div>
                <div class="column level-left">
                    <div class="home-title">
                        <p class="title is-1 has-text-danger">
                            Platform for
                            <br />English learners
                        </p>
                        <p class="subtitle is-4 has-text-grey-dark">
                            Get started for free!
                            <br />You will be able to understand how to pronounce the words in the
                            song lyrics.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import firebase from "firebase";

export default {
    name: "Signin",
    data: function() {
        return {
            email: "",
            password: "",
            progressShow: false,
            errorShow: false,
            errorMsg: ""
        };
    },
    methods: {
        signin: async function() {
            this.progressShow = true;
            this.errorShow = false;
            firebase
                .auth()
                .signInWithEmailAndPassword(this.email, this.password)
                .then(
                    () => {
                        this.$router.replace("/");
                    },
                    err => {
                        this.progressShow = false;
                        this.errorShow = true;
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
                    this.errorShow = true;
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
                    this.errorShow = true;
                    this.errorMsg = err.message;
                });
        }
    }
};
</script>

<style scoped>
@import "~bulma-divider";

.signin {
    max-width: 1000px;
    margin: auto;
}

.notify {
    margin-top: 20px;
    text-align: center;
}

.reverse-row-order {
    flex-direction: row-reverse;
}

.signin-form {
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

.new-account {
    margin-top: 20px;
    font-weight: 500;
}

.new-account a {
    color: #3173dc;
}

.new-account a:hover {
    text-decoration: underline;
}

.home-title {
    max-width: 400px;
    margin: 36px auto;
    text-align: left;
    font-weight: bolder;
}

.subtitle {
    padding-top: 8px;
}
</style>
