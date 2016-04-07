

var webpack = require('webpack');
var WebpackDevServer = require('webpack-dev-server');
var config = require('./webpack/conf/development.config');


new WebpackDevServer(webpack(config), {
  publicPath: 'http://127.0.0.1:8080/static/bundles/',
  hot: false,
  inline: false,
  historyApiFallback: true,
  stats: { colors: true },
  quiet: false,
  noInfo: false,
  headers: { "Access-Control-Allow-Origin": "*" }
}).listen(8080, '0.0.0.0', function (err, result) {
  if (err) {
    console.log(err)
  }

  console.log('Listening at 0.0.0.0:8080');
});