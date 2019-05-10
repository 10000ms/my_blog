<template>
    <Modal
        v-model="show"
        title="Common Modal dialog box title"
        @on-ok="submitComment"
        :loading="loading"
        :closable="true"
        scrollable
    >
        <p slot="header" :style="headerStyle">
            <span>{{showTitle}}</span>
        </p>
        <div class="dialog-input-div">
            <div class="dialog-single-input-div">
                <i-input v-model="title" placeholder="标题"/>
            </div>
            <div class="dialog-single-input-div">
                <i-input v-model="content" type="textarea" :rows="4" placeholder="内容"/>
            </div>
        </div>
    </Modal>
</template>

<script>
    import message from '../../utils/message';

    export default {
        name: 'CommentOperation',

        props: {
            commentData: {
                type: Object,
                require: false,
            },

            blogId: {
                type: Number,
                require: false,
            },

            mode: {
                type: String,
                default: 'create',
                validator: function (value) {
                    // 这个值必须匹配下列字符串中的一个
                    return ['create', 'change'].indexOf(value) !== -1
                }
            },
        },

        data() {
            return {
                show: false,
                headerStyle: {
                    'color': 'rgba(246, 141, 66, 1)',
                    'text-align': 'center',
                    'font-size': '18px',
                    'margin': '5px',
                    'letter-spacing': '5px',
                },
                title: '',
                content: '',
                id: null,
                loading: true,
                showTitle: '添加评论',
            };
        },

        mounted() {
            this.init();
        },

        methods: {
            init() {
                if (this.mode === 'change') {
                    this.title = this.commentData.title;
                    this.content = this.commentData.content;
                    this.id = this.commentData.id;
                    this.showTitle = '修改评论';
                }
            },

            openModal() {
                this.show = true;
            },

            changeSubmitComment() {
                if (this.title.length < 2 || this.content.length < 2) {
                    this.$Message.warning('标题或内容长度太短');
                } else {
                    let d = {
                        title: this.title,
                        content: this.content,
                    };
                    this.$api.changeComment(this.id, d)
                        .then(() => {
                            this.$Message.info('修改成功');
                            this.show = false;
                            // 发送事件
                            this.$emit('renew-comment');
                        })
                        .catch(error => {
                            message.dealReturnMessage(error.msg, this, 'warning');
                        });
                }
                // 关闭这一轮的loading，并且保证下一轮存在loading
                this.loading = false;
                this.$nextTick(() => {
                    this.loading = true;
                });
            },

            createSubmitComment() {
                if (
                    this.title.length < 2
                    || this.content.length < 2
                    || this.title.length > 15
                    || this.content.length > 1000
                ) {
                    this.$Message.warning('标题或内容长度太长或太短');
                } else {
                    let d = {
                        blog_pk: this.blogId,
                        title: this.title,
                        content: this.content,
                    };
                    this.$api.createComment(d)
                        .then(() => {
                            this.$Message.info('评论成功');
                            this.show = false;
                            // 发送事件
                            this.$emit('renew-comment');
                        })
                        .catch(error => {
                            message.dealReturnMessage(error.msg, this, 'warning');
                        });
                }
                // 关闭这一轮的loading，并且保证下一轮存在loading
                this.loading = false;
                this.$nextTick(() => {
                    this.loading = true;
                });
            },

            submitComment() {
                if (this.mode === 'change') {
                    this.changeSubmitComment();
                } else if (this.mode === 'create') {
                    this.createSubmitComment();
                }
            },
        },
    }
</script>

<style scoped>

</style>
