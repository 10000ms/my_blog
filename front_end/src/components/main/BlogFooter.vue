<template>
    <div class="footer-div">
        <div class="title-span">
            <Icon type="ios-link"/>
            <span>友情链接</span>
        </div>
        <div style="width: 80%; margin: 0 auto">
            <div v-for="f in friendLinks" :key="f.id" class="link-div">
                <a :href="f.link"><span>{{f.name}}</span></a>
            </div>
        </div>
        <div class="icp-number-div title-span">{{ICPNumber}}</div>

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

            }
        },
    }
</script>

<style scoped>
    .footer-div {
        background: linear-gradient(to left, #cc2b5e, #753a88);
        color: white;
        height: 150px;
        padding: 10px 0;
    }

    .title-span {
        font-size: 20px;
    }

    .link-div {
        float: left;
        width: 20%;
        margin: 0 15%;
        font-size: 16px;
        text-align: left;
    }

    a {
        color: white;
    }

    a:hover {
        color: rgb(45, 140, 240);
    }

    .icp-number-div {
        width: 20%;
        text-align: center;
        margin: 0 auto;
    }

</style>
