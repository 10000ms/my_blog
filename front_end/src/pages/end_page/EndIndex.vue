<template>
    <div class="thin-content-div height-min-height-div">
        <span class="content-title-items">总览</span>
        <div>
            <div class="index-header-child-div">
                <infor-card shadow :color="infor1.color" :icon="infor1.icon" :icon-size="36">
                    <count-to :end="infor1.count" count-class="count-style"/>
                    <p>{{ infor1.title }}</p>
                </infor-card>
            </div>
            <div class="index-header-child-div">
                <infor-card shadow :color="infor2.color" :icon="infor2.icon" :icon-size="36">
                    <count-to :end="infor2.count" count-class="count-style"/>
                    <p>{{ infor2.title }}</p>
                </infor-card>
            </div>
            <div class="index-header-child-div">
                <infor-card shadow :color="infor3.color" :icon="infor3.icon" :icon-size="36">
                    <count-to :end="infor3.count" count-class="count-style"/>
                    <p>{{ infor3.title }}</p>
                </infor-card>
            </div>
            <div class="index-header-child-div">
                <infor-card shadow :color="infor4.color" :icon="infor4.icon" :icon-size="36">
                    <count-to :end="infor4.count" count-class="count-style"/>
                    <p>{{ infor4.title }}</p>
                </infor-card>
            </div>
            <div class="index-header-child-div">
                <infor-card shadow :color="infor5.color" :icon="infor5.icon" :icon-size="36">
                    <count-to :end="infor5.count" count-class="count-style"/>
                    <p>{{ infor5.title }}</p>
                </infor-card>
            </div>
            <div class="index-header-child-div">
                <infor-card shadow :color="infor6.color" :icon="infor6.icon" :icon-size="36">
                    <count-to :end="infor6.count" count-class="count-style"/>
                    <p>{{ infor6.title }}</p>
                </infor-card>
            </div>
        </div>
        <div class="clear-div"></div>
        <div class="monitor-block-div">
            <span class="content-title-items">七天情况总览</span>
            <div>
                <blog-chart style="height: 310px;margin-top: 40px"></blog-chart>
            </div>
        </div>
        <div class="monitor-block-div">
            <span class="content-title-items">七天热度图</span>
            <div>
                <div id="id-allmap"></div>
            </div>
        </div>
    </div>
</template>

<script>
    import { mapState } from 'vuex';

    import InforCard from '../../components/end/InforCard.vue';
    import countTo from '../../components/end/CountTo.vue';
    import BlogChart from '../../components/end/BlogChart';

    export default {
        name: 'EndIndex',

        components: {
            BlogChart,
            InforCard,
            countTo,
        },

        data() {
            return {
                ak: this.$secret.baiduMapAK,
                mapStyle: {},
            };
        },

        methods: {
            addScript() {
                if (! document.getElementById('id-script-baidu-map')) {
                    let script = document.createElement('script');
                    script.id = 'id-script-baidu-map';
                    script.type = 'text/javascript';
                    script.src = 'http://api.map.baidu.com/api?v=3.0&ak=' + this.$secret.baiduMapAK + '&callback=init';
                    document.head.appendChild(script);
                }
                if (! document.getElementById('id-script-inmap')) {
                    let script2 = document.createElement('script');
                    script2.type = 'id-script-inmap';
                    script2.type = 'text/javascript';
                    script2.src = 'http://unpkg.com/inmap/dist/inmap.js';
                    document.head.appendChild(script2);
                }
            },
            addMap() {
                let check = setInterval(() => {
                    // 判断百度地图的代码是否加载进来了，加载进来才能使用inmap
                    if (window.BMap && 'version' in window.BMap && window.inMap) {
                        this.addInMap();
                        clearInterval(check);
                    }
                }, 100);
            },
            addInMap() {
                /*eslint-disable no-undef*/
                // 异步加载的js文件，忽略no-undef
                let myInmap = new inMap.Map({
                    id: 'id-allmap',
                    skin: "Blueness",
                    center: [105.403119, 38.028658], //地图中心点
                    zoom: {
                        value: 5, //当前地图级别
                        show: false, //放大缩小按钮显示
                        max: 5,
                        min: 5,
                    },
                });
                // 设置禁止拖拽
                myInmap.getMap().disableDragging();
                let mapData = this.mapData;
                let overlay = new inMap.PointAnimationOverlay({
                    style: {
                        fps: 30, //动画帧数
                        color: "#FAFA32",
                        size: 20,
                        speed: 0.15,
                    },
                    data: mapData,
                });
                myInmap.add(overlay);
            },

            randomColor() {
                let color = [
                    '#c7b289',
                    '#FAFA32',
                    '#f8983a',
                    '#6EE7FF',
                    '#90EE90',
                    '#f86563',
                    '#CFE8FF',
                    '#e0a6ff',
                ];
                let index = Math.round(Math.random() * color.length);
                return color[index];
            },

            /**
             * 计算size
             * @param number
             * @returns {number}
             */
            mapSize(number) {
                number = parseInt(number);
                let res = 0;
                if (number === 0) {
                    return  0;
                }
                if (number === 1) {
                    res = 1;
                } else if (number < 10) {
                    res = 4;
                } else if (number < 100) {
                    res = 10;
                } else if (number < 1000) {
                    res = 25;
                } else if (number < 10000) {
                    res = 40;
                } else {
                    res = 50;
                }
                return res
            },

            createMapDict(city, lat, lng, size) {
                return {
                    name: city,
                    geometry: {
                        type: 'Point',
                        coordinates: [lng, lat]
                    },
                    style: {
                        color: this.randomColor(),
                        speed: 1,
                        size: this.mapSize(size),
                    }
                };
            },
        },

        mounted() {
            this.addScript();
            this.addMap();
        },

        computed: {
            ...mapState('count', {
                day: state => state.day,
                region: state => state.region,
            }),

            infor1() {
                return {
                    title: '昨日浏览',
                    icon: 'md-book',
                    count: this.day.seven_day[0].read_count,
                    color: 'rgb(45,140,240)',
                };
            },

            infor2() {
                return {
                    title: '总共浏览',
                    icon: 'md-infinite',
                    count: this.day.total.read_count,
                    color: 'rgb(245,141,66)',
                };
            },

            infor3() {
                return {
                    title: '昨日评论',
                    icon: 'md-chatbubbles',
                    count: this.day.seven_day[0].comment_count,
                    color: 'rgb(45,140,240)',
                };
            },

            infor4() {
                return {
                    title: '总共评论',
                    icon: 'md-infinite',
                    count: this.day.total.comment_count,
                    color: 'rgb(245,141,66)',
                };
            },
            infor5() {
                return {
                    title: '昨日点赞',
                    icon: 'md-heart-outline',
                    count: this.day.seven_day[0].like_count,
                    color: 'rgb(45,140,240)',
                };
            },

            infor6() {
                return {
                    title: '总共点赞',
                    icon: 'md-infinite',
                    count: this.day.total.like_count,
                    color: 'rgb(245,141,66)',
                };
            },

            mapData() {
                let res = [];
                for (let i = 0; i < this.region.length; i++) {
                    res.push(this.createMapDict(
                        this.region[i].region__city,
                        this.region[i].region__lat,
                        this.region[i].region__lng,
                        this.region[i].count,
                    ))
                }
                return res
            }
        },
    }
</script>

<style scoped>
    .index-header-child-div {
        border: #000000 2px;
        float: left;
        width: 40%;
        height: 120px;
        padding-bottom: 10px;
        margin: 1% 5%;
    }

    #id-allmap {
        width: 100%;
        height: 700px;
    }

    .monitor-block-div {
        margin-top: 40px;
        border-top: 2px solid rgba(235, 150, 72, 0.7);
    }

    .content-title-items {
        display: block;
        margin: 20px;
    }
</style>
