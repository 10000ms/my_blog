<template>
    <div class="markdown-div thin-content-div" v-html="compiledMarkdown"></div>
</template>

<script>
    import '../../assets/css/marked.less';
    import 'highlight.js/styles/xcode.css';
    import { Markdown } from '../../utils/markdown.js';

    export default {
        name: 'AboutMe',

        data() {
            return {
                aboutMe: '',
            };
        },

        mounted() {
            this.init()
        },

        methods: {
            init() {
                this.$api.aboutMe()
                    .then(res => {
                        this.aboutMe = res.data['about_me'];
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
