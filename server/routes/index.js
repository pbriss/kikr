
/*
 * GET home page.
 */

exports.index = function(req, res){
    res.render('index');
};

//NOTE: All routes are sent to Angular routing for proper view rendering as a single page app