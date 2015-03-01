var PythonShell = require('python-shell');
var fs = require('fs');
var sleep = require('sleep');
var notOpen = true;

exports.btstart = function(req, res) {


  fs.writeFile('python/stateserial.txt', 0);

 	fs.writeFile('python/state.txt', 1, function(err) {
		if(err) {
			console.log(err);
		} else {
			//Start bluetooth reading
			//new PythonShell('bluetooth.py', {mode: 'binary'});

			res.json('Bluetooth & GoPro started!');
		}
	});

};

exports.btstop = function(req, res) {

  fs.writeFile('python/stateserial.txt', 0);;

  fs.writeFile('python/state.txt', 0, function(err) {
		if(err) {
			console.log(err);
		} else {

			//Start metadata reading
			var pyshell = new PythonShell('metadata.py', {mode: 'text'});
			pyshell.on('message', function (msg) {
				fs.readFile('python/metadata.txt', function(err, data) {
					if(err) {
						console.log(err);
      
					} else {
       console.log('get here btstop');
       res.json(data);
      
       sleep.sleep(5)
       //Start video processing
       new PythonShell('processing.py', {mode: 'binary'});

					}
				});



				pyshell.end(function (err) {
					if (err) throw err;
					console.log('finished');
				});
			});


		}
	});


	//Need to initiate the serial port prior to recording due to init delay of imu
	//var pyshell = new PythonShell('serialopen.py', {mode: 'text'});
	//pyshell.on('message', function (msg) {
	//	console.log(msg);
	//	//Start bluetooth reading
	//	new PythonShell('bluetooth.py', {mode: 'binary'});
	//	//Start GoPro recording
	//	new PythonShell('gopro.py', {mode: 'binary'});
	//
	//	res.json('Bluetooth & GoPro started!');
	//});
};

exports.processing = function(req, res) {


};
