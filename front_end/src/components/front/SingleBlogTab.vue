<template>
    <div class="single-blog-div color-common-black-items">
        <div class="blog-header-div">
            <div class="read-count-div">
                <Icon type="md-flame" size="30"/>
                <span>{{readCount}}</span>
            </div>
            <div class="blog-title-div">
      <span class="blog-title-span color-common-black-items">
        <router-link :to="'/blog/' + blogData.id + '/'">{{blogData.title}}</router-link>
      </span>
            </div>
            <time class="time">
                <span class="day">{{getDay}}</span>
                <span class="month">/ {{getMonth}}</span>
            </time>
        </div>
        <div class="single-blog-main-content-div">
            <div class="content color-common-black-items">{{blogData.brief}}</div>
            <div class="tabs-container">
                <tab v-for="t in blogData.tabs" :tab="t.title" :id="t.id" :key="t.id"></tab>
            </div>
        </div>
    </div>

</template>

<script>
    import Tab from '../main/Tab';
    import  month  from '../../utils/month';

    export default {
        name: 'SingleBlogTab',

        components: {
            Tab,
        },

        props: {
            blogData: Object,
        },

        data() {
            return {
                // 转化名称，使得符合js的标准
                readCount: this.blogData.read_count,
                // 获取创建时间
                date: new Date(this.blogData.create_time),
            };
        },

        computed: {
            getDay() {
                if (this.date) {
                    return this.date.getDate();
                } else {
                    return null;
                }
            },
            getMonth() {
                if (this.date) {
                    return month.monthFromNumber(this.date.getMonth() + 1);
                } else {
                    return null;
                }
            },
        },
    }
</script>

<style scoped>
    .single-blog-div {
        width: 95%;
        margin: 0 auto 20px auto;
        background-color: #ffffff;
        border-radius: 5px;
        text-align: justify;
        padding: 10px;
        position: relative;
        border: 2px solid #f1f1f1;
        border-left: 6px solid rgb(246, 141, 66);
    }

    .blog-header-div {
        border-left: 1px solid #ccc;
        margin-left: 160px;
        padding: 15px 20px;
        position: relative;
    }

    .time {
        color: #999;
        position: absolute;
        top: 15px;
        left: -140px;
        z-index: 1;
        user-select: none;
    }

    .day {
        font-size: 2em;
        color: #999;
        user-select: none;
    }

    .month {
        color: #999;
        user-select: none;
    }

    .single-blog-main-content-div {
        min-height: 150px;
        border-left: 1px solid #ccc;
        margin-left: 160px;
        line-height: 1.6;
        padding: 15px 20px 15px;
        margin-top: -15px;
        position: relative;
    }

    .single-blog-main-content-div:before {
        content: "";
        position: absolute;
        top: 15px;
        left: -5px;
        width: 7px;
        height: 7px;
        border: 1px solid #ccc;
        background: #fff;
        transform: rotate(45deg);
    }

    .blog-title-div {
        line-height: 1.1;
    }

    .blog-title-span > a {
        font-size: 2em;
    }

    .blog-title-span > a:hover {
        font-size: 2em;
        color: rgba(246, 141, 66, 1) !important;
    }

    .content {
        text-align: justify;
        font-size: 14px;
        text-shadow: 0 0 1px transparent;
        margin-top: 12px;
    }

    .tabs-container {
        color: #999;
        font-size: 0.9em;
        position: absolute;
        top: 30px;
        left: -145px;
        width: 120px;
        z-index: 1;
    }

    .read-count-div {
        position: absolute;
        right: 35px;
        top: 0;
        color: rgba(246, 141, 66, 0.4);
        font-size: 35px;
    }
</style>
