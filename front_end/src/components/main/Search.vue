<template>
    <Modal
        v-model="show"
        title="Common Modal dialog box title"
        :closable="true"
        scrollable
        @on-ok="searchBlog"
    >
        <p slot="header" :style="headerStyle">
            <span>搜索</span>
        </p>
        <div class="dialog-input-div">
            <div class="dialog-single-input-div">
                <i-input v-model="search" placeholder="搜索内容"/>
            </div>
        </div>
    </Modal>
</template>

<script>
    export default {
        name: 'Search',

        data() {
            return {
                show: false,
                headerStyle: {
                    'color': 'rgba(246, 141, 66, 1)',
                    'text-align': 'center',
                    'font-size': '18px',
                    'margin': '5px',
                    'letter-spacing': '20px',
                },
                search: '',
                mode: 'search',
            };
        },

        methods: {
            openModal() {
                this.show = true;
            },

            searchBlog() {
                this.show = false;
                this.$router.push({name: 'searchMode', params: {mode: this.mode, query: this.search}});
            },
        },
    }
</script>

<style scoped>

</style>
