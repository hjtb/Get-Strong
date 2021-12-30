$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.flash').fadeOut(3000);
    var maxField = 10; //Input fields increment limitation
    var addButton = $('.add_button'); //Add button selector
    var wrapper = $('.exercise_wrapper'); //Input field wrapper
    var fieldHTML = `
        <div class="input-field col m3 s6">
        {{ add_workout_form.exercise_name(class="validate") }}
        <label for="exercise"></label>
        </div>
        <a href="javascript:void(0);" class="remove_button"><i class="fas fa-minus-circle"></i>
        </a></div>
        `; 
        //New input field html 

    var x = 1; //Initial field counter is 1
    
    //Once add button is clicked
    $(addButton).click(function(){
        //Check maximum number of input fields
        if(x < maxField){ 
            x++; //Increment field counter
            $(wrapper).append(fieldHTML); //Add field html
        }
    });
    
    //Once remove button is clicked
    $(wrapper).on('click', '.remove_button', function(remover){
        remover.preventDefault();
        $(this).parent('div').remove(); //Remove field html
        x--; //Decrement field counter
    });
});