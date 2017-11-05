<template>
   <div>      
      <nav class="navbar has-border-bottom">
         <div class="navbar-brand">         
            <span class="navbar-item title is-size-6">
               <span>Class Search</span>               
            </span>
         </div>
      </nav>
      <section id="search" class="section">
         <label class="label">Subject</label>
         <div class="field has-addons">            
            <div class="control is-expanded">
               <input class="input" type="text" placeholder="Search" v-model="subject">
            </div>
            <div class="control">
               <span id="search-loading" class="button is-static is-color-blue"></span>
            </div>
         </div>
         <hr/>
         <div>         
            <div class="box" v-for="result in results" :class="getColor(result.professor.color_id)">
               <div class="level">
                  <div class="level-start is-flex-col">
                     <span class="title">{{ result.title }}</span>
                     <div class="subtitle is-flex">
                        <i class="fa fa-fw fa-user"></i>
                        <span class="subtitle">{{ result.professor.name }}</span>
                     </div>                     
                  </div>
               </div>
            </div>
         </div>
      </section>      
   </div>
</template>

<script>
   import _ from 'lodash';
   import config from '../util/config';

   export default {
      name: "search",
      data: function() {
         return {
            title: "Class Search",
            subject: "",
            results: []
         }         
      },
      watch: {
         subject: function(val) {
            if(val.length > 0) {
               this.search();
               this.$el.querySelector("#search-loading").classList.add("is-loading");
            } else {
               this.results = [];
            }
         }
      },
      methods: {
         getColor: function(val) {
            return "bcolor-" + val;
         },
         search: _.debounce(function() {
            fetch(config.url + "/course/" + this.subject).then((res) => {
               if(res.ok) {
                  return res.json();
               }               
            }).then((res) => {               
               this.results = res;
               this.$el.querySelector("#search-loading").classList.remove("is-loading");
            });            
         }, 500)
      }
   }
</script>

<!-- [
   {
      "title": "Intro to Accounting",
      "professor": {
         "name": "Mike Nelson",
         "color": "0"
      },
      "subject": "ACCT"
   },
   {
      "title": "Intro to Accounting",
      "professor": {
         "name": "Mike Nelson",
         "color": "0"
      },
      "subject": "ACCT"
   },
   {
      "title": "Intro to Accounting",
      "professor": {
         "name": "Mike Nelson",
         "color": "0"
      },
      "subject": "ACCT"
   }
] -->