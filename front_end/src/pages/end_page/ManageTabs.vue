<template>
    <div class="height-min-height-div thin-content-div">
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
                        title: '标签',
                        key: 'name',
                        render: (h, params) => {
                            return h('div', [
                                h('Icon', {
                                    props: {
                                        type: 'person'
                                    },
                                }),
                                h('strong', params.row.name)
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
                                            this.show(params.index);
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
                                }, '刪除'),
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
        }
    }
</script>

<style scoped>

</style>
