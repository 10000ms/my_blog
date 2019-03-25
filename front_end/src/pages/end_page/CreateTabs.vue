<template>
    <div class="index-main-div">
        <Input v-model="tab" placeholder="请输入标签..." size="large" style="width: 30%"/>
        <Button type="success" @click="submit" size="large">提交</Button>
    </div>
</template>

<script>
    export default {
        name: 'CreateTabs',
        data() {
            return {
                tab: '',
            }
        },
        methods: {
            submit() {

            },
        },

    }
</script>

<style scoped>
    .index-main-div {
        width: 80%;
        margin: 1% auto;
        min-height: 1000px;
    }
</style>
