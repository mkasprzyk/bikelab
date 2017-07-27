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
