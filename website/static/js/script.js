$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.flash').delay(2000).fadeOut(5000);
    $('select').formSelect();
    $('#comments').val('');
    M.textareaAutoResize($('#comments'));
    $('.fixed-action-btn').floatingActionButton({
        toolbarEnabled: true
      });
});
