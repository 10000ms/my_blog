<template>
    <div class="index-main-div">
        <span class="title-span">选择父标签标签</span>
        <div class="child-input-div">
            <i-select v-model="selectCategories" style="width: 100%;" :multiple="true" size="large">
                <i-option v-for="item in categories" :value="item.value" :key="item.value">{{ item.label }}</i-option>
            </i-select>
        </div>
        <span class="title-span">标签</span>
        <div class="child-input-div">
            <Input v-model="category" placeholder="请输入标签..." size="large" style="width: 100%"/>
        </div>
        <div class="child-input-div">
            <Button type="success" long @click="submit" size="large">提交</Button>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'CreateTabs',
        data() {
            return {
                category: '',
                selectCategories: '',
                categories: [
                    {
                        value: 'New York1',
                        label: 'New York1'
                    },
                    {
                        value: 'New York2',
                        label: 'New York2'
                    },
                    {
                        value: 'New York3',
                        label: 'New York3'
                    },
                    {
                        value: 'New York4',
                        label: 'New York4'
                    },
                ],

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

    .title-span {
        font-size: 20px;
    }

    .child-input-div {
        width: 50%;
        margin: 20px auto;
    }
</style>
