<template>
  <div class="vocabulary">
    <progress class="progress is-small is-primary" max="100" v-if="progressShow">15%</progress>
    <div style="height: 12px;" v-else></div>
    <div class="field has-addons search-form">
      <div class="control">
        <input class="input" type="text" placeholder="Find a word" v-model="keyword" />
      </div>
      <div class="control">
        <a class="button" @click="search">
          <span class="icon">
            <i class="fa fa-search"></i>
          </span>
        </a>
      </div>
    </div>
    <div class="card" v-if="hasWordDefinition">
      <div class="card-content">
        <div class="content">
          <p>
            <span class="word">{{ wordDefinition.word }}</span>
            {{ wordDefinition.phonetic_symbol }}
          </p>
          <p class="tag is-success">meaning</p>
          <p>{{ wordDefinition.meaning }}</p>
          <audio :src="wordDefinition.audio_url" controls></audio>
        </div>
      </div>
      <footer class="card-footer">
        <a href="#" class="card-footer-item">Register</a>
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
      hasWordDefinition: false,
      progressShow: false
    };
  },
  methods: {
    search: function() {
      if (this.keyword) {
        this.progressShow = true;
      }
      
      axios
        .get("https://backend-n2zzz72gsq-uc.a.run.app/weblio/search", {
          params: { keyword: this.keyword }
        })
        .then(response => {
          if (response.data.data) {
            this.wordDefinition = response.data.data;

            if (this.wordDefinition.phonetic_symbol) {
              this.wordDefinition.phonetic_symbol = "[" + this.wordDefinition.phonetic_symbol + "]"
            }
            this.wordDefinition.phonetic_symbol
            
            this.hasWordDefinition = true;
            this.progressShow = false;
          } else {
            this.wordDefinition = {};
            this.hasWordDefinition = false;
            this.progressShow = false;
          }
        })
        .catch(error => {
          this.wordDefinition = {};
          this.hasWordDefinition = false;
          this.progressShow = false;
          console.log(error)
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
  margin: 48px auto 0 auto;
  max-width: 300px;
}

.content {
  text-align: left;
}

.word {
  font-size: 24px;
  font-weight: bolder;
}

.meaning {
  padding: 3px 6px;
  display: inline-block;
  border-radius: 30px;
  background-color: #1b951b;
  color: #ffffff;
  font-weight: bolder;
}

audio {
  height: 42px;
}

.tag {
  font-size: 14px;
  font-weight: bolder;
}

.card-footer:hover {
  transform: translateY(-1px);
  box-shadow: 0 1px 1px rgba(50, 50, 93, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
  opacity: 0.7;
}

.card-footer:active {
  transform: translateY(1px);
  box-shadow: none;
}

a {
  color: #333333;
}
</style>>
