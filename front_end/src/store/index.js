import Vue from 'vue';
import Vuex from 'vuex';
import auth from './modules/auth';
import blog from './modules/blog';
import webMessages from './modules/webMessages';

Vue.use(Vuex);


export default new Vuex.Store({
    modules: {
        auth,
        blog,
        webMessages,
    },
});
