<template>
    <div class="thin-content-div text-align-left-div">
        <div class="category-div" v-for="c in categories" :key="c.id">
            <div class="color-common-black-items">
                <router-link :to="'/search/' + mode + '/' + c.id + '/'">
                    <span v-html="printLevel(getLevel(c.id))" class="count-span"></span>
                    {{c.title}}
                    <span class="count-span">({{c.count}})</span>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
    import categoryUtils from '../../utils/category';
    import message from '../../utils/message';

    export default {
        name: 'Categories',

        data() {
            return {
                categories: [],
                mode: 'categoryQuery',
            };
        },

        mounted() {
            this.init()
        },

        methods: {
            init() {
                this.$Loading.start();
                this.$api.category()
                    .then(res => {
                        this.categories = res.data;
                        this.$Loading.finish();
                    })
                    .catch(error => {
                        message.dealReturnMessage(error.msg, this, 'warning');
                    });
            },
            getLevel(categoryId) {
                return categoryUtils.categoryGetLevel(categoryId, this.categories);
            },
            printLevel(level) {
                return categoryUtils.categoryPrintLevel(level);
            },
        },
    }
</script>

<style scoped>

</style>
