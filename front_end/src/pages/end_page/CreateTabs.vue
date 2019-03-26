<template>
    <div class="height-min-height-div thin-content-div">
        <Input v-model="tab" placeholder="请输入标签..." size="large" class="min-input"/>
        <Button type="success" @click="submit" size="large">提交</Button>
    </div>
</template>

<script>
    export default {
        name: 'CreateTabs',
        data() {
            return {
                tab: '',
            };
        },
        methods: {
            submit() {

            },
        },

    }
</script>

<style scoped>
    .min-input {
        width: 30%;
    }
</style>
