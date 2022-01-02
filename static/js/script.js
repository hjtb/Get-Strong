$(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.flash').fadeOut(3000);
    var maxField = 10; //Input fields increment limitation
    var addButton = $('.add_button'); //Add button selector
    var wrapper = $('.exercise_wrapper'); //Input field wrapper
    //New input field html 
    var fieldHTML = `
            <div class="row exercise_input">
            <div class="input-field col m3 s6">
                <select>
                    <option value="exercises" selected>Choose an Exercise</option>
                    <option value="1">Option 1</option>
                    <option value="2">Option 2</option>
                    <option value="3">Option 3</option>
                </select>
                <label for="exercise">Exercise</label>
            </div>
            <div class="input-field col m3 s6">
                {{ add_workout_form.sets(class="validate") }}
                <label for="sets">Sets:</label>
            </div>
            <div class="input-field col m3 s6">
                {{ add_workout_form.reps(class="validate") }}
                <label for="reps">Reps:</label>
            </div>
            <div class="input-field col m3 s6">
                {{ add_workout_form.weight(class="validate") }}
                <label for="Weight(kg):">Weight(kg):</label>
            </div>
        </div>
        <a href="javascript:void(0);" class="remove_button"><i class="fas fa-minus-circle"></i>
        </a></div>
        `; 

    var x = 1; //Initial field counter is 1
    
    //Once add button is clicked
    $(addButton).click(function(){
        //Check maximum number of input fields
        if(x < maxField){ 
            x++; //Increment field counter
            $(wrapper).append(fieldHTML); //Add field html
        }
    });
    
    // Once remove button is clicked
    $(wrapper).on('click', '.remove_button', function(remover){
       remover.preventDefault();
       $(this).closest('.exercise_input')[0].remove(); //Remove field html
       x--; //Decrement field counter
    });
});