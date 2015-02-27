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


		// add full body class for custom pages.
	.directive('customPage', [function() {
		return {
			restrict: 'A',
			controller: ['$scope', '$element', '$location', function($scope, $element, $location) {
				$(window).load(function() {
					var path = function() {return $location.path()};
					var addBg = function(path) {
						$element.removeClass('body-full');
						switch(path) {
							case '/404' :
								$element.addClass('body-full');
						}
					};

					addBg($location.path());

					$scope.$watch(path, function(newVal, oldVal) {
						if(angular.equals(newVal, oldVal)) return;
						addBg($location.path());
					})
				});

			}]
		}
	}])


}());






