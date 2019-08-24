import entrypoint
import util
import repository
import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.redirect(flask.url_for('get_temperature'))


@app.route('/temperature')
def get_temperature():
    res = repository.fetch(entrypoint.DEVICES)
    temperatures = res.json()[0]['newest_events']['te']
    temperature = {
        'time': util.parse_date_time(temperatures['created_at']),
        'value': temperatures['val']
    }
    return flask.make_response(flask.jsonify(temperature))


@app.route('/users')
def get_users():
    res = repository.fetch(entrypoint.USERS)
    return flask.make_response(flask.jsonify(res.json()))


@app.route('/devices')
def get_devices():
    res = repository.fetch(entrypoint.DEVICES)
    return flask.make_response(flask.jsonify(res.json()))


@app.route('/appliances')
def get_apploances():
    res = repository.fetch(entrypoint.APPLIANCES)
    return flask.make_response(flask.jsonify(res.json()))


if __name__ == '__main__':
    app.run()
