function recaptcha_callback() {
  var $recaptcha_elem = $('.g-recaptcha'),
      $sister_form = $('.contact-form');
  $sister_form .addClass('blown-up');
  $recaptcha_elem.addClass('shrunk');
}
