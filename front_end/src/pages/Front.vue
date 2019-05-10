<template>
    <div class="basic-pages-div">
        <!--边栏-->
        <side-bar></side-bar>

        <div class="right-main-div">
            <Layout>
                <Header>
                    <!--菜单-->
                    <blog-menu></blog-menu>
                </Header>

                <Content class="main-content">
                    <!--主要页面-->
                    <router-view/>
                </Content>

                <Footer>
                    <blog-footer></blog-footer>
                </Footer>
            </Layout>
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

    import message from '../utils/message';

    export default {
        name: 'app',

        components: {
            BlogMenu,
            SideBar,
            BlogFooter,
        },

        mounted() {
            this.init();
        },

        methods: {
            init() {
                let d = {
                    mode: 'front',
                };
                this.$api.index(d)
                    .then(res => {
                        if (!(res.data['website_manage'] instanceof Array)) {
                            this.$store.commit('website/commitInit', res.data['website_manage']);
                        } else {
                            this.$Message.warning('网站未进行初始化设置');
                        }
                        this.$store.commit('auth/commitInit', res.data['user']);
                        this.$store.commit('blog/commitBlog', res.data['blog']);
                        this.$store.commit('blog/commitBlogRecommend', res.data['blog_recommend']);
                        this.$store.commit('blog/commitIndexPage', res.data['page']);
                    })
                    .catch(error => {
                        message.dealReturnMessage(error.msg, this, 'warning');
                    });
            },
        },
    };
</script>

<style scoped>

</style>
