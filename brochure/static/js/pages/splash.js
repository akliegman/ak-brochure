(function() {
  'use strict';

  var ga_events = {
    configs: {
      elem : '[data-ga="event"]',
      data_category : 'ga-category',
      data_label : 'ga-label',
      data_action : 'ga-action',
      data_value : 'ga-value'
    },
    init: function() {
      var configs = this.configs;

      $(configs.elem).click(function(e) {

        function determine_ga_event(element, data_attr, return_override) {
          if (typeof $(element).data(data_attr) !== 'undefined') {
            return $(element).data(data_attr)
          }
          if (return_override) {
            return return_override
          }
          return 'undefined'
        }

        var category = determine_ga_event(this, configs.data_category),
            action = determine_ga_event(this, configs.data_action),
            label = determine_ga_event(this, configs.data_label),
            value = determine_ga_event(this, configs.data_value, 0);

        console.log("ga('send', 'event', '" + category + "', '" + action + "', '" + label + "');");
        ga('send','event', category, action, label);
      });
    }
  }

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
        stringsElement: '.adjectives'
      }
    },
    init: function() {
      var typed = new Typed(this.configs.element, this.configs.options)
    }
  }

  $(document).ready(function() {
    typed_widget.init();
    ga_events.init();
  });

  $('[role="modal"]').on('hide.bs.modal', function () {
    $(this).addClass('out');
    $('body').addClass('modal-closed');
  });
  $('[role="modal"]').on('show.bs.modal', function () {
    $(this).removeClass('out');
    $('body').removeClass('modal-closed');

  });

})();
