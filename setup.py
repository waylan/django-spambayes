from distutils.core import setup

setup(name='django-spambayes',
      version='0.1',
      description='A collection of utility apps for using ' \
                  'SpamBayes filtering within Django projects.',
      author='Waylan Limberg',
      author_email='waylan@gmail.com',
      url='http://code.google.com/p/django-spambayes/',
      packages=['djangobayes', 'commentbayes'],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )

