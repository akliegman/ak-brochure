$contact_form = $('#' + contact_form_id),
$contact_btn = $contact_form.find('button[type=submit]'),
$contact_modal = $('#' + contact_modal_id);

(function() {
  'use strict';

  var contact_form = {
    configs: {
      form_element: '#' + elements.contact_form_id,
      modal_element: '#' + elements.contact_modal_id,
      ajax_url: '/ajax/contact',
      validation_rules: {
        contact_name: {
          required: true,
          maxlength: 50
        },
        contact_email: {
          required: true,
          email: true
        },
        contact_phone: {
          phoneUS: true
        },
        contact_reason: {
          required: true
        },
        contact_message: {
          required: true,
          minlength: 5,
          maxlength: 1000
        },
        messages: {
          contact_name: {
            required: 'Please enter your name.',
            maxlength: 'Your name is too damn long.'
          },
          contact_email: {
            required: 'Please enter a valid email address.',
            email: 'This isn\'t a valid email address.'
          },
          contact_phone: {
            phoneUS: 'Please enter a valid US phone number.'
          },
          contact_reason: {
            required: 'Please select a reason for contacting me.'
          },
          contact_message: {
            required: 'Please write something... anything.',
            minlength: 'Please write something... more?',
            maxlength: 'This is too long. Tighten up your prose!'
          }
        }
      }
    },
    init: function() {
      this.cache_dom();
      this.prevent_default_action(this.$contact_form_submit_btn);
    },
    cache_dom: function() {
      this.$contact_form = $(this.configs.form_element);
      this.$modal_element = $(this.configs.modal_element);
      this.$contact_form_submit_btn = this.$contact_form.find('button[type=submit]');
    },
    prevent_default_action: function($btn) {
      $btn.on('click', function(e) { e.preventDefault(); });
    }
  }

})();
