<template>
    <div class="footer-div">
        <div class="content-content-items color-common-white-items">
            <Icon type="ios-link"/>
            <span>友情链接</span>
        </div>
        <div class="thin-content-div">
            <div v-for="f in friendLinks" :key="f.id" class="link-div">
                <a class="color-common-white-items" :href="f.link"><span>{{f.name}}</span></a>
            </div>
        </div>
        <div class="thin-content-div text-align-center-div content-content-items color-common-white-items">{{ICPNumber}}</div>

    </div>
</template>

<script>
    export default {
        name: 'BlogFooter',
        data() {
            return {
                friendLinks: [
                    {
                        id: 1,
                        name: 'qq',
                        link: 'http://www.qq.com',
                    },
                    {
                        id: 2,
                        name: 'qqq',
                        link: 'http://www.qqq.com',
                    },
                    {
                        id: 3,
                        name: 'qqqq',
                        link: 'http://www.qqqq.com',
                    },
                    {
                        id: 4,
                        name: 'qqqqq',
                        link: 'http://www.qqqqq.com',
                    },
                    {
                        id: 5,
                        name: 'qqqqqq',
                        link: 'http://www.qqqqqq.com',
                    },
                    {
                        id: 6,
                        name: 'qqqqqqq',
                        link: 'http://www.qqqqqqq.com',
                    },
                ],
                ICPNumber: '京ICP备00000000号',
            };
        },
    }
</script>

<style scoped>
    .footer-div {
        background: linear-gradient(to left, #cc2b5e, #753a88);
        height: 150px;
        padding: 10px 0;
    }

    .link-div {
        float: left;
        width: 20%;
        margin: 0 15%;
        font-size: 16px;
        text-align: left;
    }
</style>
