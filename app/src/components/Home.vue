<template>
   <div>
      <section class="hero is-light is-large">         
         <div class="hero-head">
            <nav class="navbar">
               <div class="container">
                  <div class="navbar-brand">                     
                     <span class="navbar-burger burger" data-target="navbarMenu">
                        <span></span>
                        <span></span>
                        <span></span>
                     </span>
                  </div>
                  <div id="navbarMenu" class="navbar-menu">
                     <div class="navbar-end">
                        <router-link v-if="user" class="navbar-item" to="/user">
                           Welcome, {{ user.name }}
                        </router-link>
                        <router-link v-else class="navbar-item" to="/login">
                           Login
                        </router-link>                        
                     </div>
                  </div>
               </div>
            </nav>
         </div>
         
         <div class="hero-body">
            <div class="container has-text-centered">
               <h1 class="title">
                  Personalized Learning
               </h1>
               <h2 class="subtitle">
                  Learning, personalized.
               </h2>
            </div>
         </div>
      </section>   
   </div>
</template>

<script>
   export default {
      name: "home",
      data: function() {
         return {
            user: {}
         }
      },
      created: function() {
         let user = localStorage.getItem("user");
         this.user = JSON.parse(user);
      },
      mounted: function() {
         let $navbarBurger = this.$el.querySelector('.navbar-burger');
         $navbarBurger.addEventListener('click', () => {
            let $menu = this.$el.querySelector('#' + $navbarBurger.dataset.target);
            $menu.classList.toggle('is-active');

            $menu.querySelectorAll(".navbar-item").forEach(($el) => {
               $el.addEventListener('click', () => {
                  $menu.classList.remove('is-active');
               });
            });
         });
      }
   }   
</script>