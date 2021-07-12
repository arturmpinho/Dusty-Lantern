$('#sort-selector').change(function() {
    let selector = $(this);
    let currentUrl = new URL(window.location);

    let selectedVal = selector.val();
    if(selectedVal != "reset"){
        let sort = selectedVal.split(",")[0];
        let direction = selectedVal.split(",")[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl);
    }
})

// Countdown timer based on https://www.w3schools.com/howto/howto_js_countdown.asp

let cards = $('.card')

for (let i = 0; i < cards.length; i++) {
  let x = setInterval(function() {

    let start_date_time = new Date(document.getElementsByClassName('start_date_time').item(i).textContent);
    
    let end_date_time = new Date(document.getElementsByClassName('end_date_time').item(i).textContent);
  
    let now = new Date().getTime();
    
    let timeleft = ''
      
    if (start_date_time >= now) {
      timeleft = start_date_time - now; 
    } else {
      timeleft = end_date_time - now;
    }
    
    let days = Math.floor(timeleft / (1000 * 60 * 60 * 24));
    let hours = Math.floor((timeleft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    let minutes = Math.floor((timeleft % (1000 * 60 * 60)) / (1000 * 60));
    let seconds = Math.floor((timeleft % (1000 * 60)) / 1000);
      
    if (start_date_time >= now) {
      document.getElementsByClassName("countdowntimer").item(i).innerHTML = "Starting in: " + days + "d " + hours + "h " + minutes + "m " + seconds + "s "; 
    } else if (end_date_time < now) {
      document.getElementsByClassName("countdowntimer").item(i).innerHTML = "Auction Closed";
    } else {
      document.getElementsByClassName("countdowntimer").item(i).innerHTML = "Closing in: " + days + "d " + hours + "h " + minutes + "m " + seconds + "s ";
    }
  }, 1000);
}