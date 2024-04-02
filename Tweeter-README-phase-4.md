# TWEETER

## What's Elon Musk up to now?

Remember to check your code from Phase 3 against the starter code for Phase 4 to
see how you did!


## PHASE 4 - Tweet CRUD!

Let's go ahead and turn our Tweets into a full CRUD feature!  We already built
our form, so next we just need to save the tweets from our form!

1. Lets get back to the `'/new'` route and add in some POST functionality!  Make
   sure to set up conditional logic for your `form.validate_on_submit()` and
   `form.errors`.  

    a. As far as creating a new tweet, your `id` can be the length of the tweets
    list.  The `author` and `tweet` fields need to be populated from the form
    data.  The `date` can just be generated at the time of the post (check out
    the datetime module, it should just be the date, no need for times). Lastly
    the `likes` attribute should be set to 0 or you can randomly generate a
    value for it. (the templates do divide likes by 1,000 and add a 'k'
    afterwards, Mr Musk has a decent amount of followers...)  Make sure to add
    that new tweet to the list of tweets when you are done!

    b. If we successfully made a new tweet, we should redirect the user to the
    `feed` page so they can see their new tweet!
    
    c. If for some reason we had errors on the form submission, we should return
    those to the browser.


If you can make new tweets and they show up in the feed, then you are ready to
move on to the update and delete routes!


2. Our next task is to define an update route.  This will be the trickiest of all
   the CRUD.  Update is very similar to create, but we'll need to populate existing
   data into the form when it's loaded...

   a.  Before we start on the route, we need to make a way to navigate to
   it.  That sounds like a job for an `<a>` tag!  In the feed, where we are
   iterating over the tweets, lets add a link to the update route (and while we
   are here we might as well add a link for delete too).  URL's of
   `"/update/<int:id>"` and `"/delete/<int:id>"`seem like good ideas for our
   routes, and we have access to the `tweet.id` to interpolate into the URL 

   b. Our goal is to be able to reuse the `TweetForm`for updating, and we don't
   even need to change the form class at all, so we can go right to defining our
   update route.  It will have many similarities to the create route, we will
   need to handle both `GET` and `POST` requests, the biggest difference is we
   need to populate the form with data on our `GET` requests.  Let's check the
   docs for something that can help us here ![WTForms-Docs](https://wtforms.readthedocs.io/en/3.1.x/fields/?highlight=process#wtforms.fields.Field.process)

   c. The `process()` method on our form Class will allow us to populate the
   form with our already existing data, provided the keys match up between our
   form class and how we're storing our data (in a dictionary for now, but
   soon it will be class instance from the database).  We do want to provide
   process with a keyword arguement, here we want to use `data=` and set it to
   the tweet dictionary we are plannig to update. but `obj=` will be what we
   need for class instances in the future.  We also want to be careful where we
   process the data.  For example, on a POST request, if we process the data before invoking `validate_on_submit`, we would unintentionally overwrite all of the incoming data.  Therefore, this should only happen on GET requets.

   d. If we have implemented the above correctly, we should now have an update
   link on each tweet in our feed (and delete too).  When we click the update
   link, we should navigate to our new tweet form.  The form should already be populated with the
   current data for the tweet.  However, we still can't successfully submit yet, and we have
   some display stuff to deal with too...

   e. What happens if we click the submit form on update now? The html form we
   created in "new_tweet.html" is set to POST to the `/new` route.  This will
   make a new tweet, but it will not update the one we are editing like we want.  We can add
   all the key value pairs we want/need when we render a template, we are
   already sending our form and our errors if they exists, so one more key value
   pair to help us out here is no trouble!  We could set `type="update"` whenever
   we render our update form, and use some conditional logic in our Jinja
   template to render a form tag that has the action of `"/update/<int:id~>"` if
   type="update" and render the form tag for new posts if there is no type of
   "update" (we could use a boolean too).  We could add the title of the page to
   this `if / else` block too so that new posts say 'Create a Tweet' and updating
   tweets says 'Update Tweet'.  If we are going to hit the update URL we defined
   as the action to our form, we will need the tweet's id too.  We can send this
   with another key value pair in our render_template call.   We could also add
   another `if / else` block for our submit button, and render the `form.submit` for
   new tweets.  For updates, we'll render a button tag like this: 
   ```html
   <button type="submit">Update Tweet</button>
   ```  

   f. Almost there, we did say update is the most work!  Now we just need to
   finish the POST functionality in our route.  We can access the id from our route parameters, and use it to select the tweet from our list of tweets.  Then, simlar to how we implemented the create row, we'll update each attribute with the form.data we receive in the route.  Navigating back to the feed at the end of this update seems logical.  Now you should be able to update your tweets!
   

3. Last but not least, we need to add in a delete route!  

   a. We should already have an `<a>` tag in our feed from when we added it for our update...

   b. We want to make a delete route that will accept the id of the tweet as a route parameter.  We can retrieve the tweet the same way we did with update, and then use the `list.remove()` method to delete that tweet!  After a successful delete, we should be navigated to the `/feed` route where we can see that the tweet has been removed.  Now, our delete should work, at least once...  Any thoughts on an issue this might create?

   c. This would not be an issue if we were working with a database (like tomorrow).  However, since we are playing with list indexing, when we delete a tweet like how we did above, it will throw the id attribute we are storing in the tweet not just 1, but 2 off from the index that it's being stored in.  (Tweet with id of 1 was in index 0, we delete it so now Tweet with id of 2 is in the index of 0).  To fix this, we can iterate through all of the tweets after a delete and reassign their id's to be index + 1.  Now we should be able to delete all of the tweets without error.


After making all of these changes, we have now completed this project!  You have successfull made your first full feature CRUD with Flask!  There is a link to the solution for Phase 4 and the
whole project below!  Unless you are bold and want to try to tackles some of
these bonuses? 💪🏻


## BONUS!

Feeling pretty good about your 'Tweeter' app?  Let's see if you take it further? Here
are some things to try out!

1. Our feed is not in order, it should display 'tweets' in order from most
   recent to least recent, but it is being displayed by ID.  If only we could
   get this `sorted` out...

2. How do those dates look?  If you used something like `date.today()` to create
   new dates, you should have gotten the date, but not in the same format as the
   'seed' tweets, can we fix that?

3. It would be pretty cool if we could actually like some of the tweets, right? And
   what if we changed our minds and wanted to un-like them?




# MEGA BONUS!

1. Message flashing!  Flask has the ability to flash a message along with the next request, and only with the next request.  Think of it similar to a toast notification.  Our create, update, and delete routes, all redirect back to the feed. So, if we set a flask message in the create/update/delete routes, the next request will render the `'/feed'` route which is where these messages will appear!  If you want to get this one implemented, you will need to visit the 
![flask-docs](https://flask.palletsprojects.com/en/3.0.x/patterns/flashing)

Here are a few tips to help get you started:
   1. Read the docs at the link above
   2. The "base.html" file under the links is a good place to display the flashed messages
   3. Create, Update, and Delete routes are great places to implement this