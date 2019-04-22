<template>
    <div class="footer-div">
        <div class="content-content-items color-common-white-items">
            <Icon type="ios-link"/>
            <span>友情链接</span>
        </div>
        <div class="thin-content-div">
            <div v-for="f in getFriendshipLink" :key="f.id" class="link-div">
                <a class="color-common-white-items" :href="f.link"><span>{{f.link}}</span></a>
            </div>
        </div>
        <div class="thin-content-div text-align-center-div content-content-items color-common-white-items">{{ICPNumber}}</div>

    </div>
</template>

<script>
    import { mapState, mapGetters } from 'vuex';

    export default {
        name: 'BlogFooter',
        data() {
            return {

            };
        },
        computed: {
            ...mapState('website', {
                ICPNumber: state => state.ICPNumber,
            }),
            ...mapGetters('website', [
                'getFriendshipLink',
            ]),
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
