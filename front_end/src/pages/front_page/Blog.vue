<template>
<!--    TODO: 重新设计这个页面款式，切换页面时自动跳转顶部   -->
    <div class="markdown-div" v-html="compiledMarkdown"></div>
</template>

<script>
    import '../../assets/css/marked.less';
    import 'highlight.js/styles/xcode.css';
    import { Markdown } from '../../utils/markdown.js';

    export default {
        name: 'Blog',

        data() {
            return {
                blog: '',
            };
        },

        mounted() {
            this.init();
        },

        methods: {
            init() {
                this.$api.blog(this.$route.params.id)
                    .then(res => {
                        this.blog = res.data['content'];
                    });
            },
        },

        computed: {
            compiledMarkdown: function () {
                return Markdown(this.blog);
            },
        },
    }
</script>

<style scoped>
    .markdown-div {
        width: 80%;
        margin: 5% auto;
    }
</style>
