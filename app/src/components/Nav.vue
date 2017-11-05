<template>
   <nav class="navbar is-primary">
      <div class="navbar-brand">         
         <span class="navbar-item title is-size-6">            
            <router-link v-if="user" class="button is-primary" to="/user">Personalized Learning</router-link>
            <router-link v-else class="button is-primary" to="/">Personalized Learning</router-link>
         </span>
      </div>
   </nav>
</template>

<script>
   export default {
      name: "Nav",
      created: function() {
         let user = localStorage.getItem("user");
         if(!user) this.$router.push("/login");

         this.user = JSON.parse(user);
      }  
   }
</script>