;(function() {
'use strict';

angular.module('app.ctrls', [])

	// Root Controller
	.controller('AppCtrl', ['$rootScope', '$scope',  function($rs, $scope) {
		var mm = window.matchMedia('(max-width: 767px)');
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
	.controller('HeadCtrl', ['$scope', function($scope){
		$scope.toggleSidebar = function() {
			$scope.sidebarOpen = $scope.sidebarOpen ? false : true;
		};
	}])

	// Foot Controller
	.controller('FootCtrl', ['$scope', function($scope){
	}])

	// Start Controller
	.controller('StartCtrl', ['$scope', '$http', '$location', '$timeout', function($scope, $http, $location, $timeout){

		$scope.isInitiated = false;
		$scope.isRunning = false;
		$scope.isProcessing = false;

		$scope.startRecord = function() {

			if (!$scope.isProcessing) {

				if (!$scope.isInitiated && !$scope.isRunning) {
					$scope.isInitiated = true;
					$http.get('api/btstart').success(function (json) {
						$scope.isInitiated = false;
						$scope.isRunning = true;

					});
				}
				else {
					$http.get('api/btstop').success(function (json) {
						$scope.isRunning = false;
						$scope.isProcessing = true;
						$http.get('api/processing').success(function (json) {
							//$location.path('/events');
							alert(json);
						});
					});

					//
					//$scope.isDone = true;
					//
					//$timeout(function(){
					//	$location.path('/events');
					//}, 2000);

				}
			}
		};
	}])

	// Events Controller
	.controller('EventsCtrl', ['$scope', '$http', function($scope, $http){

	}])

}());

