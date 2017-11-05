var exec = require('child_process').exec;
var gulp = require("gulp");
var flatten = require('gulp-flatten');
var sass = require("gulp-sass");
var html = require('gulp-htmlmin');
//var del = require('del');

gulp.task("default", ["development"]);
gulp.task("development", ["clean", "build", "webpack"]);
gulp.task("production", ["clean", "build:production", "webpack:production"]);

gulp.task("clean", function() {
   //return del("./dist");
});

gulp.task("build", function () {   
   gulp.src("src/scss/*.scss") 
      .pipe(sass())
      .pipe(flatten())
      .pipe(gulp.dest("dist/css"));

   gulp.src("src/assets/*")
      .pipe(gulp.dest("dist/assets"));

   gulp.src("src/components/*.vue")
      .pipe(gulp.dest("dist/components"));

   gulp.src("src/**/*.html")
      .pipe(gulp.dest("dist"));   
});

gulp.task("build:production", function () {   
   gulp.src("src/scss/*.scss")
      .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
      .pipe(flatten())
      .pipe(gulp.dest("dist/css"));

   gulp.src("src/assets/*")
      .pipe(gulp.dest("dist/assets"));

   gulp.src("src/**/*.html")
      .pipe(html({collapseWhitespace: true}))      
      .pipe(gulp.dest("dist"));   
});

gulp.task("webpack", function() {
   exec("webpack --config webpack.js --devtool inline-source-map", function(err, stdout, stderr) {
      console.log(stdout);
      console.log(stderr);
   });
});

gulp.task("webpack:production", function() {
   // For minified JS: --optimize-minimize
   exec("webpack --config webpack.js --optimize-minimize", function(err, stdout, stderr) {
      console.log(stdout);
      console.log(stderr);
   });   
});

