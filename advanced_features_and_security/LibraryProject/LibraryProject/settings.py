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

# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security (HSTS) settings
SECURE_HSTS_SECONDS = 31536000  # Enforce HTTPS for one year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to all subdomains
SECURE_HSTS_PRELOAD = True  # Allow your domain to be preloaded in browsers' HSTS lists

# Ensure session cookies are sent over HTTPS
SESSION_COOKIE_SECURE = True

# Ensure CSRF cookies are sent over HTTPS
CSRF_COOKIE_SECURE = True

# Prevent the site from being framed (protect against clickjacking)
X_FRAME_OPTIONS = 'DENY'

# Prevent browsers from MIME-sniffing the response content type
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable the browser’s XSS protection and filter mode
SECURE_BROWSER_XSS_FILTER = True

# Redirects all HTTP requests to HTTPS for secure connections
SECURE_SSL_REDIRECT = True

# Enforces HTTPS for 1 year (HSTS)
SECURE_HSTS_SECONDS = 31536000
