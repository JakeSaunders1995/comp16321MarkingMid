#!/usr/bin/env python3

import sys
import requests
import dateutil.parser as parser

dry_run=True

# Course deadline as unix timestamp
deadline=1636912800

# URL to submit grades to
udt_base="https://benchmark.cs.manchester.ac.uk/rest/api/courses/current/COMP16321/assessment/16321-Midterm-S-Python%30Midterm/user/"
udt_header={'Private-Token': "rGPPGWkETh1AzJ5FiztJK9Fi"}

# URL for commitstore lookup
commitstore_base="https://ci.cs.manchester.ac.uk/commitstore/rest/api/"
path_base="comp16321_2021%2F16321_python_coursework_"


def commitstore_get_subdata(path, commit):

    search_url = commitstore_base + "/push/project/" + path + "/commit/" + commit + "/find"
    request = requests.get(search_url)

    if request.status_code != requests.codes.ok:
        raise ValueError("Unable to locate push data for commit "+path+":"+commit)

    return request.json()


def store_grade(username, submission_date, late_flag, path, commit, grade):

    grade_url = udt_base + username
    request = requests.post(grade_url,
                            headers=udt_header,
                            data={
                                     'grade': grade,
                                     'late': late_flag,
                                     'submitted': submission_date,
                                     'notes': '{"path": "' + path   + '",'+
                                              ' "sha1": "' + commit + '",'+
                                              ' "comments": ""}'
                            })

    if request.status_code != requests.codes.ok:
        raise ValueError('Unexpected request status code (' + str(request.status_code) +
                             ') while setting student mark (' + username + ', ' + str(grade) + ', ' +
                             submission_date + (', late' if late_flag else '') + ')' + str(request.content))

username = sys.argv[1]
commit   = sys.argv[2]
grade    = sys.argv[3]

path = path_base + username
resp = commitstore_get_subdata(path, commit)

parsed_submit = parser.parse(resp["events"][0]["timestamp"])
timestamp = parsed_submit.timestamp()
late = 1 if timestamp > deadline else 0

if not dry_run:
    print("Storing grade " + str(grade) + " for " + username + " late is " + str(late))
    store_grade(username, resp["events"][0]["timestamp"], late, path, commit, grade)
else:
    print("DRY-RUN: Would store grade " + str(grade) + " for " + username + " late is " + str(late))
