$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.flash').delay(2000).fadeOut(5000);
    $('select').formSelect();
    $('#comments').val('New Text');
    M.textareaAutoResize($('#comments'));
});
