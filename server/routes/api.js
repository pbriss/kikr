var PythonShell = require('python-shell');
var fs = require('fs');
var sleep = require('sleep');
var GoPro = require('goproh4');
var cam = new GoPro.Camera();

exports.btstart = function(req, res) {

	fs.writeFile('python/state.txt', 1, function(err) {
		if(err) {
			console.log(err);
		} else {
			//Start bluetooth reading
			//new PythonShell('bluetooth.py', {mode: 'binary'});

			//cam.deleteAll().then(function () {
			//	console.log('[storage cleared]');
			//});

			//Start GoPro recording
			cam.start().then(function () {
				var msg = 'Bluetooth & GoPro started!';
				console.log(msg);

				res.json();
			});
		}
	});
};

exports.btstop = function(req, res) {
	cam.stop().then(function () {
		var msg = 'Bluetooth & GoPro stopped';
		console.log(msg);
		res.json(msg);
	});

};

exports.processing = function(req, res) {
	sleep.sleep(2);

	cam.listMedia().then(function (result) {

		var lastDir = result.media[result.media.length - 1];
		var lastMedia = lastDir.fs[lastDir.fs.length - 1];
		var name = lastMedia.n;
		var url = 'http://' + cam._ip + '/videos/DCIM/' + lastDir.d + '/' + name;

		cam.getMedia(url, 'python/videos/src')
		.then(function (file) {
			console.log('[media downloaded]', file);
			fs.rename(file, 'python/videos/src/sample.mp4');
			res.json('Recording downloaded');
		})
		.catch(function (err) {
			console.log('[media download error]', err);
			res.json('File downloaded error');
		});

	});

};
