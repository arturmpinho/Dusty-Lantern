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

const start_date_time = new Date(document.getElementById('start_date_time').textContent);
const end_date_time = new Date(document.getElementById('end_date_time').textContent);

// Update the count down every 1 second
let x = setInterval(function() {

  // Get today's date and time
  let now = new Date().getTime();
    
  // Find the distance between now and the count down date
  let timeleft = now - (start_date_time);
    
  // Time calculations for days, hours, minutes and seconds
  let days = Math.floor(timeleft / (1000 * 60 * 60 * 24));
  let hours = Math.floor((timeleft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  let minutes = Math.floor((timeleft % (1000 * 60 * 60)) / (1000 * 60));
  let seconds = Math.floor((timeleft % (1000 * 60)) / 1000);
    
  // Output the result in an element with id="demo"
  document.getElementById("countdowntimer").innerHTML = days + "d " + hours + "h "
  + minutes + "m " + seconds + "s ";
    
  // If the count down is over, write some text 
  if (timeleft < 0) {
    clearInterval(x);
    document.getElementById("countdowntimer").innerHTML = "EXPIRED";
  }
}, 1000);