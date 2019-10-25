<template>
  <div class="home">
    <progress class="progress is-small is-primary" max="100" v-if="progressShow">15%</progress>
    <div style="height: 12px;" v-else></div>
    <div class="search-form container">
      <h1>Search Lyrics</h1>
      <div class="field is-horizontal is-hidden-tablet">
        <div class="field-body">
          <div class="field has-addons" v-if="selected === 'Artist Search'">
            <p class="control is-expanded has-icons-left">
              <input
                class="input"
                type="text"
                placeholder="Artist (e.g. The Beatles)"
                v-model="artist"
              />
              <span class="icon is-small is-left">
                <i class="fa fa-user-circle"></i>
              </span>
            </p>
          </div>
          <div class="field has-addons" v-if="selected === 'Song Search'">
            <p class="control is-expanded has-icons-left">
              <input class="input" type="email" placeholder="Song (e.g. Let It Be)" v-model="song" />
              <span class="icon is-small is-left">
                <i class="fa fa-music"></i>
              </span>
            </p>
          </div>
          <div class="field has-addons" v-if="selected === 'Artist & Song Search'">
            <p class="control is-expanded has-icons-left">
              <input
                class="input"
                type="text"
                placeholder="Artist (e.g. The Beatles)"
                v-model="artist"
              />
              <span class="icon is-small is-left">
                <i class="fa fa-user-circle"></i>
              </span>
            </p>
            <p class="control is-expanded has-icons-left">
              <input class="input" type="email" placeholder="Song (e.g. Let It Be)" v-model="song" />
              <span class="icon is-small is-left">
                <i class="fa fa-music"></i>
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
              <a class="button is-primary" @click="search">
                <span class="fa fa-search has-text-white"></span>
              </a>
            </p>
          </div>
        </div>
      </div>

      <div class="field is-horizontal is-hidden-mobile">
        <div class="field-body">
          <div class="field has-addons">
            <p class="control is-expanded has-icons-left" v-if="selected === 'Artist Search'">
              <input
                class="input"
                type="text"
                placeholder="Artist (e.g. The Beatles)"
                v-model="artist"
              />
              <span class="icon is-small is-left">
                <i class="fa fa-user-circle"></i>
              </span>
            </p>
            <p class="control is-expanded has-icons-left" v-if="selected === 'Song Search'">
              <input class="input" type="email" placeholder="Song (e.g. Let It Be)" v-model="song" />
              <span class="icon is-small is-left">
                <i class="fa fa-music"></i>
              </span>
            </p>

            <p
              class="control is-expanded has-icons-left"
              v-if="selected === 'Artist & Song Search'"
            >
              <input
                class="input"
                type="text"
                placeholder="Artist (e.g. The Beatles)"
                v-model="artist"
              />
              <span class="icon is-small is-left">
                <i class="fa fa-user-circle"></i>
              </span>
            </p>
            <p
              class="control is-expanded has-icons-left"
              v-if="selected === 'Artist & Song Search'"
            >
              <input class="input" type="email" placeholder="Song (e.g. Let It Be)" v-model="song" />
              <span class="icon is-small is-left">
                <i class="fa fa-music"></i>
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
              <a class="button is-primary" @click="search">
                <span class="fa fa-search has-text-white"></span>
              </a>
            </p>
          </div>
        </div>
      </div>

      <div class="search-result" v-if="searchResultShow">
        <h2>Search Results</h2>
        <div class="box">
          <article class="media">
            <div class="media-left">
              <figure class="image is-128x128">
                <img :src="src" alt="Image" />
              </figure>
            </div>
            <div class="media-content">
              <p class="title is-6">
                {{ data.title }}
                / {{ data.artist }}
              </p>
              <div class="content">
                <p class="ellipsis">{{ data.lyrics }}</p>
              </div>
              <nav class="level is-mobile">
                <div class="level-left">
                  <a class="level-item" aria-label="reply">
                    <span class="icon is-small">
                      <i class="fa fa-reply" aria-hidden="true"></i>
                    </span>
                  </a>
                  <a class="level-item" aria-label="retweet">
                    <span class="icon is-small">
                      <i class="fa fa-retweet" aria-hidden="true"></i>
                    </span>
                  </a>
                  <a class="level-item" aria-label="like">
                    <span class="icon is-small">
                      <i class="fa fa-heart" aria-hidden="true"></i>
                    </span>
                  </a>
                </div>
              </nav>
            </div>
          </article>
        </div>
      </div>

      <h2>Trending</h2>
      <div class="trending-box">
        <content-loader v-bind:width="400" v-bind:height="22" v-if="contentsShow">
          <rect x="0" y="0" rx="3" ry="3" width="400" height="10" />
          <rect x="0" y="12" rx="3" ry="3" width="400" height="10" />
        </content-loader>
        <div class="tags" v-else>
          <span class="tag" v-for="tl in trendingList" :key="tl">
            <span>{{ tl }}</span>
          </span>
        </div>
      </div>
      <h2>Recommended</h2>
      <div class="recommended-box">
        <div class="columns is-multiline is-mobile">
          <div
            class="column is-one-quarter-tablet is-half-mobile"
            v-for="rl in recommendedList"
            :key="rl.artist"
          >
            <div class="card">
              <div class="card-image">
                <content-loader v-bind:width="400" v-bind:height="400" v-if="contentsShow">
                  <rect x="0" y="0" rx="0" ry="0" width="400" height="400" />
                </content-loader>
                <figure class="image is-1by1" v-else>
                  <img :src="rl.image_url" alt="Image" />
                </figure>
              </div>
              <div class="card-content">
                <div class="media">
                  <div class="media-content over-text">
                    <content-loader v-bind:width="400" v-bind:height="100" v-if="contentsShow">
                      <rect x="0" y="0" rx="0" ry="0" width="400" height="100" />
                    </content-loader>
                    <div v-else>
                      <p class="title is-6">{{ rl.artist }}</p>
                      <p class="subtitle is-8">
                        <a :href="rl.lyrics" target="”_blank”" class="extra-link">{{ rl.title }}</a>
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
      song: "",
      data: {},
      src: "",
      searchResultShow: false,
      progressShow: false,
      contentsShow: true,
      trendingList: [],
      recommendedList: ["", "", "", "", "", "", "", ""],
      selected: "Artist & Song Search"
    };
  },
  methods: {
    search: function() {
      if (this.artist != "" && this.song != "") {
        this.progressShow = true;
      }

      axios
        .get("https://backend-n2zzz72gsq-uc.a.run.app/genius/search", {
          params: { artist: this.artist, song: this.song }
        })
        .then(response => {
          if (response.data.data) {
            this.data = response.data.data;
            this.src = this.data.image_url;
            this.searchResultShow = true;
          } else {
            console.log("Not data.");
          }
        })
        .catch(error => {
          console.log(error);
        })
        .finally(() => (this.progressShow = false));
    },
    getTrending: function() {
      axios
        .get("https://backend-n2zzz72gsq-uc.a.run.app/genius/new_releases", {
          params: { limit: 16, offset: 0 }
        })
        .then(response => {
          if (response.data.data) {
            this.trendingList = response.data.data;
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
        .get("https://backend-n2zzz72gsq-uc.a.run.app/genius/recommended", {
          params: {}
        })
        .then(response => {
          if (response.data.data) {
            this.recommendedList = response.data.data;
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
  },
  created: function() {
    this.getTrending();
    this.getRecommended();
  }
};
</script>>

<style scoped>
h1 {
  margin: 24px auto;
  color: #f14667;
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
  color: #f14667;
}

.extra-link:hover {
  opacity: 0.8;
}

.search-form {
  margin: auto;
  max-width: 1000px;
  text-align: left;
  padding: 0 0.75rem;
}

.fa-search {
  color: #fa4667;
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
</style>>
