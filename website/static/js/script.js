$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.flash').fadeIn('slow').delay(2000).fadeOut(5000);
    $('select').formSelect();
    $('#comments').val('');
    $("#delete-exercise-button").hide();
    M.textareaAutoResize($('#comments'));
    var counter = 0;
    $("#next-exercise-button").click(function(){
      counter++;
      if (counter >= 10){
        $(this).hide();
      }
      console.log(counter);
      $("#exercise-row").clone().addClass('added-exercise').appendTo("#exercises-list");
      $("#delete-exercise-button").show();
    });
    $("#delete-exercise-button").click(function(){
      counter--;
      if (counter < 10){
        $("#next-exercise-button").show();
      }
      console.log(counter);
      if (counter == 0){
        $("#delete-exercise-button").hide();
      };
      $(".added-exercise:last-of-type").remove();
    });
    if (counter > 0){
      $("#delete-exercise-button").show();
    };
});
