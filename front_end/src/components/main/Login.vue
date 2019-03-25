<template>
    <Modal
        v-model="show"
        title="Common Modal dialog box title"
        @on-ok="wantLogin"
        ok-text="登陆"
        cancel-text="取消">
        <p slot="header" :style="headerStyle">
            <span>登陆</span>
        </p>
        <div class="input-div">
            <div class="single-input-div">
                <Input v-model="account" placeholder="输入账户..." style="width: 100%"/>
            </div>
            <div class="single-input-div">
                <Input v-model="password" placeholder="输入密码..." type="password" style="width: 100%"/>
            </div>
        </div>
    </Modal>
</template>

<script>
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
            }
        },
        methods: {
            openModal() {
                this.show = true
            },

            wantLogin() {
                this.$Message.info('Clicked login');
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
