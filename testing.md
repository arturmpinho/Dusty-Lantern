# Testing

The full application has been checked in the following validators and all the errors were addressed.

* [HTML Validator](https://validator.w3.org/ "HTML validator")
* [CSS](https://jigsaw.w3.org/css-validator/ "CSS validator")
* [JS Hint](https://jshint.com/ "Javascript validator")
* [PEP8 Validator](http://pep8online.com/ "Python validator")


## Homepage
### Responsiveness

#### Tested on:
* Devices: Acer Spin, MacBook Pro, iPhone8, iPhone11, iPhone12 mini and iPad
* Broweser: Google Chrome, Firefox, Opera and Safari

#### Tested for:
* Jumbotron including logo and intro text
* Overview of ongoing auctions

#### Conclusion:
On large screens and above the jumbotron is nicely displayed in 2 columns of 4 and 8 with text centered within the corresponding column.
As of tablets and below, these columns become full width leaving a nice white border around the jumbotron.
Regarding the ongoing auctions preview, these are nicely displayed in large screens in 4 columns, adjusting to 2 in tablets and into 1 full-width column in mobile devices, as planned.

### Functionality
In order to be able to display the ongoing auctions preview, I have decided to reuse the same functionality used to display all the auctions but filtering the results to 4. The auctions are displayed in the order that these are appendend to the ongoing_auctions list.

For each of the auctions, I retreive the corresponding info to display to the user, namely: product image, product category, product condition, product title, product brand, auction base amount, the start/end datetimes and its unique countdowntimer.

Moreover, for each of them I also check the current highest bid by getting all the bids for that specific auction, ordering them by most recent first, and only saving the most recent bid as it is always the highest one.

When clicking on the "See details" button or the auction image, if the user is authenticated it will take him/her to the auction details page. If not authenticated, the user will be redirected to the Sign In page.

### UX
#### User Goal: The homepage must be clear, intuitive and self-explanatory about the purpose of the website

When the user enters the landing page, he/she is confrontated with a visually appealing website, with a minimalistic design, confortable and captivating colors, without overwhelming the user with tons of information.

The landing page has a small intro text, describing its core intent and uses the ongoing auctions preview as the perfect explanatory tool of the website to the user.

### Lighthouse report

## Auctions
### Responsiveness
#### Tested on:
* Devices: Acer Spin, MacBook Pro, iPhone8, iPhone11, iPhone12 mini and iPad
* Broweser: Google Chrome, Firefox, Opera and Safari

#### Tested for:
* 

#### Conclusion:

### Functionality
### UX
### Lighthouse report

## User's Dashboard
### Responsiveness
#### Tested on:
* Devices: Acer Spin, MacBook Pro, iPhone8, iPhone11, iPhone12 mini and iPad
* Broweser: Google Chrome, Firefox, Opera and Safari

#### Tested for:
* 

#### Conclusion:
### Functionality
### UX
### Lighthouse report

## Auctions Management (for store owners)
### Responsiveness
#### Tested on:
* Devices: Acer Spin, MacBook Pro, iPhone8, iPhone11, iPhone12 mini and iPad
* Broweser: Google Chrome, Firefox, Opera and Safari

#### Tested for:
* 

#### Conclusion:

### Functionality
### UX
### Lighthouse report

## Checkout
### Responsiveness
#### Tested on:
* Devices: Acer Spin, MacBook Pro, iPhone8, iPhone11, iPhone12 mini and iPad
* Broweser: Google Chrome, Firefox, Opera and Safari

#### Tested for:
* 

#### Conclusion:

### Functionality
### UX
### Lighthouse report

## Navigation
### Responsiveness
#### Tested on:
* Devices: Acer Spin, MacBook Pro, iPhone8, iPhone11, iPhone12 mini and iPad
* Broweser: Google Chrome, Firefox, Opera and Safari
### Functionality

#### Tested for:
* 

#### Conclusion:

### UX
### Lighthouse report

## Footer
### Responsiveness
#### Tested on:
* Devices: Acer Spin, MacBook Pro, iPhone8, iPhone11, iPhone12 mini and iPad
* Broweser: Google Chrome, Firefox, Opera and Safari

#### Tested for:
* 

#### Conclusion:

### Functionality
### UX
### Lighthouse report