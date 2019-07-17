(function() {

  var contact_form = {
    configs: {
      form_element: '#contact-form',
      ajax_url: '/ajax/contact',
      validation_rules: {
        contact_first_name: {
          required: true,
          maxlength: 50
        },
        contact_last_name: {
          required: true,
          maxlength: 50
        },
        contact_phone: {
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
          minlength: 1,
          maxlength: 2000
        },
        messages: {
          contact_first_name: {
            required: 'Please enter your name.',
            maxlength: 'Your name is too damn long.'
          },
          contact_last_name: {
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
      this.$contact_form_submit_btn = this.$contact_form.find('button[type=submit]');
      this.$message_field = this.$contact_form.find('[name=contact_message]');
    },
    validate_and_submit_form: function() {
      this.$contact_form.validate({
        rules: this.configs.validation_rules,
        onfocusin: function(element) {
          setTimeout(function(){
            $(element).valid();
          }, 1000);
        },
        success: "valid",
        errorElement: "span",
        errorPlacement: function(error, element) {
          error.addClass('help-block');
          element.closest('.form-group').addClass('has-feedback');

          if (element.attr('type') == 'checkbox' ) {
            error.insertBefore(element.parent('label'));
          } else {
            error.insertBefore(element);
          }

        },
        success: function ( label, element ) {
        },
        highlight: function ( element, errorClass, validClass ) {
          $(element).closest( ".form-group" ).addClass("has-error").removeClass("has-success");
          $(element).closest("form").removeClass("valid-" + $(element).attr("name"));
        },
        unhighlight: function ( element, errorClass, validClass ) {
          $(element).closest(".form-group").addClass( "has-success" ).removeClass( "has-error" );
          $(element).closest("form").addClass("valid-" + $(element).attr("name"));
        },
        submitHandler: function(form) {
          var $form = $(form),
              $submit_btn = $form.find('button[type=submit]'),
              form_data = $form.serialize();

          var $all_fields = $form.find('input').add($form.find('select')).add($form.find('textarea')).add($submit_btn);

          $all_fields.attr('disabled', true);

          var $thank_you_message = $('<div></div>');

          $thank_you_message.addClass('thank-you-message')
                            .html('<span class="h2">Thank you!</span>');

          $submit_btn.attr('disabled', true);
          $.ajax({
            url: '/ajax/contact',
            data: form_data,
            type: 'POST',
            success: function(result) {
              $('html').animate({
                scrollTop: $form.offset().top - 10
              });
              $form.after($thank_you_message);
            },
            error: function() {
              $all_fields.removeAttr('disabled');
              console.log('There was an error.');
            }
          })
        }
      });

      this.$contact_form.find('.form-control').on('input change', function() {
        console.log($(this).val().length);

        if ($(this).val().length > 0) {
          $(this).addClass('has-value')
        } else {
          $(this).removeClass('has-value')
        }
      });

      if ($("textarea.form-control").attr("maxlength") !== undefined ) {
        var $counter = $('<span>')
                        .addClass('textarea-counter')
                        .html($("textarea.form-control").attr("maxlength"))
                        .attr("for", $("textarea.form-control").attr("id"));
        $counter.insertAfter($("textarea.form-control + label"));
      }

      $('textarea.form-control').on("input", function(e) {
        var name = $(this).attr('name'),
            maxlength = $(this).attr('maxlength'),
            length = $(this).val().length;

        var $counter = $('.textarea-counter[for="' + $(this).attr("id") + '"]');

        $counter.html(maxlength - length).attr("data-value", maxlength - length);
      });
    }
  };

  $(document).ready(function() {
    contact_form.init();
  });

})();
