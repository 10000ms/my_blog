import marked from 'marked';
import hljs from 'highlight.js';

export const Markdown = (content) => {
    return marked(content, {
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
}
