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

// Countdown timer based on https://www.w3schools.com/howto/howto_js_countdown.asp

let cards = $('.card');

for (let i = 0; i < cards.length; i++) {
  setInterval(function() {

    let start_date_time = Date.parse(`${document.getElementsByClassName('start_date_time').item(i).textContent.trim().replace(/ /g,"T")}Z`);
    let end_date_time = Date.parse(`${document.getElementsByClassName('end_date_time').item(i).textContent.trim().replace(/ /g,"T")}Z`);
    let now = Date.now();

    let timeleft = '';
    
    let timer = '';
      
    if (start_date_time >= now) {
      timeleft = start_date_time - now;    
    } else {
      timeleft = end_date_time - now;
    }

    let days = Math.floor(timeleft / (1000 * 60 * 60 * 24));
    let hours = Math.floor((timeleft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    let minutes = Math.floor((timeleft % (1000 * 60 * 60)) / (1000 * 60));
    let seconds = Math.floor((timeleft % (1000 * 60)) / 1000);

    if (timeleft < 1500 && timeleft > -5000) {
      timer = 0;
    } 

    if (start_date_time > now) {
      document.getElementsByClassName("countdowntimer").item(i).innerHTML = "<i class='fas fa-clock fa-2x'></i><span> Starting in: " + days + "d " + hours + "h " + minutes + "m " + seconds + "s </span>" + "<p class='mt-4'>This auction will close on " + document.getElementsByClassName('end_date_time').item(i).textContent + ". </p>"; 

    } else if (end_date_time < now) {
      document.getElementsByClassName("countdowntimer").item(i).innerHTML = "Auction Closed";
      display_to_none();
    
      // Auto refresh auction detail page when countdowntimer reaches 0
    } else if (timer === 0) {
      location.reload();
    } 
     
      else {
        document.getElementsByClassName("countdowntimer").item(i).innerHTML = "<i class='fas fa-clock fa-2x'></i> Closing in: " + days + "d " + hours + "h " + minutes + "m " + seconds + "s ";
      }
  }, 1000);
}

function display_to_none(){
  $("#place-bid").hide();
}
    
});