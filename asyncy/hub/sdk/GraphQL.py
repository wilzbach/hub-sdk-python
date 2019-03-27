# -*- coding: utf-8 -*-
import json

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
        res = requests.post('https://api.asyncy.com/graphql',
                            data=json.dumps({
                                'query': query
                            }),
                            headers={'Content-Type': 'application/json'},
                            timeout=10)

        data = res.json()
        return data['data']['allServiceTags']['nodes']
