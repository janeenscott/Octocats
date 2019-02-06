import os
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hits():
    pass



    post_name = request.args.get('hits')

    count_text_file =  '{}_likes.txt'.format(post_name)

    print(count_text_file)

    if os.path.exists(count_text_file):
        counter_file = open(count_text_file, 'r+')
    else:
        counter_file = open(count_text_file, 'w+')

    post_count = counter_file.read()

    if not post_count:
        post_count = 0

    new_count = 1 + int(post_count)

    print(new_count)

    counter_file.seek(0)
    counter_file.write(str(new_count))
    counter_file.close()

    index_file = open('index.html', 'r')
    my_html = index_file.read()
    index_file.close()

    return my_html

# #
# post_name = request.args.get('hits')
# #not sure how to actually gather hits... but wherever this pulls from
# #   would appear in the quotes
#
# counter_file_name = '{}_page_vitis.txt'.format(post_name)
#
#     if os.path.exists(counter_file_name):
#         counter_file = open(counter_file_name, 'r+')
#     else:
#         counter_file = open(counter_file_name, 'w+')
#
#     hits_count = counter_file.read()
#
#     if not hits_count:
#         hits_count = 0
#
#     new_count = 1 + int(hits_count)
#
#     print(new_count)
#
#     counter_file.seek(0)
#     counter_file.write(str(new_count))
#     counter_file.close()
#
#
# index_file = open('index.html', 'r')
# my_html = index_file.read()
# index_file.close()
#
# return my_html
#

#code found online--possibly usable to edit for hit tracker
#
# from flask import Flask, request, render_template
#
# # app = Flask(__name__)
#
# counter = 0
#
#
# @app.route("/")
# def hello():
#     global counter
#     counter += 1
#     return str(counter)
#
#
#
#
# from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session
#
#
# # ...
# @app.route('/visits-counter/')
# def visits():
#     if 'visits' in session:
#         session['visits'] = session.get('visits') + 1  # reading and updating session data
#     else:
#         session['visits'] = 1  # setting session data
#     return "Total visits: {}".format(session.get('visits'))
#
#
# @app.route('/delete-visits/')
# def delete_visits():
#     session.pop('visits', None)  # delete visits
#     return 'Visits deleted'

