/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

var style = {
    base: {
        color: '#000',
        fontFamily: '"Karla", "Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#000'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-exclamation-circle"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});


// Handle form submit

var form = document.getElementById('checkout-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    // $('#checkout-form').fadeToggle(100);
    // $('#loading-overlay').fadeToggle(100);

    // var saveInfo = Boolean($('#id-save-info:checked').val());

    // var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    // var postData = {
    //     'csrfmiddlewaretoken': csrfToken,
    //     'client_secret': clientSecret,
    //     'save_info': saveInfo,
    // };
    // var url = '/checkout/cache_checkout_data/';

    // $.post(url, postData).done(function () {
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            // billing_details: {
            //     name: $.trim(form.full_name.value),
            //     email: $.trim(form.email.value),
            //     phone: $.trim(form.phone_number.value),
            //     address:{
            //         country: $.trim(form.country.value),
            //     }
            // }
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
            <span class="icon" role="alert">
                <i class="fas fa-exclamation-circle"></i>
            </span>
            <span>${result.error.message}</span>
            `;
            $(errorDiv).html(html);
            // $('#checkout-form').fadeToggle(100);
            // $('#loading-overlay').fadeToggle(100);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);

        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
    // })
    // .fail(function () {
    //     location.reload();
    // });
});