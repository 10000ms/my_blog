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
                AboutMe: '',
            };
        },

        computed: {
            compiledMarkdown: function () {
                return Markdown(this.AboutMe);
            },
        },
    }
</script>

<style scoped>

</style>
