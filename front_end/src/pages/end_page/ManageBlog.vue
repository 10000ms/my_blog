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
    </div>
</template>

<script>
    import time from '../../utils/time.js';

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
            };
        },

        mounted() {
            this.init();
        },

        methods: {
            init() {
                this.dataFromServer()
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
                    });
            },

            dealDataFromRaw(rawData) {
                for (let i = 0; i < rawData.length; i++) {
                    rawData[i].create_time =  time.getTimeString(rawData[i].create_time);
                    rawData[i].last_change_time =  time.getTimeString(rawData[i].last_change_time);
                    rawData[i].category = rawData[i].category.title;
                }
                return rawData;
            },

            changePage(page) {
                this.dataFromServer(page);
            },

            change(index) {
                this.$log('in change', index);
            },

            remove(index) {
                this.$log('in remove', index);
            },

            recommend(index) {
                this.$log('in recommend', index);
            },

            cancelRecommend(index) {
                this.$log('in cancelRecommend', index);
            },
        }
    }
</script>

<style scoped>

</style>
