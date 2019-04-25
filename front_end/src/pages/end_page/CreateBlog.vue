<template>
    <div class="max-width">
        <div class="child-div child-border-div height-min-height-div">
            <div class="child-input-div">
                <Button type="success" long @click="submit" size="large">提交</Button>
            </div>
            <span class="content-title-items">标题</span>
            <Input v-model="title" placeholder="请输入标题..." class="child-input-div" size="large"/>
            <span class="content-title-items">标签</span>
            <div class="child-input-div">
                <i-select v-model="selectTabs" class="max-width" :multiple="true" size="large">
                    <i-option v-for="item in tabs" :value="item.value" :key="item.value">{{ item.label }}</i-option>
                </i-select>
            </div>
            <span class="content-title-items">分类</span>
            <div class="child-input-div">
                <i-select v-model="selectCategories" class="max-width" size="large">
                    <i-option v-for="item in categories" :value="item.value" :key="item.value">{{ item.label }}
                    </i-option>
                </i-select>
            </div>
            <span class="content-title-items">简介</span>
            <Input v-model="brief" placeholder="请输入简介..." type="textarea" :autosize="{ minRows: 3, maxRows: 10 }"
                   class="child-input-div" size="large"/>
            <div class="child-input-div">
                <span class="content-title-items">是否自动生成简介:  </span>
                <i-switch v-model="autoBrief" @on-change="changeAutoBrief" class="child-input-div">
                    <span slot="open">是</span>
                    <span slot="close">否</span>
                </i-switch>
            </div>
            <span class="content-title-items">正文</span>
            <Input v-model="content" placeholder="请输入正文内容..." type="textarea" :autosize="{ minRows: 10, maxRows: 100 }"
                   size="large"/>
        </div>
        <div class="child-div markdown-div" v-html="compiledMarkdown"></div>
    </div>
</template>

<script>
    import '../../assets/css/marked.less';
    import 'highlight.js/styles/xcode.css';
    import removeMd from 'remove-markdown';
    import { Markdown } from '../../utils/markdown.js';

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
                        label: 'New York1',
                    },
                    {
                        value: 'New York2',
                        label: 'New York2',
                    },
                    {
                        value: 'New York3',
                        label: 'New York3',
                    },
                    {
                        value: 'New York4',
                        label: 'New York4',
                    },
                ],
                categories: [
                    {
                        value: 'New York1',
                        label: 'New York1',
                    },
                    {
                        value: 'New York2',
                        label: 'New York2',
                    },
                    {
                        value: 'New York3',
                        label: 'New York3',
                    },
                    {
                        value: 'New York4',
                        label: 'New York4',
                    },
                ],
            };
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

            },
        },

        watch: {
            content(val) {
                if (this.autoBrief) {
                    this.brief = this.getBrief(val);
                }
            }
        },

        computed: {
            compiledMarkdown() {
                return Markdown(this.content);
            },
        },
    }
</script>

<style scoped>

</style>
