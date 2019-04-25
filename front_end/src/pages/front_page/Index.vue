<template>
    <div>
        <single-blog-tab v-for="b in blogs" :blogData="b" :key="b.id"></single-blog-tab>
        <Page
                :total="indexPage['count']"
                :current="currentPage"
                @on-change="changePage"
                v-if="indexPage['count'] > 10"
                show-elevator
                show-total
        />
    </div>
</template>

<script>
    import { mapState } from 'vuex';
    import scroll from '../../utils/scroll';
    import SingleBlogTab from '../../components/front/SingleBlogTab';

    export default {
        name: 'index',

        components: {
            SingleBlogTab,
        },

        data() {
            return {
                currentPage: 1,

            };
        },

        methods: {
            changePage(page) {
                this.$api.blogs({page: page})
                    .then(res => {
                        this.$store.commit('blog/commitBlog', res.data);
                        // 跳转页面顶部
                        scroll.toTop();
                    });
            },
        },

        computed: {
            ...mapState('blog', {
                blogs: state => state.blog,
                indexPage: state => state.indexPage,
            }),
        },
    }
</script>

<style scoped>

</style>
