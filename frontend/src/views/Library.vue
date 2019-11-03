<template>
    <section class="library section">
        <div class="container">
            <h1 class="has-text-danger">Library</h1>
            <div v-for="song in songs" :key="song.id" class="box">
                <article class="media">
                    <div class="media-left">
                        <figure class="image is-128x128">
                            <img :src="song.jacket_image_url" alt="Image" />
                        </figure>
                    </div>
                    <div class="media-content">
                        <p class="title is-6">
                            {{ song.title }}
                            / {{ song.artist }}
                        </p>
                        <div class="content">
                            <p class="ellipsis has-text-grey-dark">{{ song.lyrics }}</p>
                        </div>
                    </div>
                </article>
            </div>
            <div v-if="isShowNoSongs" class="no-songs">
                <p>No songs yet...</p>
                <p>Let's add a song to your library!</p>
                <a>
                    <router-link to="/">Go Home</router-link>
                </a>
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
            songs: [],
            isShowNoSongs: false
        };
    },
    created: function() {
        this.getLibrary();
    },
    methods: {
        getLibrary: function() {
            axios
                .get(
                    "https://parrot-api-n2zzz72gsq-uc.a.run.app/library/list",
                    {
                        params: { user_id: firebase.auth().currentUser.uid }
                    }
                )
                .then(response => {
                    this.songs = response.data.data.library.songs;
                })
                .catch(error => {
                    console.log(error);
                })
                .finally(() => {
                    if (this.songs.length == 0) {
                        this.isShowNoSongs = true;
                    }
                });
        }
    }
};
</script>

<style scoped>
.library {
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

.ellipsis {
    position: relative;
    height: 100px;
    line-height: 24px;
    overflow: hidden;
}

.no-songs {
    text-align: center;
    font-weight: 600;
    margin-top: 40px;
}

.no-songs a {
    color: #3173dc;
}

.no-songs a:hover {
    text-decoration: underline;
}
</style>
