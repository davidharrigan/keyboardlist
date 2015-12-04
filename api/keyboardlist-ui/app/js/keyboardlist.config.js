(function() {
  'use strict';

  angular.module('keyboardlist.config', []);

  angular.module('keyboardlist.config').config(config);

  // Enable HTML5 Routing
  function config($locationProvider) {
    $locationProvider.html5Mode(true);
    $locationProvider.hashPrefix('!');
  }
})();
