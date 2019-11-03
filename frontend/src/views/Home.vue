<template>
    <section class="home section">
        <div class="container">
            <SearchResult />
            <Trending />
            <Recommended />
        </div>
    </section>
</template>

<script>
import SearchResult from "@/components/SearchResult.vue";
import Trending from "@/components/Trending.vue";
import Recommended from "@/components/Recommended.vue";

export default {
    components: {
        SearchResult,
        Trending,
        Recommended
    }
};
</script>

<style scoped>
.home {
    max-width: 1000px;
    margin: auto;
}
</style>
