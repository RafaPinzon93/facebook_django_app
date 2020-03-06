# Basic Facebook App
Basic facebook app, login, long-lived access token. Show avatar and profile name.

## Instructions
Clone or download the project
```bash
git clone https://github.com/RafaPinzon93/facebook_django_app.git
```

test_ssh

### Configure
Using python 3.7
1. Create a python virtual environment ```python -m venv virtual_env```
2. Activate the virtual environment
3. Install the requirements ```pip install -r requirements.txt```
4. Configure postgres database, and configure it in the settings file:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'facebook_django_app',
        'USER': 'facebook_django_app',
        'PASSWORD': 'test',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
```
5. Run migrations ```python manage.py migrate```
6. Start the server ```python manage.py runserver```
7. Change your site domain name to localhost:8000
8. Create Social application:
   1. Choose Provider: Facebook
   2. In Client Id and Secret Key, Use your App ID and App Secret of your facebook app website: https://developers.facebook.com/apps/
   3. Add your site: localhost:8000

### Usage
1. Login with your facebook account.
2. It will show your profile picture and name.
3. If you remove the app of your facebook apps-websites it will deactivate your user.
