<template>
    <div class="thin-content-div height-min-height-div">
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
                    <count-to :end="infor1.count" count-class="count-style"/>
                    <p>{{ infor3.title }}</p>
                </infor-card>
            </div>
            <div class="index-header-child-div">
                <infor-card shadow :color="infor4.color" :icon="infor4.icon" :icon-size="36">
                    <count-to :end="infor2.count" count-class="count-style"/>
                    <p>{{ infor4.title }}</p>
                </infor-card>
            </div>
            <div class="index-header-child-div">
                <infor-card shadow :color="infor5.color" :icon="infor5.icon" :icon-size="36">
                    <count-to :end="infor1.count" count-class="count-style"/>
                    <p>{{ infor5.title }}</p>
                </infor-card>
            </div>
            <div class="index-header-child-div">
                <infor-card shadow :color="infor6.color" :icon="infor6.icon" :icon-size="36">
                    <count-to :end="infor2.count" count-class="count-style"/>
                    <p>{{ infor6.title }}</p>
                </infor-card>
            </div>
        </div>
        <div>
            <div id="id-allmap"></div>
        </div>
        <div>
            <blog-chart style="height: 310px;margin-top: 40px"></blog-chart>
        </div>
    </div>
</template>

<script>
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
                infor1: {
                    title: '昨日浏览',
                    icon: 'md-book',
                    count: 803,
                    color: 'rgb(45,140,240)',
                },
                infor2: {
                    title: '总共浏览',
                    icon: 'md-infinite',
                    count: 150000,
                    color: 'rgb(245,141,66)',
                },
                infor3: {
                    title: '昨日评论',
                    icon: 'md-chatbubbles',
                    count: 150000,
                    color: 'rgb(45,140,240)',
                },
                infor4: {
                    title: '总共评论',
                    icon: 'md-infinite',
                    count: 150000,
                    color: 'rgb(245,141,66)',
                },
                infor5: {
                    title: '昨日点赞',
                    icon: 'md-heart-outline',
                    count: 150000,
                    color: 'rgb(45,140,240)',
                },
                infor6: {
                    title: '总共点赞',
                    icon: 'md-infinite',
                    count: 150000,
                    color: 'rgb(245,141,66)',
                },
                mapStyle: {},
            };
        },

        methods: {
            addScript() {
                let script = document.createElement('script');
                script.type = 'text/javascript';
                script.src = 'http://api.map.baidu.com/api?v=3.0&ak=' + this.$secret.baiduMapAK + '&callback=init';
                document.head.appendChild(script);
                let script2 = document.createElement('script');
                script2.type = 'text/javascript';
                script2.src = 'http://unpkg.com/inmap/dist/inmap.min.js';
                document.head.appendChild(script2);
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
                let mapData = [
                    {
                        name: '北京',
                        geometry: {
                            type: 'Point',
                            coordinates: ['116.3', '39.9']
                        },
                        style: {
                            color: 'rgba(200, 200, 50, 0.7)',
                            speed: 0.5,
                        }
                    },
                    {
                        name: '上海',
                        geometry: {
                            type: 'Point',
                            coordinates: ['121.29', '31.11']
                        },
                        style: {
                            color: '#6EE7FF',
                            speed: 1,
                            size: 40,
                        }
                    },
                    {
                        name: '福建',
                        geometry: {
                            type: 'Point',
                            coordinates: ['117.984943', '26.050118']
                        },
                        style: {
                            color: '#90EE90',
                            speed: 0.45,
                        }
                    },
                    {
                        name: '广东',
                        geometry: {
                            type: 'Point',
                            coordinates: ['113.394818', '23.408004']
                        },
                        style: {
                            color: '#f8983a',
                            speed: 0.9,
                        }
                    },
                    {
                        name: '广西',
                        geometry: {
                            type: 'Point',
                            coordinates: ['108.924274', '23.552255']
                        },
                        style: {
                            color: '#FAFA32',
                            speed: 0.8,
                            size: 50,
                        }
                    },
                ];
                let overlay = new inMap.PointAnimationOverlay({
                    style: {
                        fps: 90, //动画帧数
                        color: "#FAFA32",
                        size: 20,
                        speed: 0.15,
                    },
                    data: mapData,
                });
                myInmap.add(overlay);
            },
        },

        mounted() {
            this.addScript();
            this.addMap();
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
</style>
