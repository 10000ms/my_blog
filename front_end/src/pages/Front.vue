<template>
  <div class="front">
    <!--边栏-->
    <side-bar></side-bar>

    <div class="right-main">
      <layout>
        <header>
          <!--菜单-->
          <blog-menu></blog-menu>
        </header>

        <content class="main-content">
          <!--主要页面-->
          <router-view/>
        </content>

        <footer>

        </footer>
      </layout>
    </div>

    <!--返回顶部-->
    <BackTop :height="50" :bottom="100" :right="15">
      <Icon type="ios-arrow-dropup-circle" size="60" color="rgba(246, 141, 66, 1)"/>
    </BackTop>
  </div>
</template>

<script>
    import SideBar from '../components/main/SideBar';
    import BlogMenu from '../components/main/BlogMenu';

    export default {
        name: 'app',
        components: {BlogMenu, SideBar},

        methods: {},
    };
</script>

<style scoped>
  .front {
    text-align: center;
    height: 100%;
  }

  .right-main {
    left: 350px;
    right: 0;
    position: absolute;
  }

  .main-content {
    background-color: #fff;
  }
</style>
