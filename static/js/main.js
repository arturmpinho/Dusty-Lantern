$(document).ready(function(){

    // Adapted from: https://stackoverflow.com/questions/14249998/jquery-back-to-top

    $(window).scroll(function(){
        if ($(this).scrollTop() > 100) {
            $('.btntop').fadeIn(0);
        } else {
            $('.btntop').fadeOut(0);
        }
    });
    
    $('.btntop').click(function(){
        $('html, body').animate({scrollTop : 0},500);
        return false;
    });
    
});
