<template>
  <div class="main">
    <single-blog-tab v-for="b in blogs" :blogData="b" :key="b.id"></single-blog-tab>
  </div>
</template>

<script>
    import SingleBlogTab from '../../components/front/SingleBlogTab'

    export default {
        name: "index",
        components: {SingleBlogTab},

        data() {
            return {
                blogs: [
                    {
                        id: 1,
                        title: 'asdasdad',
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
                        title: 'asdasdad',
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
                        title: 'asdasdad',
                        tabs: ['11111', '222222', '33333'],
                        brief: 'asddddddddddddddasdadadada',
                        postTime: '2018-10-10',
                        author: 'asdsadas',
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
                        url: 'asdadasdad',
                        readCount: 264,
                    },
                ],
            }
        },
    }
</script>

<style scoped>

</style>
