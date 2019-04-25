<template>
    <div class="max-width text-align-left-div">
        <div class="child-div height-min-height-div child-border-div">
            <div class="child-input-div">
                <Button type="success" long @click="submit" size="large">提交</Button>
            </div>
            <span class="content-title-items">个人简介</span>
            <Input v-model="aboutMe" placeholder="请输入正文内容..." type="textarea" :autosize="{ minRows: 10, maxRows: 100 }"
                   size="large"/>
        </div>
        <div class="child-div height-min-height-div markdown-div" v-html="compiledMarkdown"></div>
    </div>
</template>

<script>
    import '../../assets/css/marked.less';
    import 'highlight.js/styles/xcode.css';
    import {Markdown} from '../../utils/markdown.js';

    export default {
        name: 'EndAboutMe',

        data() {
            return {
                aboutMe: '',
            }
        },

        methods: {
            submit() {

            },
        },

        computed: {
            compiledMarkdown() {
                return Markdown(this.aboutMe);
            },
        },
    }
</script>

<style scoped>

</style>
