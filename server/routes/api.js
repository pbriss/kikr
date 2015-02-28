var PythonShell = require('python-shell');
var fs = require('fs');
var GoPro = require('goproh4');
var cam = new GoPro.Camera();

exports.btstart = function(req, res) {

	fs.writeFile('python/state.txt', 1, function(err) {
		if(err) {
			console.log(err);
		} else {
			//Start bluetooth reading
			new PythonShell('bluetooth.py', {mode: 'binary'});

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

};
