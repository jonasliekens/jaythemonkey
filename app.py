from flask import Flask, jsonify

app = Flask(__name__)

alcohol_percentage = 0
times_slapped = 0


@app.route('/')
def call_monkey():
    return jsonify(create_monkey_card())


@app.route('/drink')
def drink_with_monkey():
    global alcohol_percentage
    global times_slapped
    alcohol_percentage += 0.25
    if times_slapped > 0:
        times_slapped -= 1
    return jsonify({'message': 'Jay drank some beer with you!'})


@app.route('/slap')
def slap_the_monkey():
    global times_slapped
    global alcohol_percentage
    times_slapped += 1
    if alcohol_percentage > 0:
        alcohol_percentage -= 0.125
    return jsonify({'message': 'You slapped the monkey!'})


def create_monkey_card():
    return {
        'name': 'Jay the monkey',
        'state': define_monkey_state(),
        'hits': times_slapped,
        'alcohol': alcohol_percentage
    }


def define_monkey_state():
    if alcohol_percentage > 5.0 or times_slapped >= 100:
        return 'is dead.'
    if 0 <= alcohol_percentage < 0.5:
        return 'is.... being Jay the monkey.'
    if 0.5 <= alcohol_percentage <= 1.0:
        return 'is being funny.'
    if 1.0 < alcohol_percentage <= 3.0:
        return 'is singing Alestorm songs.'
    if 3.0 < alcohol_percentage <= 4.0:
        return 'is being awkwardly desperate.'
    if 4.0 < alcohol_percentage <= 5.0:
        return 'is humping everything with a heartbeat.'


if __name__ == '__main__':
    app.run()
