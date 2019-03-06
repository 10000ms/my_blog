<template>
  <div class="single-blog-div">
    <div class="blog-header-div">
      <div class="read-count-div">
        <Icon type="md-flame" size="30"/>
        <span>{{blogData.readCount}}</span>
      </div>
      <div class="blog-title-div">
      <span class="blog-title-span">
        <router-link :to="'/' + blogData.year + '/' + blogData.month + '/' + blogData.day + '/' + blogData.did">{{blogData.title}}</router-link>
      </span>
      </div>
      <time class="time">
        <span class="day">29</span>
        <span class="month">/ Dec</span>
      </time>
    </div>
    <div class="main-content">
      <div class="content">{{blogData.brief}}</div>
      <div class="tabs-container">
        <tab v-for="t in blogData.tabs" :tab="t" :key="t"></tab>
      </div>
    </div>
  </div>

</template>

<script>
    import Tab from '../main/Tab'

    export default {
        name: 'SingleBlogTab',
        components: {Tab},
        props: {
            blogData: Object,
        },
        data() {
            return {}
        },
        methods: {

        },
    }
</script>

<style scoped>
  .single-blog-div {
    width: 95%;
    margin: 20px auto;
    background-color: #ffffff;
    /*box-shadow: 0 2px 3px 0 rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12), 0 1px 2px -1px rgba(0, 0, 0, 0.2);*/
    border-radius: 5px;
    text-align: justify;
    padding: 10px;
    color: #333;
    position: relative;
    border: 2px solid #f1f1f1;
    border-left: 6px solid rgb(246, 141, 66);
  }

  /*.single-blog-div:before {*/
  /*content: "";*/
  /*position: absolute;*/
  /*top: 0;*/
  /*left: 0;*/
  /*width: 120px;*/
  /*height: 100%;*/
  /*background: linear-gradient(left, #ddd 0%, #fff 100%);*/
  /*}*/

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

  .main-content {
    min-height: 150px;
    border-left: 1px solid #ccc;
    margin-left: 160px;
    line-height: 1.6;
    padding: 15px 20px 15px;
    margin-top: -15px;
    position: relative;
  }

  .main-content:before {
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
    color: #000;
  }

  .blog-title-span > a:hover {
    font-size: 2em;
    color: rgba(246, 141, 66, 1) !important;
  }

  .content {
    color: #333;
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
