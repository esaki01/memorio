<template>
    <div id="app">
        <NavBar />
        <main>
            <router-view />
        </main>
        <Footer />
    </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";

export default {
    components: {
        NavBar,
        Footer
    }
};
</script>

<style>
#app {
    font-family: "Roboto", sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    display: flex;
    min-height: 100vh;
    flex-direction: column;
    background-color: #ffffff;
}

main {
    flex: 1;
}
</style>
