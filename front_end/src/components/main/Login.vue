<template>
    <Modal
        v-model="show"
        title="Common Modal dialog box title"
        @on-ok="wantLogin"
        ok-text="登陆"
        cancel-text="取消"
        :loading="loading"
        :closable="true"
        scrollable
    >
        <p slot="header" :style="headerStyle">
            <span>登陆</span>
        </p>
        <div class="dialog-input-div">
            <div class="dialog-single-input-div">
                <i-input v-model="account" placeholder="账户"/>
            </div>
            <div class="dialog-single-input-div">
                <i-input v-model="password" placeholder="密码" type="password"/>
            </div>
        </div>
    </Modal>
</template>

<script>
    import message from '../../utils/message';

    export default {
        name: 'Login',

        data() {
            return {
                show: false,
                headerStyle: {
                    'color': 'rgba(246, 141, 66, 1)',
                    'text-align': 'center',
                    'font-size': '18px',
                    'margin': '5px',
                    'letter-spacing': '20px',
                },
                account: '',
                password: '',
                loading: true,
            };
        },

        methods: {
            openModal() {
                this.show = true;
            },

            wantLogin() {
                if (this.account.length < 6 || this.password.length < 6) {
                    this.$Message.warning('帐号密码错误');
                } else {
                    let d = {
                        username: this.account,
                        password: this.password,
                    };
                    this.$api.login(d)
                        .then(res => {
                            this.$store.commit('auth/commitInit', res.data);
                            this.$Message.info('登陆成功');
                            this.show = false;
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
        },
    }
</script>

<style scoped>

</style>
