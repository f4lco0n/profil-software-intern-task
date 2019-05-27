import requests

from exam_stats import ExamsStats


class DataProvider:
    def __init__(self):
        pass


    def collect_response(self,num_of_pages):
        response = []
        session = requests.session()
        for i in range(1, num_of_pages):
            url = "https://api.dane.gov.pl/resources/17363/data?page=" + str(i)
            response.append(session.get(url).json())
        return response

    def extract_data(self) -> []:
        data = []
        responses = self.collect_response(32)
        for content in responses:
            json_data = content['data']
            for json in json_data:
                exams_stats_json = json['attributes']
                data.append(ExamsStats(exams_stats_json['col4'],
                                       exams_stats_json['col1'],
                                       exams_stats_json['col5'],
                                       exams_stats_json['col2'],
                                       exams_stats_json['col3']))
        return data

