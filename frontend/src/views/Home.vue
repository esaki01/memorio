<template>
    <div class="home">
        <div class="search-form container">
            <h1 class="has-text-danger">Search Lyrics</h1>
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
                        <p
                            v-if="selected === 'Song Search'"
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

            <h2>Trending</h2>
            <div class="trending-box">
                <content-loader v-if="contentsShow" :width="400" :height="22">
                    <rect x="0" y="0" rx="3" ry="3" width="400" height="10" />
                    <rect x="0" y="12" rx="3" ry="3" width="400" height="10" />
                </content-loader>
                <div v-else class="tags">
                    <span v-for="tl in trendingList" :key="tl.id" class="tag">
                        <span>
                            <a
                                :href="tl.external_url"
                                target="_blank"
                                class="has-text-grey-dark"
                            >{{ tl.title }}</a>
                        </span>
                    </span>
                </div>
            </div>
            <h2>Recommended</h2>
            <div class="recommended-box">
                <div class="columns is-multiline is-mobile">
                    <div
                        v-for="rl in recommendedList"
                        :key="rl.id"
                        class="column is-one-quarter-tablet is-half-mobile"
                    >
                        <div class="card">
                            <a :href="rl.external_url" target="_blank">
                                <div class="card-image">
                                    <content-loader v-if="contentsShow" :width="400" :height="400">
                                        <rect x="0" y="0" rx="0" ry="0" width="400" height="400" />
                                    </content-loader>
                                    <figure v-else class="image is-1by1">
                                        <img :src="rl.jacket_image_url" alt="Image" />
                                    </figure>
                                </div>
                            </a>
                            <div class="card-content">
                                <div class="media">
                                    <div class="media-content over-text">
                                        <content-loader
                                            v-if="contentsShow"
                                            :width="400"
                                            :height="100"
                                        >
                                            <rect
                                                x="0"
                                                y="0"
                                                rx="0"
                                                ry="0"
                                                width="400"
                                                height="100"
                                            />
                                        </content-loader>
                                        <div v-else>
                                            <p class="title is-6">{{ rl.artist }}</p>
                                            <p class="subtitle is-8">
                                                <a
                                                    :href="rl.external_url"
                                                    target="_blank"
                                                    class="extra-link has-text-danger"
                                                >{{ rl.title }}</a>
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { ContentLoader } from "vue-content-loader";

export default {
    components: {
        ContentLoader
    },
    data: function() {
        return {
            artist: "",
            title: "",
            searchResultShow: false,
            progressShow: false,
            contentsShow: true,
            searchResults: [],
            trendingList: [],
            recommendedList: ["", "", "", "", "", "", "", ""],
            selected: "Artist & Song Search"
        };
    },
    mounted: function() {
        this.getTrending();
        this.getRecommended();
    },
    methods: {
        search: function() {
            this.progressShow = true;

            var requestUrl = "";

            if (this.artist != "" && this.title != "") {
                requestUrl =
                    "https://parrot-api-n2zzz72gsq-uc.a.run.app/song/artist-title/search";
            } else if (this.artist != "") {
                requestUrl =
                    "https://parrot-api-n2zzz72gsq-uc.a.run.app/song/artist/search";
            } else if (this.title != "") {
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
        },
        getTrending: function() {
            axios
                .get(
                    "https://parrot-api-n2zzz72gsq-uc.a.run.app/trending/list",
                    {
                        params: { limit: 16, offset: 0 }
                    }
                )
                .then(response => {
                    if (response.data.data) {
                        this.trendingList = response.data.data.trending;
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
        getRecommended: function() {
            axios
                .get(
                    "https://parrot-api-n2zzz72gsq-uc.a.run.app/recommended/list",
                    {
                        params: {}
                    }
                )
                .then(response => {
                    if (response.data.data) {
                        this.recommendedList = response.data.data.recommended;
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
        }
    }
};
</script>

<style scoped>
h1 {
    margin: 24px auto;
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

.extra-link {
    font-weight: 600;
    font-size: 14px;
}

.subtitle :hover {
    opacity: 0.6;
}

.search-form {
    margin: auto;
    max-width: 1000px;
    text-align: left;
    padding: 0 0.75rem;
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

.trending-box {
    margin-bottom: 16px;
}

.card-image :hover {
    opacity: 0.8;
}
</style>
