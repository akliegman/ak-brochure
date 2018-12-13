(function() {
  'use strict';

  var typed_widget = {
    configs: {
      element: '.typed-placeholder',
      options: {
        typeSpeed: 50,
        backDelay: 2000,
        backSpeed: 70,
        startDelay: 1200,
        loop: true,
        loopCount: Infinity,
        contentType: 'html',
        stringsElement: '.adjectives',
        preStringTyped: function(arrayPos, self) {

        },
      }
    },
    init: function() {
      var typed = new Typed(this.configs.element, this.configs.options)
    }
  }

  $(document).ready(function() {
    typed_widget.init();
  });

})();
