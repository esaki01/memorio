<template>
    <div class="library">
        <div class="contents">
            <h1>Song Library</h1>
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
        </div>
    </div>
</template>

<script>
import axios from "axios";
import firebase from "firebase";

export default {
    data: function() {
        return {
            songs: []
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
                });
        }
    }
};
</script>

<style scoped>
.contents {
    margin: auto;
    max-width: 1000px;
    text-align: left;
    padding: 0 0.75rem;
}

h1 {
    margin: 24px auto;
    color: #f14667;
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

.over-text {
    overflow: hidden;
    white-space: nowrap;
}
</style>
