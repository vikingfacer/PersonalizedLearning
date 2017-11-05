import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

import Home from "../components/Home.vue";
import Login from "../components/Login.vue";
import Search from "../components/Search.vue";
import User from "../components/User.vue";
import Forms from "../components/Forms.vue";

let router = new VueRouter({
   routes: [
      { path: "/", component: Home },
      { path: "/search", component: Search },
      { path: "/login", component: Login, props: { showNav: true }},
      { path: "/user", component: User, props: { showNav: true }},
      { path: "/forms", redirect: "/forms/mbti"},
      { path: "/forms/:type", component: Forms, props: { showNav: true } }
   ]
});

const app = new Vue({ 
   el: "#app",   
   router: router
});