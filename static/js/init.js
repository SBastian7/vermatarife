(function($){
  $(function(){

    $('.sidenav').sidenav();
    $('.tabs').tabs();
    $('.dropdown-trigger').dropdown({hover:true,constrainWidth:false,coverTrigger:false});
    $('select').formSelect();
    $('.modal').modal();
    


  }); // end of document ready
})(jQuery); // end of jQuery name space
