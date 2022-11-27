A simple chatbot based on chatterbot and wikipedia python module.

It's deployed on heroku so have a look at
https://chatbot-qsgdzexqtq-ue.a.run.app/

Note:It loads a bit slow so you might have to wait a lil bit.Also if application error occured please refresh the page again
and if the problem still persist report it to me.

It's a Flask app with SQLlite for storage adapter.
Built with Basic Html Css Js and Bootstrap.

#Search Options

wiki,Find,search and pedia should be used to search wikipedia for a topic.

#Server side stuff

Not really good at that but it uses gunicorn server and gevent worker.
I wanted to deploy it with Nginx but was not able to find any practical solution for it so I left it as it is.
If you know how please do share it.
