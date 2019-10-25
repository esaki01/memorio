<template>
  <div class="lyric">
    <div class="columns contents">
      <div class="column is-one-quarters">
        <img :src="$route.params.image_url" alt="Image" />
        <p class="song">{{ $route.params.song }}</p>
        <p class="artist">{{ $route.params.artist }}</p>
      </div>
      <div class="column is-three-quarters">
        <p>{{ $route.params.lyric }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: function() {
    return {

    };
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
