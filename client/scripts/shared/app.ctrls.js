;(function() {
'use strict';

angular.module('app.ctrls', [])

	// Root Controller
	.controller('AppCtrl', ['$rootScope', '$scope',  function($rs, $scope) {
		$rs.events = [];

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
	.controller('StartCtrl', ['$rootScope', '$scope', '$http', '$location', '$timeout', function($rs, $scope, $http, $location, $timeout){

		$scope.isRunning = false;
		$scope.isProcessing = false;

		$scope.startRecord = function() {

			if (!$scope.isProcessing) {

				if (!$scope.isRunning) {
					$scope.isRunning = true;
					$http.get('api/btstart').success(function () {
					
					});
				}
				else {
      $scope.isRunning = false;
      $scope.isProcessing = true;
					$http.get('api/btstop').success(function () {
						$location.path('/events');
					});


      //$scope.isRunning = false;
      //$scope.isProcessing = true;

				}
			}
		};
	}])

	// Events Controller
	.controller('EventsCtrl', ['$rootScope', '$scope', '$routeParams', function($rs, $scope, $routeParams){
		$scope.events = [
			{
				id: 1,
				category: 'Spin',
				name: '180°'
			},
			{
				id: 2,
				category: 'Spin',
				name: '360°'
			},
			{
				id: 3,
				category: 'Spin',
				name: '540°',
				competitors: [{name: 'alex'}]
			},
			{
				id: 4,
				category: 'Spin',
				name: '720°'
			},
			{
				id: 5,
				category: 'Straight Air',
				name: 'Ollie',
				competitors: [{name: 'yann'}]
			},
			{
				id: 6,
				category: 'Straight Air',
				name: 'Air-to-fakie'
			},
			{
				id: 7,
				category: 'Straight Air',
				name: 'Poptart'
			},
			{
				id: 8,
				category: 'Straight Air',
				name: 'Flail',
				competitors: [{name: 'yann'}, {name: 'alex'}]
			}
		];

		var move = {
			start: 8, end: 16
		};
		move.start = (new Date).clearTime()
		.addSeconds(move.start)
		.toString('m:ss');

		move.end = (new Date).clearTime()
		.addSeconds(move.end)
		.toString('m:ss');

		$rs.events = [{
			id: 2,
			moves: [move]
		}];

		if ($rs.events.length > 0) {
			angular.forEach($rs.events, function (item) {
				angular.forEach($scope.events, function (event, i) {
					if (event.id == item.id) {
						event.isNew = $routeParams.isNewEvent;
						event.done = true;
						event.moves = item.moves;
					}
				});
			});
		}
	}])

}());

