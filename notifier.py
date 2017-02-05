#!flask/bin/python
from flask import Flask
from flask import request
from rocketchat.api import RocketChatAPI
import os

app = Flask(__name__)

def notify_rocketchat(app, release, release_summary, sha, user):
    api.send_message(':new: *Deis({env})* {app} v#{release} - _{release_summary}_'
            .format(app=app, release=release, release_summary=release_summary, env=env), topic)

@app.route('/notify_deploy', methods=['POST'])
def notify_deploy():
    app = request.args.get('app')
    release = request.args.get('release')
    release_summary = request.args.get('release_summary')
    sha = request.args.get('sha')
    user = request.args.get('user')
    print('notifying deploy app={app}, release={release}, release_summary={release_summary} topic={topic} '.format(app=app, release=release, release_summary=release_summary, topic=topic))
    notify_rocketchat(app, release, release_summary, sha, user)
    return ''

if __name__ == '__main__':
    env = os.environ.get('ENV', 'stag')
    debug_env = os.environ.get('DEBUG', 'false')
    username = os.environ.get('ROCKETCHAT_USERNAME', 'user')
    password = os.environ.get('ROCKETCHAT_PASSWORD', 'password')
    topic = os.environ.get('ROCKETCHAT_TOPIC', 'deis-releases')
    port = int(environ.get('PORT', 5000))
    url = os.environ.get('ROCKETCHAT_URL', 'http://localhost:8080')
    api = RocketChatAPI(settings={'username': username, 'password': password,
        'domain': url})
    print 'initializing deis-rocket-notifier with rocketchat username={username}, url={url}, password={password}'.format(username=username, url=url, password=password)
    debug = False
    if debug_env == 'true':
        debug=True
    app.run(host='0.0.0.0', port=port, debug=debug)
