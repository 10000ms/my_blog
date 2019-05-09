<template>
    <div class="single-content-div">
        <div>
            <span class="content-title-span">Title: </span>
            <span class="content-content-items">{{title}}</span>
        </div>
        <div>
            <span class="content-title-span">By: </span>
            <span class="content-content-items">{{user}}</span>
        </div>
        <div v-if="canOperation()">
            <span class="content-title-span">operation: </span>
            <Button type="primary" size="small" ghost class="operation-button" @click="changeComment">修改</Button>
            <Button type="error" size="small" ghost class="operation-button" @click="deleteComment">删除</Button>
        </div>
        <div>
            <span class="content-title-span block-item">Comment:</span>
            <span class="content-content-items" style="white-space: pre;">{{content}}</span>
        </div>
        <comment-operation
                ref="CommentOperationModel"
                :commentData="commentData"
                mode="change"
                v-on:renewComment="$emit('renewComment')"
        >
        </comment-operation>
    </div>
</template>

<script>
    import { mapState } from 'vuex';

    import CommentOperation from './CommentOperation.vue';

    export default {
        name: 'Comment',

        components: {
            CommentOperation,
        },

        props: {
            commentData: Object,
        },

        data() {
            return {
                id: this.commentData.id,
                title: this.commentData.title,
                user: this.commentData.creator.username,
                userId: this.commentData.creator.id,
                content: this.commentData.content,
            };
        },

        methods: {
            canOperation() {
                return this.userId === this.loginUserId
            },

            changeComment() {
                this.$refs.CommentOperationModel.openModal();
            },

            deleteComment() {
                this.$api.deleteComment(this.id)
                    .then(() => {
                        this.$Message.info('删除评论成功');
                        this.$emit('renewComment');
                    })
                    .catch(error => {
                        this.$Message.warning(error.msg);
                    });
            },
        },

        computed: {
            ...mapState('auth', {
                loginUserId: state => state.id,
            }),
        },
    }
</script>

<style scoped lang="less">
    .single-content-div {
        width: 80%;
        margin: 0 auto 20px auto;
        background-color: #ffffff;
        border-radius: 5px;
        text-align: justify;
        padding: 10px;
        position: relative;

        div {
            padding: 5px 0;
            border-bottom:1px solid rgba(235, 150, 72, 0.7);

            span {
                padding-right: 10px;
            }
        }
    }

    .content-title-span {
        color: rgba(235, 150, 72, 1);
        font-size: 14px;
        font-weight: bolder;
        margin: 4px 0;
    }

    .operation-button {
        margin: 0 10px;
    }
</style>