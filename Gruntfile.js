'use strict';

module.exports = function(grunt) {

  grunt.initConfig({
    dirs: {
      dest_js: 'ui/js',
      dest_css: 'ui/css'
    },
    copy: {
      js: {
        files: [
          { 
             expand: true, 
             cwd: 'node_modules/@jscad/openjscad/dist', 
             src: 'min.js', 
             dest: '<%= dirs.dest_js %>',
             rename: function(dest, src) {
              return dest + '/' + 'openjscad.min.js';
             }
	  },
	  {
             expand: true,
             cwd: 'node_modules/@jscad/openjscad',
             src: 'style.css',
             dest: '<%= dirs.dest_css %>',
          }
        ]
      }
    }
  });
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.registerTask('default', ['copy']);
};
