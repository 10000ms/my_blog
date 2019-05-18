<template>
    <div class="height-min-height-div thin-content-div">
        <span class="content-title-items">网站名</span>
        <div class="child-input-div">
            <i-input v-model="websiteName" placeholder="请输入网站名..." size="large" class="max-width"/>
        </div>
        <span class="content-title-items">网站备案号</span>
        <div class="child-input-div">
            <i-input v-model="ICPNumber" placeholder="请输入备案号..." size="large" class="max-width"/>
        </div>
        <span class="content-title-items">网站头像</span>
        <div class="main-profile-image-div"><img :src="websiteImage" class="website-image" alt="网站头像"/></div>
        <div class="child-input-div">
            <i-input v-model="websiteImage" placeholder="请输入网站头像地址..." size="large" class="max-width"/>
        </div>
        <span class="content-title-items">主页侧栏图片1</span>
        <div class="ad-container-div">
            <img :src="ad1" class="ad-image" alt="ad1"/>
        </div>
        <div class="child-input-div">
            <i-input v-model="ad1" placeholder="请输入主页侧栏图片1地址..." size="large" class="max-width"/>
        </div>
        <span class="content-title-items">主页侧栏图片1跳转url</span>
        <div class="child-input-div">
            <i-input v-model="ad1URL" placeholder="请输入主页侧栏图片1跳转url..." size="large" class="max-width"/>
        </div>
        <span class="content-title-items">主页侧栏图片2</span>
        <div class="ad-container-div">
            <img :src="ad2" class="ad-image" alt="ad1"/>
        </div>
        <div class="child-input-div">
            <i-input v-model="ad2" placeholder="请输入主页侧栏图片2地址..." size="large" class="max-width"/>
        </div>
        <span class="content-title-items">主页侧栏图片2跳转url</span>
        <div class="child-input-div">
            <i-input v-model="ad2URL" placeholder="请输入主页侧栏图片2跳转url..." size="large" class="max-width"/>
        </div>
        <span class="content-title-items">Github地址</span>
        <div class="child-input-div">
            <i-input v-model="github" placeholder="请输入Github地址..." size="large" class="max-width"/>
        </div>
        <span class="content-title-items">邮箱地址</span>
        <div class="child-input-div">
            <i-input v-model="email" placeholder="请输入邮箱地址..." size="large" class="max-width"/>
        </div>
        <span class="content-title-items">友情链接地址</span>
        <div class="child-input-div">
            <i-input v-model="friendshipLink" type="textarea" :autosize="{ minRows: 3, maxRows: 10 }"
                     placeholder="请输入友情链接地址，;分割，前面带有前缀，http:// 等..." size="large" class="max-width"/>
        </div>
        <div class="child-input-div">
            <span class="content-title-items">是否开放注册:  </span>
            <i-switch v-model="openRegister">
                <span slot="open">是</span>
                <span slot="close">否</span>
            </i-switch>
        </div>
        <div class="child-input-div">
            <span class="content-title-items">是否打开demo模式:  </span>
            <i-switch v-model="demoModel">
                <span slot="open">是</span>
                <span slot="close">否</span>
            </i-switch>
        </div>
        <div class="child-input-div">
            <Button type="success" long @click="submit" size="large">提交</Button>
        </div>
    </div>
</template>

<script>
    import message from '../../utils/message';

    export default {
        name: 'ManageWebsite',

        data() {
            return {
                id: null,
                websiteName: '',
                ICPNumber: '',
                github: '',
                email: '',
                websiteImage: '',
                ad1: '',
                ad1URL: '',
                ad2: '',
                ad2URL: '',
                friendshipLink: '',
                openRegister: false,
                demoModel: false,
            };
        },

        mounted() {
            this.init();
        },

        methods: {
            init() {
                this.$Loading.start();
                this.$api.websiteManage()
                    .then(res => {
                        if (res.data) {
                            this.id = res.data.id;
                            this.websiteName = res.data.website_name;
                            this.ICPNumber = res.data.ICP_number;
                            this.github = res.data.github;
                            this.email = res.data.email;
                            this.websiteImage = res.data.website_image;
                            this.ad1 = res.data.ad_1;
                            this.ad1URL = res.data.ad_1_url;
                            this.ad2 = res.data.ad_2;
                            this.ad2URL = res.data.ad_2_url;
                            this.friendshipLink = res.data.friendship_link;
                            this.openRegister = res.data.open_register;
                            this.demoModel = res.data.demo_model;
                        }
                        this.$Loading.finish();
                    })
                    .catch(error => {
                        this.$Loading.error();
                        message.dealReturnMessage(error.msg, this, 'warning');
                    });
            },

            submit() {
                this.$Loading.start();
                let p = {
                    website_name: this.websiteName,
                    ICP_number: this.ICPNumber,
                    github: this.github,
                    email: this.email,
                    website_image: this.websiteImage,
                    ad_1: this.ad1,
                    ad_1_url: this.ad1URL,
                    ad_2: this.ad2,
                    ad_2_url: this.ad2URL,
                    friendship_link: this.friendshipLink,
                    open_register: this.openRegister,
                    demo_model: this.demoModel,
                };
                this.$api.changeWebsiteManage(this.id, p)
                    .then(() => {
                        this.$Message.info('修改成功');
                        this.$Loading.finish();
                    })
                    .catch(error => {
                        this.$Loading.error();
                        message.dealReturnMessage(error.msg, this, 'warning');
                    });
            },
        },
    }
</script>

<style scoped>
    .child-input-div {
        width: 50%;
    }
</style>
