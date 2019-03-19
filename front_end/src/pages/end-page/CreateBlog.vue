<template>
  <div class="main-div">
    <div class="child-div">
      <Input v-model="title" placeholder="请输入标题..." class="child-input-div"/>
      <Input v-model="brief" placeholder="请输入简介..." type="textarea" :autosize="{ minRows: 10, maxRows: 100 }" class="child-input-div"/>
      <div style="height: 100px">
        <i-switch v-model="autoBrief" @on-change="changeAutoBrief"/>
      </div>
      <Input v-model="content" placeholder="请输入正文内容..." type="textarea" :autosize="{ minRows: 10, maxRows: 100 }"/>
    </div>
    <div class="child-div markdown-div" v-html="compiledMarkdown"></div>
  </div>
</template>

<script>
    import marked from 'marked';
    import hljs from 'highlight.js';
    import '../../assets/marked.css';
    import 'highlight.js/styles/xcode.css';
    import removeMd from 'remove-markdown';

    export default {
        name: 'CreateBlog',
        data() {
            return {
                title: '',
                brief: '',
                content: '',
                autoBrief: true,
            }
        },
        methods: {
            changeAutoBrief(status) {
                this.autoBrief = status;
            },
            getBrief(val) {
                let res = '';
                if (val.length > 200) {
                    res = val.slice(0, 196) + '......'
                } else {
                    res = val;
                }
                return removeMd(res);
            },
        },
        watch: {
            content(val) {
                if (this.autoBrief) {
                    this.brief = this.getBrief(val)
                }
            }
        },
        computed: {
            compiledMarkdown() {
                return marked(this.content, {
                    'baseUrl': null,
                    'breaks': false,
                    'gfm': true,
                    'headerIds': true,
                    'headerPrefix': '',
                    'langPrefix': 'language-',
                    'mangle': true,
                    'pedantic': false,
                    'sanitize': false,
                    'sanitizer': null,
                    'silent': false,
                    'smartLists': false,
                    'smartypants': false,
                    'tables': true,
                    'xhtml': false,
                    'highlight': function (code,lang) {
                        //使用 highlight 插件解析文档中代码部分
                        return hljs.highlightAuto(code,[lang]).value;
                    }
                })
            },
        }
    }
</script>

<style scoped>
  .main-div {
    width: 100%;
  }

  .child-div {
    margin: 1%;
    width: 45%;
    float: left;
    text-align: left;
    min-height: 1000px;
    border: aliceblue;
  }

  .child-input-div {
    margin: 20px 0;
  }
</style>
