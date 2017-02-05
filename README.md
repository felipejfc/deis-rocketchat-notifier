deis-rocket-notifier
====================

A deis webhook rocketchat notifier

#### Usage

* It's recommended to use [virtualenv](https://github.com/pypa/virtualenv) to manage dependencies
* Install dependencies using pip with ```pip install -r requirements.txt```
* Configure as described below
* Run the project with ```python notifier.py```
* It can also be deployed into deis, note that the Procfile is already included into the project

#### Configuration

Set the following environment variables:

* ROCKETCHAT_USERNAME - the username that will send messaages to ROCKETCHAT_TOPIC
* ROCKETCHAT_PASSWORD - the password of the user that will send messages to ROCKETCHAT_TOPIC
* ROCKETCHAT_TOPIC - the topic on which notifier will notify new releases of apps (e.g. #releases)
* ROCKETCHAT_URL - the rocketchat url
