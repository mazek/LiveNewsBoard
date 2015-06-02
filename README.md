# LiveNewsBoard

[![Join the chat at https://gitter.im/mazek/LiveNewsBoard](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/mazek/LiveNewsBoard?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Live News Board - news, data, info aggregator.

Goal is to create simple server with rest api that collects information from many sources and provides it via it's api. Default as a auto refreshing webpage. Could be used as a info, twitter, currency, changes in infrastructure configuration, releases announcements etc log.

This is a learning project. Don't get too serious ;)
Any help and suggestions appreciated.

## What You need for sure.

`apt-get install python-pip python-virtualenv git redis-server`

## Prepare a directory where you will hold all the files and download the code.

`mkdir ./lnb && cd lnb`

`virtualenv virt`

`source virt/bin/activate`

`git clone https://github.com/mazek/LiveNewsBoard.git`

`cd LiveNewsBoard`

`make install`

## Initialization

Create example data with `lnb --generate-fixtures`.

## Run instance

By default, lnb uses redis server as a backend. 
To start redis, just type `redis-server` on the second terminal.
Now you can just type `lnb` to run app server on port 5000.


#### Start!

Point your browser to: http://localhost:5000/www/index.html

#### Get all posts.
`curl -i http://localhost:5000/api/v1.0/posts`

#### Simple auth test.
`curl -u username:pass -i http://localhost:5000/api/v1.0/tasks`

#### Adding a post.
`curl -i -H "Content-Type: application/json" -X POST -d '{"author": "jan dlugosz", "sec_level": 0, "priority": 0, "source": "twitter", "message": "Przykladowy post mowiacy o niczym"}' http://localhost:5000/api/v1.0/posts`

#### Deleting a post(not implemented yet).
`curl -i -H "Content-Type: application/json" -X DELETE  http://localhost:5000/lnb/api/v1.0/posts/8`

#### Patch a post(Not implemented yet).
`curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/lnb/api/v1.0/posts/2`

#### Simple auth test.
`curl -u username:pass -i http://localhost:5000/api/v1.0/tasks`


## What could be done later on.
*  Many sources of information

*  Different priorities - with influence on formating and time of exopsure on the list.

*  Different classes of security with regard to data protection (eg. no limit, internal information).

*  Aggregator gathering data into queue.

*  Data timeout from the queue, maybe archived somehow?

*  Data with high priority on top of the queue?


## What sources of information could we use?

*  Information about releases?

*  Jira

*  Planned changes from ChM

*  Planned technical breaks.

*  News athered from people (maybe as a pull requests introduced into the queue)

*  Twitter and observed accounts.

*  RSS feeds.

*  Exchange rates?

*  Stock exchange

*  Jabber channels.

*  Hipchat rooms.


## Resources.
* http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

* http://codeforgeek.com/2014/09/refresh-div-angularjs-interval/

* http://codeforgeek.com/2014/09/two-way-data-binding-angularjs/

* http://tweetdump.info/320704340320993280/

* http://www.456bereastreet.com/lab/developing_with_web_standards/csslayout/2-col/

* https://docs.angularjs.org/api



