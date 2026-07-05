---
title: "Python FastAPI Tutorial (Part 4): Pydantic Schemas - Request and Response Validation"
source: "https://www.youtube.com/watch?v=9GHxnttXxrA"
author:
  - "[[Corey Schafer]]"
published: 2026-01-12
created: 2026-06-20
description: "In this Python FastAPI tutorial, we'll be learning how to use Pydantic schemas to validate API requests and responses in FastAPI. We'll create a schemas file with request and response models, add fiel"
tags:
  - "clippings"
---
*
*![](https://www.youtube.com/watch?v=9GHxnttXxrA)

In this Python FastAPI tutorial, we'll be learning how to use Pydantic schemas to validate API requests and responses in FastAPI. We'll create a schemas file with request and response models, add field validations for things like minimum and maximum length, update our GET endpoints with response models, and create a POST endpoint to add new posts. Pydantic schemas define your API contract - what data goes in and what comes out - and FastAPI uses them for validation, serialization, and automatic documentation. Let's get started...  
  
The code from this video can be found here:  
https://github.com/CoreyMSchafer/FastAPI-04-Pydantic-Schemas  
  
Full FastAPI Course:  
https://www.youtube.com/playlist?list=PL-osiE80TeTsak-c-QsVeg0YYG\_0TeyXI  
  
Pydantic Tutorial - https://youtu.be/M81pfi64eeM  
  
✅ Support My Channel Through Patreon:  
https://www.patreon.com/coreyms  
  
✅ Become a Channel Member:  
https://www.youtube.com/channel/UCCezIgC97PvUuR4\_gbFUs5g/join  
  
✅ One-Time Contribution Through PayPal:  
https://goo.gl/649HFY  
  
✅ Cryptocurrency Donations:  
Bitcoin Wallet - 3MPH8oY2EAgbLVy7RBMinwcBntggi7qeG3  
Ethereum Wallet - 0x151649418616068fB46C3598083817101d3bCD33  
Litecoin Wallet - MPvEBY5fxGkmPQgocfJbxP6EmTo5UUXMot  
  
✅ Corey's Public Amazon Wishlist  
http://a.co/inIyro1  
  
✅ Equipment I Use and Books I Recommend:  
https://www.amazon.com/shop/coreyschafer  
  
▶️ You Can Find Me On:  
My Website - http://coreyms.com/  
My Second Channel - https://www.youtube.com/c/coreymschafer  
Facebook - https://www.facebook.com/CoreyMSchafer  
Twitter - https://twitter.com/CoreyMSchafer  
Instagram - https://www.instagram.com/coreymschafer/  
  
#Python #FastAPI

## Transcript

**0:00** · Hey there. How's it going everybody? In this video, we're going to be learning how to use pyantic schemas to validate our API request and responses in fast API. So in this series so far, we've set up the basic structure of our API with some getit endpoints that return our post. But right now, we're just returning plain dictionaries with no validation. And we don't have any way to create post through the API yet. So in this video we're going to introduce paidantic and create schema files uh with request and response models.

**0:30** · We'll add field validations for things like minimum and maximum length. Then we'll update our git endpoints to use those response models and create a post endpoint to add new posts. So and then we'll test everything in the interactive docs as well. And at the end I'll show you why we need a database for the next tutorial. So first what is paidantic?

**0:56** · So it is a data validation library that uses Python type hints and those type hints aren't just for documentation uh like in normal Python code. Pyantic actually enforces them at runtime and gives you detailed error messages when something doesn't match up. And the nice thing is that pyantic comes built in with fast API. So when we installed fast API, pyantic was automatically installed as a dependency. So we don't need to install anything extra.

**1:26** · Now why are we covering this before the database? So fast API's biggest strength is how it integrates with paidantic. So these schemas define what data we accept from clients and what data we return. Uh the database which we'll cover next, it defines what we store. So we are keeping a nice separation of concerns here. Now if you're coming from a framework like Flask, uh validation usually looks like WT forms or manual checks.

**1:57** · Uh Pyantic is more Pythonic since it uses typins and it gives us automatic API documentation and better IDE support with autocomplete. It's a really nice workflow how they have it set up. Now, if you want a deeper dive, then I do have a full Pyantic tutorial that goes way more in depth on all of those features, and I'll leave a link to that video in the description section below.

**2:23** · But we're going to take a look at it here. Uh, but for now, let's look at our current docs. So, let me make sure I have my development server running here.

**2:34** · Let's look at our current documentation.

**2:37** · And this is still from the last tutorial. So, let me refresh that. So right now we have two API endpoints. We have one to get our post which returns a list of posts and then we have one for getting a single post uh with a post ID.

**2:55** · Now if I expand one of these then if we look down through here there is no information about what a response looks like. It just says successful response with no details. And we can't create posts through our API yet either. So, we're going to fix this by adding a response model to our endpoints, which tells Fast API exactly what we're returning. So, after this tutorial, our docs will show the exact fields, types, and validation rules. So, let's go ahead and get started with this.

**3:26** · So, first I'm going to create a new file for our schemas here. Uh, and this is going to be separate from our main. py file. So, up here in our project, I'm just going to create a new file. I'm going to call this schemas. py and I'll close down that sidebar. Now, first we need to import uh what we need from paidantic.

**3:50** · So I'll say from paidantic we will import base model and we will also import config dict and also field and we'll go over all of these here. So base model is the base class that all of our paidantic models inherit from. Uh field lets us add constraints like minimum and maximum length and config dict is the modern pyantic version two way to configure models.

**4:21** · So now let's create our base schema with the fields shared between creating and returning posts. So this follows the drive principle of not repeating ourselves here. So I will say that this is going to be the post base and this is going to inherit from base model. Now this is going to be what is shared between both creating and returning post.

**4:47** · So when we're creating and returning a post, we want things like the title that's going to be a string. We want the content that is also going to be a string. And we also want the author and that is also going to be a string. Now if you've used data classes then you can tell that this looks a bit like a data class but paidantic uses these types to validate data at runtime.

**5:14** · So right now these fields accept any string uh including empty strings. So let's add some constraints here. So if I say that we want this to be a field, we'll say that we want the min length for a title to at least be one. And let's set the maximum length to for a title to 100 characters.

**5:41** · Sounds good there. Let me copy this here. And now for our content, let's not set a max length here. We'll just say that the min length is one. And for an author, let's say that we want a min length of one and a max length of 50 characters. Now, you'll notice that we've set some constraints here like the minimum and maximum length, but we haven't given default values. So, without default values, it means that these fields are required. Okay.

**6:11** · So, now let's create a post create schema. So this defines what we accept when creating a new post. So I will just call this post create and that's going to inherit from post base that we just created. And for now I'm just going to put in a pass here. So right now this is identical to post base.

**6:37** · Uh but having uh this as a separate class shows our intent and also gives us some flexibility here. So for example when we add authentication later uh we might not need the author field here because we get that from the loggedin user but basically just by inheriting from post base here and then passing we're just saying when we create a post we also want the title the content and the author okay so now let's create a post

**7:10** · response and so I will call this post response let me spell that correctly and that is also going to inherit from post base. Now this defines what we return from our API and this is going to include fields that the client doesn't provide. So let me go ahead and do this and I will explain all of this here in a second. So I'm going to do this thing here where we do this model config config dict and I am going to say from attributes is equal to true.

**7:43** · Now I'll explain this in just a second here. Uh but now let's do the fields that we want in a response that are not provided by the client. So that would be something like an ID and an ID is an integer and then the date posted. uh that is just going to be a string for now. So that's going to be a string.

**8:10** · So post response inherits uh title, content and author from the post base and then it adds the ID and the date posted uh fields that are generated by the system and not provided by the client. Now just a quick note about the ID field. In my pyantic video, I mentioned that you generally should avoid naming fields ID since it's a Python built-in. But for database models and API responses, using ID is basically the standard convention.

**8:42** · Uh, so this is scoped to the class. It won't conflict with the global function and it won't trigger any llinter warnings or anything like that. And you're going to see this everywhere in real world APIs.

**8:56** · So I'm just sticking to that convention.

**8:58** · Now about this model config here uh in paidantic version two we configure models with config dict instead of the old config class. So setting from attributes equal to true that tells paidantic that it can read data from objects with attributes and not just dictionaries and this will be important when we add a database in the next tutorial. So you might see uh some older code using underscore or OM mode.

**9:25** · Uh that's the paidantic version one name for the same thing. But if \[clears throat\] this didn't make sense uh let me explain it a little bit more concretely here. So right now our posts are dictionaries. So we access data with uh you know bracket notation like uh you know post and then we get uh title. But when we add a database, our uh data is going to be accessed through dot notation like post.title.

**9:58** · So by default, paidantic uh knows how to read dictionaries. Uh but setting this from attributes equal to true, it teaches it how uh it allows it to also read from objects using that dot notation. So without that, when we would try to read from the database uh from our API, pyantic would fail. But with this uh it'll work just fine. Okay. So another thing here uh right now our date posted is a string uh because our in-memory data uses strings for dates.

**10:28** · When we add a database we're going to change this to actually be a datetime. Okay. So I'm going to save that. And now let's update our main.py to use our schemas. So first we are going to import these from the top. So up here I'll say from schemas we want to import uh both the postcreate and the post response.

**10:56** · Now we don't need post base in our main. py that is just our base class that others inherit from.

**11:07** · Uh we only want uh what we are going to be creating posts with and uh our post response for uh returning posts from the API. So now let's update our get endpoints here. So if I scroll down to the API section here, for slappi for these, here's what we have now. So we can see that we're just returning these posts here. But in the decorator here, I'm going to add something called a response model.

**11:36** · And now what are we responding with at this route? we are responding with a list of post responses. So I will add that in because remember this is the route that returns all of our posts.

**11:52** · And now just by adding that in fast API will validate that each post uh matches our post response schema and the documentation will show that exact structure and it's not just for documentation. response model also acts as a safeguard for us here. So if our data had extra fields that aren't in the schema, then those would be filtered out and if we have missing required fields, then we'd get an error.

**12:20** · Uh so it helps prevent accidentally exposing data that we shouldn't. Now for our single post route here, we are also going to do a response model, but here we're not returning a list of posts. we are just returning a single post. So I'll say that we expect a post response from a single post at this get endpoint. Okay.

**12:46** · So so far we can uh get posts but we can't create post. So let's create uh that post endpoint. Now this is where pyantic really shines. So let me actually grab this from my snippets here since it's a lot to type out but we'll go over exactly what's going on here.

**13:05** · So, let me grab this and I am going to uh let's put this right in between these here and I will save that. Okay. So, now let's go over exactly what's going on here. So, here you can see that we're using app.get for our decorator. Here we're using app.post. Uh a post request is what we use to create resources. So we are also so we're making a post to API post.

**13:36** · Our response model is going to be post response and our status code here is HTTP201 created. So that 2011 response that's a restful best practice uh when we create resources. It tells the client that a new resource was successfully created rather than just returning a 200 success. But the key part here is that we're using our schema uh postcreate. So fast API sees this type hint and automatically parses the JSON body.

**14:08** · It validates it against our schema and it returns a 422 validation error with details if anything is invalid. All before our function even runs. But if someone is trying to create a post and everything looks good and it matches all of the credentials that we set up in our schema here, which will be the title, content, and author with those fields and those constraints, uh, then it will run our function.

**14:38** · So inside the function, right now we're generating a new ID. I know this might look a little complicated here. That is just because we are manually generating IDs since we're using dummy data. Don't worry about the complexity there. Once we set up our database, uh the database will handle ids for us. So, this is just like a temporary thing to where if our uh last post had an ID of two, this will generate an ID of three. It's really not important.

**15:08** · So then after we get that new ID, then we're creating a dictionary using the validated data with, you know, post author, post title, and post content. and we have a hard-coded date for now. And then we are appending that to our post list which is up here at the top. Uh so we're appending that to our post list and then returning that new post.

**15:34** · So now that we've added this uh post creation route here and also added in these pidantic schemas, let me save this. And now let's go back to our documentation and I'll show you that this has improved a bit. So if I reload this here then we can see that we now have our create post route there. But before I show you that let me show you our get post route here. If I click on this then we can see in this response section down here it now shows that we have this uh list of post response.

**16:06** · The schema section shows all the fields uh with their types. And if I click on schema here, then we can also see the constraints as well. So we can see that this is a string. Uh shows us that it's between one and 100 characters, greater than one character and things like that.

**16:28** · So that's pretty cool. And if I look at our single post endpoint, let's see if that's the same thing here. Uh so we can see an example value. If I click on the schema, then we can see the same thing that we're just getting a single post here. it's no longer in that list and we can see all of the constraints on that as well. Okay. So now here's our new post endpoint for creating resources.

**16:50** · So if I look at this here, so we can see that the request body is expecting a title that is a string, a content, and an author. And again, if we click on schema, we can see exactly what this is expecting. So that's great because anybody using our API can see exactly what to send to the API to create a new post. So let's test this out. If I click on try it out here, then this is going to give us some sample values here.

**17:21** · So now let's fill in some of these. So I'll just say my new post. Doesn't really matter if I spell everything correctly.

**17:32** · This is my content. And let's just do a test user for that. And let me click execute here. And we can see that it gives us the curl command to do the exact same thing. We got a response code 201 which means that uh it was successful and that it created something. And we can see that it included that generated ID. Uh we get our title back, content, author, and our hard-coded date posted. So everything worked well. So now let's test some validation here.

**18:02** · Uh so for example, let's say that I tried to do a post here. I'll say this is my updated content, but I'm not going to add a title here. So if I execute that, then we can see that we get a 422 response.

**18:19** · And in this response, it says string should have at least one character. So it's telling us exactly what went wrong there. So now let's try removing a required field uh that we required for our post creation. So if I go back to the schemas here then remember postcreate just inherits from post base.

**18:41** · It's expecting title content and author.

**18:44** · So let's take away one of those fields.

**18:46** · So I'll just say that we didn't provide an author and I'll just say this is a test post. Let's execute that. Look at the response here. And it's saying, oh, let's see. This is uh expecting something in double quotes. Maybe it's because I have a comma there. Let me try that. Okay. Yeah, I think I had some bad JSON there. Uh, but now we're getting a 422 here and it's saying uh that we are missing a required field of author.

**19:16** · So all that validation, all of that is automatic. We didn't have to write any if statements, any try accept blocks, nothing like that. It just came built in with fast API and paidantic as long as we hook all of that up properly. Okay, so we did have that one successful created post. So let's see if uh that worked. So I'm going to go to uh try it out on get post here to get all of our post.

**19:46** · We can see that the one that was successful, it actually is in our list of posts there. And let's also check this on our HTML front end here. So if I go back and reload our page, we can see down here at the bottom that we have our new post. So it's there as well. So that's nice. So the API and the templates share the same data. So posts created through the API also appear on the templates page as well. Now, one thing to point out here, our template routes work exactly as they did before.

**20:18** · They're using dictionaries. They don't know about paidantic. Uh the schemas only apply to the a API endpoints uh where we set the response model or uh use pyantic types in parameters. And that's a nice separation that we have for now. API routes, they use pyantic for validation documentation. Uh template routes are just rendering the data for now. Now, our schemas are working great, but there's one big problem that we need to address here.

**20:45** · So, we just created our post. Uh, but let me show you what happens when we restart our server. So, I'm going to kill our development server here. And now, let's rerun that. And now, if I go back to our page, reload our homepage, we can see that our new post is gone.

**21:06** · And that's because we are just storing these posts in our if I go back to main.py, we are just storing these posts in a Python list in memory. So when the server restarts, that list is recreated with only the hard-coded post there. Any posts that we create are going to disappear. So obviously this isn't practical for real applications. We need data to persist across restarts and the solution obviously is to use a database and that's exactly what we're going to cover in the next tutorial.

**21:37** · So quickly let's recap what we covered here. So we created this schemas py file and we have our three schemas here. We have our post base uh that has shared fields. We have our post create for what we accept when creating a post. And right now it's the exact same as our post base here. And we have a post response for what we will return.

**22:04** · So it returns all the stuff that we accepted when we created the post, but also some things that are generated on the server like the ID and the date posted. We also added our field validation with uh constraints like min length and max length. and we updated our git endpoints uh to use these response models.

**22:26** · And again, not only did that improve the documentation in our API documentation, but it vastly improves our app itself because of the built-in validation that it gives us there. So basically the key takeaway here is that the pyantic schemas, they define our APIs contract. They specify what data goes in and what comes out. So fast API uses these for validation, serialization, and documentation.

**22:54** · It's a really elegant system how it all works together. So in the next tutorial when we add the database, we're going to restructure the schemas a bit to work with database relationships. Uh but the validation concepts that we learned here are still going to apply. But I think that's going to do it for this video.

**23:13** · Hopefully now you have a good idea uh how to use paidantic schemas for validating API requests and responses in fast API. In the next video, we're setting up our database with SQL alchemy. We'll replace that in-memory list with real persistent storage. Uh we will create database models that are separate from our pyantic schemas and connect everything so that data sticks around after we restart our server.

**23:39** · But if anyone has any questions about what we covered in this video, then feel free to ask in the comment section below, and I'll do my best to answer those. And if you enjoyed these tutorials and would like to support them, then there are several ways you can do that. The easiest way is to simply like the video and give it a thumbs up. Also, it's a huge help to share these videos with anyone who you think would find them useful. And if you have the means, you can contribute through Patreon or YouTube, and there are links to those pages in the description section below.

**24:06** · Be sure to subscribe for future videos, and thank you all for watching.