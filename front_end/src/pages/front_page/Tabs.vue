<template>
    <div>
        <span class="content-title-items">目前共计{{tabCount}}个标签</span>
        <div class="text-align-center-div">
            <tab-tabs v-for="t in tabs" :key="t.id" :tab="t.name" :count="t.count" :url="t.url"></tab-tabs>
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
                tabs: [
                    {
                        id: 1,
                        name: 'asdasd',
                        count: 100,
                        url: 'asd',
                    },
                    {
                        id: 2,
                        name: 'qwer',
                        count: 1,
                        url: 'asd',
                    },
                    {
                        id: 3,
                        name: 'reqwer',
                        count: 5,
                        url: 'asd',
                    },
                    {
                        id: 4,
                        name: 'asdasd',
                        count: 20,
                        url: 'asd',
                    },
                    {
                        id: 5,
                        name: 'fdgfsafda',
                        count: 7,
                        url: 'asd',
                    },
                    {
                        id: 6,
                        name: '111111111',
                        count: 10,
                        url: 'asd',
                    },
                    {
                        id: 7,
                        name: '2222222222',
                        count: 8,
                        url: 'asd',
                    },
                    {
                        id: 8,
                        name: '33333333',
                        count: 35,
                        url: 'asd',
                    },
                    {
                        id: 9,
                        name: '44444444444',
                        count: 20,
                        url: 'asd',
                    },
                ],
            };
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
