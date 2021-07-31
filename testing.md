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


## Profile/User's Dashboard
### Responsiveness
#### Tested on:
* Devices: Acer Spin, MacBook Pro, iPhone8, iPhone11, iPhone12 mini and iPad
* Broweser: Google Chrome, Firefox, Opera and Safari

#### Tested for:
* Pending payments
* Default Delivery Information
* Orders history

#### Conclusion:
Despite of this 3 sections being functionally independent, I have managed to integrate them quite nicely. These are separated in large screens between 2 rows (1st for the pending payments and the 2nd for the remaining sections), stacking the default delivery information and orders sections into a full width column in smaller devices.

To display the pending payments and the orders history, I have used a responsive table in order to allow horizontal scroll. This allows the user to have available all the information necessary at this stage. 


### Functionality

* Pending payments

The user will has available a dedicated space to display all the won auctions. To attain this the best way possible, I first retreive the user's past orders, if any. At the same time, loop through all the bids placed by the user, taking the auction id as a parameter and appending the matches to a unique auctions list, if the bid is not there yet. Afterwards, from the unique auctions list, I retreive the highest bid restricting the search to the only auctions where the user was the highest bidder, and checking if those items have been already sold. 

This functionality has passed all the tests and is working as intended, only displaying the current pending to be paid auctions ti the user, if he/she has them, or a cheering sentence if all payments are up to date.


* Default Delivery Information

The default delivery information is working as planned. The form is being prepopulated with the default user info straight from the DB and on click of update my info button, the user receives a success message stating the profile has correctly updated or and error message if profile fails to be updated.


* Orders history

The orders history section is merely displaying the orders list for a given authenticated user. The orders are created at a later stage during the checkout phase.

On click of the order number, the user is redirected to a new page, displaying the full detail of their past order. The user is, as well, alerted to the fact that he/she is looking into a past order.

The testing succeeded for this functionality as it is working as planned, only displaying the concluded orders for that specific user.

The order detail page is shared with the checkout success page, adapting to the situation if the user just finished a payment or, in this case, he/she comes from the profile page. All redirects are working properly.


* Add to bag and proceed to checkout

***For the sake of clarification, the words bag and cart are being displayed in the code interchangeably.***

To attain this functionality, I first get all the auctions and all the bids linked to each one of them, if any bid was placed in the auction. 

If no bids were placed, the functionality ends here. If bids do exist, than before creating the new bag, I first rensure that no other bag, for that specific auction with that specific highest bid from that specific user does not exist. If that specific bag do exists, it will be deleted, and the new bag created instead.

This option only allows the user to proceed to the checkout 1 item at a time, meaning that he/she won't be able to make bulk payments. This choice has been thought carefully in order and the reason why I picked this way is to not force the user to have to pay for a big amount if at the moment that is not possible, due to several reasons. This way, the user has the option to pay for the articles that he/she can pay at that moment. 

In the future, I intend to implement bulk payments, giving the user the option to choose which items they want to pay, for via checkboxex displayed in the table.

The functionality is fully working, no bags are being displayed duplicate and only the ones not paid yet are shown. The checkout button takes the user to the checkout.

### UX

#### User Stories
* I want to see my outstanding auctions
When the user goes to his/hers dashboard/profile page, he/she is confrontated with the pending payments table. If auctions are outstanding, they will be displayed in that table, if not the table displays a cheering message that no outstanding payments are available.

This user story is tackled perfectly in this approach.


* I want to see my history of won auctions
On the same line as the previous point, the user is also shown a table with the summary of all the auctions that he/she won. This table not only meets but exceededs the user story, giving the usert he option to see the full details of the won aution.


## Auctions Management (for store owners)
### Responsiveness
#### Tested on:
* Devices: Acer Spin, MacBook Pro, iPhone8, iPhone11, iPhone12 mini and iPad
* Broweser: Google Chrome, Firefox, Opera and Safari

#### Tested for:
* Data tables for auctions/products
* Add/Edit forms for auctions/products

#### Conclusion:

Due to the high amount of data to be displayed in these 2 sections (acutions & products), I have decided to use the DataTables from jQuery in order to guarantee the best responsiveness and UX for the site owners.

The tables are displaying the most important corresponding info com with a search and pagination functionality. This approach has saved me a lot of time during the development phase.

On small and medium devices, due to the amount of information, the tables auto generate an horizontal scroll but on large devices all the info is displayed without it in one good-looking and easily readble table.

The forms are displayed full width across devices and are fully responsive and the images stack nicely in smaller devices when there are more than 1 and no issues are present.

### Functionality
* Auctions/Products CRUD functionalities

In order to display all the auctions and products in their respective tables to the super user I simply get all the auctions and products that are saved in the DB, passing to the front all the important fields from the Auctions/Products models.

These tables also contain an edit/delete button per line to give the super user the ability to edit/delete these one per one if necessary.

To delete an auction or product these functions get that specific auction/product and delete it from the DB. This is not done without a prior reconfirmation displayed through a modal.

If the superuser decides to edit the auction/product, he/she is redirected to the specific form, which is being prepolupated with the current info stored in the DB. On change of the forms and submiting the forms, the new info is stored in the DB and the user redirected to the respective DataTable with a nice message confirming the editing was susscessfuly. If not, an error message is displayed.

Still during the editing, a form validation of the required fields is done, not allowing the user to proceed without completing these.

Moreover, as explained before, this edit form does not give the user the option of updating these, displaying a warning to do it so in the Django Admin.

Back to the Auctions Management page, the user is shown a button to add new auctions, which will take him/her to the add auction form.

In the form, upon submission, a datetime verification is done. If the auction start datetime is later than the current time and if the end datetime is later than the start enddate time, it allows the user to create the auction, if not, an error message will pop up with the corresponding message guiding the user to what the problem was during the submission. If submission is successfull, the user is redirected to the auctions management page with the success message in the toast.

The add product follows the exact same logic, but instead of dealing with the datetime conditions, it has the multiple images twist. This means that for each image that is uploaded to the form, it creates an Image object and sets the first image as the main image.

On save, the product is added to the DB, the user successfully informed and redirected to the product management section. If not, an error message is displayed. Form validation does not allow the user to proceed withou filling all the required fields first.

CRUD functionality is fully met in this approach.

### UX
#### Site owner's stories
* I want to add products to auctions

Whenever, the store owner wants to add a product to the auctions, he goes has to go to the auctions manegement page. Here, he can proceed to the auction creation page, if the product he wants to sell already exists, or move to the products management if not.
In case the the product already exists, he enters the add auction form and form all the products list in the select box, he can select the desired product to be sold. After going through all the fields in the form, he is able to submit the form and the auction is created and the product put for auction.

With this, this store owner's story is fully met.

* I want to delete/edit auctions created 

Whenever the site owner has the need to edit or delete an auction, he can start these actions form the DataTable in the auction management page.
If the intention is to edit, clicking in the corresponding icon of that given auction will take the user to the edit form of that specific auction. Here the user can edit all the fields and submit once more the auction for sale.
Whenever the site owner decides to move on with this action, he is alerted to the fact that he need to respect the datetime format of the start and end date times.

If delete is the action that the user want to pursue, the trash icon in the DataTable triggers a reconfirmation modal to guarantee that the user did not press it by mistake and unintentionally deleting an auction.

In the future I want to restrict the delete auction to only the ones that did not start yet, in order to safeguard a fair and safe platform for the user,

User story is fully met.


* I want to have an overview of the items sold

As a site owner, considering the potential amount of auctions that will created, guaranteeing that he/she can check which items are already sold is crucial for a good management.

This is tackled by the is_sold boolean field in the auctions are displayed in the auctions management page.



## Checkout
### Responsiveness
#### Tested on:
* Devices: Acer Spin, MacBook Pro, iPhone8, iPhone11, iPhone12 mini and iPad
* Broweser: Google Chrome, Firefox, Opera and Safari

#### Tested for:
* Checkout form
* Order Summary

#### Conclusion:

On small and medium devices, these two sections are displayed on top of each other, being the first one the order summary, containing the most important info for the user, followed then by the payment form. In large devices these are placed next to each other.

No responsivness issues were detected.

### Functionality
* Checkout bag/Order summary

When the user proceeds to the checkout from the profile page, he/she triggers the creation of a session bag.
For this functionality to work, I grab the current bag of the user that contain all the  won auctions and for the items in the bag filter them via the item auction id and the item bid id, storing them in the checkout bag (session). If any other session bag already exists, it is deleted first in order to avoid duplicate items to be paid during checkout.

The bag is then complemented with the auction fee, which sums up to the bag total in order to attain the grand total.

The auction fee is calculated according to the amount of the bid. Whenever the order total is less than €500, an auction fee of 5% is calculated, between €500 and €999 it applies a 2,5% and for the rest a 1%.

This amount is then stored in the intent variable together with the payment currency to be used by Stripe.

* Checkout form

The checkout form is powered by the django forms, and it has prefilled the user details with the information saved up till that moment in the user profile. The same goes to the Delivery Information.

The card number input field verification is handled via JS following the stripe documentation.

* Payment
The payment follow has per base the stripe documentation, which I have followed in order to implement this feature.

Payments are being done correctly, followed by the order creation in the DB, and a confirmation email to the user triggered.

The entire payment flow is working properly.

### UX
#### User stories:
* I want to have a full overview of how much I will pay for the won auction in the checkout

When the user gets to the checkout page, he can immediately see the order overview under the order summary.
This summary meets this user story fully.


## Navigation
### Responsiveness
#### Tested on:
* Devices: Acer Spin, MacBook Pro, iPhone8, iPhone11, iPhone12 mini and iPad
* Broweser: Google Chrome, Firefox, Opera and Safari
#### Tested for:
* Logo display across devices
* Nav links display
* Buttons across the pages
* Auctions search bar

#### Conclusion:
The logo responds well in all devices, adapting its size responsively depending on the type of device.

Nav links are displayed on the right side of the page in large screens and compacted into an hamburguer icon in small and medium devices where on toggle these are nicely displayed in the center of the dropdown menu.

The auction search bar, giving the user the ability to search for a particular item, is placed in the navbar on purpose, allowing helping the user to find any particular auction regardless of the step he is taking at any given moment. It also responds well in every device format.


### Functionality
All navlinks and buttons work as intended, not broken and take the user to the wanted page.
The logo responsiveness is powered by the follwoing piece of CSS, adjsuting the font-size automatically:

    #dlbrand{
        font-size: min(max(2rem, 7vw), 5rem);
    }

The auction search bar functionality, is based on a search query, look for those word(s) in the product title and/or product description and filter the auctions list to the matches it gets.

The auctions counter will warn the user if there is no ongoing auctions matching the search criteria.

The search bar functionality is working as planned.

### UX
#### User requirements:
* Easy and intuitive navigation system across pages through a navbar
* Efficient way of finding auctions of interest

Even though the navbar does not tackle any user stories, it meets the user requirements.

Tha navbar and buttons across the website give the user the ability to easily navigate from page to page without any inconvenience and the sear the search bar is the efficient way of finding auctions of interest.

These requirement are fully met


## Footer
### Responsiveness
#### Tested on:
* Devices: Acer Spin, MacBook Pro, iPhone8, iPhone11, iPhone12 mini and iPad
* Broweser: Google Chrome, Firefox, Opera and Safari

#### Tested for:
* Broken links
* Responsiveness across devices

#### Conclusion:
The footer does not present any broken link and responds well across devices.

It is devided in 2 rows, each one of them in 3 columns that stack nicely and smoothly in small devices. 

### Functionality
### UX
All links open the corresponding pages. The ones that link to a 3rd party website/app are opened in a new tab.

#### User requirement:
* Contact information easy to find

User is able to find all the points of contact with the store owner via the footer in an easy manner.

User requirement is fully met.


## Lighthouse reports

### Homepage Desktop
![Lighthouse report Desktop Homepage](/README-images/homepage-desktop.png)
### Homepage Mobile
![Lighthouse report Mobile Homepage](/README-images/homepage-mobile.png)


### Auctions Desktop
![Lighthouse report Desktop Auctions](/README-images/auctions-desktop.png)
### Auctions Mobile
![Lighthouse report Mobile Auctions](/README-images/auctions-mobile.png)


### Auction Detail Desktop
![Lighthouse report Desktop Auction Detail](/README-images/auction-detail-desktop.png)
### Auction Detail Mobile
![Lighthouse report Mobile Auction Detail](/README-images/auction-detail-mobile.png)


### Dashboard Desktop
![Lighthouse report Desktop Dashboard](/README-images/dashboard-desktop.png)
### Dashboard Mobile
![Lighthouse report Mobile Dashboard](/README-images/dashboard-mobile.png)


### Auctionsmng Desktop
![Lighthouse report Desktop Auctionsmng](/README-images/auctionsmng-desktop.png)
### Auctionsmng Mobile
![Lighthouse report Mobile Auctionsmng](/README-images/auctionsmng-mobile.png)


### Add Auction Desktop
![Lighthouse report Desktop Add Auction](/README-images/add-auction-desktop.png)
### Add Auction Mobile
![Lighthouse report Mobile Add Auction](/README-images/add-auction-mobile.png)


### Products Desktop
![Lighthouse report Desktop Products](/README-images/auctionsmng-products-desktop.png)
### Products Mobile
![Lighthouse report Mobile Products](/README-images/auctionsmng-products-mobile.png)


### Edit Product Desktop
![Lighthouse report Desktop Edit Product](/README-images/edit-product-desktop.png)
### Edit Product Mobile
![Lighthouse report Mobile Edit Product](/README-images/edit-product-mobile.png)


### Checkout Desktop
![Lighthouse report Desktop Checkout](/README-images/checkout-desktop.png)
### Checkout Mobile
![Lighthouse report Mobile Checkout](/README-images/checkout-mobile.png)

### Checkout Success Desktop
![Lighthouse report Desktop Checkout Success](/README-images/checkout-success-desktop.png)
### Checkout Success Mobile
![Lighthouse report Mobile Checkout Success](/README-images/checkout-success-mobile.png)


### Conclusion Lighthouse reports

Overall all the pages scores very good on point of performance, accessibility, best practises and SEO. 

Nonetheless it would be ideal if all the page would scores above 90 for mobile and desktop for all parameters. 

To achieve this in the future, I would implement the following:

* Serve images that are appropriately-sized to save cellular data and improve load tim by using responsive images

* Serve static assets with an efficient cache policy. I have already added metadata to my AWS Bucket, setting the max age for th eCache-Control for all static files and media files to max-age=94608000 but it is still mentioned as a point of improvement for the performance. I will research this more in order to improve this.


* Minify all the files in order to improve the loading time
