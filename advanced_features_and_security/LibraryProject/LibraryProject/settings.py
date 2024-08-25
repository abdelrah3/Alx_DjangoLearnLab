import os

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-default-secret-key')
AUTH_USER_MODEL = 'accounts.CustomUser'
bookshelf.CustomUser
DEBUG = False
SECURE_BROWSER_XSS_FILTER = True  # Enables the X-XSS-Protection header to prevent cross-site scripting attacks.
X_FRAME_OPTIONS = 'DENY'  # Prevents the site from being displayed in an iframe to avoid clickjacking attacks.
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents the browser from guessing the content type, reducing the risk of XSS attacks.

CSRF_COOKIE_SECURE = True  # Ensures the CSRF cookie is only sent over HTTPS.
SESSION_COOKIE_SECURE = True  # Ensures the session cookie is only sent over HTTPS.

MIDDLEWARE = [
    ...
    'csp.middleware.CSPMiddleware',
    ...
]

# Define your Content Security Policy
CSP_DEFAULT_SRC = ("'self'",)
CSP_IMG_SRC = ("'self'", 'data:')
CSP_SCRIPT_SRC = ("'self'",)
