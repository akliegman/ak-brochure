(function() {

  var $nav_link_elements = $("header nav a");
  var current_href = window.location.href;


  $(document).on("scroll", function() {
    if ($(document).scrollTop() > 160) {
      $("header").addClass("scrolled-state");
    }
    else {
      $("header").removeClass("scrolled-state");
      $nav_link_elements.removeClass("active").removeClass("inactive");
    }

    $.each($nav_link_elements, function(i, el) {
      var target = $(this).attr('href');

      if ($(target).visible()) {
        console.log(target)
        $nav_link_elements.removeClass("active").addClass("inactive");
        $(this).removeClass("inactive").addClass("active");
      }
    });
  });

  $(document).ready(function() {
    $.each($nav_link_elements, function(i, e) {
     if (current_href.indexOf($(this).attr("href")) >= 0) {
       var element = $(this).attr("href");
       var position = $(element).offset().top - 40;
       console.log(position);
       $('html').scrollTop(position);
     }
    });
  });

  $nav_link_elements.on("click", function(e) {

    var target = $(this).attr('href');
    e.preventDefault();


    $('html').animate({
      scrollTop: $(target).offset().top - 40
    });
  });
})();
