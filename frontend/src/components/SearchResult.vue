<template>
    <div class="search-result">
        <h1 class="has-text-danger">Search Lyrics</h1>

        <!-- search form for mobile -->
        <div class="field is-hidden-tablet">
            <div class="field-body">
                <div v-if="selected === 'Artist Search'" class="field has-addons">
                    <p class="control is-expanded has-icons-left">
                        <input
                            v-model="artist"
                            class="input"
                            type="text"
                            placeholder="Artist (e.g. The Beatles)"
                        />
                        <span class="icon is-small is-left">
                            <i class="fa fa-user-circle" />
                        </span>
                    </p>
                </div>
                <div v-if="selected === 'Song Search'" class="field has-addons">
                    <p class="control is-expanded has-icons-left">
                        <input
                            v-model="title"
                            class="input"
                            type="email"
                            placeholder="Song (e.g. Let It Be)"
                        />
                        <span class="icon is-small is-left">
                            <i class="fa fa-music" />
                        </span>
                    </p>
                </div>
                <div v-if="selected === 'Artist & Song Search'" class="field has-addons">
                    <p class="control is-expanded has-icons-left">
                        <input
                            v-model="artist"
                            class="input"
                            type="text"
                            placeholder="Artist (e.g. The Beatles)"
                        />
                        <span class="icon is-small is-left">
                            <i class="fa fa-user-circle" />
                        </span>
                    </p>
                </div>
                <div v-if="selected === 'Artist & Song Search'" class="field has-addons">
                    <p class="control is-expanded has-icons-left">
                        <input
                            v-model="title"
                            class="input"
                            type="email"
                            placeholder="Song (e.g. Let It Be)"
                        />
                        <span class="icon is-small is-left">
                            <i class="fa fa-music" />
                        </span>
                    </p>
                </div>
                <div class="field has-addons">
                    <p class="control is-expanded">
                        <span class="select is-fullwidth">
                            <select v-model="selected">
                                <option>Artist &amp; Song Search</option>
                                <option>Artist Search</option>
                                <option>Song Search</option>
                            </select>
                        </span>
                    </p>
                    <p class="control">
                        <a
                            class="button is-primary"
                            style="width: 48px;"
                            @click="search"
                            v-bind:class="{'is-loading':progressShow}"
                        >
                            <span class="fa fa-search has-text-white" v-if="!progressShow" />
                        </a>
                    </p>
                </div>
            </div>
        </div>

        <!-- search form for tablet, desktop -->
        <div class="field is-horizontal is-hidden-mobile">
            <div class="field-body">
                <div class="field has-addons">
                    <p
                        v-if="selected === 'Artist Search'"
                        class="control is-expanded has-icons-left"
                    >
                        <input
                            v-model="artist"
                            class="input"
                            type="text"
                            placeholder="Artist (e.g. The Beatles)"
                        />
                        <span class="icon is-small is-left">
                            <i class="fa fa-user-circle" />
                        </span>
                    </p>
                    <p v-if="selected === 'Song Search'" class="control is-expanded has-icons-left">
                        <input
                            v-model="title"
                            class="input"
                            type="email"
                            placeholder="Song (e.g. Let It Be)"
                        />
                        <span class="icon is-small is-left">
                            <i class="fa fa-music" />
                        </span>
                    </p>

                    <p
                        v-if="selected === 'Artist & Song Search'"
                        class="control is-expanded has-icons-left"
                    >
                        <input
                            v-model="artist"
                            class="input"
                            type="text"
                            placeholder="Artist (e.g. The Beatles)"
                        />
                        <span class="icon is-small is-left">
                            <i class="fa fa-user-circle" />
                        </span>
                    </p>
                    <p
                        v-if="selected === 'Artist & Song Search'"
                        class="control is-expanded has-icons-left"
                    >
                        <input
                            v-model="title"
                            class="input"
                            type="email"
                            placeholder="Song (e.g. Let It Be)"
                        />
                        <span class="icon is-small is-left">
                            <i class="fa fa-music" />
                        </span>
                    </p>

                    <p class="control">
                        <span class="select">
                            <select v-model="selected">
                                <option>Artist &amp; Song Search</option>
                                <option>Artist Search</option>
                                <option>Song Search</option>
                            </select>
                        </span>
                    </p>
                    <p class="control">
                        <a
                            class="button is-fullwidth is-primary"
                            style="width: 48px;"
                            @click="search"
                            v-bind:class="{'is-loading':progressShow}"
                        >
                            <span class="fa fa-search has-text-white" v-if="!progressShow" />
                        </a>
                    </p>
                </div>
            </div>
        </div>

        <div v-if="searchResultShow" class="search-result">
            <h2>Search Results</h2>
            <div v-for="sr in searchResults" :key="sr.id" class="box">
                <router-link
                    :to="{
              name: 'lyrics',
              params: {
                artist: sr.artist,
                title: sr.title,
                jacket_image_url: sr.jacket_image_url,
                lyrics: sr.lyrics,
              },
            }"
                >
                    <article class="media">
                        <div class="media-left">
                            <figure class="image is-128x128">
                                <img :src="sr.jacket_image_url" alt="Image" />
                            </figure>
                        </div>
                        <div class="media-content">
                            <p class="title is-6">
                                {{ sr.title }}
                                / {{ sr.artist }}
                            </p>
                            <div class="content">
                                <p class="ellipsis has-text-grey-dark">{{ sr.lyrics }}</p>
                            </div>
                            <nav class="level is-mobile">
                                <div class="level-left">
                                    <a class="level-item" aria-label="reply">
                                        <span class="icon is-small">
                                            <i class="fa fa-reply" aria-hidden="true" />
                                        </span>
                                    </a>
                                    <a class="level-item" aria-label="retweet">
                                        <span class="icon is-small">
                                            <i class="fa fa-retweet" aria-hidden="true" />
                                        </span>
                                    </a>
                                    <a class="level-item" aria-label="like">
                                        <span class="icon is-small">
                                            <i class="fa fa-heart" aria-hidden="true" />
                                        </span>
                                    </a>
                                </div>
                            </nav>
                        </div>
                    </article>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    data: function() {
        return {
            artist: "",
            title: "",
            searchResultShow: false,
            progressShow: false,
            searchResults: [],
            selected: "Artist & Song Search"
        };
    },
    methods: {
        search: function() {
            var requestUrl = "";

            if (this.artist != "" && this.title != "") {
                this.progressShow = true;
                requestUrl =
                    "https://parrot-api-n2zzz72gsq-uc.a.run.app/song/artist-title/search";
            } else if (this.artist != "") {
                this.progressShow = true;
                requestUrl =
                    "https://parrot-api-n2zzz72gsq-uc.a.run.app/song/artist/search";
            } else if (this.title != "") {
                this.progressShow = true;
                requestUrl =
                    "https://parrot-api-n2zzz72gsq-uc.a.run.app/song/title/search";
            }

            axios
                .get(requestUrl, {
                    params: { artist: this.artist, title: this.title }
                })
                .then(response => {
                    if (response.data.data) {
                        this.searchResults = response.data.data.songs;
                        this.searchResultShow = true;
                    } else {
                        console.log("Not data.");
                    }
                })
                .catch(error => {
                    console.log(error);
                })
                .finally(() => {
                    this.progressShow = false;
                    this.artist = "";
                    this.title = "";
                });
        }
    }
};
</script>

<style scoped>
h1 {
    margin-bottom: 24px;
    font-size: 24px;
    font-weight: bolder;
    text-align: left;
    font-family: "Oswald", sans-serif;
}

h2 {
    margin: 24px auto;
    color: #333333;
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
</style>
