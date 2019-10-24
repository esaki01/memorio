<template>
  <div class="home">
    <progress class="progress is-small is-primary" max="100" v-if="progressShow">15%</progress>
    <div style="height: 12px;" v-else></div>

    <div class="search-form container">
      <h1>Search</h1>
      <div class="field is-horizontal">
        <div class="field-body">
          <div class="field">
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
          <div class="field">
            <p class="control is-expanded has-icons-left has-icons-right">
              <input class="input" type="email" placeholder="Song (e.g. Let It Be)" v-model="song" />
              <span class="icon is-small is-left">
                <i class="fa fa-music"></i>
              </span>
            </p>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-primary" @click="search">Search lyrics</button>
            </div>
          </div>
        </div>
      </div>

      <div class="search-result" v-if="searchResultShow">
        <h2>Search Results</h2>
        <div class="box">
          <article class="media">
            <div class="media-left">
              <figure class="image is-64x64">
                <img :src="src" alt="Image" />
              </figure>
            </div>
            <div class="media-content">
              <div class="content">
                <p class="ellipsis">
                  <strong>{{ data.title }}</strong>
                  / {{ data.artist }}
                  <br />
                  {{ data.lyrics }}
                </p>
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
        <div class="tags">
          <span class="tag" v-for="l in list" :key="l">{{ l }}</span>
        </div>
      </div>
      <h2>Recommended</h2>
      <div class="recommended-box">
        <div class="columns is-multiline">
          <div class="column is-half" v-for="l2 in list2" :key="l2.artist">
            <div class="box">
              <article class="media">
                <div class="media-left">
                  <figure class="image is-64x64">
                    <img :src="l2.image_url" alt="Image" />
                  </figure>
                </div>
                <div class="media-content">
                  <div class="content">
                    <p>
                      <strong>{{ l2.artist }}</strong>
                      <br />
                      <a
                        :href="l2.lyrics"
                        target="”_blank”"
                        class="extra-link has-text-link"
                      >{{ l2.title }}</a>
                    </p>
                  </div>
                </div>
              </article>
            </div>
          </div>
        </div>
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
      song: "",
      data: {},
      src: "",
      searchResultShow: false,
      progressShow: false,
      list: [],
      list2: []
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
    }
  },
  created: function() {
    axios
      .get("https://backend-n2zzz72gsq-uc.a.run.app/genius/new_releases", {
        params: { limit: 16, offset: 0 }
      })
      .then(response => {
        if (response.data.data) {
          this.list = response.data.data;
        } else {
          console.log("Not data.");
        }
      })
      .catch(error => {
        console.log(error);
      });

    axios
      .get("https://backend-n2zzz72gsq-uc.a.run.app/genius/recommended", {
        params: {}
      })
      .then(response => {
        if (response.data.data) {
          this.list2 = response.data.data;
        } else {
          console.log("Not data.");
        }
      })
      .catch(error => {
        console.log(error);
      });
  }
};
</script>>

<style scoped>
h1 {
  margin: 32px auto 8px auto;
  color: #f14667;
  font-size: 24px;
  font-weight: bolder;
  text-align: left;
}

h2 {
  margin: 24px auto;
  color: #333333;
  font-size: 16px;
  font-weight: bolder;
  text-align: left;
}

.extra-link {
  font-weight: 500;
  font-size: 14px;
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

.media-content {
}

.ellipsis {
  position: relative;
  height: 100px;
  line-height: 24px;
  overflow: hidden;
}

.trending-box {
  margin-bottom: 16px;
}
</style>>
