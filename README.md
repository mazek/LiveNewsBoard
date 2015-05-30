# LiveNewsBoard

[![Join the chat at https://gitter.im/mazek/LiveNewsBoard](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/mazek/LiveNewsBoard?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Live News Board - news, data, info aggregator.

Goal is to create simple server with rest api that collects information from many sources and provides it via it's api. Default as a auto refreshing webpage. Could be used as a info, twitter, currency, changes in infrastructure configuration, releases announcements etc log.

This is a learning project. Don't get too serious ;)
Any help and suggestions appreciated.

## What You need for sure.

`apt-get install python-pip sqlite git`

`virtualenv virt`

`source virt/bin/activate`

## Prepare a directory where you will hold all the files and download the code.

`mkdir ./lnb && cd lnb`

`git clone https://github.com/mazek/LiveNewsBoard.git .`

`make install`


## Initialization

Just run `lwb --generate-fixtures`. This will create sample demo data.

## Run instance

Just type `lwb` to run server on port 5000.

### Testing links, assuming Your app is at: http://localhost:5000/

#### Accessing html page

To access web page on localhost: `http://localhost:5000/www/index.html`

#### Get all posts.
curl -i http://localhost:5000/api/v1.0/posts

#### Adding a post.
curl -i -H "Content-Type: application/json" -X POST -d '{"author": "jan dlugosz", "sec_level": 0, "priority": 0, "source": "twitter", "message": "Przykladowy post mowiacy o niczym"}' http://localhost:5000/api/v1.0/posts

#### Deleting a post.
curl -i -H "Content-Type: application/json" -X DELETE  http://localhost:5000/api/v1.0/posts/8


#### Not implemented yet:
curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/api/v1.0/posts/2

#### Simple auth test.
curl -u username:pass -i http://localhost:5000/api/v1.0/tasks

#### Adding a post.
`curl -i -H "Content-Type: application/json" -X POST -d '{"author": "jan dlugosz", "timestamp": 1422455451, "sec_level": 0, "priority": 0, "source": "twitter", "message": "Przykladowy post mowiacy o niczym"}' http://localhost:5000/lwb/api/v1.0/posts`

#### Deleting a post.
`curl -i -H "Content-Type: application/json" -X DELETE  http://localhost:5000/lwb/api/v1.0/posts/8`


#### Not implemented yet:
`curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/lwb/api/v1.0/posts/2`

#### Simple auth test.
`curl -u username:pass -i http://localhost:5000/lwb/api/v1.0/tasks`
>>>>>>> bf0b03e7065edf5603bc86c76984cdacce324848


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



