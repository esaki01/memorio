<template>
    <div class="trending">
        <h2>Trending</h2>
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
            contentsShow: true,
            trendingList: []
        };
    },
    mounted: function() {
        this.getTrending();
    },
    methods: {
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
        }
    }
};
</script>

<style scoped>
h2 {
    margin: 24px auto;
    color: #333333;
    font-size: 24px;
    font-weight: bolder;
    text-align: left;
    font-family: "Oswald", sans-serif;
}
</style>
