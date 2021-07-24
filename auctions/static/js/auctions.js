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
  
    let now = new Date();

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
      
    if (start_date_time > now) {
      document.getElementsByClassName("countdowntimer").item(i).innerHTML = "Starting in: " + days + "d " + hours + "h " + minutes + "m " + seconds + "s "; 
    } else if (end_date_time < now) {
      document.getElementsByClassName("countdowntimer").item(i).innerHTML = "Auction Closed";
    
      // Auto refresh auction detail page when countdowntimer reaches 0
    } else if (timeleft == 0) {
        setTimeout(function(){
          $('.auto-refresh').location.reload();
      }); 
          
    } else {
      document.getElementsByClassName("countdowntimer").item(i).innerHTML = "Closing in: " + days + "d " + hours + "h " + minutes + "m " + seconds + "s ";
    }
  }, 1000);
}



// Number of ongoing auction counter

$(window).on('load', function(){

  let ongoingAuctions =  $('.card').length
  
  if (ongoingAuctions > 1){
    $('#cards-counter').append(`There are ${ongoingAuctions} auctions matching your search criteria`)
  } else if (ongoingAuctions == 0) {
    $('#cards-counter').append(`There are no auctions matching your search criteria`)
  } else {
    $('#cards-counter').append(`There is ${ongoingAuctions} auction matching your search criteria`)
  }
})

// Disable manual input for input field type number on bidding form
$("[type='number']").keypress(function (evt) {
  evt.preventDefault();
});



function addToCart() {
  var auctionId = document.getElementById('auction_id').value;
  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  var postData = {
    "auction_id": auctionId,
    'csrfmiddlewaretoken': csrfToken,
  }

  var url = `${auctionId}/add_to_cart`
  // var url = "4/add_to_cart"
  $.post(url, postData).done(function () {
    console.log("Hello")
      
    .then(function(result) {
          console.log("then")
      });
  }).fail(function (e) {
      // just reload the page, the error will be in django messages
      console.log(e)
  })

  
};
