# **Deployment**

## Local Deployment

I have created Dusty Lantern using Github and Gitpod to write my code.

Then, I used commits to git followed by "git push" to my GitHub repository.

This project has been deployed to Heroku which was previously connected with the Speranza Repository in Github to automatically get all the pushes done in Github.

For this project you will need to create an account on Stripe for the checkout module as well as an account on AWS in order to store your static and media files.

### To run this project locally, follow the next steps:

This project can be run locally by following the following steps: ( as I have user used Gitpod for development, the next steps are specific to it. Adjustment may be necessary depending on your IDE. More information about installing packages using pip and virtual environments [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).


To clone the project: 

1. From the application's repository, click the "code" button and download the zip of the repository. 
    You can also clone the repository using the following command in your terminal:

    ``` 
    git clone https://github.com/arturmpinho/Dusty-Lantern.git
    ``` 

1. Access the folder in your terminal window and install the application's [link to required modules](https://github.com/arturmpinho/Dusty-Lantern/blob/master/requirements.txt) using the following command:

    ```
    pip3 install -r requirements.txt
    ```

1. In your IDE, create your env.py file at the root level of the application, containing the following lines and variables:

    ```
    import os

    os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"
    os.environ["DEBUG"] = "True"

    os.environ["DEFAULT_FROM_EMAIL"] = 'DEFAULT_FROM_EMAIL'

    os.environ["STRIPE_PUBLIC_KEY"] = "STRIPE_PUBLIC_KEY"
    os.environ["STRIPE_SECRET_KEY"] = "STRIPE_SECRET_KEY"
    os.environ["STRIPE_WH_SECRET"] = "STRIPE_WH_SECRET"
    os.environ["STRIPE_CURRENCY"] = "EUR"

    ```

    Please note that you will need to update the "YOUR_SECRET_KEY" with your own secret key, as well as the STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY and STRIPE_WH_SECRET with values provided by Stripe.

    If you're not sure how to get the above Stripe variables, please visit the [Stripe Documentation](https://stripe.com/docs)

    Tip for your YOUR_SECRET_KEY: you can use a [Password Generator](https://randomkeygen.com/) in order to have a secure secret key.

    It is recommended to use minimum the 'Fort Knox Passwords'.

    To find your YOUR_MONGODB_URI, go to your clusters and click on 'connect'. Choose 'connect' your application and copy the link provided. Don't forget to update the necessary fields such as password and database name.

    If you plan on pushing this application to a public repository, ensure that env.py is added to your .gitignore file in order to safeguard your sensitive information.


1. Migrate the database models by executing the following command in your terminal
    ```
    python3 manage.py migrate
    ```
1. Create a superuser and set up the credentials with the following command
    ```
    python3 manage.py createsuperuser
    ```
1. Run the application with the following command
    ```
    python manage.py runserver
    ```
    
    The address to access the website is displayed in the terminal  
    Add /admin to the end to access the Django admin panel with your superuser credentials

    
## Heroku Deployment 

1. Login to your [Heroku](https://www.heroku.com/) account and create a new app. Preferably, choose the region where you are located.

1. Once the app is created click on the resources button and under Add-ons, look for the Heroku Postgres to attach a postgres database to your project.
    
    ``` Select the Hobby Dev - Free plan and click 'Submit order form' ```

1. Scroll back up and click "settings". Scroll down and click "Reveal config vars". Set up the same variables as in your env.py :

    ! You shouldn't set the DEBUG variable in under config vars, only in your env.py to prevent DEBUG being active on live website. 

    ```
    AWS_ACCESS_KEY_ID = "AWS_ACCESS_KEY_ID"
    AWS_SECRET_ACCESS_KEY = "AWS_SECRET_ACCESS_KEY"
    AWS_S3_REGION_NAME = "AWS_S3_REGION_NAME"
    AWS_STORAGE_BUCKET_NAME = "AWS_STORAGE_BUCKET_NAME"
    USE_AWS = True
    
    DATABASE_URL = "This variable is automatically set when adding the Postgres Add on"

    SECRET_KEY = "SECRET_KEY"

    STRIPE_PUBLIC_KEY = "STRIPE_PUBLIC_KEY"
    STRIPE_SECRET_KEY = "STRIPE_SECRET_KEY"
    STRIPE_WH_SECRET = "STRIPE_WH_SECRET"
    STRIPE_CURRENCY = EUR

    DEFAULT_FROM_EMAIL = "your email address"
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_PASS = "EMAIL_HOST_PASS"
    EMAIL_HOST_USER = "EMAIL_HOST_USER"
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    ```
1. From this screen, copy the value of DATABASE_URL
1. After this go to your settings.py the dusty_lantern directory and comment out the default database configuration and add:
    ```
    DATABASES = {
        'default': dj_database_url.parse('DATABASE_URL you have just copied'))
    }
    ```

1. Login in to heroku via your terminal by using the following command 

```
 heroku login -i
```

In case you have set up two factor authentication on Heroku, you will need an API in order to proceed with the login

1. Migrate again with the following command
    ```
    python3 manage.py migrate
    ```


1. Create a superuser for the postgres database so you can have access to the Django admin by setting up the credentials with the following command
    ```
    python3 manage.py createsuperuser
    ```

    --> Don't forget to login to the admin page and check the boxes 'Verified and primary"

1. Load the data into your newly created database by using the following command: 

    ```
    python3 manage.py loaddata <name of file containing the data *>
    ``` 

    * db.json

1. After migrations are complete, change database configurations to:
```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
```
This set up will allow your site to use Postgres in deployment and sqlite3 in development.


1. Ensure the Procfile and requirements.txt files are created and updated in your local repository.

    Requirements:
    ```
    pip3 freeze --local > requirements.txt
    ```
    Procfile:
    ```
    echo web: python app.py > Procfile
    ```
1. The Procfile should contain the following line:
    ```
    web: gunicorn <project_name>.wsgi:application

    ```

1. Add your files and commit them to GITHUB by running the following commands:
    ```
    git add . 
    git commit -m "Your commit message"
    git push
    ```

1. Add your Heroku app URL to ALLOWED_HOSTS in your settings.py file
1. Disable collect static so that Heroku doesn't try to collect static files when you deploy by typing the following command in the terminal
    ```
    heroku config:set DISABLE_COLLECTSTATIC=1
    ```

1. Go back to Heroku and proceed to "Deploy" in the navigation. 
1. Go to your "deployment method"-section and Choose "Github" for automatic deployment.
1. Below, make sure your Github user is selected, and then enter the name of your repository. Click "search". When it finds the repository, then click the "connect" button.
1. Scroll down and click "Enable automatic deployment".
1. Just beneath, click "Deploy branch". Heroku will now start building the app.
1. When Heroku finishes the build, click "view app" to open it.
1. In order to commit your changes to the branch, use git push to push your changes via your IDE.


1. Tp store your static files and media files on AWS, you can find more information about this on [Amazon S3 Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).
    If you would prefer to follow a tutorial instead, visit [this tutorial on Youtube from Amazon Web Services](https://youtube.com/watch?v=e6w9LwZJFIA)

1. Set up your email service to send the bidding confirmation email, order confirmation email and user verification email to the users. You can do this by following the next steps (The following steps are specificely for Gmail)

(Be aware that this migth be different for other providers or the process might have changed over time)

* Go to your email account and go to your account settings
* Under Security, scroll down to Signing in to Google and make sure 2 step verification is turned on
* Under the same heading (Signing in to Google) you will see the 'App passwords' option.
* Click on the option, select mail for the app and under device type select other and fill in a name for your app.
* You will now get a password which you should copy and set it as a config variable in Heroku:

```
    EMAIL_HOST_PASSWORD = 'Password you just copied'
    EMAIL_HOST_USER = 'Your gmail account'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = smtp.gmail.com
    DEFAULT_FROM_EMAIL = "your email"

```
* Go to your settings.py in dusty_lantern directory and add the following:

```
    if "DEVELOPMENT" in os.environ:
        EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
        DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
    else:
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
        EMAIL_PORT = os.environ.get('EMAIL_PORT)
        EMAIL_HOST = os.environ.get('EMAIL_HOST')
        EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
        EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
        DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
```


