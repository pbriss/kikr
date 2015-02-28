var PythonShell = require('python-shell');
var fs = require('fs');
var sleep = require('sleep');

//GoPro3

var Camera = require('gopro').Camera;
var cam = new Camera('10.5.5.9', 'yanncamera');


//GoPro4
//var GoPro = require('goproh4');
//var cam = new GoPro.Camera();

exports.btstart = function(req, res) {

	//fs.writeFile('python/state.txt', 1, function(err) {
	//	if(err) {
	//		console.log(err);
	//	} else {
			//Need to initiate the serial port prior to recording due to init delay of imu
			//var pyshell = new PythonShell('serialopen.py', {mode: 'text'});
			//pyshell.on('message', function (msg) {
			//	console.log(msg);
			//	////Start bluetooth reading
			//	//new PythonShell('bluetooth.py', {mode: 'binary'});
			//	////Start GoPro recording
			//	//new PythonShell('gopro.py', {mode: 'binary'});
			//
			//});
			//res.json('Bluetooth & GoPro started!');

	//	}
	//});


//GoPro3
	cam.startCapture().then(function () {
		var msg = 'Bluetooth & GoPro started!';
		console.log(msg);
		res.json();
	});

//GoPro4
	//Start GoPro recording
	//cam.start().then(function () {
	//	var msg = 'Bluetooth & GoPro started!';
	//	console.log(msg);
	//	res.json();
	//});
};

exports.btstop = function(req, res) {

//GoPro3
	cam.stopCapture().then(function () {
		sleep.sleep(2);
		cam.powerOff();
		sleep.sleep(2);
		cam.powerOn();
		sleep.sleep(2);
		cam.powerOn();

		var msg = 'Bluetooth & GoPro stopped!';
		console.log(msg);

		res.json();
	});

//GoPro4
	//Start GoPro recording
	//cam.stop().then(function () {
	//	var msg = 'Bluetooth & GoPro started!';
	//	console.log(msg);
	//
	//	res.json();
	//});


	//fs.writeFile('python/state.txt', 0, function(err) {
	//	if(err) {
	//		console.log(err);
	//	} else {
	//		res.json('Bluetooth & GoPro stopped!');
	//
	//		//Start metadata reading
	//		new PythonShell('metadata.py', {mode: 'binary'});
	//		//Start video processing
	//		new PythonShell('processing.py', {mode: 'binary'});
	//	}
	//});
};

exports.processing = function(req, res) {


};
