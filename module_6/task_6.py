from flask import Flask, url_for

app = Flask(__name__)


@app.route('/good_morning')
def good_morning():
    return "Утро доброе ***"


@app.route('/good_evening')
def good_evening():
    return "Вечер добрый ***"


@app.route('/new_year')
def new_year():
    return "С рождеством ***"


@app.route('/maslenitsa')
def maslenitsa():
    return "С масленицей ***"


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@app.errorhandler(404)
def list_routes(err):
    result = ''
    links = []
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    for link, name in links:
        result += f'<a href="{link}">{link}<a></br>'
    return "Страница не найдена, доступные страницы:</br>" + result


if __name__ == '__main__':
    app.run(debug=True)
