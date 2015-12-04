(function () {
  'use strict';

  // Initialize module and inject dependencies
  angular
    .module('keyboardlist.keyboards.services')
    .factory('Keyboards', Keyboards);

  var apiRoute = '/api/keyboards/';

  function Keyboards($http) {

    // Factory to be returned
    var Keyboards = {
      get: get
    };
    return Keyboards;

    // Call GET on the api endpoint
    function get() {
      return $http.get(apiRoute);
    }
  }
})();
