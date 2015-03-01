;(function() {
	"use strict";

	angular.module("app.filters", [])

	.filter('iconify', ['$filter', function ($filter) {
		return function (value) {
			return value.replace(' ', '-').toLowerCase();
		};
	}]);

}());

