(function() {
  'use strict';

  // Here we define all submodules for keyboardlist.keyboards module
  angular.module('keyboardlist.keyboards', [
    'keyboardlist.keyboards.services',
    'keyboardlist.keyboards.controllers',
    'keyboardlist.keyboards.directives'
  ]);

  angular.module('keyboardlist.keyboards.services', []);
  angular.module('keyboardlist.keyboards.controllers', []);
  angular.module('keyboardlist.keyboards.directives', []);
})();
