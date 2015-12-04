(function () {
  'use strict';

  // Initialize module and inject dependencies
  angular
    .module('keyboardlist.keyboards.controllers')
    .controller('KeyboardListController', KeyboardListController);

  function KeyboardListController($scope, $location, Keyboards) {
    var vm = this;
    vm.keyboards = [];

    function updateKeyboards() {
      Keyboards.get().then(getSuccess, getError);

      function getSuccess(data) {
        vm.keyboards = data.data;
      }

      function getError(data) {
        console.error(data);
      }
    }

    updateKeyboards();
  }
})();
