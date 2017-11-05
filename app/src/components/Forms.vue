<template>   
   <div>
      <nav-bar v-if="showNav"></nav-bar>
      <div id="form" class="section">
         <form class="box form" @submit.prevent="submit">
            <div class="field has-text-centered">
               <span class="is-size-3 has-text-weight-semibold is-uppercase">{{ $route.params.type }} Form</span>
            </div>

            <div v-if="$route.params.type === 'mbti'">
               <div class="field" v-for="q in questions">
                  <label class="label">{{ q.content }}</label>               
                  <div class="control">
                     <label class="radio">
                        <input type="radio" :name="q.id" value="3">
                        Yes
                     </label>
                     <label class="radio">
                        <input type="radio" :name="q.id" value="2">
                        Maybe
                     </label>
                     <label class="radio">
                        <input type="radio" :name="q.id" value="1">
                        No
                     </label>
                  </div>
               </div>
            </div>
            <div v-else-if="$route.params.type === 'lp'">
               <div class="field" v-for="q in questions">
                  <label class="label">{{ q.content }}</label>               
                  <div class="control">
                     <label class="radio" v-for="a in q.answers">
                        <input type="radio" :name="q.id" :value="a.id">
                        {{ a.content }}
                     </label>
                  </div>
               </div>
            </div>
            <div v-else>
               <div class="field">
                  Not a valid form.
               </div>
            </div>

            <!-- <div class="modal">
               <div class="modal-background"></div>
               <div class="modal-card">
                  <header class="modal-card-head">
                     <p class="modal-card-title">Results</p>
                     <button class="delete" aria-label="close"></button>
                  </header>
                  <section class="modal-card-body">
                     
                  </section>
                  <footer class="modal-card-foot">
                     <button class="button is-primary">Okay</button>                     
                  </footer>
               </div>
            </div> -->

            <div class="field is-clearfix">
               <div class="control">
                  <input type="submit" id="submit" class="button is-primary is-pulled-right" value="Submit">
               </div>
            </div>
         </form>
      </div>
   </div>
</template>

<script>
   import NavBar from './Nav.vue';   
   import config from '../util/config';

   export default {
      name: "forms",
      data: function() {
         return {
            user: {},
            questions: [],
            postUrl: ""
         }         
      },
      watch: {
         questions: function(val) {
            console.log("Questions changed:", val);
         }
      },
      created: function() {
         let user = localStorage.getItem("user");
         if(!user) this.$router.push("/login");         

         this.user = JSON.parse(user);

         fetch(config.url + "/questions/" + this.$route.params.type).then((res) => res.json())
            .then((res) => {
               this.questions = res;               
            });
      },
      methods: {
         submit: function(e) {
            let data = new FormData(e.target);
            let button = this.$el.querySelector("#submit");
            button.classList.add("is-loading");

            fetch(config.url + "/questions/" + this.$route.params.type + "/" + this.user.id, {
               method: "POST",
               body: data
            }).then((res) => res.json())
            .then((res) => {               
               button.classList.remove("is-loading");
               this.$router.push("/user");
            });
         }
      },
      props: {
         showNav: {
            type: Boolean,
            default: false
         }
      },
      components: {
         NavBar
      }
   }
</script>

<style>
   #form {
      display: flex;   
      width: 100%;
      justify-content: center;
   }

   .box.form {
      max-width: 950px;
   }
</style>