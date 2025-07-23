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