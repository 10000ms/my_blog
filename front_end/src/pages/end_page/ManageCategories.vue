<template>
    <div class="max-width height-min-height-div">
        <div class="child-div">
            <i-table size="large" border :columns="columns7" :data="data6"></i-table>
            <Page :total="100" :current="1" @on-change="changePage"></Page>
        </div>
        <div class="child-div">
            <div class="category-div" v-for="c in categories" :key="c.id">
                <a :href="c.url" class="color-common-black-items">
                    <span v-html="printLevel(getLevel(c.id))" class="content-content-items"></span>
                    {{c.name}}
                    <span class="count-span">({{c.count}})</span>
                </a>
            </div>
        </div>
    </div>
</template>

<script>
    import categoryUtils from '../../utils/category';

    export default {
        name: 'ManageBlog',
        data() {
            return {
                categories: [
                    {
                        id: 1,
                        name: '111',
                        fid: 0,
                        url: 'asdasd',
                        count: 5,
                    },
                    {
                        id: 2,
                        name: '112',
                        fid: 1,
                        url: 'asdasd',
                        count: 5,
                    },
                    {
                        id: 3,
                        name: '113',
                        fid: 1,
                        url: 'asdasd',
                        count: 5,
                    },
                    {
                        id: 4,
                        name: '131',
                        fid: 3,
                        url: 'asdasd',
                        count: 5,
                    },
                    {
                        id: 5,
                        name: '222',
                        fid: 0,
                        url: 'asdasd',
                        count: 5,
                    },
                    {
                        id: 6,
                        name: '333',
                        fid: 0,
                        url: 'asdasd',
                        count: 5,
                    },
                    {
                        id: 7,
                        name: '444',
                        fid: 0,
                        url: 'asdasd',
                        count: 5,
                    },
                    {
                        id: 8,
                        name: '555',
                        fid: 0,
                        url: 'asdasd',
                        count: 5,
                    },
                ],
                columns7: [
                    {
                        title: '标签',
                        key: 'name',
                        render: (h, params) => {
                            return h('div', [
                                h('Icon', {
                                    props: {
                                        type: 'person'
                                    }
                                }),
                                h('strong', params.row.name)
                            ]);
                        }
                    },
                    {
                        title: '父类型',
                        key: 'address',
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
                                            this.show(params.index)
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
                                            this.remove(params.index);
                                        },
                                    },
                                }, '刪除')
                            ]);
                        },
                    },
                ],
                data6: [
                    {
                        name: 'John Brown',
                        age: 18,
                        address: 'New York No. 1 Lake Park',
                    },
                    {
                        name: 'Jim Green',
                        age: 24,
                        address: 'London No. 1 Lake Park',
                    },
                    {
                        name: 'Joe Black',
                        age: 30,
                        address: 'Sydney No. 1 Lake Park',
                    },
                    {
                        name: 'Jon Snow',
                        age: 26,
                        address: 'Ottawa No. 2 Lake Park',
                    },
                ],
            };
        },
        methods: {
            show(index) {
                this.$Modal.info({
                    title: 'User Info',
                    content: `Name：${this.data6[index].name}<br>Age：${this.data6[index].age}<br>Address：${this.data6[index].address}`
                })
            },
            remove(index) {
                this.data6.splice(index, 1);
            },
            changePage() {

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
