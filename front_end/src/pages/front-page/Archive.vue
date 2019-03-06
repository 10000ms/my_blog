<template>
  <div class="light-timeline-container-div">
    <light-timeline :items="items">
      <template v-slot:content="item">
        <router-link to="/2018/8/10">dasdasdsaadasd {{item.content}}</router-link>
      </template>
    </light-timeline>
  </div>
</template>

<script>

    export default {
        name: 'Archive',
        data () {
            return {
                items: [
                    {
                        type: 'star',
                        tag: '2018-01-12',
                        htmlMode: true,
                        content: 'halloaaaaaaaaaaaaaaaaaa',
                        color: 'rgba(246, 141, 66, 1)',
                    },
                    {
                        type: 'star',
                        tag: '2018-01-13',
                        htmlMode: true,
                        content: 'world',
                        color: 'rgba(246, 141, 66, 1)',
                    },
                    {
                        type: 'star',
                        tag: '2018-01-14',
                        htmlMode: true,
                        content: `5464564565`,
                        color: 'rgba(246, 141, 66, 1)',
                    }
                ]
            }
        },
    }
</script>

<style scoped>
  .light-timeline-container-div {
    margin: 5% 10%;
  }
  a {
    color: rgb(60, 60, 60);
    font-size: 20px;
  }
</style>
