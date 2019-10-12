<template>
  <div class="home">
    <div class="card">
      <header class="card-header">
        <div class="field has-addons search-form">
          <div class="control">
            <input class="input" type="text" placeholder="Find a word" v-model="keyword" />
          </div>
          <div class="control">
            <a class="button" @click="search">Search</a>
          </div>
        </div>
      </header>
      <div class="card-content">
        <div class="content">
          <p>word: {{ wordDefinition.word }}</p>
          <p>meaning: {{ wordDefinition.meaning }}</p>
          <p>phonetic symbol: {{ wordDefinition.phonetic_symbol }}</p>
          <audio :src="wordDefinition.audio_url" v-if="audioControl" controls></audio>
        </div>
      </div>
      <footer class="card-footer">
        <a href="#" class="card-footer-item">Save</a>
        <a href="#" class="card-footer-item">Edit</a>
        <a href="#" class="card-footer-item">Delete</a>
      </footer>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: function() {
    return {
      keyword: "",
      wordDefinition: {},
      audioControl: false
    };
  },
  methods: {
    search: function() {
      axios
        .get("https://backend-o5x5u66yaq-uc.a.run.app/weblio/search", {
          params: { keyword: this.keyword }
        })
        .then(response => {
          if (response.data.data) {
            this.wordDefinition = response.data.data;
            this.audioControl = true;
          } else {
            this.wordDefinition = {};
            this.audioControl = false;
          }
        });
    }
  }
};
</script>>

<style scoped>
.card {
  max-width: 600px;
  margin: 50px auto 0 auto;
}

.search-form {
  margin: 0 auto;
  padding: 30px;
}

.content {
  text-align: left;
}
</style>>
