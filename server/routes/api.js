var PythonShell = require('python-shell');

exports.btstart = function(req, res) {
	var pyshell = new PythonShell('bluetooth.py', {mode: 'binary'});
};

exports.btstop = function(req, res) {

};
