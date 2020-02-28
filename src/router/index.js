import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("@/components/HelloWorld.vue")
    },
    {
      path: "/example",
      name: "example",
      component: () => import("@/components/Example.vue")
    },
    {
      path: "/example2",
      name: "example2",
      component: () => import("@/components/Example2.vue")
    }
  ]
});
