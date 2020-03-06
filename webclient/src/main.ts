import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import jquery from "jquery";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.js";
import "bootstrap-vue/dist/bootstrap-vue";
import BootstrapVue from "bootstrap-vue";

// 引入elementui
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

// TODO:[-] 20-01-04 引入fortAwesome
// import 'font-awesome/css/font-awesome.min.css';
import { library } from '@fortawesome/fontawesome-svg-core';
import { fas } from '@fortawesome/free-solid-svg-icons';
import { far } from '@fortawesome/free-regular-svg-icons';
import { fab } from '@fortawesome/free-brands-svg-icons';
import { FontAwesomeIcon, FontAwesomeLayers, FontAwesomeLayersText } from '@fortawesome/vue-fontawesome';

library.add(fas, far, fab);
Vue.component('font-awesome-icon', FontAwesomeIcon);
Vue.component('font-awesome-layers', FontAwesomeLayers);
Vue.component('font-awesome-layers-text', FontAwesomeLayersText);
Vue.config.productionTip = false;

Vue.use(BootstrapVue);
Vue.use(ElementUI);
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
