# -*- coding: utf-8 -*-
import json
from time import sleep

import requests


class GraphQL:
    @classmethod
    def get_all(cls):
        query = """
        {
          allServiceTags {
            nodes {
              service {
                name
                alias
                owner {
                  username
                }
                topics
                description
                isCertified
                public
              }
              serviceUuid
              state
              configuration
              readme
            }
          }
        }
        """
        max_attempts = 5
        attempts = 0
        res = None
        while attempts < max_attempts:
            attempts += 1

            try:
                res = requests.post('https://api.asyncy.com/graphql',
                                    data=json.dumps({'query': query}),
                                    headers={
                                        'Content-Type': 'application/json'
                                    },
                                    timeout=10)
                if res.status_code != 200:
                    raise Exception(f'Status code is not 200, '
                                    f'but {res.status_code}!')
                break
            except BaseException as e:
                sleep(0.5)
                if attempts == max_attempts:
                    raise e

        data = res.json()
        return data['data']['allServiceTags']['nodes']
