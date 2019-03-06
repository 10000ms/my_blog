<template>
  <div class="markdown-div" v-html="compiledMarkdown"></div>
</template>

<script>
    import marked from 'marked'

    export default {
        name: 'Blog',
        data() {
            return {
                input: '# hello',
            }
        },
        computed: {
            compiledMarkdown: function () {
                return marked(this.input, { sanitize: true })
            }
        },
    }
</script>

<style scoped>
  .markdown-div {
    width: 80%;
    margin: 5% auto;
  }

</style>
