function recaptcha_callback() {
  var $recaptcha_elem = $('.g-recaptcha'),
      $sister_form = $recaptcha_elem.next('form');
  $sister_form .removeClass('hidden');
  $recaptcha_elem.addClass('hidden');
}
