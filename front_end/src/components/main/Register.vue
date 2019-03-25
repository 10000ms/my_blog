<template>
    <Modal
        v-model="show"
        title="Common Modal dialog box title"
        @on-ok="wantRegister"
        ok-text="注册"
        cancel-text="取消">
        <p slot="header" :style="headerStyle">
            <span>注册</span>
        </p>
        <div class="input-div">
            <div class="single-input-div">
                <Input v-model="account" placeholder="账户" style="width: 100%"/>
            </div>
            <div class="single-input-div">
                <Input v-model="password" placeholder="密码" type="password" style="width: 100%"/>
            </div>
            <div class="single-input-div">
                <Input v-model="repeatPassword" placeholder="重复密码" type="password" style="width: 100%"/>
            </div>
            <div class="single-input-div">
                <Input v-model="userName" placeholder="用户名" style="width: 100%"/>
            </div>
            <div class="single-input-div">
                <Input v-model="phone" placeholder="手机" style="width: 100%"/>
            </div>
            <div class="single-input-div">
                <Input v-model="email" placeholder="邮箱" type="email" style="width: 100%"/>
            </div>
        </div>
    </Modal>
</template>

<script>
    export default {
        name: "Register",
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
                userName: '',
                phone: '',
                email: '',
            }
        },
        methods: {
            openModal() {
                this.show = true
            },

            wantRegister() {
                this.$Message.info('Clicked register');
            },
        }
    }
</script>

<style scoped>
    .input-div {
        padding: 20px;
        text-align: center;
    }

    .single-input-div {
        margin: 20px;
    }
</style>
