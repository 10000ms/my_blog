<template>
    <router-link :to="'/search/' + mode + '/' + id + '/'">
        <div>
            <Icon type="ios-pricetag" color="#999"/>
            <span class="tab-span">{{tab}}</span>
        </div>
    </router-link>
</template>

<script>
    export default {
        name: 'Tab',

        props: {
            tab: String,
            id: Number,
        },

        data() {
            return {
                mode: 'tabQuery',
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
