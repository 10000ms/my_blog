<template>
    <Modal
        v-model="show"
        title="Common Modal dialog box title"
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
        <div slot="footer">
            <Button size="large" @click="close">取消</Button>
            <Button v-if="demoModel" type="info" size="large" :loading="loading" @click="wantDemoLogin">
                <span>demo模式登录</span>
            </Button>
            <Button type="primary" size="large" :loading="loading" @click="wantLogin">登陆</Button>
        </div>
    </Modal>
</template>

<script>
    import { mapState } from 'vuex';

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
                loading: false,
            };
        },

        methods: {
            openModal() {
                this.show = true;
            },

            close() {
                this.show = false;
                this.loading = false;
            },

            wantDemoLogin() {
                this.loading = true;
                this.$api.demoLogin()
                    .then(res => {
                        this.$store.commit('auth/commitInit', res.data);
                        this.$Message.info('登陆成功');
                        this.show = false;
                        this.loading = false;
                    })
                    .catch(error => {
                        message.dealReturnMessage(error.msg, this, 'warning');
                        this.loading = false;
                    });
            },

            wantLogin() {
                if (this.account.length < 6 || this.password.length < 6) {
                    this.$Message.warning('帐号密码错误');
                } else {
                    let d = {
                        username: this.account,
                        password: this.password,
                    };
                    this.loading = true;
                    this.$api.login(d)
                        .then(res => {
                            this.$store.commit('auth/commitInit', res.data);
                            this.$Message.info('登陆成功');
                            this.show = false;
                            this.loading = false;
                        })
                        .catch(error => {
                            message.dealReturnMessage(error.msg, this, 'warning');
                            this.loading = false;
                        });
                }
            },
        },

        computed: {
            ...mapState('website', {
                demoModel: state => state.demoModel,
            }),
        },
    }
</script>

<style scoped>

</style>
