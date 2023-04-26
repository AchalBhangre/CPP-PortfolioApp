# CPP-PortfolioApp
 email sending Library is created
 
 defination 'send_confirmation_email' is implemented in email_lib.py
 
 in views.py send_confirmation_email is used inside registration defination view. 
 which will trigger the mail to user, once form is filled withh all necessary valid deatils
 
 
the libray is packed and published on pypi.org on yanked
setup.py and pyproject.toml is crreated with metadata

python3 -m build
python3 -m twine upload --repository testpypi dist/*
 
then through below command, user can install this library in their application

https://test.pypi.org/project/pkg-custom-emailsendingLib/0.0.1/
 
pip install -i https://test.pypi.org/simple/ emailsendingLib-AB==0.0.1

once aftr installing, below way library can be used

from emailsendingLib_AB import email_lib

in settings.py you need to add below lines

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'example@gmail.com'
EMAIL_HOST_PASSWORD = 'gmailAppTokenNeedtobeGenerated'
 
 