$(document).ready(function() {
  var offcanvasHeight = $(".sidebar-offcanvas").height();
  if (offcanvasHeight > $(".container-new").height()) {
    $(".container-new").height(offcanvasHeight);
  }
});

$(window).resize(function() {
  var offcanvasHeight = $(".sidebar-offcanvas").height();
  if (offcanvasHeight > $(".container-new").height()) {
    $(".container-new").height(offcanvasHeight);
  }
});
