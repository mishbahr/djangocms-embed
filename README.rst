===============
djangocms-embed
===============


.. image:: http://img.shields.io/pypi/v/djangocms-embed.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-embed/
    :alt: Latest Version

.. image:: http://img.shields.io/pypi/dm/djangocms-embed.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-embed/
    :alt: Downloads

.. image:: http://img.shields.io/pypi/l/djangocms-embed.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-embed/
    :alt: License


Embedly supports more than 300+ content providers. Video, audio, photos, product and more. See http://embed.ly/providers

You will need a Embedly API key, you can sign up for an API key at http://app.embed.ly/signup

Features
--------

* Uses the Embedly API
* Embeds indexable by search engines (SEO-friendly)

Make your Embeds Visible to Search Engines. Your content looks like this to crawlers::

    <blockquote>
        <h4><a href="http://embed.ly">
          Embedly makes your content
          more engaging and easier to share</a></h4>
        <p>
          Embed Content On Any Site. Bring engaging content
          to your viewers. Our embeds display whether you're
           on the web or mobile.
        </p>
    </blockquote>

Instead of a simple a tag like::

  <a href="http://embed.ly" class="embedly-card">Embedly makes your content more
    engaging and easier to share</a>


Embedly Features
----------------

**Responsive Embed**

Embeds are responsive and adapt to automatically fit the page they are placed in.

**Google Analytics**

Embedly will send events in your Google Analytics dashboard! You can see clicks on social buttons, plays of a video and even when a user clicks on a video recommendation.

**Social Sharing**

Embedly allow you to publish content into your social networks with built-in sharing, tweeting, and reposting.

For more information, see: http://embed.ly/cards

Quickstart
----------

1. Install ``djangocms-embed``::

    pip install djangocms-embed

2. Add ``djangocms_embed`` to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'djangocms_embed',
        ...
    )

3. Sync database::

    python manage.py migrate


4. Add ``DJANGOCMS_EMBED_API_KEY`` to your project settings::

    DJANGOCMS_EMBED_API_KEY = '<Embedly API Key>'

