import Vue from 'vue';
import App from './App';
import { router } from './router';
import Vuex from 'vuex';
import store from './store/index';

import iView from 'iview';
import 'iview/dist/styles/iview.css';

import { log } from './utils/console';
import { axiosConfig }from './server/config';
import Secret from './utils/secret';
import ServerIndex from './server/index';

import './assets/css/common.less'
import './assets/css/theme.less'
import './assets/css/phone-common.less'

Vue.config.productionTip = false;
Vue.prototype.$log = log;
Vue.prototype.$secret = Secret;
Vue.prototype.$api = ServerIndex;

Vue.use(Vuex);
Vue.use(iView);

// 先绑定Message组建
axiosConfig(Vue.prototype.$Message);

// 配置loading条
Vue.prototype.$Loading.config({
    height: 5,
});

new Vue({
    el: '#app',
    router,
    store,
    render: h => h(App),
});
