<template>
    <div class="main-page">
        <Layout>
            <Header>
                <!--菜单-->
                <end-blog-menu></end-blog-menu>
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

</template>

<script>
    import EndBlogMenu from '../components/end/EndBlogMenu.vue';
    import BlogFooter from '../components/main/BlogFooter';

    import message from '../utils/message';

    export default {
        name: 'end',

        components: {
            EndBlogMenu,
            BlogFooter,
        },

        mounted() {
            this.init();
        },

        methods: {
            init() {
                let d = {
                    mode: 'end',
                };
                this.$api.index(d)
                    .then(res => {
                        if (!(res.data['website_manage'] instanceof Array)) {
                            this.$store.commit('website/commitInit', res.data['website_manage']);
                        } else {
                            this.$Message.warning('网站未进行初始化设置');
                        }
                        this.$store.commit('auth/commitInit', res.data['user']);
                        this.$store.commit('count/commitInit', res.data['count_data']);
                    })
                    .catch(error => {
                        message.dealReturnMessage(error.msg, this, 'warning');
                    });
            },
        },
    };
</script>

<style scoped>
    .main-page {
        background-color: rgb(245, 245, 245);
    }

    .main-content {
        width: 100%;
        /*margin: 1% auto;*/
    }

</style>
