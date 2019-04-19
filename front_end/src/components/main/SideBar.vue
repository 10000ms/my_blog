<template>
    <div class="side-bar-div">
        <div class="main-profile-image-div"><img :src="websiteImage" class="website-image"/></div>
        <span class="blog-name-span">{{websiteName}}</span>
        <div class="contact-div">
            <a :href="github"><Icon type="logo-github" size="25"/></a>
            <a :href="'mailto:' + email"><Icon type="ios-mail" size="25"/></a>
        </div>
        <div class="recommend-div">
            <span class="recommend-span" v-for="r in recommends" :key="r.title"
                  @click="toRecommend(r.id)">{{r.title}}</span>
        </div>
        <div class="ad-container-div">
            <a :href="ad1URL">
                <img :src="ad1" class="ad-image"/>
            </a>
        </div>
        <div class="ad-container-div">
            <a :href="ad2URL">
                <img :src="ad2" class="ad-image"/>
            </a>
        </div>
    </div>
</template>

<script>
    import { mapState } from 'vuex';

    export default {
        name: 'side-bar',
        data() {
            return {
                recommends: [
                    {
                        title: '1111111111111111111111111111111111111',
                        id: '111111',
                    },
                    {
                        title: 22222211111111,
                        id: '222222',
                    },
                    {
                        title: 333333,
                        id: '333333',
                    },
                    {
                        title: 444444,
                        id: '444444',
                    },

                ],
            };
        },
        methods: {
            toRecommend(id) {
                this.$log(id);
            }
        },
        computed: {
            ...mapState('website', {
                websiteName: state => state.websiteName,
                websiteImage: state => state.websiteImage,
                github: state => state.github,
                email: state => state.email,
                ad1URL: state => state.ad1URL,
                ad1: state => state.ad1,
                ad2URL: state => state.ad2URL,
                ad2: state => state.ad2,
            }),
        },
    }
</script>

<style scoped>
    .side-bar-div {
        height: 100%;
        width: 350px;
        background: #512e92 url("../../assets/img/bg.jpg") no-repeat center center;
        background-size: cover;
        left: 0;
        top: 0;
        z-index: 10000;
        position: fixed;
        text-align: center;
    }

    .main-profile-image-div {
        margin-right: auto;
        margin-left: auto;
        margin-top: 25%;
        width: 120px;
        height: 120px;
        border-radius: 999em;
        background-color: black;
        overflow: hidden;
    }

    .blog-name-span {
        font-size: 40px;
        color: rgb(255, 255, 255);
    }

    .recommend-div {
        background-color: rgba(255, 255, 255, 0.2);
        width: 80%;
        margin-left: auto;
        margin-right: auto;
        margin-top: 10%;
        border-radius: 5px;
        height: 35%;
        overflow: hidden;
    }

    .recommend-span {
        font-size: 16px;
        color: rgba(255, 255, 255, 0.8);
        display: block;
        cursor: pointer;
        height: 10%;
    }

    .recommend-span:hover {
        color: rgb(45, 140, 240) !important;
    }

    .ad-container-div {
        margin-top: 8%;
        margin-left: auto;
        margin-right: auto;
        width: 80%;
        border-radius: 5px;
        height: 10%;
        background-color: rgba(255, 255, 255, 0.2);
        overflow: hidden;
    }

    .website-image {
        width: 100%;
        height: 100%;
    }

    .ad-image {
        height: 100%;
        width: 100%;
        border-radius: 5px;
    }
</style>
