<template>
    <div v-show="id">
        <div>
            <span class="content-title-items" style="font-size: 30px">{{title}}</span>
        </div>
        <div class="content-title-items info-div">
            <span>Post on: {{time}} </span>
            <span class="separator-span">|</span>
            <span> Author: {{author}} </span>
            <span class="separator-span">|</span>
            <span> In: {{category}}</span>
            <span class="separator-span">|</span>
            <span class="heart-span" @click="heart">
                <Icon type="md-heart" />
                <span> {{like}}</span>
            </span>
        </div>
        <div class="markdown-div" v-html="compiledMarkdown"></div>
        <div>
            <div class="content-title-items thin-content-div text-align-left-div comment-title-div">
                <span>Comment: </span>
                <span v-if="comments.length === 0">Empty</span>
                <Button type="primary" ghost class="operation-button" @click="addComment">Add comment</Button>
            </div>
            <comment v-for="c in comments" :key="c.id" :commentData="c"></comment>
            <Page
                    :total="indexPage['count']"
                    :current="currentPage"
                    @on-change="changePage"
                    v-if="indexPage['count'] > 10"
                    show-elevator
                    show-total
            />
            <comment-operation ref="CommentOperationModel" :blogId="id"></comment-operation>
        </div>
    </div>
</template>

<script>
    import '../../assets/css/marked.less';
    import 'highlight.js/styles/xcode.css';
    import { Markdown } from '../../utils/markdown.js';

    import Comment from '../../components/front/Comment';
    import CommentOperation from '../../components/front/CommentOperation';

    export default {
        name: 'Blog',

        components: {
            Comment,
            CommentOperation,
        },

        data() {
            return {
                id: null,
                title: '',
                content: '',
                time: '',
                author: '',
                category: '',
                like: 0,
                isLike: false,
                comments: [],
                indexPage: {},
                currentPage: 1,
            };
        },

        mounted() {
            this.init();
        },

        methods: {
            init() {
                this.$api.blog(this.$route.params.id)
                    .then(res => {
                        this.id = res.data.id;
                        this.title = res.data.title;
                        this.content = res.data.content;
                        this.time = this.getTimeString(res.data.create_time);
                        this.author = res.data.author;
                        this.category = res.data.category.title;
                        this.like = res.data.like_count;
                        // 获取完文章再拿评论
                        this.getCommentData();
                    });
            },

            changePage(page) {
                let queryDict = {
                    id: this.id,
                    page: page,
                };
                this.$Loading.start();
                this.$api.blogComment(queryDict)
                    .then(res => {
                        this.comments = res.data;
                        this.indexPage = res.page;
                        this.$Loading.finish();
                    });
            },

            getTimeString(timeString) {
                let date = new Date(timeString);
                let year = date.getFullYear().toString();
                let month = (date.getMonth() + 1).toString();
                if (month.length < 2) {
                    month = '0' + month;
                }
                let day = date.getDate().toString();
                if (day.length < 2) {
                    day = '0' + day;
                }
                let hour = date.getHours().toString();
                let minute = date.getMinutes().toString();
                if (minute.length < 2) {
                    minute = '0' + minute;
                }
                return `${year} - ${month} - ${day} ${hour}:${minute}`;
            },

            /**
             * 点赞方法
             */
            heart() {
                if (! this.isLike) {
                    let dict = {
                        id: this.id,
                    };
                    this.$api.heart(dict)
                        .then(() => {
                            this.like ++;
                            this.isLike = true;
                        })
                } else {
                    this.$Message.info('已点赞');
                }
            },

            addComment() {
                this.$refs.CommentOperationModel.openModal();
            },

            getCommentData(page=null) {
                let dict = {
                    id: this.id,
                };
                if (page) {
                    dict.page = page
                }
                this.$api.blogComment(dict)
                    .then(res => {
                        this.comments = res.data;
                        this.indexPage = res.page;
                    })
            },

            renewComment() {
                this.getCommentData(this.currentPage);
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
    .markdown-div {
        width: 80%;
        margin: 5% auto;
    }

    .info-div {
        color: #999999;
        font-size: 14px;
    }

    .separator-span {
        color: rgb(55, 55, 55);
        margin: 0 10px;
    }

    .heart-span {
        color: rgb(204, 43, 94);
        font-size: 16px;
        font-weight: bolder;
        cursor: pointer;
    }

    .operation-button {
        float:right;
    }

    .comment-title-div {
        border-top: 2px solid rgba(235, 150, 72, 0.7);
        margin: 10px auto;
        padding: 10px 0;
    }
</style>
