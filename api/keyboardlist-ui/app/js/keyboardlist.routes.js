(function() {
  'use strict';

  angular.module('keyboardlist.routes', ['ngRoute']);

  angular.module('keyboardlist.routes').config(config);
  config.$inject = ['$routeProvider'];

  function config($routeProvider) {
    $routeProvider
    .otherwise('/');
  }
})();
