(function() {

  var $nav_link_elements = $("header nav a");
  var $scroll_link_elements = $('a.scroll-to, button.scroll-to');

  var current_href = window.location.href;

  function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
  }

  if (getCookie('kd_cookies_accepted') !== undefined) {
    $('.cookies').addClass('hidden');
  } else {
    $('.cookies').removeClass('hidden');
  }

  $(document).on("scroll", function() {
    if ($(document).scrollTop() > 60) {
      $("header").addClass("scrolled-state");
    }
    else {
      $("header").removeClass("scrolled-state");
      $nav_link_elements.removeClass("active-s").removeClass("inactive-s");
    }

    $.each($nav_link_elements, function(i, el) {
      var target = $(this).attr('href').substr(1);

      if ($(target).visible()) {

        $nav_link_elements.removeClass("active-s").addClass("inactive-s");
        $(this).removeClass("inactive-s").addClass("active-s");
      }
    });
  });

  $(document).ready(function() {
    if (window.location.pathname == '/' ) {
      setTimeout(function(e) {
        $("#not-loaded").fadeOut(600, function(e){
          $(this).remove();
        });
      }, 800);
    }

    $.each($nav_link_elements, function(i, e) {
     if (current_href.indexOf($(this).attr("href")) >= 0) {
       var element = $(this).attr("href").substr(1);
       var position = $(element).offset().top - 40;

       $('html').scrollTop(position);
     }
    });
  });

  $nav_link_elements.add($scroll_link_elements).on("click", function(e) {
    if (window.location.pathname == '/' ) {
      var target = $(this).attr('href').substr(1);
      e.preventDefault();
      $('.navbar-collapse').collapse('hide');
      $('html').animate({
        scrollTop: $(target).offset().top - 40
      });
    }
  });

  $("button.cookies-close").on("click", function(e) {
    e.preventDefault();
    $(this).closest('.cookies').fadeOut('fast');
    document.cookie = "kd_cookies_accepted=true;"
  });


})();
