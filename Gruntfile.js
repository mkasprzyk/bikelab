'use strict';

module.exports = function(grunt) {

  grunt.initConfig({
    dirs: {
      dest: 'ui/js'
    },
    copy: {
      js: {
        files: [
          { 
             expand: true, 
             cwd: 'node_modules/@jscad/openjscad/dist', 
             src: 'min.js', 
             dest: '<%= dirs.dest %>',
             rename: function(dest, src) {
              return dest + '/' + 'openjscad.min.js';
            }
          }
        ]
      }
    }
  });
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.registerTask('default', ['copy']);
};
