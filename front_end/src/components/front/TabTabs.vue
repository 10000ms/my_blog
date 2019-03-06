<template>
  <a :style="tabStyle" :href="url"><div class="tab-div">{{tab}}</div></a>
</template>

<script>
    export default {
        name: 'TabTabs',
        props: {
            tab: String,
            count: Number,
            url: String,
        },
        methods: {
            getSize() {
                let c = 0
                if (this.count < 40) {
                    c = parseInt(this.count / 2)
                } else {
                    c = 20
                }
                c = 12 + c
                c = c.toString() + 'px'
                return c
            },
        },
        computed: {
            tabStyle() {
                return {
                    'font-size': this.getSize(),
                    'margin': '0',
                    'display': 'inline-block',
                    // 'border-bottom': '1px solid #999',
                }
            }
        },
    }
</script>

<style scoped>
  .tab-div {
    display: inline-block;
    padding: 2px 20px;
    border-radius: 30px;
    border: 1px solid rgb(60, 60, 60);
    color: rgb(60, 60, 60);
    margin: 10px;
  }
  .tab-div > a {
    color: inherit;
  }
  .tab-div:hover {
    background-color: rgb(60, 60, 60);
    color: rgb(255, 255, 255);
  }
</style>
