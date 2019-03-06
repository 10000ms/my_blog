<template>
  <div style="text-align: left; margin: 5% auto; width: 80%">
    <div class="category-div" v-for="c in categories" :key="c.id" >
      <a :href="c.url" class="category-a"><span v-html="printLevel(getLevel(c.id))" style="font-size: 15px"></span> {{c.name}} <span class="count-span">({{c.count}})</span></a>
    </div>
  </div>
</template>

<script>
    export default {
        name: 'Categories',
        data() {
            return {
                // TODO：排序在服务端做
                categories: [
                    {
                        id: 1,
                        name: '111',
                        fid: 0,
                        url: 'asdasd',
                        count: 5,
                    },
                    {
                        id: 2,
                        name: '112',
                        fid: 1,
                        url: 'asdasd',
                        count: 5,
                    },
                    {
                        id: 3,
                        name: '113',
                        fid: 1,
                        url: 'asdasd',
                        count: 5,
                    },
                    {
                        id: 4,
                        name: '131',
                        fid: 3,
                        url: 'asdasd',
                        count: 5,
                    },
                    {
                        id: 5,
                        name: '222',
                        fid: 0,
                        url: 'asdasd',
                        count: 5,
                    },
                    {
                        id: 6,
                        name: '333',
                        fid: 0,
                        url: 'asdasd',
                        count: 5,
                    },
                    {
                        id: 7,
                        name: '444',
                        fid: 0,
                        url: 'asdasd',
                        count: 5,
                    },
                    {
                        id: 8,
                        name: '555',
                        fid: 0,
                        url: 'asdasd',
                        count: 5,
                    },
                ]
            }
        },
        mounted() {
            // for (let i = 0; i < this.categories.length; i++) {
            //     let c = this.categories[i]
            //     c.level = this.getLevel(c.id)
            // }
        },
        methods: {
            getLevel(categoryId, nowLevel = 0) {
                for (let i = 0; i < this.categories.length; i++) {
                    let c = this.categories[i]
                    if (c.id === categoryId) {
                        if (c.fid !== 0) {
                            nowLevel++
                            nowLevel = this.getLevel(c.fid, nowLevel)
                            break
                        }
                    }
                }
                return nowLevel
            },
            printLevel(level) {
                let c = '&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp'
                if (level) {
                    return (c).repeat(level - 1) + '&nbsp&nbsp ● -- '
                } else {
                    return '● '
                }

            }
        },
        computed: {},

    }
</script>

<style scoped>
  .category-div {
    padding: 8px;
    border-bottom: 1px solid rgba(60, 60, 60, 0.3);
    font-size: 20px;

  }

  .count-span {
    font-size: 14px;
  }

  .category-a {
    color: rgb(60, 60, 60);
    /*background-color: black;*/
    /*padding: 20px 20px;*/
    /*border-radius: 50%;*/
  }

</style>
