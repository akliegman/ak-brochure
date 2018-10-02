(function() {
  'use strict';

  var typed_widget = {
    configs: {
      element: '.typed-placeholder',
      options: {
        typeSpeed: 100,
        backDelay: 2000,
        backSpeed: 40,
        startDelay: 2000,
        loop: true,
        loopCount: Infinity,
        contentType: 'html',
        stringsElement: '.adjectives',
        preStringTyped: function(arrayPos, self) {
          var color_map = [
            'color-purple',
            'color-green',
            'color-red',
            'color-light-green'
          ];

          $(self.el).removeClass(color_map[arrayPos - 1]).addClass(color_map[arrayPos]);
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
