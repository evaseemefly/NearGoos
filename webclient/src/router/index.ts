import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Content from "../views/Content.vue";
import OverView from "../views/content/OverView.vue";
import Product from "../views/content/Product.vue";
import DataView from "../views/content/Data.vue";
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/content",
    name: "content",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: Content,
    children: [
      {
        path: "overview",
        component: OverView,
        meta: []
      },
      {
        path: "product",
        component: Product,
        meta: []
      },
      {
        path: "data",
        component: DataView,
        meta: []
      }
    ]
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
