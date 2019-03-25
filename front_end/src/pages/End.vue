<template>
    <div class="main-page">
        <layout>
            <header>
                <!--菜单-->
                <end-blog-menu></end-blog-menu>
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

</template>

<script>
    import EndBlogMenu from '../components/end/EndBlogMenu.vue';
    import BlogFooter from '../components/main/BlogFooter';

    export default {
        name: 'end',
        components: {
            EndBlogMenu,
            BlogFooter,
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
