<template>
    <div class="index-main-div">
        <span class="title-span">网站名</span>
        <div class="child-input-div">
            <Input v-model="websiteName" placeholder="请输入网站名..." size="large" style="width: 100%"/>
        </div>
        <span class="title-span">网站备案号</span>
        <div class="child-input-div">
            <Input v-model="ICPNumber" placeholder="请输入备案号..." size="large" style="width: 100%"/>
        </div>
        <div class="child-input-div">
            <span class="title-span">网站头像</span>
            <div class="child-input-div">
                <Upload
                    ref="upload"
                    :show-upload-list="false"
                    :on-success="handleSuccess"
                    :format="['jpg','jpeg','png']"
                    :max-size="2048"
                    :on-format-error="handleFormatError"
                    :on-exceeded-size="handleMaxSize"
                    type="drag"
                    action="//jsonplaceholder.typicode.com/posts/"
                    style="display: inline-block;width:58px;">
                    <div style="width: 58px;height:58px;line-height: 58px;">
                        <Icon type="ios-camera" size="20"></Icon>
                    </div>
                </Upload>
            </div>
        </div>
        <span class="title-span">主页侧栏图片1</span>
        <div class="child-input-div">
            <Upload
                ref="upload"
                :show-upload-list="false"
                :on-success="handleSuccess"
                :format="['jpg','jpeg','png']"
                :max-size="2048"
                :on-format-error="handleFormatError"
                :on-exceeded-size="handleMaxSize"
                type="drag"
                action="//jsonplaceholder.typicode.com/posts/"
                style="display: inline-block;width:58px;">
                <div style="width: 58px;height:58px;line-height: 58px;">
                    <Icon type="ios-camera" size="20"></Icon>
                </div>
            </Upload>
        </div>
        <span class="title-span">主页侧栏图片2</span>
        <div class="child-input-div">
            <Upload
                ref="upload"
                :show-upload-list="false"
                :on-success="handleSuccess"
                :format="['jpg','jpeg','png']"
                :max-size="2048"
                :on-format-error="handleFormatError"
                :on-exceeded-size="handleMaxSize"
                type="drag"
                action="//jsonplaceholder.typicode.com/posts/"
                style="display: inline-block;width:58px;">
                <div style="width: 58px;height:58px;line-height: 58px;">
                    <Icon type="ios-camera" size="20"></Icon>
                </div>
            </Upload>
        </div>
        <span class="title-span">Github地址</span>
        <div class="child-input-div">
            <Input v-model="githubAddress" placeholder="请输入Github地址..." size="large" style="width: 100%"/>
        </div>
        <span class="title-span">邮箱地址</span>
        <div class="child-input-div">
            <Input v-model="email" placeholder="请输入邮箱地址..." size="large" style="width: 100%"/>
        </div>
        <span class="title-span">友情链接地址</span>
        <div class="child-input-div">
            <Input v-model="email" type="textarea" :autosize="{ minRows: 3, maxRows: 10 }"
                   placeholder="请输入友情链接地址，;分割..." size="large" style="width: 100%"/>
        </div>
        <div class="child-input-div">
            <span class="title-span">是否开放注册:  </span>
            <i-switch v-model="openRegister" @on-change="changeOpenRegister">
                <span slot="open">是</span>
                <span slot="close">否</span>
            </i-switch>
        </div>
        <div class="child-input-div">
            <span class="title-span">是否打开demo模式:  </span>
            <i-switch v-model="demoModel" @on-change="changeDemoModel">
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
    export default {
        name: 'ManageWebsite',
        data() {
            return {
                websiteName: '',
                ICPNumber: '',
                githubAddress: '',
                email: '',
                openRegister: false,
                demoModel: false,
                websiteLogo: [],
            }
        },
        methods: {
            submit() {

            },
            handleSuccess(res, file) {
                file.url = 'https://o5wwk8baw.qnssl.com/7eb99afb9d5f317c912f08b5212fd69a/avatar';
                file.name = '7eb99afb9d5f317c912f08b5212fd69a';
            },
            handleFormatError(file) {
                this.$Notice.warning({
                    title: 'The file format is incorrect',
                    desc: 'File format of ' + file.name + ' is incorrect, please select jpg or png.'
                });
            },
            handleMaxSize(file) {
                this.$Notice.warning({
                    title: 'Exceeding file size limit',
                    desc: 'File  ' + file.name + ' is too large, no more than 2M.'
                });
            },
            changeOpenRegister() {

            },
            changeDemoModel() {

            },

        }
    }
</script>

<style scoped>
    .index-main-div {
        width: 80%;
        margin: 1% auto;
        min-height: 1000px;
    }

    .title-span {
        font-size: 20px;
    }

    .child-input-div {
        width: 50%;
        margin: 20px auto;
    }
</style>
