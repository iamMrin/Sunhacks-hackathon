$(document).ready(function () {
  $(".iframe").hide();
  $("#streetView").hide();
  // $("#street_btn").on("click", function () {
  //   console.log("Hi");
  //   $("#streetView").show();
  //   $(".iframe").show();
  // });
  $(".btn").on("click", function () {
    console.log("Hi");
  });

  $("html").on("keydown", function (event) {
    if (event.key == "Escape" && $(".iframe").is(":visible")) {
      $("#map").animate({ opacity: 1 });
      $(".iframe").hide();
      $("#streetView").hide();
    }
  });
});
