import Vue from 'vue';
import App from './App';
import router from './router';
import Vuex from 'vuex';
import store from './store/index';

import iView from 'iview';
import 'iview/dist/styles/iview.css';
import LightTimeline from 'vue-light-timeline';

import Console from './utils/Console';

Vue.config.productionTip = false;
Vue.prototype.$log = Console.log;
Vue.prototype.$bus = new Vue();

Vue.use(Vuex);
Vue.use(iView);
Vue.use(LightTimeline);

new Vue({
    el: '#app',
    router,
    store,
    render: h => h(App),
});
