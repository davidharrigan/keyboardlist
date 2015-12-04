(function () {
  'use strict';

  // Initialize module and inject dependencies
  angular
    .module('keyboardlist.keyboards.directives')
    .directive('keyboardList', KeyboardList);

  function KeyboardList() {
    return {
      controller: 'KeyboardListController',
      controllerAs: 'vm',
      restrict: 'E',
      templateUrl: '/dist/partials/keyboards/keyboard-list.html'
    };
  }
})();
