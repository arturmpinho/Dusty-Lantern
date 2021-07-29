# Bugs

## Responsiveness

### Footer is not fixed to the bottom
TBF




## Functionality

### Countdown timer
As part of an additional feature for the project and extreamly important requirement for any auction plaftorm, I have built a countdowntimer in order to establish if an auction is ongoing or currently closed.

Depsite the ease of reasoning behind, I have come across several challenges when dealing with time formats.

Firstly, I was confrontated with the weird difference when displaying the minutes in the countdown. 
After going through several attemps to debug my functionality in Javascript, I have realized that the difference, in the end, was being generated due to a typo in the Django datetime format in the auctions/auction_detail templates. Where I was using "|date:"Y-m-d H:**m**:s", I add to use |date:"Y-m-d H:**i**:s".

After this issue was corrected, and following the attempt to refresh the page when the countdowntimer reaches **0**, an additional issue cama along. Due to the milliseconds format used in the javascript, the timer was never exactly **0**. After researching for a long time in the internet, I have not found any fix for this peculiarity. Therefore, I have built the following workaround:

    if (timeleft < 1500 && timeleft > -5000) {
      timer = 0
    } 

This piece of logic allows the timer to be exaclty **0** for around 6,5 seconds, attempting the refresh at least for 5 times, ensuring that the "place bid" section will be removed automatically from the auction when this closes.

I understand that this is not bullet-proof but a workaround instead and that this issue must be addressed in the future in order to gurantee 99,9% that anyone can place a bid after the auction closes, as well-functioning countdowntimer is a core piece in any auctions platform.


### Timezone difference
Another time related bug that I have fixed was when creating an auction in my current timezone.

As per default, Django as the timezone set to 'UTC' ans 'USE_TZ' set to 'False'. Nontheless, when I was creating an auction in my timezone (Europe/Amsterdam), it was being created with the server time, originating a time difference between the input time and the actual time in the DB.

To tackle this issue, I have set the time zone settings as such:

    TIME_ZONE = 'Europe/Amsterdam'
    USE_TZ = True


### Add to cart functionality
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
            .then(function(result) {
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

Nonetheless, before reaching this solution I tried, without success to implement, background tasks (like [Django Background Tasks](https://django-background-tasks.readthedocs.io/en/latest/ "Django Background Tasks") and  [Django Compat](https://github.com/arteria/django-compat "Django Compat")) to run synchronous/asynchronous with the database and close the auction in the background. Unfortunately, this was not possible with my current knowledge. 

3rd approach: Boolean field in auctions models (is_sold)


### Countdown timer is not being displayed properly in iphones

NaNd NaNh NaNm NaNs


### Duplicate order via webhook due to name split

### Country field select-box arrows are not being displayed

TBF

### Start/End date timesare and images are not being populated on editing the auctions and editing products respectively

TBF