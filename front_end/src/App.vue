<template>
    <div id="app">
        <router-view></router-view>
    </div>
</template>

<script>
    import { mapState } from 'vuex';

    export default {
        name: 'app',
        methods: {

        },
        computed: {
            ...mapState('website', {
                websiteName: state => state.websiteName,
            }),
        },
        watch: {
            websiteName(value) {
                // 动态修改网页标题
                document.title = value;
            }
        }
    }

</script>

<style>
    html, body {
        height: 100%;
    }

    #app {
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        height: 100%;
    }
</style>
