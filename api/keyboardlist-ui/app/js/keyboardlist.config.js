(function() {
  'use strict';

  angular.module('keyboardlist.config', []);

  angular.module.config(config);
  config.$inject = ['$locationProvider'];

  // Enable HTML5 Routing
  function config($locationProvider) {
    $locationProvider.html5Mode(true);
    $locationProvider.hashPrefix('!');
  }
})();
