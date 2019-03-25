<template>
    <div class="main-div">
        <div class="child-div child-border-div">
            <div class="child-input-div">
                <Button type="success" long @click="submit" size="large">提交</Button>
            </div>
            <span class="title-span">个人简介</span>
            <Input v-model="aboutMe" placeholder="请输入正文内容..." type="textarea" :autosize="{ minRows: 10, maxRows: 100 }"
                   size="large"/>
        </div>
        <div class="child-div markdown-div" v-html="compiledMarkdown"></div>
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
                return Markdown(this.aboutMe)
            },
        },
    }
</script>

<style scoped>
    .main-div {
        width: 100%;
        min-height: 100px;
    }

    .child-div {
        margin: 1%;
        width: 45%;
        float: left;
        text-align: left;
        min-height: 1000px;
    }

    .title-span {
        font-size: 20px;
    }

    .child-border-div {
        border: 1px #c8c8c8;
        border-right-style: solid;
        padding-right: 10px;
        margin-right: 10px;
    }

    .child-input-div {
        margin: 20px 0;
    }
</style>
