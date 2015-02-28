module.exports = function(grunt) {
    "use strict";
    // var RELOAD_PORT = 35729;
    var dirConfig = {
        src: "client",
        dest: "dist"
    };

    // Project Configuration
    grunt.initConfig({
        pkg: grunt.file.readJSON("package.json"),	// load the package.json
        // specify configuration for each plugin
        dir: dirConfig,
        uglify: {
            options: {
                mangle: false
            },
            scripts: {
                expand: true,
                cwd: "<%= dir.src %>/scripts",
                dest: "<%= dir.dest %>/scripts/_tmp",
                src: [
                    "**/*.js"
                ]
            }
        },

        copy: {
            dist: {
                expand: true,
                cwd: "<%= dir.src %>",
                dest: "<%= dir.dest %>",
                src: [
                    "*",
                    "fonts/**/*",
                    "images/**/*",
                    "views/**/*",
                    "!**/index.html", //Since we send and rename the index.dist.html
                    "!**/bower_components/**"
                ]
            }
        },
        bowercopy: {
            options: {
                runbower: false,
                srcPrefix: '<%= dir.src %>/bower_components'
            },
            dev: {
                options: {
                    destPrefix: '<%= dir.src %>/scripts/dev'
                },
                files: {
                    'less.min.js': 'less/dist/less.min.js'
                }
            },
            vendors: {
                options: {
                    destPrefix: '<%= dir.src %>/scripts/vendors'
                },
                files: {
                    'jquery.js': 'jquery/dist/jquery.js',
                    'angular.js': 'angular/angular.js'
                }
            },
            ie: {
                options: {
                    destPrefix: '<%= dir.src %>/scripts/ie'
                },
                files: {
                    'matchMedia.js': 'matchMedia/matchMedia.js'
                }
            },
            plugins: {
                options: {
                    destPrefix: '<%= dir.src %>/scripts/plugins'
                },
                files: {
                    'angular-route.js': 'angular-route/angular-route.js',
                    'angular-animate.js': 'angular-animate/angular-animate.js',
                    'angular-sanitize.js': 'angular-sanitize/angular-sanitize.js',
                    'ui-bootstrap-tpls.js': 'angular-bootstrap/ui-bootstrap-tpls.js',
					'video.js': 'video.js/dist/video-js/video.js'
                    //NOTE: bower_component styles are not copied since we have custom less implementations of them with variables
                    //which means we need to include them by hand in styles/plugins
                }
            }
        },
        // Clean the distribution folder.
        clean: {
            dist: {
                src: ["<%= dir.dest %>"]
            },
            tmp: {
                src: [
                    "<%= dir.dest %>/scripts/_tmp",
                    "<%= dir.dest %>/bower_components"
                ]
            }
        },

        less: {
            options: {
                cleancss: true
            },
            dist: {
                files: [
                    {
                        expand: true,
                        cwd: "<%= dir.src %>/styles",
                        dest: "<%= dir.dest %>/styles",
                        src: "main.less",
                        ext: ".min.css"
                    },
                    {
                        expand: true,
                        cwd: "<%= dir.src %>/styles/bootstrap",
                        dest: "<%= dir.dest %>/styles",
                        src: "bootstrap.less",
                        ext: ".min.css"
                    }
                ]
            },
            dev: {
                files: [
                    {
                        expand: true,
                        cwd: "<%= dir.src %>/styles/bootstrap",
                        dest: "<%= dir.src %>/styles/vendors",
                        src: "bootstrap.less",
                        ext: ".min.css"
                    },
                    {
                        expand: true,
                        cwd: "<%= dir.src %>/styles",
                        dest: "<%= dir.src %>/_tmp",
                        src: "main.less",
                        ext: ".min.css"
                    }

                ]
            }
        },

        jshint: {
            all: ["Gruntfile.js", "<%= dir.src %>/scripts/**/*.js"]
        },

        concat: {
            options: {
                separator: grunt.util.linefeed + '\n' + grunt.util.linefeed
            },
            vendors: {
                src: [
                    "<%= dir.dest %>/scripts/_tmp/vendors/jquery.js",	// this must be before angular, because some custom script depend on jquery
                    "<%= dir.dest %>/scripts/_tmp/vendors/angular.js"
                ],
                dest: "<%= dir.dest %>/scripts/vendors.js"
            },
            plugins: {
                src: ["<%= dir.dest %>/scripts/_tmp/plugins/*.js"],
                dest: "<%= dir.dest %>/scripts/plugins.js"
            },
            ie: {
                src: ["<%= dir.dest %>/scripts/_tmp/ie/matchMedia.js"],
                dest: "<%= dir.dest %>/scripts/ie/matchMedia.js"
            },
            custom: {
                src: [
                    "<%= dir.dest %>/scripts/_tmp/**/*.js",
                    "!<%= dir.dest %>/scripts/_tmp/ie/*.js",		// exclude ie
                    "!<%= dir.dest %>/scripts/_tmp/vendors/*.js",	// already done
                    "!<%= dir.dest %>/scripts/_tmp/plugins/*.js"	// already done
                ],
                dest: "<%= dir.dest %>/scripts/app.js"
            }

        },
        rename: {
            //Need to use index.dist.html since it has the proper include references
            index: {
                src: "<%= dir.dest %>/index.dist.html",
                dest: "<%= dir.dest %>/index.html"
            }
        }


    });

    // Load  all grunt plugins
    grunt.loadNpmTasks("grunt-contrib-uglify");
    grunt.loadNpmTasks("grunt-contrib-jshint");
    grunt.loadNpmTasks("grunt-contrib-watch");
    grunt.loadNpmTasks("grunt-contrib-clean");
    grunt.loadNpmTasks("grunt-contrib-copy");
    grunt.loadNpmTasks("grunt-contrib-concat");
    grunt.loadNpmTasks("grunt-contrib-less");
    grunt.loadNpmTasks("grunt-rename");
    grunt.loadNpmTasks("grunt-bowercopy");

    // Default Task (that can be run by typing only "grunt" in cmd)
    grunt.registerTask("default", ["build"]);
    grunt.registerTask("cleanBuild", ["clean:dist"]);
    grunt.registerTask("build", ["clean:dist", "copy:dist", "bowercopy", "less:dist", "uglify", "concat", "rename:index", "clean:tmp"]);
    grunt.registerTask("dev", ["less:dev"]);
};