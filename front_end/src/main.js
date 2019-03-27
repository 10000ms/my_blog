import Vue from 'vue';
import App from './App';
import router from './router';
import Vuex from 'vuex';
import store from './store/index';

import iView from 'iview';
import 'iview/dist/styles/iview.css';

import Console from './utils/console';
import Secret from './utils/secret';

import './assets/css/common.less'
import './assets/css/theme.less'

Vue.config.productionTip = false;
Vue.prototype.$log = Console.log;
Vue.prototype.$bus = new Vue();
Vue.prototype.$secret = Secret;


Vue.use(Vuex);
Vue.use(iView);

new Vue({
    el: '#app',
    router,
    store,
    render: h => h(App),
});
