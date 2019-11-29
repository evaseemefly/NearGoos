import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import jquery from "jquery";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.js";
import "bootstrap-vue/dist/bootstrap-vue";
import BootstrapVue from "bootstrap-vue";

Vue.config.productionTip = false;

Vue.use(BootstrapVue);
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
