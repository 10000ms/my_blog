<template>
    <div ref="dom"></div>
</template>

<script>
    import { mapState } from 'vuex';

    import echarts from 'echarts';
    import {on, off} from '../../utils/tools.js';

    export default {
        name: 'blogChart',

        data() {
            return {
                dom: null
            }
        },

        mounted() {
            this.init();
        },

        methods: {
            resize() {
                this.dom.resize()
            },

            /**
             * 获取option，用于生成最新的option
             */
            getOption() {
                return {
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'cross',
                            label: {
                                backgroundColor: '#6a7985',
                            },
                        },
                    },
                    grid: {
                        top: '3%',
                        left: '1.2%',
                        right: '1%',
                        bottom: '3%',
                        containLabel: true,
                    },
                    xAxis: [
                        {
                            type: 'category',
                            boundaryGap: false,
                            data: [
                                this.day.seven_day[6].date,
                                this.day.seven_day[5].date,
                                this.day.seven_day[4].date,
                                this.day.seven_day[3].date,
                                this.day.seven_day[2].date,
                                this.day.seven_day[1].date,
                                this.day.seven_day[0].date,
                            ],
                        },
                    ],
                    yAxis: [
                        {
                            type: 'value',
                        },
                    ],
                    series: [
                        {
                            name: '浏览',
                            type: 'line',
                            areaStyle: {
                                normal: {
                                    color: '#2d8cf0',
                                },
                            },
                            label: {
                                normal: {
                                    show: true,
                                    position: 'top',
                                },
                            },
                            data: [
                                this.day.seven_day[6].read_count,
                                this.day.seven_day[5].read_count,
                                this.day.seven_day[4].read_count,
                                this.day.seven_day[3].read_count,
                                this.day.seven_day[2].read_count,
                                this.day.seven_day[1].read_count,
                                this.day.seven_day[0].read_count,
                            ],
                        },
                        {
                            name: '评论',
                            type: 'line',
                            areaStyle: {
                                normal: {
                                    color: '#ffff4f',
                                },
                            },
                            data: [
                                this.day.seven_day[6].comment_count,
                                this.day.seven_day[5].comment_count,
                                this.day.seven_day[4].comment_count,
                                this.day.seven_day[3].comment_count,
                                this.day.seven_day[2].comment_count,
                                this.day.seven_day[1].comment_count,
                                this.day.seven_day[0].comment_count,
                            ],
                        },
                        {
                            name: '点赞',
                            type: 'line',
                            areaStyle: {
                                normal: {
                                    color: '#ff8d90',
                                },
                            },
                            data: [
                                this.day.seven_day[6].like_count,
                                this.day.seven_day[5].like_count,
                                this.day.seven_day[4].like_count,
                                this.day.seven_day[3].like_count,
                                this.day.seven_day[2].like_count,
                                this.day.seven_day[1].like_count,
                                this.day.seven_day[0].like_count,
                            ],
                        },
                    ],
                };
            },

            init() {
                const option = this.getOption();

                this.$nextTick(() => {
                    this.dom = echarts.init(this.$refs.dom);
                    this.dom.setOption(option);
                    on(window, 'resize', this.resize);
                });
            },
        },

        watch: {
            /**
             * watch day情况，保证图表能实时更新
             */
            day () {
                this.dom.setOption(this.getOption());
            }
        },

        computed: {
            ...mapState('count', {
                day: state => state.day,
            }),
        },

        beforeDestroy() {
            off(window, 'resize', this.resize);
        },
    }
</script>
