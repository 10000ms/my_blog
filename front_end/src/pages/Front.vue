<template>
    <div class="basic-pages-div">
        <!--边栏-->
        <side-bar></side-bar>

        <div class="right-main-div">
            <layout>
                <header>
                    <!--菜单-->
                    <blog-menu></blog-menu>
                </header>

                <content class="main-content">
                    <!--主要页面-->
                    <router-view/>
                </content>

                <footer>
                    <blog-footer></blog-footer>
                </footer>
            </layout>
        </div>

        <!--返回顶部-->
        <BackTop :height="50" :bottom="100" :right="15">
            <Icon type="ios-arrow-dropup-circle" size="60" color="rgba(246, 141, 66, 1)"/>
        </BackTop>
    </div>
</template>

<script>
    import SideBar from '../components/main/SideBar';
    import BlogMenu from '../components/main/BlogMenu';
    import BlogFooter from '../components/main/BlogFooter';

    export default {
        name: 'app',
        components: {
            BlogMenu,
            SideBar,
            BlogFooter,
        },
        mounted() {
            this.init()
        },

        methods: {
            init() {
                let d = {
                    mode: 'front',
                };
                this.$api.index(d)
                    .then(res => {
                        this.$store.commit('website/commitInit', res.data['website_manage']);
                        this.$store.commit('auth/commitInit', res.data['user']);
                        this.$store.commit('blog/commitBlog', res.data['blog']);
                        this.$store.commit('blog/commitBlogRecommend', res.data['blog_recommend']);
                    });
            },
        },
    };
</script>

<style scoped>

</style>
