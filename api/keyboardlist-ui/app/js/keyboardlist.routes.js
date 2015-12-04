(function() {
  'use strict';

  angular.module('keyboardlist.routes', ['ngRoute']);

  angular.module('keyboardlist.routes').config(config);

  function config($routeProvider) {
    $routeProvider
    .otherwise('/');
  }
})();
