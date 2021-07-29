# Bugs
## Countdown timer differences
When comparing to datetime fields, the result of the difference between these always show a difference of minutes between this calculation and the real time.

## Add to cart functionality
1st approach: Add to cart via JS
        // Add to cart functionality when auction closes

        function addToCart() {
        var auctionId = document.getElementById('auction_id').value;
        var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        var postData = {
            "auction_id": auctionId,
            'csrfmiddlewaretoken': csrfToken,
        }

        var url = `${auctionId}/add_to_cart`
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

2nd approach: scheduler
    1-django-compt
    2-django-background-tasks
    3-schedule

3rd approach: Boolean field in auctions models (is_sold)


## Countdown timer is not being displayed properly in iphone

NaNd NaNh NaNm NaNs



