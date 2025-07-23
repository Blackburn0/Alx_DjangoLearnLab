# This is django project setup

## Permissions and Groups Setup

### Custom Permissions
The `Book` model has the following custom permissions:
- `can_view`: Allows viewing books.
- `can_create`: Allows creating books.
- `can_edit`: Allows editing books.
- `can_delete`: Allows deleting books.

### Groups
The following groups are configured:
- `Viewers`: Assigned `can_view` permission.
- `Editors`: Assigned `can_view`, `can_create`, and `can_edit` permissions.
- `Admins`: Assigned all permissions (`can_view`, `can_create`, `can_edit`, `can_delete`).

### Enforcing Permissions
Permissions are enforced in views using the `@permission_required` decorator. For example:

# Security Measures

## Settings
- `DEBUG` is set to `False` in production to prevent sensitive data exposure.
- `SECURE_BROWSER_XSS_FILTER`, `X_FRAME_OPTIONS`, and `SECURE_CONTENT_TYPE_NOSNIFF` are configured to protect against XSS and clickjacking.
- `CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE` ensure cookies are sent over HTTPS.

## Templates
- All forms include `{% csrf_token %}` to protect against CSRF attacks.

## Views
- User inputs are validated using Django forms.
- Queries are parameterized using Django ORM to prevent SQL injection.

## Content Security Policy (CSP)
- Configured to restrict content sources to `'self'` and inline scripts/styles.