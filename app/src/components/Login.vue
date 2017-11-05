<template>   
   <div>
      <nav-bar v-if="showNav"></nav-bar>
      <div id="login" class="section">
         <div class="box login" @keyup.enter="submit">
            <div class="field has-text-centered">
               <span class="is-size-3 has-text-weight-semibold">Login</span>
            </div>

            <div class="field">         
               <label class="label">UML Email</label>
               <div class="control has-icons-left">
                  <input class="input" type="text" placeholder="Email" v-model="email">
                  <span class="icon is-small is-left">
                     <i class="fa fa-user"></i>
                  </span>
               </div>         
            </div>

            <div class="field">         
               <label class="label">Password</label>
               <div class="control has-icons-left">
                  <input class="input" type="password" placeholder="Password" v-model="password">
                  <span class="icon is-small is-left">
                     <i class="fa fa-unlock"></i>
                  </span>
               </div>         
            </div>

            <div class="field">
               <div class="control">
                  <button id="submit" class="button is-primary is-pulled-right" @click="submit">Login</button>
               </div>
            </div>
         </div>
      </div>
   </div>
</template>

<script>
   import NavBar from './Nav.vue';
   import config from '../util/config';

   export default {
      name: "login",
      data: function() {
         return {
            email: "",
            password: ""
         }         
      },
      props: {
         showNav: {
            type: Boolean,
            default: false
         }
      },
      created: function() {         
         let user = localStorage.getItem("user");
         if(user) this.$router.push("/user");
      },
      methods: {
         submit: function(e) {
            let button = this.$el.querySelector("#submit");            
            button.classList.add("is-loading");

            let data = new FormData();
            data.append('email', this.email);
            data.append('password', this.password);
            
            fetch(config.url + '/login', {
               method: "POST",
               body: data
            }).then((res) => res.json())
            .then((res) => {
               localStorage.setItem("user", JSON.stringify(res));
               button.classList.remove("is-loading");
               this.$router.push("/user");
            });
         }
      },
      components: {
         NavBar
      }
   }
</script>

<style scoped>
   #login {
      display: flex;   
      width: 100%;
      justify-content: center;
   }

   .box.login {
      min-width: 300px;   
   }
</style>