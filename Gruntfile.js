'use strict';

module.exports = function(grunt) {

  grunt.initConfig({
    dirs: {
      dest_js: 'ui/js',
      dest_css: 'ui/css',
      patch: 'patch',
      node_modules: 'node_modules'
    },
    copy: {
      js: {
        files: [
	      {
             expand: true,
             cwd: '<%= dirs.node_modules %>/@jscad/openjscad',
             src: 'min.css',
             dest: '<%= dirs.dest_css %>',
          }
        ]
      }
    },
    exec: {
      patch: "patch -N -p0 <  <%= dirs.patch %>/min_as_module.patch | true",
      build: "browserify ui/src/bikelab.js -o <%= dirs.dest_js %>/bikelab.js"
    }
  });
  grunt.loadNpmTasks('grunt-exec');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.registerTask('default', ['exec', 'copy']);
};
