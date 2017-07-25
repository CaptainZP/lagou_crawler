#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
import csv


def get_json(url, data):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
               'Referer': 'https://www.lagou.com/jobs/list_Python?px=default&city=%E5%8D%97%E4%BA%AC'
               }
    back_json = requests.post(url, data=data, headers=headers)
    return back_json.json()


def parse_json(back_json):
    job = json.loads(back_json)
    # page_size = job["content"]["pageSize"]
    result_size = job["content"]["positionResult"]["resultSize"]
    position_list = job["content"]["positionResult"]["result"]

    job_list = list()
    for i in range(result_size):
        this_job = position_list[i]['positionName']
        this_salary = position_list[i]['salary']
        this_district = position_list[i]['district']
        job_list.append(this_job)
        job_list.append(this_salary)
        job_list.append(this_district)
    return job_list


def main():
    url = r'https://www.lagou.com/jobs/positionAjax.json?px=default&city=南京&needAddtionalResult=false'
    page_no = 1
    while page_no < 3:
        data = {'first': 'false', 'pn': page_no, 'kd': 'Python'}
        job_json = json.dumps(get_json(url, data))
        job_list = parse_json(job_json)
        print(job_list)
        with open('lagou_job.csv', 'a+') as f:
            csvf = csv.writer(f)
            for i in range(0, len(job_list), 3):
                csvf.writerow(job_list[i:i+3])
        page_no += 1


if __name__ == '__main__':
    main()
