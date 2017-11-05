const webpack = require('webpack');
const path = require('path');

module.exports = {   
   entry: {      
      "main": './src/js/main.js'
   },
   //devtool: 'inline-source-map',
   output: {
      filename: 'js/[name].js',
      path: path.resolve(__dirname, 'dist/')
   },
   module: {
      rules: [
         {
            test: /\.js$/,
            exclude: /(node_modules|bower_components)/,
            use: {
               loader: 'babel-loader',
               options: {
                  presets: ['env']                
               }
            }
         },
         {
            test: /\.vue$/,
            exclude: /(node_modules|bower_components)/,
            use: {
               loader: 'vue-loader'
            }
         }
      ]
   },
   resolve: {
      alias: {
         'vue$': 'vue/dist/vue.esm.js' // Map 'import Vue from "vue"' to 'vue.esm.js'
      }
   },
   plugins: [   
      new webpack.DefinePlugin({
         'process.env': {
            //NODE_ENV: '"production"'
            NODE_ENV: '"development"'
         }
      })
   ]
}