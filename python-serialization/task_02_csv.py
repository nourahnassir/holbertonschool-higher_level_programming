#!/usr/bin/env python3
"""Module to convert CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Reads data from a CSV file and converts it to JSON format."""
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            # استخدام DictReader لقراءة الصفوف كقواميس
            reader = csv.DictReader(csv_file)
            data = list(reader)

        # كتابة البيانات المحولة إلى ملف data.json
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except Exception:
        return False
