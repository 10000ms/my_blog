<template>
    <div class="thin-content-div text-align-left-div">
        <timeline>
            <timeline-item v-for="b in blogs" :key="b.id" bg-color="rgba(246, 141, 66, 1)" icon-size="large">
                <router-link :to="'/blog/' + b.id + '/'">
                    <span class="time-span content-content-items">{{getTime(b.create_time)}}:</span>
                    <span class="content-title-items">{{b.title}}</span>
                </router-link>
            </timeline-item>
        </timeline>
        <div class="text-align-center-div">
            <Page
                    :total="blogsPage['count']"
                    :current="currentPage"
                    @on-change="changePage"
                    v-if="blogsPage['count'] > 10"
                    show-elevator
                    show-total
            />
        </div>
    </div>
</template>

<script>
    import { Timeline, TimelineItem } from 'vue-cute-timeline';

    export default {
        name: 'Archive',

        components: {
            Timeline,
            TimelineItem,
        },

        data() {
            return {
                blogs: [],
                blogsPage: {},
                currentPage: 1,
            };
        },

        mounted() {
            this.init();
        },

        methods: {
            init() {
                this.dataFromServer();
            },

            changePage(page) {
                this.dataFromServer(page);
            },

            dataFromServer(page=null) {
                let dict = {};
                if (page) {
                    dict.page = page
                }
                this.$Loading.start();
                this.$api.blogs({page: page})
                    .then(res => {
                        this.blogs = res.data;
                        this.blogsPage = res.page;
                        this.$Loading.finish();
                    });
            },

            /**
             * 获取时间字符串
             * @param timeString
             * @returns {string}
             */
            getTime(timeString) {
                let date = new Date(timeString);
                let year = date.getFullYear().toString();
                let month = (date.getMonth() + 1).toString();
                if (month.length < 2) {
                    month = '0' + month;
                }
                let day = date.getDate().toString();
                if (day.length < 2) {
                    day = '0' + day;
                }
                return `${year} - ${month} - ${day}`;
            },
        },
    }
</script>

<style scoped>
    .time-span {
        margin-right: 20px;
        float: left;
        width: 100px;
    }
</style>
