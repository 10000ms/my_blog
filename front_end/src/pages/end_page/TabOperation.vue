<template>
    <div class="height-min-height-div thin-content-div">
        <i-input v-model="tab" placeholder="请输入标签..." size="large" class="min-input"/>
        <Button type="success" @click="submit" size="large">提交</Button>
    </div>
</template>

<script>
    import message from '../../utils/message';

    export default {
        name: 'TabOperation',

        data() {
            return {
                id: null,
                tab: '',
                mode: 'create',
            };
        },

        mounted() {
            this.init();
        },

        methods: {
            init() {
                // 如果是修改模式
                if (this.$route.params.mode && this.$route.params.mode === 'change') {
                    this.id = this.$route.query.id;
                    this.mode = this.$route.params.mode;
                    this.$api.tab(this.id)
                        .then(res => {
                            this.tab = res.data.title;
                        })
                        .catch(error => {
                            message.dealReturnMessage(error.msg, this, 'warning');
                        });
                }
            },

            createSubmit() {
                let d = {
                    title: this.tab,
                };
                this.$api.createTab(d)
                    .then(res => {
                        this.$Message.info('添加成功');
                        this.$router.push({name: 'change-tab', params: {mode: 'change'}, query: {id: res.data.id}});
                    })
                    .catch(error => {
                        message.dealReturnMessage(error.msg, this, 'warning');
                    });
            },

            changeSubmit() {
                let d = {
                    title: this.tab,
                };
                this.$api.changeTab(this.id, d)
                    .then(() => {
                        this.$Message.info('修改成功');
                        this.$router.push({name: 'change-tab', params: {mode: 'change'}, query: {id: this.id}});
                    })
                    .catch(error => {
                        message.dealReturnMessage(error.msg, this, 'warning');
                    });
            },

            submit() {
                if (this.mode === 'create') {
                    this.createSubmit();
                } else if (this.mode === 'change') {
                    this.changeSubmit();
                }
            },
        },

    }
</script>

<style scoped>
    .min-input {
        width: 30%;
    }
</style>
