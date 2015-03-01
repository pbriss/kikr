;(function() {
"use strict";

angular.module("app.directives", [])


	.directive('toggleSidebar', [function() {
		return {
			restrict: 'A',
			link: function(scope, el, attrs) {

				el.click(function(e) {
					//Make sure the target is not the floating sidebar itself
					if ($(e.target).is('i') || $(e.target).is('a')) {
						scope.sidebarOpen = scope.sidebarOpen ? false : true;
					}
				});
			}
		}
	}])




}());






