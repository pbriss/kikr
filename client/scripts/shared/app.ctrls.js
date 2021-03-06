;(function() {
	'use strict';

	angular.module('app.ctrls', [])

		// Root Controller
	.controller('AppCtrl', ['$rootScope', function($rs) {
		$rs.completedEvents = [];

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
		// Loading Controller
	.controller('LoadingCtrl', ['$rootScope', '$scope', '$location', function($rs, $scope, $location){

		setTimeout(function() {
			$scope.safeApply(function() {
				$location.path('/events');
			});
		}, 2000);
	}])
		// Head Controller
	.controller('HeadCtrl', ['$scope', '$location', function($scope, $location){
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
					//$scope.isRunning = true;
					//$http.get('api/btstart').success(function () {
					//
					//});
				}
				else {
					$scope.isRunning = false;
					$scope.isProcessing = true;

					setTimeout(function() {
						$scope.safeApply(function() {
							$scope.isProcessing = false;

							//$http.get('api/btstop').success(function (json) {

							var move = {
								//start: json[0].start, end: json[0].end
								start: 10, end: 20
							};
							move.start = (new Date).clearTime()
							.addSeconds(move.start)
							.toString('m:ss');

							move.end = (new Date).clearTime()
							.addSeconds(move.end)
							.toString('m:ss');

							$rs.completedEvents = [{
								id: 1,
								category: 'Spin',
								name: '180°',
								moves: [move]
							}];

							$location.path('/success');
						});
					//});
					}, 2000);
				}
			}
		};
	}])

		// Events Controller
	.controller('SuccessCtrl', ['$rootScope', '$scope', '$location', function($rs, $scope, $location) {

		var completedEvent = $rs.completedEvents[0];
		$scope.event = completedEvent;
		$scope.event.moves = completedEvent.moves;


		$scope.goToList = function() {
			$location.path('/events').search({isNewEvent: true});
		};

		$scope.goToPlay = function() {
			$location.path('/start');
		};
	}])
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
				category: 'Spin',
				name: '1080°'
			},
			{
				id: 6,
				category: 'Straight Air',
				name: 'Ollie',
				competitors: [{name: 'yann'}]
			},
			{
				id: 7,
				category: 'Straight Air',
				name: 'Air-to-fakie'
			},
			{
				id: 8,
				category: 'Straight Air',
				name: 'Poptart'
			},
			{
				id: 9,
				category: 'Straight Air',
				name: 'Flail',
				competitors: [{name: 'yann'}, {name: 'alex'}]
			},
			{
				id: 10,
				category: 'Straight Air',
				name: 'Shify'
			},
			{
				id: 11,
				category: 'Flip',
				name: 'Back Flip',
				competitors: [{name: 'yann'}, {name: 'alex'}]
			},
			{
				id: 12,
				category: 'Flip',
				name: 'Front Flip'
			},
			{
				id: 13,
				category: 'Flip',
				name: 'McTwist'
			},
			{
				id: 14,
				category: 'Flip',
				name: 'Crippler'
			}
		];

		if ($rs.completedEvents.length > 0) {
			angular.forEach($rs.completedEvents, function (item) {
				angular.forEach($scope.events, function (event, i) {
					if (event.id == item.id) {
						event.isNew = $routeParams.isNewEvent;
						event.done = true;
						event.moves = item.moves;
					}
				});
			});
		}

		$scope.toggleMoves = function(event) {
			event.showMoves = !event.showMoves;
		};
	}])

}());

