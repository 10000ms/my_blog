<template>
    <div class="thin-content-div height-min-height-div">
        <div class="margin-bottom-20">
            <i-table size="large" border :columns="columns" :data="blogs"></i-table>
        </div>
        <Page
                :total="blogsPage['count']"
                :current="currentPage"
                @on-change="changePage"
                v-if="blogsPage['count'] > 10"
                show-elevator
                show-total
        />
        <Modal
                v-model="deleteModal"
                title="删除警告"
                @on-ok="doRemove"
                :closable="true"
                scrollable
        >
            <p>是否确定删除，删除后不可恢复！</p>
        </Modal>
    </div>
</template>

<script>
    import time from '../../utils/time.js';
    import message from '../../utils/message';

    export default {
        name: 'ManageBlog',

        data() {
            return {
                columns: [
                    {
                        title: '标题',
                        key: 'title',
                        width: 400,
                        fixed: 'left',
                        render: (h, params) => {
                            return h('div', [
                                h('strong', params.row.title),
                            ]);
                        },
                    },
                    {
                        title: '分类',
                        key: 'category',
                    },
                    {
                        title: '创建时间',
                        key: 'create_time',
                    },
                    {
                        title: '修改时间',
                        key: 'last_change_time',
                    },
                    {
                        title: '操作',
                        key: 'action',
                        width: 260,
                        align: 'center',
                        fixed: 'right',
                        render: (h, params) => {
                            return h('div', [
                                h('Button', {
                                    props: {
                                        type: 'success',
                                        size: 'default',
                                    },
                                    style: {
                                        marginRight: '5px',
                                        display:(params.row.is_recommend)?"none":"inline-block",
                                    },
                                    on: {
                                        click: () => {
                                            this.recommend(params.row.id);
                                        }
                                    }
                                }, '设置推荐'),
                                h('Button', {
                                    props: {
                                        type: 'info',
                                        size: 'default',
                                    },
                                    style: {
                                        marginRight: '5px',
                                        display:(! params.row.is_recommend)?"none":"inline-block",
                                    },
                                    on: {
                                        click: () => {
                                            this.cancelRecommend(params.row.id);
                                        }
                                    }
                                }, '取消推荐'),
                                h('Button', {
                                    props: {
                                        type: 'primary',
                                        size: 'default',
                                    },
                                    style: {
                                        marginRight: '5px',
                                    },
                                    on: {
                                        click: () => {
                                            this.change(params.row.id);
                                        }
                                    }
                                }, '修改'),
                                h('Button', {
                                    props: {
                                        type: 'error',
                                        size: 'default',
                                    },
                                    on: {
                                        click: () => {
                                            this.remove(params.row.id);
                                        },
                                    },
                                }, '刪除'),
                            ]);
                        },
                    },
                ],
                blogs: [],
                blogsPage: {},
                currentPage: 1,
                deleteModal: false,
                deleteModalId: null,
            };
        },

        mounted() {
            this.init();
        },

        methods: {
            init() {
                this.dataFromServer();
            },

            dataFromServer(page=null) {
                let dict = {};
                if (page) {
                    dict.page = page
                }
                this.$Loading.start();
                this.$api.blogs({page: page})
                    .then(res => {
                        this.blogs = this.dealDataFromRaw(res.data);
                        this.blogsPage = res.page;
                        this.$Loading.finish();
                    })
                    .catch(error => {
                        message.dealReturnMessage(error.msg, this, 'warning');
                    });
            },

            dealDataFromRaw(rawData) {
                for (let i = 0; i < rawData.length; i++) {
                    rawData[i].create_time =  time.getTimeString(rawData[i].create_time);
                    rawData[i].last_change_time =  time.getTimeString(rawData[i].last_change_time);
                    if (rawData[i].category) {
                        rawData[i].category = rawData[i].category.title;
                    }
                }
                return rawData;
            },

            changePage(page) {
                this.dataFromServer(page);
            },

            change(blogId) {
                this.$router.push({name: 'change-blog', params: {mode: 'change'}, query: {id: blogId}});
            },

            /**
             * 因为删除是危险方法，所以需要再次确认再进行删除
             */
            remove(blogId) {
                this.deleteModalId = blogId;
                this.deleteModal = true;
            },

            /**
             * 真正执行删除方法
             */
            doRemove() {
                if (this.deleteModalId) {
                    this.$api.deleteBlog(this.deleteModalId)
                        .then(() => {
                            this.$Message.info('删除成功');
                            // 重置页面数据
                            this.dataFromServer(this.currentPage);
                            // 清空删除id数据
                            this.deleteModalId = null;
                        })
                        .catch(error => {
                            message.dealReturnMessage(error.msg, this, 'warning');
                        });
                }
            },

            recommend(blogId) {
                let dict = {
                    id: blogId,
                };
                this.$api.addRecommend(dict)
                    .then(() => {
                        this.$Message.info('设置推荐成功');
                        // 重置页面数据
                        this.dataFromServer(this.currentPage);
                    })
                    .catch(error => {
                        message.dealReturnMessage(error.msg, this, 'warning');
                    });
            },

            cancelRecommend(blogId) {
                let dict = {
                    id: blogId,
                };
                this.$api.cancelRecommend(dict)
                    .then(() => {
                        this.$Message.info('取消推荐成功');
                        // 重置页面数据
                        this.dataFromServer(this.currentPage);
                    })
                    .catch(error => {
                        message.dealReturnMessage(error.msg, this, 'warning');
                    });
            },
        }
    }
</script>

<style scoped>

</style>
