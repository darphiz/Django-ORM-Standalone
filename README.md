# Django Standalone ORM

Leverage the power and simplicity of the Django ORM in your non-web Python projects with ease.

## Getting Started

Follow these steps to set up and use the Django ORM in your standalone Python project:

1. **Clone this project**:
    ```bash
    git clone <repository_url>
    ```

2. **Connect to your database**:
    Configure your database settings in the `settings.py` file as you would in any Django project.

3. **Write your models**:
    Define your database models in `database/models.py` following the standard Django model syntax.

## Importing the Models

You can import your models easily in your project files. Instead of the traditional way, you can now use:

```python
from database import YourModelClass
```