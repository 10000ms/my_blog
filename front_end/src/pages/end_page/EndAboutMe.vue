<template>
    <div class="max-width text-align-left-div">
        <div class="child-div height-min-height-div child-border-div">
            <div class="child-input-div">
                <Button type="success" long @click="submit" size="large">提交</Button>
            </div>
            <span class="content-title-items">个人简介</span>
            <i-input v-model="aboutMe" placeholder="请输入正文内容..." type="textarea" :autosize="{ minRows: 10, maxRows: 100 }"
                   size="large"/>
        </div>
        <div class="child-div height-min-height-div markdown-div" v-html="compiledMarkdown"></div>
    </div>
</template>

<script>
    import '../../assets/css/marked.less';
    import 'highlight.js/styles/xcode.css';
    import { Markdown } from '../../utils/markdown.js';

    import message from '../../utils/message';

    export default {
        name: 'EndAboutMe',

        data() {
            return {
                id: null,
                aboutMe: '',
            }
        },

        mounted() {
            this.init();
        },

        methods: {
            init() {
                this.$Loading.start();
                this.$api.aboutMe()
                    .then(res => {
                        this.aboutMe = res.data.about_me;
                        this.id = res.data.id;
                        this.$Loading.finish();
                    })
                    .catch(error => {
                        message.dealReturnMessage(error.msg, this, 'warning');
                    });
            },

            submit() {
                let p = {
                    about_me: this.aboutMe,
                };
                this.$api.changeAboutMe(this.id, p)
                    .then(() => {
                        this.$Message.info('修改成功');
                        this.$Loading.finish();
                    })
                    .catch(error => {
                        message.dealReturnMessage(error.msg, this, 'warning');
                    });
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
