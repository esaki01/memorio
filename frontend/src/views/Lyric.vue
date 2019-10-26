<template>
  <div class="lyric">
    <div class="columns contents">
      <div class="column is-one-quarters">
        <img :src="$route.params.image_url" alt="Image" />
        <p class="song">{{ $route.params.song }}</p>
        <p class="artist">{{ $route.params.artist }}</p>
      </div>
      <div class="column is-three-quarters">
        <table class="table is-striped is-fullwidth">
          <div v-for="i in 10" :key="i.id">
            <tbody>
              <tr>
                <td v-for="l in 10" :key="l.id">
                  <span class="title is-6">{{ lyrics[l - 1 + (i - 1) * 10] }}</span>
                </td>
              </tr>
              <tr>
                <td v-for="p in 10" :key="p.id">
                  <span class="subtitle is-6">{{ pronunciations[p - 1 + (i - 1) * 10] }}</span>
                </td>
              </tr>
            </tbody>
          </div>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: function() {
    return {
      lyrics: [],
      pronunciations: []
    };
  },
  created: function() {
    this.get_pronunciation(this.$route.params.lyric);
    this.lyrics = this.$route.params.lyric.split(/\s+/);
  },
  methods: {
    get_pronunciation: function(k) {
      axios
        .get(
          "https://backend-n2zzz72gsq-uc.a.run.app/word/pronunciation/search",
          {
            params: { keyword: k }
          }
        )
        .then(response => {
          if (response.data.data) {
            this.pronunciations = response.data.data.phonetic_symbols;
          } else {
            console.log("Not data.");
          }
        })
        .catch(error => {
          console.log(error);
        })
        .finally(() => {});
    }
  }
};
</script>

<style scoped>
.contents {
  max-width: 1000px;
  margin: 36px auto 0 auto;
}

.song {
  text-align: center;
  font-size: 18px;
  font-weight: bolder;
  margin: 5px 0;
}

.artist {
  text-align: center;
  font-size: 16px;
  font-weight: 500;
}
</style>
