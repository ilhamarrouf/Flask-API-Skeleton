"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 18/04/20
    :time: 08.29
"""

from app import app
from app.jobs import example_job
from app.utils.response import respond_json
from flask import Blueprint, request, url_for

mod = Blueprint("homepage_controller", __name__)


@mod.route("/", methods=["GET"])
def index():
    # capture log with level info store to storage/logs/yyyy-mm-dd.log
    app.logger.info('Hi, im logger with level info')

    # perform job with params
    # for n in range(10):
    #     example_job.perform.queue(n)

    return respond_json(
        message="Don't know where to go? Query /help for more information.",
        success=True,
        data=None
    )


@mod.route("/help", methods=["GET"])
def help():
    func_list = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint != "static":
            func_list.append({
                'rule': rule.rule,
                'methods': [method for method in rule.methods],
            })

    return respond_json(
        message="All URL endpoints",
        success=True,
        data=func_list
    )
