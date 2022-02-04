$(document).ready(function(){
  $('.sidenav').sidenav();
  $('.flash').fadeIn('slow').delay(2000).fadeOut(5000);
  $('#exercise-row select').formSelect();
  $('#comments').val('');
  $("#delete-exercise-button").hide();
  $("#template-1").hide();
  M.textareaAutoResize($('#comments'));
  // initially disable the submit button to prevent a form
  // being submitted without all values filled in
  $("#add-workout-submit-button").prop('disabled', true);
  // function to check if all rows have been filled out
  $("#add-workout-form").mouseover(function(){
    var formOk = true;
    var form = document.getElementById("add-workout-form");
    for (let index = 0; index < form.elements.length; index++) {
      const input = form.elements[index];
      if (!input.value){
        formOk = false;
      }
      // console.log("value ", input.value, "name ", input.name);
      // console.log(input);
    }

    if(formOk == true){
      $("#add-workout-submit-button").prop('disabled', false);
    };
  });
  // generate our exercise rows dynamically using buttons
  var counter = 0;
  $("#next-exercise-button").click(function(){
    // ensure the submit button stays disabled when we add a new row
    $("#add-workout-submit-button").prop('disabled', true);
    counter++;
    // set the limit of rows that can be generated
    if (counter >= 10){
      $(this).hide();
    }
    // Generate new ids for each row 
    var rowId = 'added-exercise-row' + '_' + counter;
    // Clone our new rows from the hidden template row
    $("#template-1").clone().attr('id', rowId).addClass('added-exercise').appendTo("#exercises-list").show();
    // Only show our delete row button for newly created rows
    $("#delete-exercise-button").show();
    // initialise the select dropdown for materialize on each of the new rows
    $(`#${rowId} select`).formSelect();
  });
  // delete row functionality on the delete button
  $("#delete-exercise-button").click(function(){
    counter--;
    // If we delete the final row we allow the row to be regenerated
    if (counter < 10){
      $("#next-exercise-button").show();
    }
    // If we go back to the initial row being the only left we remove the delete option
    if (counter == 0){
      $("#delete-exercise-button").hide();
    };
    $(".added-exercise:last-of-type").remove();
  });
});
