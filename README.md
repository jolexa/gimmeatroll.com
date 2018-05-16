## https://gimmeatroll.com

### WHAT?!
> _"What IS this?"_  :trollface:

This is a fun little serverless site. Don't take it too _seriously_, please. It
was fun to build and I was experiementing with AWS API Gateway and Lambda
integration. Every request to https://gimmeatroll.com/ will return a random
troll gif.

### How

This site is powered by a CloudFormation template that provisions:
* Route 53
* ACM Certificate (SSL)
* API Gateway with Custom Domain
* Lambda
* S3

![architechture](https://raw.githubusercontent.com/jolexa/gimmeatroll.com/master/architecture.png)

#### Caching?
I assume this will be used in Slack. When posted in Slack, the meta tag will be
cached in the "unfurl cache" on Slack's service for approximately 30 minutes.
Obviously, I cannot control this. So, to workaround that, this site does the
_same thing_ for any path on the url. That means,
https://gimmeatroll.com/some_text_goes_here
will also return a random gif. Now you can troll all the time. :trollface:

#### Rate Limiting?
> _"What if this goes viral?"_

True! I don't want to get charged! There is a rate limit of 1 req/s on the site.
At capacity, - this will still result in a $3.50+ service fee. =/
