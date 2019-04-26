<template>
    <Modal
        v-model="show"
        title="Common Modal dialog box title"
        @on-ok="wantRegister"
        ok-text="注册"
        cancel-text="取消"
        :loading="loading"
        :closable="true"
    >
        <p slot="header" :style="headerStyle">
            <span>注册</span>
        </p>
        <div class="dialog-input-div">
            <div class="dialog-single-input-div">
                <i-input v-model="account" placeholder="账户"/>
            </div>
            <div class="dialog-single-input-div">
                <i-input v-model="password" placeholder="密码" type="password"/>
            </div>
            <div class="dialog-single-input-div">
                <i-input v-model="repeatPassword" placeholder="重复密码" type="password"/>
            </div>
            <div class="dialog-single-input-div">
                <i-input v-model="lastName" placeholder="姓"/>
            </div>
            <div class="dialog-single-input-div">
                <i-input v-model="firstName" placeholder="名"/>
            </div>
            <div class="dialog-single-input-div">
                <i-input v-model="phone" placeholder="手机"/>
            </div>
            <div class="dialog-single-input-div">
                <i-input v-model="email" placeholder="邮箱" type="email"/>
            </div>
        </div>
    </Modal>
</template>

<script>
    export default {
        name: 'Register',
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
                repeatPassword: '',
                firstName: '',
                lastName: '',
                phone: '',
                email: '',
                loading: true,
            };
        },
        methods: {
            openModal() {
                this.show = true;
            },

            wantRegister() {
                if (this.account.length < 6 || this.password.length < 6) {
                    this.$Message.warning('帐号密码错误');
                } else if (this.password !== this.repeatPassword) {
                    this.$Message.warning('两次输入密码不一致');
                } else if (this.firstName && this.lastName && this.phone && this.email) {
                    let d = {
                        username: this.account,
                        password: this.password,
                        first_name: this.firstName,
                        last_name: this.lastName,
                        phone: this.phone,
                        email: this.email,
                    };
                    this.$api.register(d)
                        .then(res => {
                            this.$store.commit('auth/commitInit', res.data);
                            this.show = false;
                            this.$Message.info('注册成功');
                        })
                        .catch(error => {
                            this.$Message.warning(error.msg);
                        });
                } else {
                    this.$Message.warning('请完整输入信息');
                }
                // 关闭这一轮的loading，并且保证下一轮存在loading
                this.loading = false;
                this.$nextTick(() => {
                    this.loading = true;
                });
            },
        }
    }
</script>

<style scoped>

</style>
