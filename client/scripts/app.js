;(function() {
	"use strict";

	angular.module("app", [
		/* Angular modules */
		"ngRoute",
		"ngAnimate",
		"ngSanitize",

		/* 3rd Party Modules */
		"ui.bootstrap",

		/* Custom Modules */
		"app.ctrls",
		"app.directives"

	])

	// route provider
	.config(["$routeProvider", "$locationProvider", function($routeProvider, $locationProvider) {

		var routes = [
			"start"
		];

		function setRoutes(route) {
			var url = '/' + route,
				config = {
					templateUrl: "views/" + route + ".html"
				};

			$routeProvider.when(url, config);
			return $routeProvider;
		}

		routes.forEach(function(route) {
			setRoutes(route);
		});

		$routeProvider
			.when("/", {redirectTo: "/start"})
			.when("/404", {templateUrl: "views/404.html"})
			.otherwise({redirectTo: "/404"});
		

	}])
    .run(function(){
    });
}());


