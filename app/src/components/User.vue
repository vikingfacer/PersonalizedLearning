<template>   
   <div>
      <nav-bar v-if="showNav"></nav-bar>
      <section class="hero is-primary">
         <div class="hero-head">
         </div>
         <div class="hero-body">
            <div class="container">
               <div class="columns">
                  <div class="column is-one-third is-flex-col box">
                     <span class="title is-size-5">My Personality</span>
                     <a v-if="user.mbti_value" class="subtitle tag is-medium" :class="getColor(user.mbti_color_id)">{{ user.mbti_value }}</a>
                     <span v-else class="subtitle tag is-medium is-warning">Take the Personality Test</span> 
                     <br/>
                     <span class="title is-size-5">My Learning Type</span>
                     <a v-if="user.lp_value" class="subtitle tag is-medium" :class="getColor(user.lp_color_id)">{{ user.lp_value }}</a>
                     <span v-else class="subtitle tag is-medium">Take the Learning Type Test</span>                    
                  </div>
                  <div class="column">
                     <div class="field is-pulled-right">
                        <label class="label has-text-light is-size-5">Take the tests</label>
                        <div class="control buttons has-addons">
                           <router-link to="/forms/mbti" class="button is-large">Personality</router-link>
                           <router-link to="/forms/lp" class="button is-large">Learning Type</router-link>
                        </div>
                     </div>
                  </div>
               </div>
            </div>
         </div>
      </section>
      <search-component></search-component>
   </div>
</template>

<script>
   import NavBar from './Nav.vue';
   import SearchComponent from './Search.vue';

   export default {
      name: "user",
      data: function() {
         return {
            user: {}
         }         
      },
      created: function() {
         let user = localStorage.getItem("user");
         if(!user) this.$router.push("/login");         

         this.user = JSON.parse(user);
      },
      methods: {
         getColor: function(val) {
            return "color-" + val;
         }
      },
      props: {
         showNav: {
            type: Boolean,
            default: false
         }
      },
      components: {
         NavBar,
         SearchComponent
      }
   }
</script>

<style>
   .box .title {
      margin-bottom: 2.25rem;
   }
</style>