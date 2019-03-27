<template>
    <div id="app">
        <router-view></router-view>
    </div>
</template>

<script>
    export default {
        name: 'app',
        mounted() {
            this.init()
        },
        methods: {
            init() {
                this.$log(1111)
            },
        },
        computed: {
            getWebMessages() {
                return this.$store.state.webMessages.getMessages;
            }
        },
        watch: {
            getWebMessages: {
                // 发送提示信息方法
                handler(newer, older) {
                    if (newer.length > older.length) {
                        // 增加的时候才进行处理
                        let m = newer[0];
                        this.$store.commit('webMessages/renewMessage');
                        switch (m.state) {
                            case 'info':
                                this.$Message.info(m.message);
                                break;
                            case 'success':
                                this.$Message.success(m.message);
                                break;
                            case 'warning':
                                this.$Message.warning(m.message);
                                break;
                            case 'error':
                                this.$Message.error(m.message);
                                break;
                            case 'loading':
                                this.$Message.loading(m.message);
                                break;
                        }
                    }
                },
                deep: true // 开启深度监听
            },
        },
    }

</script>

<style>
    html, body {
        height: 100%;
    }

    #app {
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        height: 100%;
    }
</style>
