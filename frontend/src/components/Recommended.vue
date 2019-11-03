<template>
    <div class="recommended">
        <h2>Recommended</h2>
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
                                <content-loader v-if="contentsShow" :width="400" :height="100">
                                    <rect x="0" y="0" rx="0" ry="0" width="400" height="100" />
                                </content-loader>
                                <div v-else>
                                    <p class="title is-6">{{ rl.artist }}</p>
                                    <p class="subtitle is-8">
                                        <a
                                            :href="rl.external_url"
                                            target="_blank"
                                            class="external-link has-text-danger"
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
            recommendedList: ["", "", "", "", "", "", "", ""]
        };
    },
    mounted: function() {
        this.getRecommended();
    },
    methods: {
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
h2 {
    margin: 24px auto;
    color: #333333;
    font-size: 24px;
    font-weight: bolder;
    text-align: left;
    font-family: "Oswald", sans-serif;
}

.external-link {
    font-weight: 600;
    font-size: 14px;
}

.subtitle :hover {
    opacity: 0.6;
}

.card-image :hover {
    opacity: 0.8;
}

.over-text {
    overflow: hidden;
    white-space: nowrap;
}
</style>
