import requests


def getting_organization_id(org_name: str):
    cookies = {
        'mutiny.user.token': 'a09a53f2-d3a9-4f8b-8b32-c56a4bb0d66c',
        'zp__initial_referrer': 'https://www.google.com/',
        'zp__initial_utm_source': 'www.google.com',
        'hubspotutk': '4a2146072fd6ebc326a2036b61a92083',
        '_gcl_au': '1.1.242791361.1712320823',
        '_ga': 'GA1.1.1316935289.1712320823',
        '_fbp': 'fb.1.1712320824991.1284233262',
        'zp__utm_medium': '(none)',
        'zp__initial_utm_medium': '(none)',
        '__hssrc': '1',
        '_hjSessionUser_3601622': 'eyJpZCI6ImQ3ZGNjNzZjLTc3NjUtNTI5Zi05YzhiLWM0MzcwY2ZkMDBmNSIsImNyZWF0ZWQiOjE3MTIzNzU2NTA2MjEsImV4aXN0aW5nIjpmYWxzZX0=',
        '__q_state_xnwV464CUjypYUw2': 'eyJ1dWlkIjoiODAxOTgyNzctYWFkZS00ZDc2LTgyMDktNGQ1OWVmMjU0ZWI3IiwiY29va2llRG9tYWluIjoiYXBvbGxvLmlvIiwibWVzc2VuZ2VyRXhwYW5kZWQiOmZhbHNlLCJwcm9tcHREaXNtaXNzZWQiOmZhbHNlLCJjb252ZXJzYXRpb25JZCI6IjEzNjg5Nzg2NzUyMjIzOTgyMDQifQ==',
        'ps_mode': 'trackingV1',
        'remember_token_leadgenie_v2': 'eyJfcmFpbHMiOnsibWVzc2FnZSI6IklqWTJNVEJqT0RCaE56VXlaalEzTURGak4yTTBPV000TkY5c1pXRmtaMlZ1YVdWamIyOXJhV1ZvWVhOb0lnPT0iLCJleHAiOiIyMDI0LTA1LTA2VDAzOjU2OjU4LjE5OVoiLCJwdXIiOiJjb29raWUucmVtZW1iZXJfdG9rZW5fbGVhZGdlbmllX3YyIn19--80577a53ef6a8d38a3a8f32902048d44017ee4f4',
        'zp__utm_source': 'accounts.google.com',
        '_clck': 'kpxcyb%7C2%7Cfkp%7C0%7C1557',
        '_cioanonid': '244fb471-512d-bb97-c967-15c0239cd826',
        'ZP_LATEST_LOGIN_PRICING_VARIANT': '23Q4_EC_Z59',
        'ZP_Pricing_Split_Test_Variant': '23Q4_EC_Z59',
        'intercom-device-id-dyws6i9m': 'd835a66e-ccf3-4d02-8ec1-b7bc725d3142',
        '_cioid': '6610c80a752f4701c7c49c84',
        '__stripe_mid': '6534d13a-416c-47e6-8b40-bd7d7f375fedc20888',
        'amplitude_id_122a93c7d9753d2fe678deffe8fac4cfapollo.io': 'eyJkZXZpY2VJZCI6ImUyMjg4MWRmLTg5NWEtNGFiYy04MGExLWZkNjZmZjFjYTMwMFIiLCJ1c2VySWQiOiI2NjEwYzgwYTc1MmY0NzAxYzdjNDljODQiLCJvcHRPdXQiOnRydWUsInNlc3Npb25JZCI6MTcxMjM5OTA1NzMyMCwibGFzdEV2ZW50VGltZSI6MTcxMjM5OTA1NzMyMCwiZXZlbnRJZCI6MSwiaWRlbnRpZnlJZCI6NCwic2VxdWVuY2VOdW1iZXIiOjV9',
        '__hstc': '21978340.4a2146072fd6ebc326a2036b61a92083.1712320822561.1712378455051.1712399064113.4',
        '__stripe_sid': 'b320a3a8-6577-4aa8-a526-a15b45bbcc43fd6d43',
        '_ga_76XXTC73SP': 'GS1.1.1712406524.5.0.1712406524.60.0.1375068758',
        '_clsk': '1e9jxd4%7C1712407070570%7C2%7C0%7Cd.clarity.ms%2Fcollect',
        'GCLB': 'CKHd3cS0n8q97gEQAw',
        'intercom-session-dyws6i9m': 'Znl3T2R1aXdXd0hVWE9TRDgwbURuSDF4cFJDTmR5eW5UY0xoV0h1L1NIREdhMi9MeUFPWEVDdUZpc2czSzRxcy0tRTNuMXdPYUVBNFl5S0xlelRmU1E0QT09--9518f4e8b4882fee7ac77b8287ee1a9a90a0b2de',
        'X-CSRF-TOKEN': '1gIJStU8aRhMoI2eFqiwac6CGGD5tkoC70m-Jr60Zuew4RCQDkhW3durZoJekJwsebjM4qCI2AboJepYQtcf8g',
        '_leadgenie_session': '1g47MhlU3%2BVOI3XncgFPrT3%2FEAMXeAIz65Yd54xf3eAiXh2ARLZzMkMl2CmXu%2BvuYM2LvmoGqY%2FUTvFt5IMzDZYDpcLFK%2FheS7KUszzwxys6jPGU9RZilyEVbZMgSY0dXfPxxIRB%2BRYsSsgM7HZx3tnw%2F9DzQEBrBJQGOivQLeNGd5V6B4Ws3KmQxIS386yCrg9jwFtUR2vZB%2BW75ZVX7Q2I4y69jKxvsuArDVa6rQMUVGAYya2GSOGQHX4h5EuAeP%2FyphQwxuCa79Dqtpn4rezjrOlJHrTZsRg%3D--dCd08P4lymGzImzy--%2FASFJdRHqFXiAMjb5Ypl8A%3D%3D',
        '_dd_s': 'rum=0&expire=1712408170633',
    }

    headers = {
        'x-csrf-token': '1gIJStU8aRhMoI2eFqiwac6CGGD5tkoC70m-Jr60Zuew4RCQDkhW3durZoJekJwsebjM4qCI2AboJepYQtcf8g',
    }

    json_data = {
        'q_organization_fuzzy_name': org_name,
    }

    response = requests.post('https://app.apollo.io/api/v1/organizations/search',
                             cookies=cookies, headers=headers, json=json_data)
    org_id = response.json()['organizations'][0]['id']

    return org_id


def getting_person_object(org_id: str, name: str):
    """# For finding out the Persons Object """

    cookies = {
        'mutiny.user.token': 'a09a53f2-d3a9-4f8b-8b32-c56a4bb0d66c',
        'zp__initial_referrer': 'https://www.google.com/',
        'zp__initial_utm_source': 'www.google.com',
        'hubspotutk': '4a2146072fd6ebc326a2036b61a92083',
        '_gcl_au': '1.1.242791361.1712320823',
        '_ga': 'GA1.1.1316935289.1712320823',
        '_fbp': 'fb.1.1712320824991.1284233262',
        'zp__utm_medium': '(none)',
        'zp__initial_utm_medium': '(none)',
        '__hssrc': '1',
        '_hjSessionUser_3601622': 'eyJpZCI6ImQ3ZGNjNzZjLTc3NjUtNTI5Zi05YzhiLWM0MzcwY2ZkMDBmNSIsImNyZWF0ZWQiOjE3MTIzNzU2NTA2MjEsImV4aXN0aW5nIjpmYWxzZX0=',
        '__q_state_xnwV464CUjypYUw2': 'eyJ1dWlkIjoiODAxOTgyNzctYWFkZS00ZDc2LTgyMDktNGQ1OWVmMjU0ZWI3IiwiY29va2llRG9tYWluIjoiYXBvbGxvLmlvIiwibWVzc2VuZ2VyRXhwYW5kZWQiOmZhbHNlLCJwcm9tcHREaXNtaXNzZWQiOmZhbHNlLCJjb252ZXJzYXRpb25JZCI6IjEzNjg5Nzg2NzUyMjIzOTgyMDQifQ==',
        'ps_mode': 'trackingV1',
        'remember_token_leadgenie_v2': 'eyJfcmFpbHMiOnsibWVzc2FnZSI6IklqWTJNVEJqT0RCaE56VXlaalEzTURGak4yTTBPV000TkY5c1pXRmtaMlZ1YVdWamIyOXJhV1ZvWVhOb0lnPT0iLCJleHAiOiIyMDI0LTA1LTA2VDAzOjU2OjU4LjE5OVoiLCJwdXIiOiJjb29raWUucmVtZW1iZXJfdG9rZW5fbGVhZGdlbmllX3YyIn19--80577a53ef6a8d38a3a8f32902048d44017ee4f4',
        'zp__utm_source': 'accounts.google.com',
        '_clck': 'kpxcyb%7C2%7Cfkp%7C0%7C1557',
        '_cioanonid': '244fb471-512d-bb97-c967-15c0239cd826',
        'ZP_LATEST_LOGIN_PRICING_VARIANT': '23Q4_EC_Z59',
        'ZP_Pricing_Split_Test_Variant': '23Q4_EC_Z59',
        'intercom-device-id-dyws6i9m': 'd835a66e-ccf3-4d02-8ec1-b7bc725d3142',
        '_cioid': '6610c80a752f4701c7c49c84',
        '__stripe_mid': '6534d13a-416c-47e6-8b40-bd7d7f375fedc20888',
        'amplitude_id_122a93c7d9753d2fe678deffe8fac4cfapollo.io': 'eyJkZXZpY2VJZCI6ImUyMjg4MWRmLTg5NWEtNGFiYy04MGExLWZkNjZmZjFjYTMwMFIiLCJ1c2VySWQiOiI2NjEwYzgwYTc1MmY0NzAxYzdjNDljODQiLCJvcHRPdXQiOnRydWUsInNlc3Npb25JZCI6MTcxMjM5OTA1NzMyMCwibGFzdEV2ZW50VGltZSI6MTcxMjM5OTA1NzMyMCwiZXZlbnRJZCI6MSwiaWRlbnRpZnlJZCI6NCwic2VxdWVuY2VOdW1iZXIiOjV9',
        '__hstc': '21978340.4a2146072fd6ebc326a2036b61a92083.1712320822561.1712378455051.1712399064113.4',
        '_ga_76XXTC73SP': 'GS1.1.1712406524.5.0.1712406524.60.0.1375068758',
        '__stripe_sid': 'b320a3a8-6577-4aa8-a526-a15b45bbcc43fd6d43',
        '_clsk': 'splziu%7C1712421215364%7C3%7C0%7Cd.clarity.ms%2Fcollect',
        'intercom-session-dyws6i9m': 'Z1pKdXRUZmlqeWx1ZnYxemZGa0RNbVB0bURmak1WOWc0VVhrelFJTmFIK3ZFOGhTK2JvWGFRdzlYYzZwYjY2eS0tOUh4MElQU0VYbVVxTjZlWTA4VkwyQT09--9d022660189d0b4d4980edcd1a710230b0b4a9f7',
        'X-CSRF-TOKEN': 'r1Y8kkMUecuqHSSIzjeeiPMJZA7ygk3K96iHZj0MRzPJtSVImGBGDj0Wz5SGD7LNRDOwjKu8387wxNMYwW8-Jg',
        '_leadgenie_session': 'X1TlHzF6a3HaZdkfEkNl0ief%2FCaKTjG9Kz5rVY0XHaGYcFgt5Hxp0BmOszR4q0gt85B7L2aCpaLP5erJQWULOeNHGpaSV3GfezmBG7sMXTBjT%2F2zH8S8ibJ98Kd79eBX9h8brXge50hUpBPwvjBRWCALRJ4hweriESHMYYDOhH9nbmGmAnJbKW02J%2B%2FEqRUnv3VkYtI7wqNVlYUsvXAj4Ez7ywNQp2505Rt%2BtxP7EqV9uzruiGKrlrRHHnLZOR5sZTpbA%2B03aFELobOGJnRH9hHKhkiiUVWXd5A%3D--CD%2Fm8YUPgOQprXlZ--10aevnmd8Ib6wXTHxHdw%2Bg%3D%3D',
        '_dd_s': 'rum=0&expire=1712423067095',
    }

    headers = {
        'x-csrf-token': 'r1Y8kkMUecuqHSSIzjeeiPMJZA7ygk3K96iHZj0MRzPJtSVImGBGDj0Wz5SGD7LNRDOwjKu8387wxNMYwW8-Jg',
    }

    json_data = {
        'finder_table_layout_id': None,
        'finder_view_id': '5b8050d050a3893c382e9360',
        'page': 1,
        'organization_ids': [
            org_id,
        ],
        'q_person_name': name,
        'display_mode': 'explorer_mode',
        'per_page': 25,
        'open_factor_names': [],
        'num_fetch_result': 16,
        'context': 'people-index-page',
        'show_suggestions': False,
        'ui_finder_random_seed': 'g609x0unbm7',
    }

    response = requests.post('https://app.apollo.io/api/v1/mixed_people/search',
                             cookies=cookies, headers=headers, json=json_data)

    return response.json()
