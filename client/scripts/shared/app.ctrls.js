;(function() {
"use strict";

angular.module("app.ctrls", [])

	// Root Controller
	.controller("AppCtrl", ["$rootScope", "$scope",  function($rs, $scope) {
		var mm = window.matchMedia("(max-width: 767px)");
		$rs.isMobile = mm.matches ? true: false;

		$rs.safeApply = function(fn) {
			var phase = this.$root.$$phase;
			if(phase == '$apply' || phase == '$digest') {
				if(fn && (typeof(fn) === 'function')) {
					fn();
				}
			} else {
				this.$apply(fn);
			}
		};

		mm.addListener(function(m) {
			$rs.safeApply(function() {
				$rs.isMobile = (m.matches) ? true : false;
			});
		});



	}])

	// Head Controller
	.controller("HeadCtrl", ["$scope", function($scope){
		$scope.toggleSidebar = function() {
			$scope.sidebarOpen = $scope.sidebarOpen ? false : true;
		};
	}])

	// Start Controller
	.controller("StartCtrl", ["$scope", "$http", function($scope, $http){
	}])

}());

