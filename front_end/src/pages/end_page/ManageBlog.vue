<template>
    <div class="thin-content-div height-min-height-div">
        <div class="margin-bottom-20">
            <i-table size="large" border :columns="columns7" :data="data6"></i-table>
        </div>
        <Page
                :total="100"
                :current="1"
                @on-change="changePage"
                show-elevator
                show-total
        />
    </div>
</template>

<script>
    export default {
        name: 'ManageBlog',

        data() {
            return {
                columns7: [
                    {
                        title: '标题',
                        key: 'name',
                        width: 600,
                        fixed: 'left',
                        render: (h, params) => {
                            return h('div', [
                                h('Icon', {
                                    props: {
                                        type: 'person',
                                    },
                                }),
                                h('strong', params.row.name),
                            ]);
                        },
                    },
                    {
                        title: '分类',
                        key: 'age',
                        width: 210,
                    },
                    {
                        title: '创建时间',
                        key: 'address',
                        width: 225,
                    },
                    {
                        title: '修改时间',
                        key: 'address',
                        width: 225,
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
                                        type: 'info',
                                        size: 'default',
                                    },
                                    style: {
                                        marginRight: '5px',
                                    },
                                    on: {
                                        click: () => {
                                            this.recommend(params.index);
                                        }
                                    }
                                }, '设置推荐'),
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
                                            this.show(params.index);
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
                        address: 'New York No. 1 Lake Park'
                    },
                    {
                        name: 'Jim Green',
                        age: 24,
                        address: 'London No. 1 Lake Park'
                    },
                    {
                        name: 'Joe Black',
                        age: 30,
                        address: 'Sydney No. 1 Lake Park'
                    },
                    {
                        name: 'Jon Snow',
                        age: 26,
                        address: 'Ottawa No. 2 Lake Park'
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
            recommend(index) {
                this.$log(index)
            },
            changePage() {

            },
        }
    }
</script>

<style scoped>

</style>
