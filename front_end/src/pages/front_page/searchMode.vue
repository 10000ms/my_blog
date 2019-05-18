<template>
    <div>
        <span class="content-title-items" v-show="isEmpty">没有对应查询结果</span>
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
    import message from '../../utils/message';

    export default {
        name: 'searchMode',

        components: {
            SingleBlogTab,
        },

        data() {
            return {
                currentPage: 1,
                blogs: [],
                blogsPage: {},
                mode: this.$route.params.mode,
                query: this.$route.params.query,
                isEmpty: false,
            };
        },

        mounted() {
            this.init()
        },

        methods: {
            init() {
                this.dataFromServer();
            },

            changePage(page) {
                this.dataFromServer(page);
            },

            dataFromServer(page=null) {
                let queryDict = {
                    query: this.query,
                };
                if (page) {
                    queryDict.page = page
                }
                this.$Loading.start();
                this.$api[this.mode](queryDict)
                    .then(res => {
                        this.blogs = res.data;
                        this.blogsPage = res.page;
                        this.$Loading.finish();
                        if (this.blogs.length === 0) {
                            // 没有结果返回显示空
                            this.isEmpty = true;
                        }
                    })
                    .catch(error => {
                        this.$Loading.error();
                        message.dealReturnMessage(error.msg, this, 'warning');
                    });
            },
        },

        computed: {
            blogCount() {
                if ('count' in this.blogsPage) {
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