$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.flash').fadeIn('slow').delay(2000).fadeOut(5000);
    $('#exercise-row select').formSelect();
    $('#comments').val('');
    $("#delete-exercise-button").hide();
    $("#template-1").hide();
    M.textareaAutoResize($('#comments'));
    var counter = 0;
    $("#next-exercise-button").click(function(){
      counter++;
      if (counter >= 10){
        $(this).hide();
      }
      console.log(counter);
      var rowId = 'added-exercise-row' + '_' + counter;
      $("#template-1").clone().attr('id', rowId).addClass('added-exercise').appendTo("#exercises-list").show();
      $("#delete-exercise-button").show();
      console.log('options');
      var $newRow = $(`#${rowId}`);
      console.log($newRow.contents());
      $(`#${rowId} select`).formSelect();
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
