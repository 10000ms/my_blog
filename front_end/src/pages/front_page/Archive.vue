<template>
    <div class="thin-content-div text-align-left-div">
        <timeline>
            <timeline-item v-for="b in blogs" :key="b.id" bg-color="rgba(246, 141, 66, 1)" icon-size="large">
                <router-link :to="'/' + b.year + '/' + b.month + '/' + b.day + '/' + b.did">
                    <span class="time-span content-content-items">{{b.year}} - {{b.month}} - {{b.day}}:</span>
                    <span class="content-title-items">{{b.title}}</span>
                </router-link>
            </timeline-item>
        </timeline>
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
                blogs: [
                    {
                        id: 1,
                        title: '阿速達熟讀阿薩德',
                        tabs: ['11111', '222222', '33333'],
                        brief: 'asddddddddddddddasdadadada',
                        postTime: '2018-10-10',
                        author: 'asdsadas',
                        year: 2018,
                        month: 9,
                        day: 7,
                        did: 2,
                        readCount: 100,
                    },
                    {
                        id: 2,
                        title: '阿水暖搜安娜上锁部分把的速度',
                        tabs: ['11111', '222222', '33333'],
                        brief: 'asddddddddddddddasdadadada',
                        postTime: '2018-10-10',
                        author: 'asdsadas',
                        year: 2018,
                        month: 10,
                        day: 2,
                        did: 2,
                        readCount: 5,
                    },
                    {
                        id: 3,
                        title: '阿森纳新组成必备的补习班补补刀',
                        tabs: ['11111', '222222', '33333'],
                        brief: 'asddddddddddddddasdadadada',
                        postTime: '2018-10-10',
                        author: 'asdsadas',
                        year: 2018,
                        month: 10,
                        day: 2,
                        did: 2,
                        url: 'asdadasdad',
                        readCount: 0,
                    },
                    {
                        id: 4,
                        title: 'asdasdad',
                        tabs: ['11111', '222222', '33333'],
                        brief: 'asddddddddddddddasdadadada',
                        postTime: '2018-10-10',
                        author: 'asdsadas',
                        year: 2018,
                        month: 10,
                        day: 2,
                        did: 2,
                        url: 'asdadasdad',
                        readCount: 1000,
                    },
                    {
                        id: 5,
                        title: 'asdasdad',
                        tabs: ['11111', '222222', '33333'],
                        brief: 'asddddddddddddddasdadadada',
                        postTime: '2018-10-10',
                        author: 'asdsadas',
                        year: 2018,
                        month: 10,
                        day: 2,
                        did: 2,
                        url: 'asdadasdad',
                        readCount: 999,
                    },
                    {
                        id: 6,
                        title: 'asdasdad',
                        tabs: ['11111', '222222', '33333'],
                        brief: 'asddddddddddddddasdadadada',
                        postTime: '2018-10-10',
                        author: 'asdsadas',
                        year: 2018,
                        month: 10,
                        day: 2,
                        did: 2,
                        url: 'asdadasdad',
                        readCount: 264,
                    },
                ],
            };
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
