<template>
    <div>
        <span class="content-title-items">目前共计{{tabCount}}个标签</span>
        <div class="text-align-center-div">
            <tab-tabs v-for="t in tabs" :key="t.id" :tab="t.title" :count="t.count" :id="t.id"></tab-tabs>
        </div>
    </div>
</template>

<script>
    import TabTabs from '../../components/front/TabTabs';

    export default {
        name: 'Tabs',

        components: {
            TabTabs,
        },

        data() {
            return {
                tabs: [],
            };
        },

        mounted() {
            this.init();
        },

        methods: {
            init() {
                this.$api.tab()
                    .then(res => {
                        this.tabs = res.data;
                    });
            },
        },

        computed: {
            tabCount() {
                return this.tabs.length;
            },
        },
    }
</script>

<style scoped>

</style>
