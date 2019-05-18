<template>
    <div class="markdown-div thin-content-div" v-html="compiledMarkdown"></div>
</template>

<script>
    import '../../assets/css/marked.less';
    import 'highlight.js/styles/xcode.css';
    import { Markdown } from '../../utils/markdown.js';

    import message from '../../utils/message';

    export default {
        name: 'AboutMe',

        data() {
            return {
                aboutMe: '空',
            };
        },

        mounted() {
            this.init()
        },

        methods: {
            init() {
                this.$Loading.start();
                this.$api.aboutMe()
                    .then(res => {
                        this.aboutMe = res.data.about_me;
                        this.$Loading.finish();
                    })
                    .catch(error => {
                        this.$Loading.error();
                        message.dealReturnMessage(error.msg, this, 'warning');
                    });
            },
        },

        computed: {
            compiledMarkdown: function () {
                return Markdown(this.aboutMe);
            },
        },
    }
</script>

<style scoped>

</style>
