<template>
    <div :style="tabStyle">
        <router-link :to="'/search/' + mode + '/' + id + '/'">
            <div class="tab-div color-common-black-items">{{tab}}</div>
        </router-link>
    </div>
</template>

<script>
    export default {
        name: 'TabTabs',

        props: {
            tab: String,
            count: Number,
            id: Number,
        },

        data() {
            return {
                mode: 'tabQuery'
            }
        },

        methods: {
            getSize() {
                let c = 0;
                if (this.count < 40) {
                    c = parseInt((this.count / 2).toString());
                } else {
                    c = 20;
                }
                c = 12 + c;
                c = c.toString() + 'px';
                return c;
            },
            urlFromId(id) {
                this.$log(id);
            },
        },

        computed: {
            tabStyle() {
                return {
                    'font-size': this.getSize(),
                    'margin': '0',
                    'display': 'inline-block',
                };
            },
        },
    }
</script>

<style scoped>
    .tab-div {
        display: inline-block;
        padding: 2px 20px;
        border-radius: 30px;
        border: 1px solid rgb(55, 55, 55);
        margin: 10px;
    }

    .tab-div:hover {
        background-color: rgb(55, 55, 55);
        color: rgb(255, 255, 255);
    }
</style>
