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