## Permissions and Groups Setup

### Custom Permissions:
- `can_view`: Allows viewing books.
- `can_create`: Allows creating books.
- `can_edit`: Allows editing books.
- `can_delete`: Allows deleting books.

### Groups:
- **Editors**: Can create and edit books.
- **Viewers**: Can view books.
- **Admins**: Can perform all actions including deletion.

### Applying Permissions:
Permissions are enforced using the `@permission_required` decorator in views to control access based on user roles.
