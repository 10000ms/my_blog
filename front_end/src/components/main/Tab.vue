<template>
    <div>
        <Icon type="ios-pricetag"/>
        <span class="tab-span">{{tab}}</span>
    </div>
</template>

<script>
    export default {
        name: 'Tab',

        props: {
            tab: String,
        },

        data() {
            return {

            };
        },

        methods: {

        },
    }
</script>

<style scoped>
    .tab-span {
        color: #999;
    }

</style>
