<template>
    <div>
        <single-blog-tab v-for="b in blogs" :blogData="b" :key="b.id"></single-blog-tab>
        <Page
                :total="blogCount"
                :current="currentPage"
                @on-change="changePage"
                v-if="blogCount > 10"
                show-elevator
                show-total
        />
    </div>
</template>

<script>
    import SingleBlogTab from '../../components/front/SingleBlogTab';

    export default {
        name: 'searchMode',

        components: {
            SingleBlogTab,
        },

        data() {
            return {
                currentPage: 1,
                blogs: [],
                blogsPage: [],
                mode: '',
                query: '',
            };
        },

        mounted() {
            this.init()
        },

        methods: {
            init() {
                this.mode = this.$route.params.mode;
                this.query = this.$route.params.query;
                let queryDict = {
                    query: this.query,
                };
                this.$api[this.mode](queryDict)
                    .then(res => {
                        this.blogs = res.data;
                        this.blogsPage = res.page;
                        this.$Loading.finish();
                    });

            },
            changePage(page) {
                this.$Loading.start();
                this.blogs = [];
                let queryDict = {
                    page: page,
                    query: this.query,
                };
                this.$api[this.mode](queryDict)
                    .then(res => {
                        this.blogs = res.data;
                        this.blogsPage = res.page;
                        this.$Loading.finish();
                    });
            },
        },

        computed: {
            blogCount() {
                if (this.blogsPage.length > 0) {
                    return this.blogsPage['count'];
                } else {
                    return 0;
                }
            },
        },
    }
</script>

<style scoped>

</style>