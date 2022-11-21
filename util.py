def date_format(dt):
    import datetime
    import humanize
    return humanize.naturaltime(datetime.datetime.now() - datetime.datetime.fromisoformat(str(dt)))


def message(content, code=200, extra={}):
    from flask import jsonify
    response = jsonify({
        'message': content,
        **extra
    })
    response.status_code = code
    return response


def error(content, code=400, extra={}):
    return message(content, code, extra)
