Installation
============

Basic Installation
------------------
Add juntagrico-crowdfunding to the requirements.txt::

    git+https://github.com/juntagrico/juntagrico-crowdfunding.git

Django Settings
---------------
You have to add the app to your installed apps in your Django settings and add middleware

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'juntagrico',
        'juntagrico_crowdfunding',
    ]
    
    MIDDLEWARE = [
        ...
        'juntagrico_crowdfunding.middleware.FunderAccess'
    ]

and include the paths in `urls.py`

.. code-block:: python

    urlpatterns = [
        ...
        path(r'', include('juntagrico_crowdfunding.urls')),
    ]