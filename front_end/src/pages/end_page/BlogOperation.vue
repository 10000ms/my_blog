<template>
    <div class="max-width">
        <div class="child-div child-border-div height-min-height-div">
            <div class="child-input-div">
                <Button type="success" long @click="submit" size="large">提交</Button>
            </div>
            <span class="content-title-items">标题</span>
            <i-input v-model="title" placeholder="请输入标题..." class="child-input-div" size="large"/>
            <span class="content-title-items">作者</span>
            <i-input v-model="author" placeholder="请输入作者..." class="child-input-div" size="large"/>
            <span class="content-title-items">标签</span>
            <div class="child-input-div">
                <i-select v-model="selectTabs" class="max-width" :multiple="true" size="large">
                    <i-option v-for="item in tabs" :value="item.id" :key="item.id">{{ item.title }}</i-option>
                </i-select>
            </div>
            <span class="content-title-items">分类</span>
            <div class="child-input-div">
                <i-select v-model="selectCategories" class="max-width" size="large">
                    <i-option v-for="item in categories" :value="item.id" :key="item.id">{{ item.title }}
                    </i-option>
                </i-select>
            </div>
            <span class="content-title-items">简介</span>
            <i-input v-model="brief" placeholder="请输入简介..." type="textarea" :autosize="{ minRows: 3, maxRows: 10 }"
                     class="child-input-div" size="large"/>
            <div class="child-input-div">
                <span class="content-title-items">是否自动生成简介:  </span>
                <i-switch v-model="autoBrief" @on-change="changeAutoBrief" class="child-input-div">
                    <span slot="open">是</span>
                    <span slot="close">否</span>
                </i-switch>
            </div>
            <span class="content-title-items">正文</span>
            <i-input v-model="content" placeholder="请输入正文内容..." type="textarea"
                     :autosize="{ minRows: 10, maxRows: 100 }"
                     size="large"/>
        </div>
        <div class="child-div markdown-div" v-html="compiledMarkdown"></div>
    </div>
</template>

<script>
    import '../../assets/css/marked.less';
    import 'highlight.js/styles/xcode.css';
    import removeMd from 'remove-markdown';
    import { Markdown } from '../../utils/markdown.js';

    import message from '../../utils/message';

    export default {
        name: 'BlogOperation',

        data() {
            return {
                id: null,
                title: '',
                brief: '',
                content: '',
                author: '',
                autoBrief: true,
                selectTabs: [],
                selectCategories: null,
                tabs: [],
                categories: [],
                mode: 'create',
            };
        },

        mounted() {
            this.init();
        },

        methods: {
            init() {
                this.$api.tab()
                    .then(res => {
                        this.tabs = res.data;
                    })
                    .catch(error => {
                        message.dealReturnMessage(error.msg, this, 'warning');
                    });
                this.$api.category()
                    .then(res => {
                        this.categories = res.data;
                    })
                    .catch(error => {
                        message.dealReturnMessage(error.msg, this, 'warning');
                    });
                // 如果是修改模式
                if (this.$route.params.mode && this.$route.params.mode === 'change') {
                    this.id = this.$route.query.id;
                    this.mode = this.$route.params.mode;
                    this.$api.blog(this.id)
                        .then(res => {
                            // 关闭自动简介
                            this.autoBrief = false;
                            this.title = res.data.title;
                            this.brief = res.data.brief;
                            this.content = res.data.content;
                            this.author = res.data.author;
                            if (res.data.category) {
                                this.selectCategories = res.data.category.id;
                            }
                            this.selectTabs = this.listToIdList(res.data.tabs);
                        })
                        .catch(error => {
                            message.dealReturnMessage(error.msg, this, 'warning');
                        });
                } else {
                    this.id = null;
                    this.title = '';
                    this.brief = '';
                    this.content = '';
                    this.author = '';
                    this.autoBrief = true;
                    this.selectTabs = [];
                    this.selectCategories = null;
                }
            },

            /**
             * 从返回的对象数组中获取只含有id的数组
             * @param rawList
             * @returns {Array}
             */
            listToIdList(rawList) {
                let res = [];
                for (let i = 0; i < rawList.length; i++) {
                    res.push(rawList[i].id);
                }
                return res
            },

            changeAutoBrief(status) {
                this.autoBrief = status;
            },

            getBrief(val) {
                let res = '';
                if (val.length > 200) {
                    res = val.slice(0, 196) + '......'
                } else {
                    res = val;
                }
                return removeMd(res);
            },

            createSubmit() {
                let d = {
                    title: this.title,
                    author: this.author,
                    brief: this.brief,
                    content: this.content,
                    tabs_pk: this.selectTabs,
                    category_pk: this.selectCategories,
                };
                this.$api.createBlog(d)
                    .then(res => {
                        this.$Message.info('发表成功');
                        this.$router.push({name: 'change-blog', params: {mode: 'change'}, query: {id: res.data.id}});
                    })
                    .catch(error => {
                        message.dealReturnMessage(error.msg, this, 'warning');
                    });
            },

            changeSubmit() {
                let d = {
                    title: this.title,
                    author: this.author,
                    brief: this.brief,
                    content: this.content,
                    tabs_pk: this.selectTabs,
                    category_pk: this.selectCategories,
                };
                this.$api.changeBlog(this.id, d)
                    .then(() => {
                        this.$Message.info('修改成功');
                        this.$router.push({name: 'change-blog', params: {mode: 'change'}, query: {id: this.id}});
                    })
                    .catch(error => {
                        message.dealReturnMessage(error.msg, this, 'warning');
                    });
            },

            submit() {
                if (this.mode === 'create') {
                    this.createSubmit();
                } else if (this.mode === 'change') {
                    this.changeSubmit();
                }
            },
        },

        watch: {
            /**
             * 内容改变的时候才会触发自动简介
             * @param val
             */
            content(val) {
                if (this.autoBrief) {
                    this.brief = this.getBrief(val);
                }
            },
            /**
             * 地址改变的时候重新初始化
             */
            '$route'() {
                this.init()
            },
        },

        computed: {
            compiledMarkdown() {
                return Markdown(this.content);
            },
        },
    }
</script>

<style scoped>

</style>
