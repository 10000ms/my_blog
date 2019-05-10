<template>
    <div class="max-width height-min-height-div">
        <div class="child-div">
            <i-table size="large" border :columns="columns" :data="categories"></i-table>
        </div>
        <div class="child-div">
            <div class="category-div" v-for="c in categories" :key="c.id">
                <span v-html="printLevel(getLevel(c.id))" class="content-content-items"></span>
                {{c.title}}
                <span class="count-span">({{c.count}})</span>
            </div>
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
    import categoryUtils from '../../utils/category';
    import message from '../../utils/message';

    export default {
        name: 'ManageBlog',

        data() {
            return {
                categories: [],
                columns: [
                    {
                        title: '标签',
                        key: 'title',
                        render: (h, params) => {
                            return h('div', [
                                h('strong', params.row.title)
                            ]);
                        },
                    },
                    {
                        title: '父类型',
                        key: 'father_category',
                        render: (h, params) => {
                            if (params.row.father_category) {
                                return h('div', [
                                    h('span', params.row.father_category.title),
                                ]);
                            } else {
                                return h('div', [
                                    h('span', ''),
                                ]);
                            }
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
                                }, '刪除')
                            ]);
                        },
                    },
                ],
                deleteModalId: null,
                deleteModal: false,
            };
        },

        mounted() {
            this.init();
        },

        methods: {
            init() {
                this.$api.category()
                    .then(res => {
                        this.categories = res.data;
                    })
                    .catch(error => {
                        message.dealReturnMessage(error.msg, this, 'warning');
                    });
            },

            change(CategoryId) {
                this.$router.push({name: 'change-category', params: {mode: 'change'}, query: {id: CategoryId}});
            },

            remove(CategoryId) {
                this.deleteModalId = CategoryId;
                this.deleteModal = true;
            },

            doRemove() {
                if (this.deleteModalId) {
                    this.$api.deleteCategory(this.deleteModalId)
                        .then(() => {
                            this.$Message.info('删除成功');
                            // 重置页面数据
                            this.init();
                            // 清空删除id数据
                            this.deleteModalId = null;
                        })
                        .catch(error => {
                            message.dealReturnMessage(error.msg, this, 'warning');
                        })
                }
            },

            getLevel(categoryId) {
                return categoryUtils.categoryGetLevel(categoryId, this.categories);
            },

            printLevel(level) {
                return categoryUtils.categoryPrintLevel(level);
            },
        }
    }
</script>

<style scoped>

</style>
