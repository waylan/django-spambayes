Django-SpamBayes includes a few utility apps for [Django](http://djangoproject.com/) that offer an easy to use interface to the [SpamBayes](http://spambayes.sourceforge.net/) statistical anti-spam filter allowing filtering and moderation (with training) of comments, contact forms and other publicly submitted data.

**Note**: These apps do not depend on any of the e-mail client plugins (i.e.: Outlook plugin) available from the SpamBayes project. However, the core `spambayes` python package needs to be installed on your `PYTHONPATH`. It is recommended that you download and install a recent "source release" of SpamBayes appropriate for your platform.

## Apps: ##

### djangobayes ###

The "`djangobayes`" app is the workhorse that gets Django and SpamBayes to talk to each other. It contains a Django model for SpamBayes to store its 'learned' data in and a SpamBayes `Classifier` subclass that wraps the Django model. This is all wrapped up in a SpamBayes `Hammie` instance (`djangobayes.filter.filter`) which contains the public API accessed by other apps.

Basic Usage:
```
>>> from djangobayes.filter import filter
>>> score = filter.score('some text')
>>> if score < 0.3:
...     # do something with spam
... elif score > 0.8:
...     # do something with ham
... else:
...     # unsure - do something else
```

Of course, this will only work if SpamBayes has been trained. To train do:

```
>>> filter.train('some spam', True)
>>> filter.store()
>>> filter.train('some ham', False)
>>> filter.store()
```

In some situations you may want to filter based on more than a single body of text. For example, an author's name, e-mail address, IP address, etc. As SpamBayes is intended for filtering e-mail, you can pass in a message object rather than a plain string. djangobayes provides a handy shortcut, `build_msg` which excepts a `body` and any keywords you provide to build a message. For example:

```
>>> from djangobayes.filter import build_msg
>>> msg = build_msg('some text', author='Bob', email='bob@example.com')
>>> score = filter.score(msg)
>>> # or ...
>>> msg = build_msg('body text', **{'name' : 'Sue', 'ip' : '127.0.0.1'})
>>> filter.train(msg)
>>> filter.store()
```

As far as I can tell, SpamBayes doesn't really care what the names of the keywords are as long as they are consistent throughout your app. It simply sees them as e-mail headers and doesn't give any particular headers more weight than others. That's why the primary text _must_ be passed in separately.

As this is a SpamBayes API, see the SpamBayes documentation (and read the code) for more information.

### commentbayes ###

An add-on to the `django.contrib.comments` app that adds SpamBayes filtering. Requires "`djangobayes`" to be installed in the project. `commentbayes` simply uses signals to add scoring and training to `django.contrib.comments` moderation.

`commentbayes` supports two optional settings to indicate the ham and spam thresholds. Each should be a floating point number between 0 and 1:
  * `HAM_LEVEL` (default is `0.3`)
  * `SPAM_LEVEL` (default is `0.8`)

Assuming you have already installed `django.contrib.comments`, add `commentbayes` and `djangobayes` to `INSTALLED_APPS` in your `settings.py` file, run `manage.py syncdb` (to add the `djangobayes` table) and your all set. All future comments will be run through the SpamBayes filter. Any comment with a score greater than `SPAM_LEVEL` will be marked for deletion (`comment.is_removed = True`), any comment with a score equal to or between `HAM_LEVEL` and `SPAM_LEVEL` will be marked for moderation (`comment.is_public = False`), and any comment with a score less than `HAM_LEVEL` will be marked as ham.

To train SpamBayes, point your browser at `http://yourdomain.com/comments/moderate/` (an undocumented part of `django.contrib.comments`) and either 'approve' or 'remove' the comments awaiting moderation. In a short time and with good training, you will be enjoying spam-free comments!

You may want to set up a cron job to remove comments marked for deletion (`comment.is_removed = True`) on occasion.

### sb\_demo ###

The "`sb_demo`" app is a very simple demonstration that provides a single page of comments with feedback on the SpamBayes scoring. This app does not use Django's forms or various other mechanisms that would make is useful for others. It's simply a demonstration that filtering works - mostly.

It also adds a very basic template for flatpages with comments enabled which provides a demo of `commentbayes`.


## GAE Branch ##
The `gae` branch in the repo is an early semi-working version of the code for Google App Engine and BigTable. The file `sb.py` is essentially the same as the `sbayes` app above, but for BigTable. I'm not currently using or maintaining this branch, but it's available for anyone who wants it.