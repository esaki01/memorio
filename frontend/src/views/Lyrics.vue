<template>
    <section class="lyrics section">
        <div class="container">
            <h1 class="has-text-danger">Pronunciation of the Lyrics</h1>
            <div class="columns">
                <div class="column is-one-quarters">
                    <img :src="$route.params.jacket_image_url" alt="Image" />
                    <p class="song-title">{{ $route.params.title }}</p>
                    <p class="song-artist has-text-danger">{{ $route.params.artist }}</p>
                    <a
                        class="button is-fullwidth is-primary"
                        @click="addSong"
                        v-bind:class="{'is-loading':progressShow}"
                    >
                        <strong>Add a song</strong>
                    </a>
                </div>
                <div class="column is-three-quarters pronunciation-box">
                    <table class="table is-striped is-fullwidth">
                        <div v-for="i in 10" :key="i.id">
                            <tbody>
                                <tr>
                                    <td v-for="l in 10" :key="l.id">
                                        <span class="lyrics">
                                            {{
                                            lyrics[l - 1 + (i - 1) * 10]
                                            }}
                                        </span>
                                    </td>
                                </tr>
                                <tr>
                                    <td v-for="p in 10" :key="p.id">
                                        <img
                                            v-if="contentsShow"
                                            style="width: 16px;"
                                            alt="logo"
                                            src="@/assets/loading.gif"
                                        />
                                        <span v-else class="pronunciation is-6">
                                            {{
                                            pronunciation[p - 1 + (i - 1) * 10]
                                            }}
                                        </span>
                                    </td>
                                </tr>
                            </tbody>
                        </div>
                    </table>
                </div>
            </div>
        </div>

        <div class="modal" v-bind:class="{ 'is-active': isShowModal }">
            <div class="modal-background" v-on:click="isShowModal = false"></div>
            <div class="modal-content">
                <div class="notification is-primary">
                    <button class="delete" v-on:click="isShowModal = false"></button>
                    <p>
                        Success to add
                        <strong>"{{ $route.params.title }}"</strong> to your library.
                        <router-link to="/library">Go to library!</router-link>
                    </p>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import axios from "axios";
import firebase from "firebase";

export default {
    data: function() {
        return {
            lyrics: [],
            pronunciation: [],
            progressShow: false,
            contentsShow: true,
            isShowModal: false
        };
    },
    created: function() {
        this.getPronunciation(this.$route.params.lyrics);
        this.lyrics = this.$route.params.lyrics.split(/\s+/);
    },
    methods: {
        getPronunciation: function(param) {
            axios
                .get(
                    "https://parrot-api-n2zzz72gsq-uc.a.run.app/pronunciation/search",
                    {
                        params: { words: param }
                    }
                )
                .then(response => {
                    if (response.data.data) {
                        this.pronunciation = response.data.data.pronunciation;
                    } else {
                        console.log("Not data.");
                    }
                })
                .catch(error => {
                    console.log(error);
                })
                .finally(() => {
                    this.contentsShow = false;
                });
        },
        addSong: function() {
            var user = firebase.auth().currentUser;

            if (user) {
                this.progressShow = true;
                axios
                    .post(
                        "https://parrot-api-n2zzz72gsq-uc.a.run.app/library/add/song",
                        {
                            user_id: user.uid,
                            artist: this.$route.params.artist,
                            title: this.$route.params.title,
                            jacket_image_url: this.$route.params
                                .jacket_image_url,
                            lyrics: this.$route.params.lyrics
                        }
                    )
                    .then(response => {
                        console.log(response.data.data);
                        this.isShowModal = true;
                    })
                    .catch(error => {
                        console.log(error);
                    })
                    .finally(() => {
                        this.progressShow = false;
                    });
            } else {
                this.$router.push("/signin");
            }
        }
    }
};
</script>

<style scoped>
.lyrics {
    max-width: 1000px;
    margin: auto;
}

h1 {
    margin-bottom: 24px;
    font-size: 24px;
    font-weight: bolder;
    text-align: left;
    font-family: "Oswald", sans-serif;
}

.pronunciation {
    color: #888888;
}

.song-title {
    text-align: center;
    font-size: 16px;
    font-weight: 600;
    margin: 5px 0;
}

.song-artist {
    text-align: center;
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 15px;
}

.pronunciation-box {
    overflow: scroll;
}
</style>
