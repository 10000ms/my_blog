<template>
  <div class="main-div">
    <div class="child-div child-border-div">
      <div class="child-input-div">
        <Button type="success" long @click="submit" size="large">提交</Button>
      </div>
      <span class="title-span">标题</span>
      <Input v-model="title" placeholder="请输入标题..." class="child-input-div" size="large"/>
      <span class="title-span">标签</span>
      <div class="child-input-div">
        <i-select v-model="selectTabs" style="width: 100%;" :multiple="true" size="large">
          <i-option v-for="item in tabs" :value="item.value" :key="item.value">{{ item.label }}</i-option>
        </i-select>
      </div>
      <span class="title-span">分类</span>
      <div class="child-input-div">
        <i-select v-model="selectCategories" style="width: 100%;" size="large">
          <i-option v-for="item in categories" :value="item.value" :key="item.value">{{ item.label }}</i-option>
        </i-select>
      </div>
      <span class="title-span">简介</span>
      <Input v-model="brief" placeholder="请输入简介..." type="textarea" :autosize="{ minRows: 3, maxRows: 10 }"
             class="child-input-div" size="large"/>
      <div class="child-input-div">
        <span class="title-span">是否自动生成简介:  </span>
        <i-switch v-model="autoBrief" @on-change="changeAutoBrief" class="child-input-div">
          <span slot="open">是</span>
          <span slot="close">否</span>
        </i-switch>
      </div>
      <span class="title-span">正文</span>
      <Input v-model="content" placeholder="请输入正文内容..." type="textarea" :autosize="{ minRows: 10, maxRows: 100 }"
             size="large"/>
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
                selectTabs: [],
                selectCategories: '',
                tabs: [
                    {
                        value: 'New York1',
                        label: 'New York1'
                    },
                    {
                        value: 'New York2',
                        label: 'New York2'
                    },
                    {
                        value: 'New York3',
                        label: 'New York3'
                    },
                    {
                        value: 'New York4',
                        label: 'New York4'
                    },
                ],
                categories: [
                    {
                        value: 'New York1',
                        label: 'New York1'
                    },
                    {
                        value: 'New York2',
                        label: 'New York2'
                    },
                    {
                        value: 'New York3',
                        label: 'New York3'
                    },
                    {
                        value: 'New York4',
                        label: 'New York4'
                    },
                ],
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
            submit() {
              this.$log('点击了提交');
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
                    'highlight': function (code, lang) {
                        //使用 highlight 插件解析文档中代码部分
                        return hljs.highlightAuto(code, [lang]).value;
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
  }

  .title-span {
    font-size: 20px;
  }

  .child-border-div {
    border: 1px #c8c8c8;
    border-right-style: solid;
    padding-right: 10px;
    margin-right: 10px;
  }

  .child-input-div {
    margin: 20px 0;
  }
</style>
