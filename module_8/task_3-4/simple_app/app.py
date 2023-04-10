import datetime
from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route("/good_time")
def good_time():
    return render_template('index.html')
    # return f"Доброго времени суток, текущее время: {datetime.datetime.now().time()}"


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
