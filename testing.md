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
#### User Goal
* The homepage must be clear, intuitive and self-explanatory about the purpose of the website

When the user enters the landing page, he/she is confrontated with a visually appealing website, with a minimalistic design, confortable and captivating colors, without overwhelming the user with tons of information.

The landing page has a small intro text, describing its core intent and uses the ongoing auctions preview as the perfect explanatory tool of the website to the user.

### Lighthouse report

## Auctions
### Responsiveness
#### Tested on:
* Devices: Acer Spin, MacBook Pro, iPhone8, iPhone11, iPhone12 mini and iPad
* Broweser: Google Chrome, Firefox, Opera and Safari

#### Tested for:
* Display of the various categories
* DIsplay of the select box with sorting possibilities
* Display of the ongoing auctions

#### Conclusion:
The **category filters**, represented via FontAwesome icons and the category name, are displayed on large screens in a row, stacking in a nicely manner when moving to smaller screens, as intended.

The sorting functionality is represented by a centered select box, below the categories filter that maintains the same format across devices.

Regarding the auctions, these are, as well as in the homepage, nicely displayed in large screens in 4 columns, adjusting to 2 in tablets and into 1 full-width column in mobile devices, as planned.

### Functionality
* Filter auctions by category
These categories are the product of a for loop in the categories model, retreiving all the current categories available and adjusting automatically when a new category is added via the django admin. Whenever the user clicks in one of the categories, the corresponding auctions are being displayed.

* Sort auctions by category, product condition and end datetime
The select box is powered by a sort filter and direction which displays the auctions in the correct order. Whne filtering on First closing/last closing, the auctions that are to be started are also part of the equation. This might be confusing for the user and therefore I have decided for the auctions that still have to start, to include a sentence mentioning the end datetime of the auction.

* Auctions counter
This functionality is intended to retreive the number of ongoing auctions to the user. To attain this, I have used javascript to count all the card elements and depending on the length (0,1 or more than 1) I append the approriate sentance to the cards-counter element.

* List of ongoing auctions

As per explained above in the Home section of this testing, for each of the auctions, I retreive the corresponding info to display to the user and also checking for the current highest bid by getting all the bids for that specific auction, ordering them by most recent first, and only saving the most recent bid.

As well, on the "See details" button or the auction image, if the user is authenticated it will take him/her to the auction details page. If not authenticated, the user will be redirected to the Sign In page.

* Place bid functionality
When an user is definetly interested in an article, he is guided to the auction details page of that specific auction. Here, on top of the already mentioned information that is displayed to the user and of additional product info, he/she are now able place bids.

For this, the user has available a place bid button that submits the input field number to the DB. To accomplish this, I get a list of all the bids for that specific auction, if they exist, and once again order them by the bidding time (as it is always the highest bid). If the amount of the bid that the user submitted already exists, this will trigger an error message with the appropriate explanation of why the bid did not go through. If the bid goes through, it will be saved in the DB and a confirmation email sent to the user.

After several tests I conclude that the functionality is working properly and without any inconveniences.


### UX
#### User stories: 
* I want to see second-hand articles of my interest
In order to meet this user story, I have decided to implement the filtering functionality and the sorting based on different criterias.

Both functionalities are working porperly, which gives any user the ability of filtering and sorting between all the auctions according to their likes.

* I want to place bids on auctions of my interest
This user story is tackled on the auction detail page where the user has the ability of placing the bids on the auctions of interest.

The bidding functionality is working smoothly and gives the user the feeling of being in control. Unfortunately, there is a minor unresolved bug, which you can read more about [here](https://github.com/arturmpinho/Dusty-Lantern/blob/master/bugs.md), that might not generate the best UX. Nonetheless, I consider that this user story is well attained.

* I want to have a good overview of the ongoing auctions
The main auction page tackles this user story fully by displaying all the ongoing auctions.


### Lighthouse report

## Profile/User's Dashboard
### Responsiveness
#### Tested on:
* Devices: Acer Spin, MacBook Pro, iPhone8, iPhone11, iPhone12 mini and iPad
* Broweser: Google Chrome, Firefox, Opera and Safari

#### Tested for:
* Pending payments
* Default Delivery Information
* Orders

#### Conclusion:
Despite of this 3 sections being functionally independent, I have managed to integrate them quite nicely. These are separated in large screens between 2 rows (1st for the pending payments and the 2nd for the remaining sections), stacking the default delivery information and orders sections into a full width column in smaller devices.

To display the pending payments and the orders history, I have used a responsive table in order to allow horizontal scroll. This allows the user to have available all the information necessary at this stage. 


### Functionality
* Pending payments

The user will has available a dedicated space to display all the won auctions. To attain this the best way possible, I first retreive the user's past orders, if any. At the same time, loop through all the bids placed by the user, taking the auction id as a parameter and appending the matches to a unique auctions list, if the bid is not there yet. Afterwards, from the unique auctions list, I retreive the highest bid restricting the search to the only auctions where the user was the highest bidder, and checking if the items has been sold already. 

While testing this 



* Default Delivery Information
* Orders
* Add to bag and proceed to checkout

### UX

#### User Stories

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
#### User Stories
* I want to add products to auctions
* I want to delete/edit auctions created 
* I want to follow my auctions bids live
* I want to have an overview of the items sold

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