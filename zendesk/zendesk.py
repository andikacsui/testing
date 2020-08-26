import requests
import time
import json

class ZendeskAPI:

    def __init__(self):

        self.credentials = 'andika@gmail.com/token', 'token_from_zendesk' # anonymized
        self.zendesk_url = 'https://{zendesk_domain}.zendesk.com' # anonymized
        self.session = requests.Session()
        self.zendesk_api_tickets_url = 'api/v2/incremental/tickets/cursor.json?start_time=0'
        self.ticket_data = []
        self.next_url = None

    def connect(self):
        '''
        Connect to the zendesk session
        '''

        self.session.auth = self.credentials

    def get_tickets(self):
        '''
        Incrementally retrieve zendesk tickets by using cursor-based API

        :return:
        ticket_data: list of dictionary of retrieved data
        next_url: URL with the latest cursor for next extraction
        '''

        api_url = '{}/{}'.format(self.zendesk_url, self.zendesk_api_tickets_url)
        end_of_stream = False

        while not end_of_stream:

            response = self.session.get(api_url)

            if response.status_code == 429:
                print('Rate limited! Please wait.')
                time.sleep(int(response.headers['retry-after']))
                continue
            if response.status_code != 200:
                print('Error with status code {}'.format(response.status_code))
                exit()

            data = response.json()

            api_url = data['after_url']
            end_of_stream = data['end_of_stream']

            self.ticket_data.append(response.json())
            self.next_url = data['after_url']

        return json.dumps(self.ticket_data), self.next_url



if __name__ == "__main__":

    za = ZendeskAPI()
    za.connect()
    ticket_data, next_url = za.get_tickets()

    print(ticket_data)
    print(next_url)