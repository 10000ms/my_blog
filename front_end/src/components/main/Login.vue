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
        <div class="dialog-input-div">
            <div class="dialog-single-input-div">
                <Input v-model="account" placeholder="账户"/>
            </div>
            <div class="dialog-single-input-div">
                <Input v-model="password" placeholder="密码" type="password"/>
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
            };
        },
        methods: {
            openModal() {
                this.show = true;
            },

            wantLogin() {
                this.$Message.info('Clicked login');
            },
        },
    }
</script>

<style scoped>

</style>
