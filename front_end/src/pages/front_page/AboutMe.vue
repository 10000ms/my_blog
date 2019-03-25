<template>
    <div class="markdown-div thin-content-div" v-html="compiledMarkdown"></div>
</template>

<script>
    import '../../assets/css/marked.less';
    import 'highlight.js/styles/xcode.css';
    import {Markdown} from '../../utils/markdown.js';

    export default {
        name: 'AboutMe',
        data() {
            return {
                input: '# hello',
            }
        },
        computed: {
            compiledMarkdown: function () {
                return Markdown(this.input);
            },
        },
    }
</script>

<style scoped>

</style>
