(function() {
  'use strict';

  angular.module('keyboardlist', [
    'keyboardlist.config',
    'keyboardlist.routes',
    'keyboardlist.keyboards'
  ]);

  angular.module('keyboards').run(run);
  run.$inject = ['$http'];

  function run($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  }
})();
