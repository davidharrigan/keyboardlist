(function() {
  'use strict';

  angular.module('keyboardlist', [
    'keyboardlist.config',
    'keyboardlist.routes',
    'keyboardlist.keyboards'
  ]);

  angular.module('keyboardlist').run(run);

  function run($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  }
})();
