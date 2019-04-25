<template>
    <div class="thin-content-div text-align-left-div">
        <div class="category-div" v-for="c in categories" :key="c.id">
            <a :href="c.url" class="color-common-black-items">
                <span v-html="printLevel(getLevel(c.id))" class="count-span"></span>
                {{c.name}}
                <span class="count-span">({{c.count}})</span>
            </a>
        </div>
    </div>
</template>

<script>
    import categoryUtils from '../../utils/category';

    export default {
        name: 'Categories',

        data() {
            return {
                // TODO：排序在服务端做
                categories: [
                    {
                        id: 1,
                        name: '111',
                        fid: 0,
                        url: 'asdasd',
                        count: 5,
                    },
                    {
                        id: 2,
                        name: '112',
                        fid: 1,
                        url: 'asdasd',
                        count: 5,
                    },
                    {
                        id: 3,
                        name: '113',
                        fid: 1,
                        url: 'asdasd',
                        count: 5,
                    },
                    {
                        id: 4,
                        name: '131',
                        fid: 3,
                        url: 'asdasd',
                        count: 5,
                    },
                    {
                        id: 5,
                        name: '222',
                        fid: 0,
                        url: 'asdasd',
                        count: 5,
                    },
                    {
                        id: 6,
                        name: '333',
                        fid: 0,
                        url: 'asdasd',
                        count: 5,
                    },
                    {
                        id: 7,
                        name: '444',
                        fid: 0,
                        url: 'asdasd',
                        count: 5,
                    },
                    {
                        id: 8,
                        name: '555',
                        fid: 0,
                        url: 'asdasd',
                        count: 5,
                    },
                ],
            };
        },

        mounted() {

        },

        methods: {
            getLevel(categoryId) {
                return categoryUtils.categoryGetLevel(categoryId, this.categories);
            },
            printLevel(level) {
                return categoryUtils.categoryPrintLevel(level);
            },
        },

        computed: {

        },

    }
</script>

<style scoped>

</style>
