# djangocms-time-wizard
Simple plugin with django-time-wizard relation.

## Quick start

1. Install using pip:

    ```
    pip install djangocms-time-wizard
    ```

1. Add to your `INSTALLED_APPS`:

    ```
    'time_wizard',
    'djangocms_time_wizard',
    ```

2. Include the time_wizard admin URLs in your project urls.py:

    ```
    url(^'admin/', include('time_wizard.urls')),
    ```

3. Run `python manage.py migrate` to create the time_wizard and
   djangocms_time_wizard models.

## Configuration

The TimeWizard-Plugin has a wrapper for its child-plugins if they are not shown
on published pages. You can also disable this in your settings.py:

    ```
    DJANGOCMS_TIME_WIZARD_WRAPPER = False
    ```

The wrapper is a simple div with the class `time-wizard` and inline styling.
You can customize its appearance to whatever you want. **Note** that
child-plugins with `inline` styling may appear different because of the
additional wrapper around.

## Requirements

- django-cms
- django-time-wizard
