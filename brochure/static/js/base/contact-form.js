(function() {

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
      this.validate_and_submit_form();
    },
    cache_dom: function() {
      this.$contact_form = $(this.configs.form_element);
      this.$modal_element = $(this.configs.modal_element);
      this.$contact_form_submit_btn = this.$contact_form.find('button[type=submit]');
    },
    validate_and_submit_form: function() {

      this.$contact_form.validate({
        rules: this.configs.validation_rules,
        errorElement: "em",
        errorPlacement: function(error, element) {
          error.addClass('help-block');
          element.closest('.form-group').addClass('has-feedback');

          if (element.attr('type') == 'checkbox' ) {
            error.insertAfter(element.parent('label'));
          } else {
            error.insertAfter(element);
          }

        },
        success: function ( label, element ) {
        },
        highlight: function ( element, errorClass, validClass ) {
          $(element).closest( ".form-group" ).addClass("has-error").removeClass("has-success");
        },
        unhighlight: function ( element, errorClass, validClass ) {
          $( element ).parents( ".col-sm-5" ).addClass( "has-success" ).removeClass( "has-error" );
        },
        submitHandler: function(form) {
          var $form = $(form),
              $submit_btn = $form.find('button[type=submit]'),
              form_data = $form.serialize();

          $submit_btn.attr('disabled', true);
          $.ajax({
            url: '/ajax/contact',
            data: form_data,
            type: 'POST',
            success: function(result) {
              console.log(result);
              $submit_btn.removeAttr('disabled');
            },
            error: function() {
              $submit_btn.removeAttr('disabled');
            }
          })
        }
      });

    }
  };

  $(document).ready(function() {
    contact_form.init();
  });

})();
