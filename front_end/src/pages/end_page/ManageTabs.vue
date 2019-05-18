<template>
    <div class="height-min-height-div thin-content-div">
        <div class="margin-bottom-20">
            <i-table size="large" border :columns="columns" :data="tabs"></i-table>
        </div>

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
    import message from '../../utils/message';

    export default {
        name: 'ManageBlog',

        data() {
            return {
                columns: [
                    {
                        title: '标签',
                        key: 'title',
                        render: (h, params) => {
                            return h('div', [
                                h('Icon', {
                                    props: {
                                        type: 'ios-pricetag'
                                    },
                                }),
                                h('strong', params.row.title),
                            ]);
                        },
                    },
                    {
                        title: '操作',
                        key: 'action',
                        width: 210,
                        align: 'center',
                        render: (h, params) => {
                            return h('div', [
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
                                        },
                                    },
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
                tabs: [],
                deleteModal: false,
                deleteModalId: null,
            };
        },

        mounted() {
            this.init();
        },

        methods: {
            init() {
                this.$Loading.start();
                this.$api.tab()
                    .then(res => {
                        this.tabs = res.data;
                        this.$Loading.finish();
                    })
                    .catch(error => {
                        this.$Loading.error();
                        message.dealReturnMessage(error.msg, this, 'warning');
                    });
            },

            change(tabId) {
                this.$router.push({name: 'change-tab', params: {mode: 'change'}, query: {id: tabId}});
            },

            remove(tabId) {
                this.deleteModalId = tabId;
                this.deleteModal = true;
            },

            doRemove() {
                if (this.deleteModalId) {
                    this.$api.deleteTab(this.deleteModalId)
                        .then(() => {
                            this.$Message.info('删除成功');
                            // 重置页面数据
                            this.init();
                            // 清空删除id数据
                            this.deleteModalId = null;
                        })
                        .catch(error => {
                            message.dealReturnMessage(error.msg, this, 'warning');
                        });
                }
            },
        },
    }
</script>

<style scoped>

</style>
