'use strict';

var BigPipe = require('../../utils/bigpipe.js');
var pagelets = require('../../pagelets/index.js');

function homeHandler(req, res, next) {
    var bp = new BigPipe(req, res, next);
    bp.push(pagelets.head);
    bp.push(pagelets.layout.home);
    bp.push(pagelets.navbar);
    bp.push(pagelets.sidebar);
    bp.finish(); 
}

module.exports = {
    home: homeHandler
}