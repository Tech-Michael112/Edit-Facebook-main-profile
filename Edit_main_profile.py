import requests
import json
import time
import uuid



import os

# NOTE: THIS IS HOW ACCESS TOKEN EXPIRES AND THAT'S THE MESSAGE THERE  {"error":{"message":"Error validating access token: The session has been invalidated because the user changed their password or Facebook has changed the session for security reasons.","type":"OAuthException","code":190,"error_subcode":452,"error_data":"{\"fb-svr-classification\":\"0\"}","fbtrace_id":"AL61UfxtfmzsJJ5LrDvlLPa"}}
'''
keep cover photo upload file image as "cover.jpg"
and also profile picture image as "img.png"

'''



os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls')


def generate_uuid():
    return str(uuid.uuid4())

def generate_ts():
    return int(time.time() * 1000)

TOKEN = "EAAAAUaZA8jlABQC7ace16x1mhcPd1n9v1WK7ACNkqhtrzv6NxURA3cAEJfuRlUodzDmRJTiZCMO29C129TqBoCUzR6zaULINh3WtrhNdVeOoZAKjR7Cy4ZAicVmZCu7qRafXVdnEE6fZAQhBqcsOwHYZCihbik5RKQZBh3CRZCfp9TBP7f53HxtiRUh3Chvp7EyPag9PztzMXWL4GoZBpOsdlAMJxS3wZDZD"
USER_ID = "61583064755802"

sim_hni=str(random.randint(11111,99999))

TOKEN_Ect=''


def upload_photo():
    print("--- PROFILE PICTURE: Uploading photo ---")
    url = "https://graph-fallback.facebook.com/me/photos"
    composer_id = generate_uuid()
    payload = {
        'published': 'false',
        'audience_exp': 'true',
        'qn': composer_id,
        'composer_session_id': composer_id,
        'idempotence_token': f'{composer_id}_-310624152_0',
        'composer_entry_point': 'camera_roll',
        'locale': 'en_GB',
        'client_country_code': 'CN',
        'fb_api_req_friendly_name': 'upload-photo',
        'fb_api_caller_class': 'MultiPhotoUploader'
    }
    files = [
        ('source', (generate_uuid(), open('img.jpg', 'rb'), 'image/jpeg'))
    ]
    headers = {
        'User-Agent': "[FBAN/FB4A;FBAV/486.0.0.66.70;FBBV/653066364;FBDM/{density=2.0,width=720,height=1504};FBLC/en_GB;FBRV/656162831;FBCR/CHINA UNICOM;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.mahos;FBDV/23106RN0DA;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
#        'Accept-Encoding': "zstd, gzip, deflate",
        'priority': "u=3, i",
        'x-fb-device-group': "2265",
        'x-fb-connection-type': "WIFI.ETHERNET",
        'x-fb-session-id': "nid=7/ooHeZO3kAk;tid=206;nc=0;fc=0;bc=0;cid=edce77cb44abd27e48b078fed1c94593",
        'x-zero-eh': "2,9ca33d98bff6305c9e2f9666f22196f0,AUkqxQqP_ucO9oooAWAutxuZx7-dxjyBXnbOiovsriHmh71G-bNGIZ4W5baSFt-giGY",
        'x-fb-qpl-active-flows-json': json.dumps({"schema_version":"v2","inprogress_qpls":[{"marker_id":25952257,"annotations":{"current_endpoint":"ProfileFragment:profile_vnext_tab_posts"}}],"snapshot_attributes":{}}),
        'x-fb-connection-bandwidth': "5073417",
        'x-tigon-is-retry': "False",
        'x-fb-rmd': "state=URL_MODIFIED;v=1;ip=105.113.117.247;tkn=2721a66c1b60009c25ee371051ac5bc5;reqTime=287543;recvTime=287544;rn=APP_RESUME;if=Wifi;fbn=2;fbu=1;fbr=2",
        'x-fb-connection-quality': "EXCELLENT",
        'x-fb-sim-hni': sim_hni,
        'x-fb-friendly-name': "upload-photo",
        'x-fb-session-gk': "v1:gk:fb_android_tasos_congestion_signal:@pass;",
        'authorization': f"OAuth {TOKEN}",
        'x-fb-net-hni': sim_hni,
        'x-fb-request-analytics-tags': json.dumps({"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"PROFILE_PIC"}),
        'x-fb-http-engine': "Tigon/Liger",
        'x-fb-client-ip': "True",
        'x-fb-server-cluster': "True",
        'x-fb-conn-uuid-client': "edce77cb44abd27e48b078fed1c94593"
    }
    response = requests.post(url, data=payload, files=files, headers=headers)
    if response.status_code == 200:
        result = response.json()
        photo_id = result.get('id', 'Unknown')
        print(f"Uploaded photo ID: {photo_id}")
        return photo_id, composer_id
    else:
        print(f"Photo upload failed: {response.status_code}")
        print(response.text)
        return None, None

def confirm_upload(photo_id, composer_id):
    print("--- PROFILE PICTURE: Confirming photo upload ---")
    ts = generate_ts()
    variables = {
        "photo_fbid": photo_id,
        "composer_session_id": composer_id,
        "profile_id": USER_ID,
        "profile_pic_method": "camera_roll"
    }
    url = "https://graph-fallback.facebook.com/graphql"
    payload = {
        'method': "post",
        'pretty': "false",
        'format': "json",
        'server_timestamps': "true",
        'locale': "en_GB",
        'fb_api_req_friendly_name': "ComposerPhotoUploadConfirmMutation",
        'fb_api_caller_class': "graphservice",
        'client_doc_id': "12345678901234567890",
        'variables': json.dumps(variables),
        'fb_api_analytics_tags': json.dumps(["GraphServices"]),
        'client_trace_id': generate_uuid()
    }
    headers = {
        'User-Agent': "[FBAN/FB4A;FBAV/486.0.0.66.70;FBBV/653066364;FBDM/{density=2.0,width=720,height=1504};FBLC/en_GB;FBRV/656162831;FBCR/CHINA UNICOM;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.mahos;FBDV/23106RN0DA;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
 #       'Accept-Encoding': "zstd, gzip, deflate",
        'x-fb-rmd': "state=URL_MODIFIED;v=1;ip=105.113.117.247;tkn=2721a66c1b60009c25ee371051ac5bc5;reqTime=287543;recvTime=287544;rn=APP_RESUME;if=Wifi;fbn=2;fbu=1;fbr=2",
        'x-fb-qpl-active-flows-json': json.dumps({"schema_version":"v2","inprogress_qpls":[{"marker_id":25952257,"annotations":{"current_endpoint":"ProfileFragment:profile_vnext_tab_posts"}}],"snapshot_attributes":{}}),
        'x-fb-device-group': "2265",
        'x-tigon-is-retry': "False",
        'x-fb-connection-type': "WIFI.ETHERNET",
        'x-fb-session-id': "nid=7/ooHeZO3kAk;tid=207;nc=0;fc=0;bc=0;cid=edce77cb44abd27e48b078fed1c94593",
        'x-zero-eh': "2,9ca33d98bff6305c9e2f9666f22196f0,AUkqxQqP_ucO9oooAWAutxuZx7-dxjyBXnbOiovsriHmh71G-bNGIZ4W5baSFt-giGY",
        'x-fb-friendly-name': "ComposerPhotoUploadConfirmMutation",
        'x-fb-sim-hni': sim_hni,
        'x-graphql-client-library': "graphservice",
        'priority': "u=3, i",
        'x-fb-background-state': "1",
        'x-fb-net-hni': sim_hni,
        'authorization': f"OAuth {TOKEN}",
        'x-fb-request-analytics-tags': json.dumps({"network_tags":{"product":"350685531728","purpose":"none","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}),
        'x-fb-http-engine': "Tigon/Liger",
        'x-fb-client-ip': "True",
        'x-fb-server-cluster': "True",
        'x-fb-conn-uuid-client': "edce77cb44abd27e48b078fed1c94593"
    }
    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == 200:
        print("Photo upload confirmed")
        return True
    else:
        print(f"Photo upload confirm failed: {response.status_code}")
        print(response.text)
        return False

def set_profile_picture(photo_id):
    print("--- PROFILE PICTURE: Setting profile picture ---")
    ts = generate_ts()
    client_mutation_id = f"client_mutation_{ts}"
    variables = {
        "input": {
            "suppress_stories": False,
            "set_profile_photo_shield": "TURN_OFF",
            "scaled_crop_rect": {"y": 0, "width": 1, "x": 0, "height": 1},
            "composer_session_id": generate_uuid(),
            "profile_pic_source": "UNKNOWN",
            "client_mutation_id": client_mutation_id,
            "profile_id": USER_ID,
            "has_umg": False,
            "existing_photo_id": photo_id,
            "frame_entrypoint": "camera_roll",
            "profile_pic_method": "camera_roll",
            "photo_id_for_media_effects": None,
            "actor_id": USER_ID
        }
    }
    url = "https://graph-fallback.facebook.com/graphql?_nc_eh=2,9ca33d98bff6305c9e2f9666f22196f0,AUkqxQqP_ucO9oooAWAutxuZx7-dxjyBXnbOiovsriHmh71G-bNGIZ4W5baSFt-giGY"
    payload = {
        'method': "post",
        'pretty': "false",
        'format': "json",
        'server_timestamps': "true",
        'locale': "en_GB",
        'fb_api_req_friendly_name': "ProfilePictureSetMutation",
        'fb_api_caller_class': "graphservice",
        'client_doc_id': "1809709338612031039675685261",
        'variables': json.dumps(variables),
        'fb_api_analytics_tags': json.dumps(["visitation_id=null","session_id=UFS-27047b5d-fc7c-b7e4-80d6-85b4226aec58-fg-4","GraphServices"]),
        'client_trace_id': generate_uuid()
    }
    headers = {
        'User-Agent': "[FBAN/FB4A;FBAV/486.0.0.66.70;FBBV/653066364;FBDM/{density=2.0,width=720,height=1504};FBLC/en_GB;FBRV/0;FBCR/CHINA UNICOM;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.mahos;FBDV/23106RN0DA;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
  #      'Accept-Encoding': "zstd, gzip, deflate",
        'x-fb-rmd': "state=URL_MODIFIED;v=1;ip=105.113.117.247;tkn=2721a66c1b60009c25ee371051ac5bc5;reqTime=287543;recvTime=287544;rn=APP_RESUME;if=Wifi;fbn=2;fbu=1;fbr=2",
        'x-fb-qpl-active-flows-json': json.dumps({"schema_version":"v2","inprogress_qpls":[{"marker_id":25952257,"annotations":{"current_endpoint":"ProfileFragment:profile_vnext_tab_posts"}}],"snapshot_attributes":{}}),
        'x-fb-device-group': "2265",
        'x-tigon-is-retry': "False",
        'x-fb-connection-type': "WIFI.ETHERNET",
        'x-fb-session-id': "nid=7/ooHeZO3kAk;tid=208;nc=0;fc=0;bc=0;cid=edce77cb44abd27e48b078fed1c94593",
        'x-zero-eh': "2,9ca33d98bff6305c9e2f9666f22196f0,AUkqxQqP_ucO9oooAWAutxuZx7-dxjyBXnbOiovsriHmh71G-bNGIZ4W5baSFt-giGY",
        'x-fb-friendly-name': "ProfilePictureSetMutation",
        'x-fb-sim-hni': sim_hni,
        'x-fb-navigation-chain': f"ProfileFragment,profile_vnext_tab_posts,tap_composer_profile_photo_from_feed,{ts-5000}.20,228257481,,,,{ts-1000}.192;NewsFeedFragment,native_newsfeed,cold_start,{ts-100000}.836,236709143,4748854339,,,{ts-5000}.912",
        'x-graphql-client-library': "graphservice",
        'priority': "u=3, i",
        'x-fb-background-state': "1",
        'x-fb-net-hni': sim_hni,
        'authorization': f"OAuth {TOKEN}",
        'x-fb-request-analytics-tags': json.dumps({"network_tags":{"product":"350685531728","purpose":"none","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}),
        'x-fb-http-engine': "Tigon/Liger",
        'x-fb-client-ip': "True",
        'x-fb-server-cluster': "True",
        'x-fb-conn-uuid-client': "edce77cb44abd27e48b078fed1c94593"
    }
    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == 200:
        result = response.json()
        if "data" in result and "profile_picture_set" in result["data"]:
            print("Profile picture set successfully")
            return True
        else:
            print("Profile picture set response format unexpected")
            print(json.dumps(result, indent=2))
            return False
    else:
        print(f"Profile picture set failed: {response.status_code}")
        print(response.text)
        return False

def fetch_profile_pic():
    print("--- PROFILE PICTURE: Fetching updated profile picture ---")
    ts = generate_ts()
    variables = {
        "square_profile_pic_size_big": 188,
        "profile_image_big_size": 188,
        "square_profile_pic_size_small": 80,
        "square_profile_pic_size_huge": 720
    }
    url = "https://graph-fallback.facebook.com/graphql?_nc_eh=2,9ca33d98bff6305c9e2f9666f22196f0,AUkqxQqP_ucO9oooAWAutxuZx7-dxjyBXnbOiovsriHmh71G-bNGIZ4W5baSFt-giGY"
    payload = {
        'method': "post",
        'pretty': "false",
        'format': "json",
        'server_timestamps': "true",
        'locale': "en_GB",
        'fb_api_req_friendly_name': "FetchProfilePicGraphQL",
        'fb_api_caller_class': "graphservice",
        'client_doc_id': "33229769511835222968702236232",
        'variables': json.dumps(variables),
        'fb_api_analytics_tags': json.dumps(["GraphServices"]),
        'client_trace_id': generate_uuid()
    }
    headers = {
        'User-Agent': "[FBAN/FB4A;FBAV/486.0.0.66.70;FBBV/653066364;FBDM/{density=2.0,width=720,height=1504};FBLC/en_GB;FBRV/0;FBCR/CHINA UNICOM;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.mahos;FBDV/23106RN0DA;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
   #     'Accept-Encoding': "zstd, gzip, deflate",
        'x-fb-rmd': "state=URL_MODIFIED;v=1;ip=105.113.117.247;tkn=2721a66c1b60009c25ee371051ac5bc5;reqTime=287543;recvTime=287544;rn=APP_RESUME;if=Wifi;fbn=2;fbu=1;fbr=2",
        'x-fb-qpl-active-flows-json': json.dumps({"schema_version":"v2","inprogress_qpls":[{"marker_id":25952257,"annotations":{"current_endpoint":"ProfileFragment:profile_vnext_tab_posts"}}],"snapshot_attributes":{}}),
        'x-fb-connection-type': "WIFI.ETHERNET",
        'x-fb-device-group': "2265",
        'x-fb-privacy-context': "696323304542553",
        'x-tigon-is-retry': "False",
        'x-fb-friendly-name': "FetchProfilePicGraphQL",
        'x-graphql-client-library': "graphservice",
        'x-fb-session-id': "nid=7/ooHeZO3kAk;tid=209;nc=0;fc=0;bc=0;cid=edce77cb44abd27e48b078fed1c94593",
        'x-zero-eh': "2,9ca33d98bff6305c9e2f9666f22196f0,AUkqxQqP_ucO9oooAWAutxuZx7-dxjyBXnbOiovsriHmh71G-bNGIZ4W5baSFt-giGY",
        'priority': "u=3, i",
        'x-fb-background-state': "1",
        'x-fb-net-hni': "46001",
        'x-fb-sim-hni': "46001",
        'authorization': f"OAuth {TOKEN}",
        'x-fb-request-analytics-tags': json.dumps({"network_tags":{"product":"350685531728","purpose":"none","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}),
        'x-fb-http-engine': "Tigon/Liger",
        'x-fb-client-ip': "True",
        'x-fb-server-cluster': "True",
        'x-fb-conn-uuid-client': "edce77cb44abd27e48b078fed1c94593"
    }
    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == 200:
        result = response.json()
        if "data" in result and "viewer" in result["data"]:
            actor = result["data"]["viewer"]["actor"]
            print(f"Profile photo ID: {actor.get('profile_photo', {}).get('id', 'Unknown')}")
            print(f"Profile picture URL: {actor.get('profile_picture', {}).get('uri', 'Unknown')}")
            return True
        else:
            print("Profile picture fetch response format unexpected")
            print(json.dumps(result, indent=2))
            return False
    else:
        print(f"Profile picture fetch failed: {response.status_code}")
        print(response.text)
        return False

def update_profile_website():
    print("--- PROFILE INFORMATION: Updating website ---")
    ts = generate_ts()
    variables = {
        "input": {
            "client_mutation_id": "1",
            "actor_id": USER_ID,
            "websites": [{
                "fbid": None,
                "website": "https://heylink.me/AERO88PASTIJP()))",
                "privacy": None
            }]
        }
    }
    url = "https://graph.facebook.com/graphql?locale=en_GB&_nc_eh=2,9ca33d98bff6305c9e2f9666f22196f0,AUkqxQqP_ucO9oooAWAutxuZx7-dxjyBXnbOiovsriHmh71G-bNGIZ4W5baSFt-giGY"
    payload = {
        'access_token': TOKEN,
        'fb_api_caller_class': "RelayModern",
        'fb_api_req_friendly_name': "ProfileEditWebsitesSaveMutation",
        'variables': json.dumps(variables),
        'server_timestamps': "true",
        'doc_id': "3159239490825255",
        'fb_api_analytics_tags': json.dumps(["session_id=UFS-cf051af2-06cb-8728-09f5-990aad680414-fg-2","nav_attribution_id="])
    }
    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 9; 23106RN0DA Build/PQ3A.190801.002) [FBAN/FB4A;FBAV/486.0.0.66.70;FBPN/com.facebook.mahos;FBLC/en_GB;FBBV/653066364;FBCR/CHINA UNICOM;FBMF/Xiaomi;FBBD/Redmi;FBDV/23106RN0DA;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1504};FB_FW/1;FBRV/656162831;]",
        'priority': "u=3, i",
        'x-fb-rmd': "state=URL_ELIGIBLE",
        'x-fb-qpl-active-flows-json': json.dumps({"schema_version":"v2","inprogress_qpls":[{"marker_id":25952257,"annotations":{"current_endpoint":"FbReactFragment:react_ProfileEditLinksRoute"}}],"snapshot_attributes":{}}),
        'x-tigon-is-retry': "False",
        'x-fb-device-group': "2265",
        'x-zero-eh': "2,9ca33d98bff6305c9e2f9666f22196f0,AUkqxQqP_ucO9oooAWAutxuZx7-dxjyBXnbOiovsriHmh71G-bNGIZ4W5baSFt-giGY",
        'x-fb-session-id': "nid=RwflWFgd5l1z;tid=132;nc=0;fc=0;bc=0;cid=0a620158903041d647934688f519432b",
        'privacy_context': "ProfileEditLinksRoute",
        'x-fb-net-hni': "46001",
        'x-fb-friendly-name': "RelayFBNetwork_ProfileEditWebsitesSaveMutation",
        'x-fb-session-gk': "v1:gk:fb_android_tasos_congestion_signal:@pass;",
        'x-fb-sim-hni': "46001",
        'x-fb-connection-type': "WIFI.ETHERNET",
        'x-fb-request-analytics-tags': json.dumps({"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}),
        'x-fb-http-engine': "Tigon/Liger",
        'x-fb-client-ip': "True",
        'x-fb-server-cluster': "True",
        'x-fb-conn-uuid-client': "0a620158903041d647934688f519432b"
    }
    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == 200:
        print("Website updated successfully")
        return True
    else:
        print(f"Website update failed: {response.status_code}")
        print(response.text)
        return False

def update_current_city():
    print("--- PROFILE INFORMATION: Updating current city ---")
    ts = generate_ts()
    variables = {
        "input": {
            "client_mutation_id": "2",
            "actor_id": USER_ID,
            "current_city_id": "106741529360687",
            "privacy": {
                "allow": [],
                "base_state": "EVERYONE",
                "deny": [],
                "tag_expansion_state": "UNSPECIFIED"
            },
            "life_event_publish_type": None
        }
    }
    url = "https://graph.facebook.com/graphql?locale=en_GB&_nc_eh=2,9ca33d98bff6305c9e2f9666f22196f0,AUkqxQqP_ucO9oooAWAutxuZx7-dxjyBXnbOiovsriHmh71G-bNGIZ4W5baSFt-giGY"
    payload = {
        'access_token': TOKEN,
        'fb_api_caller_class': "RelayModern",
        'fb_api_req_friendly_name': "ProfileEditCurrentCitySaveMutation",
        'variables': json.dumps(variables),
        'server_timestamps': "true",
        'doc_id': "8315735705176207",
        'fb_api_analytics_tags': json.dumps(["session_id=UFS-cf051af2-06cb-8728-09f5-990aad680414-fg-2","nav_attribution_id="])
    }
    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 9; 23106RN0DA Build/PQ3A.190801.002) [FBAN/FB4A;FBAV/486.0.0.66.70;FBPN/com.facebook.mahos;FBLC/en_GB;FBBV/653066364;FBCR/CHINA UNICOM;FBMF/Xiaomi;FBBD/Redmi;FBDV/23106RN0DA;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1504};FB_FW/1;FBRV/656162831;]",
    #    'Accept-Encoding': "zstd, gzip, deflate",
        'priority': "u=3, i",
        'x-fb-rmd': "state=URL_ELIGIBLE",
        'x-fb-qpl-active-flows-json': json.dumps({"schema_version":"v2","inprogress_qpls":[{"marker_id":25952257,"annotations":{"current_endpoint":"FbReactFragment:react_ProfileEditCurrentCityRoute"}}],"snapshot_attributes":{}}),
        'x-fb-device-group': "2265",
        'x-tigon-is-retry': "False",
        'x-fb-connection-type': "WIFI.ETHERNET",
        'x-fb-session-id': "nid=RwflWFgd5l1z;tid=234;nc=0;fc=0;bc=0;cid=4cc7196ccc4b93fe8b80c608d567ff9c",
        'x-zero-eh': "2,9ca33d98bff6305c9e2f9666f22196f0,AUkqxQqP_ucO9oooAWAutxuZx7-dxjyBXnbOiovsriHmh71G-bNGIZ4W5baSFt-giGY",
        'x-fb-sim-hni': "46001",
        'x-fb-net-hni': "46001",
        'x-fb-friendly-name': "RelayFBNetwork_ProfileEditCurrentCitySaveMutation",
        'x-fb-session-gk': "v1:gk:fb_android_tasos_congestion_signal:@pass;",
        'x-fb-request-analytics-tags': json.dumps({"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}),
        'x-fb-http-engine': "Tigon/Liger",
        'x-fb-client-ip': "True",
        'x-fb-server-cluster': "True",
        'x-fb-conn-uuid-client': "4cc7196ccc4b93fe8b80c608d567ff9c"
    }
    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == 200:
        print("Current city updated successfully")
        return True
    else:
        print(f"Current city update failed: {response.status_code}")
        print(response.text)
        return False

def fetch_city_info():
    print("--- PROFILE INFORMATION: Fetching city info ---")
    ts = generate_ts()
    variables = {
        "entity_id": "106741529360687",
        "life_event_category": "HOME",
        "life_event_type": "136805663075786"
    }
    url = "https://graph.facebook.com/graphql?_nc_eh=2,9ca33d98bff6305c9e2f9666f22196f0,AUkqxQqP_ucO9oooAWAutxuZx7-dxjyBXnbOiovsriHmh71G-bNGIZ4W5baSFt-giGY"
    payload = {
        'method': "post",
        'pretty': "false",
        'format': "json",
        'server_timestamps': "true",
        'locale': "en_GB",
        'fb_api_req_friendly_name': "FetchMLEEntityContentQuery",
        'fb_api_caller_class': "graphservice",
        'client_doc_id': "14726011952274367242967632694",
        'variables': json.dumps(variables),
        'fb_api_analytics_tags': json.dumps(["GraphServices"]),
        'client_trace_id': generate_uuid()
    }
    headers = {
        'User-Agent': "[FBAN/FB4A;FBAV/486.0.0.66.70;FBBV/653066364;FBDM/{density=2.0,width=720,height=1504};FBLC/en_GB;FBRV/656162831;FBCR/CHINA UNICOM;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.mahos;FBDV/23106RN0DA;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
     #   'Accept-Encoding': "zstd, gzip, deflate",
        'x-fb-rmd': "state=URL_ELIGIBLE",
        'x-fb-qpl-active-flows-json': json.dumps({"schema_version":"v2","inprogress_qpls":[{"marker_id":25952257,"annotations":{"current_endpoint":"FbReactFragment:react_ProfileEditCurrentCityRoute"}}],"snapshot_attributes":{}}),
        'x-fb-connection-type': "WIFI.ETHERNET",
        'x-fb-device-group': "2265",
        'x-fb-privacy-context': "721963578552414",
        'x-tigon-is-retry': "False",
        'x-fb-friendly-name': "FetchMLEEntityContentQuery",
        'x-graphql-client-library': "graphservice",
        'x-fb-session-id': "nid=RwflWFgd5l1z;tid=235;nc=0;fc=0;bc=0;cid=4cc7196ccc4b93fe8b80c608d567ff9c",
        'x-zero-eh': "2,9ca33d98bff6305c9e2f9666f22196f0,AUkqxQqP_ucO9oooAWAutxuZx7-dxjyBXnbOiovsriHmh71G-bNGIZ4W5baSFt-giGY",
        'priority': "u=3, i",
        'x-fb-background-state': "1",
        'x-fb-net-hni': "46001",
        'x-fb-sim-hni': "46001",
        'authorization': f"OAuth {TOKEN}",
        'x-fb-request-analytics-tags': json.dumps({"network_tags":{"product":"350685531728","purpose":"none","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}),
        'x-fb-http-engine': "Tigon/Liger",
        'x-fb-client-ip': "True",
        'x-fb-server-cluster': "True",
        'x-fb-conn-uuid-client': "4cc7196ccc4b93fe8b80c608d567ff9c"
    }
    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == 200:
        print("City info fetched successfully")
        return True
    else:
        print(f"City info fetch failed: {response.status_code}")
        print(response.text)
        return False

def update_bio():
    print("--- PROFILE BIO: Updating bio ---")
    ts = generate_ts()
    bio_text = "Drama selalu ada di hidup"
    variables = {
        "input": {
            "text": bio_text,
            "message": {
                "text": bio_text,
                "ranges": []
            },
            "expiration_time": 0
        }
    }
    url = "https://graph.facebook.com/graphql?_nc_eh=2,233da7ced277aed0f3706b996beb3d75,AUnfF27ggp_S11Fn6Xbcgep4LPmg5J2jiFDc0__Jy-luP33oJRsQFooxGQmBKaC7Pyc"
    payload = {
        'method': "post",
        'pretty': "false",
        'format': "json",
        'server_timestamps': "true",
        'locale': "en_GB",
        'fb_api_req_friendly_name': "StatusSetMutation",
        'fb_api_caller_class': "graphservice",
        'client_doc_id': "21136863437138669878401139874",
        'fb_api_client_context': json.dumps({"is_background": False}),
        'variables': json.dumps(variables),
        'fb_api_analytics_tags': json.dumps(["visitation_id=null","session_id=UFS-dd92740f-659b-35a1-cd00-888a5f643fcc-fg-4","GraphServices"]),
        'client_trace_id': generate_uuid()
    }
    headers = {
        'User-Agent': "[FBAN/FB4A;FBAV/486.0.0.66.70;FBBV/653066364;FBDM/{density=2.0,width=720,height=1504};FBLC/en_GB;FBRV/656162831;FBCR/CHINA UNICOM;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.mahos;FBDV/23106RN0DA;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
      #  'Accept-Encoding': "zstd, gzip, deflate",
        'x-fb-request-analytics-tags': json.dumps({"network_tags":{"product":"350685531728","request_category":"graphql","purpose":"none","retry_attempt":"0"},"application_tags":"graphservice"}),
        'x-fb-rmd': "state=URL_ELIGIBLE",
        'x-fb-friendly-name': "StatusSetMutation",
        'x-zero-f-device-id': "1beaf9e6-0fe6-4f88-b320-114add7b2da2",
        'x-graphql-client-library': "graphservice",
        'x-fb-appnetsession-sid': "46d48f6544208c7cde7ca22b90dbbd1b",
        'x-fb-sim-hni': "46001",
        'x-fb-navigation-chain': f"StatusEditFragment,,,{ts-10000}.315,265904802,,,,{ts-10000}.315;FbReactFragment,react_ProfileEditRoute,,{ts-15000}.784,229013574,,,,{ts-15000}.784;ProfileFragment,profile_vnext_tab_posts,tap_composer_profile_photo_from_feed,{ts-20000}.224,178090828,,,,{ts-20000}.913;NewsFeedFragment,native_newsfeed,,{ts-25000}.862,258336888,,,,{ts-25000}.862",
        'authorization': f"OAuth {TOKEN}",
        'app-scope-id-header': "1beaf9e6-0fe6-4f88-b320-114add7b2da2",
        'x-fb-connection-type': "WIFI.ETHERNET",
        'x-fb-appnetsession-nid': "b38fe83843d8657c4e1756d879468134,Wifi",
        'x-fb-net-hni': "46001",
        'x-fb-session-id': "nid=JivIUbJimsdH;tid=828;nc=0;fc=0;bc=0",
        'x-fb-device-group': "5130",
        'x-zero-eh': "2,233da7ced277aed0f3706b996beb3d75,AUnfF27ggp_S11Fn6Xbcgep4LPmg5J2jiFDc0__Jy-luP33oJRsQFooxGQmBKaC7Pyc",
        'x-fb-network-properties': "Wifi;Validated;",
        'x-fb-qpl-active-flows-json': json.dumps({"schema_version":"v3","inprogress_qpls":[],"snapshot_attributes":{}}),
        'priority': "u=3, i",
        'x-fb-congestion-signal': "0",
        'x-meta-enable-tasos-ss-bwe': "1",
        'x-tigon-is-retry': "False",
        'x-fb-http-engine': "Tigon/Liger",
        'x-fb-client-ip': "True",
        'x-fb-server-cluster': "True",
        'x-fb-conn-uuid-client': "4076121289c7eaff0acaf89f2abee80e"
    }
    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == 200:
        result = response.json()
        if "data" in result and "profile_status_set" in result["data"]:
            status = result["data"]["profile_status_set"]["status"]
            print(f"Bio updated successfully")
            print(f"Bio ID: {status.get('id', 'Unknown')}")
            print(f"Bio text: {status.get('profile_status_text', {}).get('text', 'Unknown')}")
            return True
        else:
            print("Bio update response format unexpected")
            print(json.dumps(result, indent=2))
            return False
    else:
        print(f"Bio update failed: {response.status_code}")
        print(response.text)
        return False

def upload_cover_photo():
    print("--- COVER PHOTO: Uploading cover photo ---")
    url = "https://graph.facebook.com/me/photos"
    composer_id = generate_uuid()
    payload = {
        'published': 'false',
        'audience_exp': 'true',
        'qn': composer_id,
        'composer_session_id': composer_id,
        'idempotence_token': f'{composer_id}_892714756_0',
        'locale': 'en_GB',
        'client_country_code': 'CN',
        'fb_api_req_friendly_name': 'upload-photo',
        'fb_api_caller_class': 'MultiPhotoUploader'
    }
    files = [
        ('source', (generate_uuid(), open('cover.jpg', 'rb'), 'image/jpeg'))
    ]
    headers = {
        'User-Agent': "[FBAN/FB4A;FBAV/486.0.0.66.70;FBBV/653066364;FBDM/{density=2.0,width=720,height=1504};FBLC/en_GB;FBRV/656162831;FBCR/CHINA UNICOM;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.mahos;FBDV/23106RN0DA;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
       # 'Accept-Encoding': "zstd, gzip, deflate",
        'priority': "u=3, i",
        'x-fb-device-group': "2265",
        'x-fb-connection-type': "WIFI.ETHERNET",
        'x-fb-session-id': f"nid=ahX12/cHaSb4;tid=109;nc=0;fc=0;bc=0;cid={generate_uuid()[:32]}",
        'x-zero-eh': "2,9ca33d98bff6305c9e2f9666f22196f0,AUrK4tBXR60Uo0uMjm6_fJOT57jZMzNAsbaGioKGiXBLnw449Uv4hQyZGQBr43baykM",
        'x-fb-qpl-active-flows-json': json.dumps({"schema_version":"v2","inprogress_qpls":[{"marker_id":25952257,"annotations":{"current_endpoint":"ProfileFragment:profile_vnext_tab_posts"}}],"snapshot_attributes":{}}),
        'x-fb-connection-bandwidth': "4547468",
        'x-tigon-is-retry': "False",
        'x-fb-rmd': "state=URL_ELIGIBLE",
        'x-fb-connection-quality': "EXCELLENT",
        'x-fb-sim-hni': "46001",
        'x-fb-friendly-name': "upload-photo",
        'x-fb-session-gk': "v1:gk:fb_android_tasos_congestion_signal:@pass;",
        'authorization': f"OAuth {TOKEN}",
        'x-fb-net-hni': "46001",
        'x-fb-request-analytics-tags': json.dumps({"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"COVER_PHOTO"}),
        'x-fb-http-engine': "Tigon/Liger",
        'x-fb-client-ip': "True",
        'x-fb-server-cluster': "True",
        'x-fb-conn-uuid-client': generate_uuid()[:32]
    }
    response = requests.post(url, data=payload, files=files, headers=headers)
    if response.status_code == 200:
        result = response.json()
        photo_id = result.get('id', 'Unknown')
        print(f"Cover photo uploaded successfully. ID: {photo_id}")
        return photo_id, composer_id
    else:
        print(f"Cover photo upload failed: {response.status_code}")
        print(response.text)
        return None, None

def publish_cover_photo(photo_id, composer_id):
    print("--- COVER PHOTO: Publishing cover photo ---")
    batch_payload = {
        "method": "POST",
        "body": f"qn={composer_id}&photo={photo_id}&focus_x=0.5&focus_y=0.49947917&cover_photo_type=PHOTO&cover_video_type=SLIDESHOW&no_feed_story=false&locale=en_GB&client_country_code=CN&fb_api_req_friendly_name=publish-photo",
        "name": "publish",
        "omit_response_on_success": False,
        "relative_url": f"{USER_ID}/cover"
    }
    url = "https://graph.facebook.com?include_headers=false&decode_body_json=false&streamable_json_response=true&locale=en_GB&client_country_code=CN&_nc_eh=2,9ca33d98bff6305c9e2f9666f22196f0,AUrK4tBXR60Uo0uMjm6_fJOT57jZMzNAsbaGioKGiXBLnw449Uv4hQyZGQBr43baykM"
    payload = {
        'batch': json.dumps([batch_payload]),
        'fb_api_caller_class': "PhotoPublisher",
        'fb_api_req_friendly_name': "single_photo_publish"
    }
    headers = {
        'User-Agent': "[FBAN/FB4A;FBAV/486.0.0.66.70;FBBV/653066364;FBDM/{density=2.0,width=720,height=1504};FBLC/en_GB;FBRV/656162831;FBCR/CHINA UNICOM;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.mahos;FBDV/23106RN0DA;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
        #'Accept-Encoding': "zstd, gzip, deflate",
        'priority': "u=3, i",
        'x-fb-rmd': "state=NO_MATCH",
        'x-fb-qpl-active-flows-json': json.dumps({"schema_version":"v2","inprogress_qpls":[{"marker_id":25952257,"annotations":{"current_endpoint":"ProfileFragment:profile_vnext_tab_posts"}}],"snapshot_attributes":{}}),
        'x-fb-device-group': "2265",
        'x-tigon-is-retry': "False",
        'x-fb-connection-type': "WIFI.ETHERNET",
        'x-fb-session-id': f"nid=ahX12/cHaSb4;tid=110;nc=0;fc=0;bc=0;cid={generate_uuid()[:32]}",
        'x-fb-session-gk': "v1:gk:fb_android_tasos_congestion_signal:@pass;",
        'authorization': f"OAuth {TOKEN}",
        'x-zero-eh': "2,9ca33d98bff6305c9e2f9666f22196f0,AUrK4tBXR60Uo0uMjm6_fJOT57jZMzNAsbaGioKGiXBLnw449Uv4hQyZGQBr43baykM",
        'x-fb-sim-hni': "46001",
        'x-fb-net-hni': "46001",
        'x-fb-friendly-name': "single_photo_publish",
        'x-fb-request-analytics-tags': json.dumps({"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}),
        'x-fb-http-engine': "Tigon/Liger",
        'x-fb-client-ip': "True",
        'x-fb-server-cluster': "True",
        'x-fb-conn-uuid-client': generate_uuid()[:32]
    }
    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == 200:
        print("Cover photo published successfully")
        return True
    else:
        print(f"Cover photo publish failed: {response.status_code}")
        print(response.text)
        return False

def fetch_timeline():
    print("--- PROFILE: Fetching timeline ---")
    ts = generate_ts()
    variables = {
        "automatic_photo_captioning_enabled": "false",
        "image_high_height": 2048,
        "image_landscape_height": "470",
        "image_low_width": 240,
        "narrow_portrait_height": "708",
        "image_landscape_width": "708",
        "image_large_thumbnail_width": "470",
        "fetch_entity_end_of_feed_bloks_anchor": True,
        "enable_pplus_wa_data_fetch": True,
        "is_self_profile": True,
        "image_portrait_height": "708",
        "image_portrait_width": "470",
        "fetch_gender": True,
        "inspiration_capabilities": [
            {
                "version": 191,
                "type": "MSQRD_MASK",
                "capabilities": [
                    {"value": "multiplane_disabled", "name": "multiplane"},
                    {"value": "world_tracker_enabled", "name": "world_tracker"},
                    {"value": "xray_disabled", "name": "xray"},
                    {"value": "world_tracking_disabled", "name": "world_tracking"},
                    {"value": "half_float_render_pass_enabled", "name": "half_float_render_pass"},
                    {"value": "multiple_render_targets_enabled", "name": "multiple_render_targets"},
                    {"value": "vertex_texture_fetch_enabled", "name": "vertex_texture_fetch"},
                    {"value": "render_settings_high_enabled", "name": "render_settings_high"},
                    {"value": "body_tracking_enabled", "name": "body_tracking"},
                    {"value": "gyroscope_disabled", "name": "gyroscope"},
                    {"value": "geoanchor_disabled", "name": "geoanchor"},
                    {"value": "scene_depth_disabled", "name": "scene_depth"},
                    {"value": "189,191", "name": "supported_beta_sdk_versions"},
                    {"value": "segmentation_enabled", "name": "segmentation"},
                    {"value": "hand_tracking_enabled", "name": "hand_tracking"},
                    {"value": "real_scale_estimation_disabled", "name": "real_scale_estimation"},
                    {"value": "hair_segmentation_disabled", "name": "hair_segmentation"},
                    {"value": "depth_shader_read_enabled", "name": "depth_shader_read"},
                    {"value": "etc2_compression", "name": "compression"},
                    {"value": "0", "name": "face_tracker_version"},
                    {"value": "149.0,150.0,151.0,152.0,153.0,154.0,155.0,156.0,157.0,158.0,159.0,160.0,161.0,162.0,163.0,164.0,165.0,166.0,167.0,168.0,169.0,170.0,171.0,172.0,173.0,174.0,175.0,176.0,177.0,178.0,179.0,180.0,181.0,182.0,183.0,184.0,185.0,186.0,187.0,188.0,189.0,190.0,191.0", "name": "supported_sdk_versions"}
                ]
            },
            {"version": 1, "type": "FRAME"},
            {
                "version": 1,
                "type": "SHADER_FILTER",
                "capabilities": [{"value": "true", "name": "multipass"}]
            }
        ],
        "profile_image_size": 80,
        "reading_attachment_profile_image_height": 270,
        "photos_tab_collection_count": 3,
        "image_medium_width": 360,
        "should_fetch_wem_private_sharing_params": True,
        "media_type": "image/x-auto",
        "profile_image_big_size": 188,
        "profile_image_big_size_relative": 360,
        "fetch_profile_pic_expiration_information": True,
        "profile_pic_media_type": "image/x-auto",
        "show_presence_info_for_redesigned_protile": True,
        "image_medium_height": 2048,
        "show_admin_prompt": True,
        "fetch_spams_megaphone": True,
        "profile_id": USER_ID,
        "msqrd_instruction_image_width": 200,
        "home_tab_protiles_enable_deferred_sections": True,
        "image_low_height": 2048,
        "should_fetch_wem_private_sharing_eligibility": True,
        "frame_scale": "2",
        "image_high_width": 720,
        "should_fetch_birthday_avatar_nt_action": True,
        "scale": "2",
        "show_pplus_megaphone_qp": True,
        "enable_bloks_action_bar": True,
        "include_image_ranges": True,
        "story_card_cover_width": 238,
        "angora_attachment_cover_image_size": 960,
        "msqrd_supported_capabilities": [
            {"value": "multiplane_disabled", "name": "multiplane"},
            {"value": "world_tracker_enabled", "name": "world_tracker"},
            {"value": "xray_disabled", "name": "xray"},
            {"value": "world_tracking_disabled", "name": "world_tracking"},
            {"value": "half_float_render_pass_enabled", "name": "half_float_render_pass"},
            {"value": "multiple_render_targets_enabled", "name": "multiple_render_targets"},
            {"value": "vertex_texture_fetch_enabled", "name": "vertex_texture_fetch"},
            {"value": "render_settings_high_enabled", "name": "render_settings_high"},
            {"value": "body_tracking_enabled", "name": "body_tracking"},
            {"value": "gyroscope_disabled", "name": "gyroscope"},
            {"value": "geoanchor_disabled", "name": "geoanchor"},
            {"value": "scene_depth_disabled", "name": "scene_depth"},
            {"value": "189,191", "name": "supported_beta_sdk_versions"},
            {"value": "segmentation_enabled", "name": "segmentation"},
            {"value": "hand_tracking_enabled", "name": "hand_tracking"},
            {"value": "real_scale_estimation_disabled", "name": "real_scale_estimation"},
            {"value": "hair_segmentation_disabled", "name": "hair_segmentation"},
            {"value": "depth_shader_read_enabled", "name": "depth_shader_read"},
            {"value": "etc2_compression", "name": "compression"},
            {"value": "0", "name": "face_tracker_version"},
            {"value": "149.0,150.0,151.0,152.0,153.0,154.0,155.0,156.0,157.0,158.0,159.0,160.0,161.0,162.0,163.0,164.0,165.0,166.0,167.0,168.0,169.0,170.0,171.0,172.0,173.0,174.0,175.0,176.0,177.0,178.0,179.0,180.0,181.0,182.0,183.0,184.0,185.0,186.0,187.0,188.0,189.0,190.0,191.0", "name": "supported_sdk_versions"}
        ],
        "home_tab_protiles_deferred_sections": ["FRIENDS"],
        "story_card_cover_height": 238,
        "supported_model_compression_types": ["TAR_BROTLI", "NONE"],
        "show_presence_info": True,
        "reading_attachment_profile_image_width": 180,
        "angora_attachment_profile_image_size": 80,
        "image_thumbnail_width": "232",
        "goodwill_small_accent_image": 72,
        "image_large_aspect_height": 376,
        "enable_bloks_profile_prompt": True,
        "fetch_fbc_header": True,
        "device_type": "23106RN0DA",
        "default_landing_type": "HOME",
        "thumbnail_width": 120,
        "profile_image_small_size": 80,
        "narrow_landscape_height": "351",
        "action_bar_render_location": "ANDROID_PROFILE",
        "enable_bloks_top_header": True,
        "default_image_scale": "2",
        "enable_stars_deepdive_pill": True,
        "enable_takeover_for_stars_pill": True,
        "nt_context": {
            "using_white_navbar": True,
            "styles_id": "cfe75e13b386d5c54b1de2dcca1bee5a",
            "pixel_ratio": 2,
            "is_push_on": True,
            "debug_tooling_metadata_token": None,
            "is_flipper_enabled": False,
            "theme_params": [],
            "bloks_version": "3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5"
        },
        "fetch_birthday_data": True,
        "image_large_aspect_width": 720,
        "fetch_bloks_anchors": True,
        "include_stars_ufi_metadata": True,
        "should_fetch_message_box_id": True,
        "should_fetch_light_bucket_for_highlights_pagination": True,
        "msqrd_instruction_image_height": 200,
        "skip_cover_photo_preview": True,
        "photos_tab_grid_media_paginated_object_first": 6,
        "should_fetch_profile_deferred_action_name": True,
        "large_portrait_height": "705",
        "should_fetch_profile_plus_full_width_action_button_eligible": True,
        "featured_highlights_paginating_first": 5,
        "should_fetch_cutover_info": True,
        "supported_compression_types": ["ZIP", "TAR_BROTLI"],
        "use_native_entrypoint_for_stars_on_reels": True
    }
    url = "https://graph.facebook.com/graphql?_nc_eh=2,9ca33d98bff6305c9e2f9666f22196f0,AUrK4tBXR60Uo0uMjm6_fJOT57jZMzNAsbaGioKGiXBLnw449Uv4hQyZGQBr43baykM"
    payload = {
        'method': "post",
        'pretty': "false",
        'format': "json",
        'server_timestamps': "true",
        'locale': "en_GB",
        'purpose': "refresh",
        'fb_api_req_friendly_name': "UserTimelineQuery",
        'fb_api_caller_class': "graphservice",
        'client_doc_id': "36410619714057063917658040352",
        'variables': json.dumps(variables),
        'fb_api_analytics_tags': json.dumps(["At_Connection","surfaces.fb.GraphServiceEmitter","GraphServices"]),
        'client_trace_id': generate_uuid()
    }
    headers = {
        'User-Agent': "[FBAN/FB4A;FBAV/486.0.0.66.70;FBBV/653066364;FBDM/{density=2.0,width=720,height=1504};FBLC/en_GB;FBRV/656162831;FBCR/CHINA UNICOM;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.mahos;FBDV/23106RN0DA;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
        'x-fb-rmd': "state=URL_ELIGIBLE",
        'x-fb-qpl-active-flows-json': json.dumps({"schema_version":"v2","inprogress_qpls":[{"marker_id":25952257,"annotations":{"current_endpoint":"ProfileFragment:profile_vnext_tab_posts"}}],"snapshot_attributes":{}}),
        'x-fb-connection-type': "WIFI.ETHERNET",
        'x-fb-session-id': f"nid=ahX12/cHaSb4;tid=112;nc=0;fc=0;bc=0;cid={generate_uuid()[:32]}",
        'x-zero-eh': "2,9ca33d98bff6305c9e2f9666f22196f0,AUrK4tBXR60Uo0uMjm6_fJOT57jZMzNAsbaGioKGiXBLnw449Uv4hQyZGQBr43baykM",
        'x-fb-friendly-name': "UserTimelineQuery",
        'x-graphql-client-library': "graphservice",
        'x-fb-device-group': "2265",
        'x-graphql-request-purpose': "refresh",
        'x-fb-privacy-context': "2644666885789663",
        'x-tigon-is-retry': "False",
        'priority': "u=3, i",
        'x-fb-background-state': "1",
        'x-fb-net-hni': sim_hni,
        'x-fb-sim-hni': sim_hni,
        'authorization': f"OAuth {TOKEN}",
        'x-fb-request-analytics-tags': json.dumps({"network_tags":{"product":"350685531728","purpose":"refresh","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}),
        'x-fb-http-engine': "Tigon/Liger",
        'x-fb-client-ip': "True",
        'x-fb-server-cluster': "True",
        'x-fb-conn-uuid-client': generate_uuid()[:32]
    }
    response = requests.post(url, data=payload, headers=headers)
    print(response.text)
    if response.status_code == 200:
        try:
            result = response.json()
        except json.JSONDecodeError:
            try:
                lines = response.text.strip().split('\n')
                if len(lines) > 0:
                    result = json.loads(lines[0])
                else:
                    print("Empty response received")
                    return False
            except Exception as e:
                print(f"Failed to parse response: {e}")
                return False
        
        if isinstance(result, list) and len(result) > 0:
            for item in result:
                if isinstance(item, dict) and "data" in item and "user" in item["data"]:
                    user = item["data"]["user"]
                    print("Timeline fetched successfully")
                    if "cover_photo" in user and user["cover_photo"]:
                        print(f"Cover photo ID: {user['cover_photo'].get('photo', {}).get('id', 'Unknown')}")
                    else:
                        print("No cover photo found")
                    return True
        elif isinstance(result, dict) and "data" in result and "user" in result["data"]:
            user = result["data"]["user"]
            print("Timeline fetched successfully")
            if "cover_photo" in user and user["cover_photo"]:
                print(f"Cover photo ID: {user['cover_photo'].get('photo', {}).get('id', 'Unknown')}")
            else:
                print("No cover photo found")
            return True
        
        print("Timeline fetch response format unexpected")
        return False
    else:
        print(f"Timeline fetch failed: {response.status_code}")
        print(response.text[:500])
        return False





def main():
    cover_photo_id, cover_composer_id = upload_cover_photo()
    if cover_photo_id:
        time.sleep(1)
        if publish_cover_photo(cover_photo_id, cover_composer_id):
            time.sleep(1)
            if fetch_timeline():
                photo_id, composer_id = upload_photo()
                if photo_id:
                    time.sleep(1)
                    if confirm_upload(photo_id, composer_id):
                        time.sleep(1)
                        if set_profile_picture(photo_id):
                            time.sleep(1)
                            if fetch_profile_pic():
                                time.sleep(1)
                                if update_profile_website():
                                    time.sleep(1)
                                    if update_current_city():
                                        time.sleep(1)
                                        if fetch_city_info():
                                            time.sleep(1)
                                            if update_bio():
                                                print("--- All 11 requests completed successfully ---")
                                            else:
                                                print("--- Bio update failed ---")
                                        else:
                                            print("--- City info fetch failed ---")
                                    else:
                                        print("--- Current city update failed ---")
                                else:
                                    print("--- Website update failed ---")
                            else:
                                print("--- Profile picture fetch failed ---")
                        else:
                            print("--- Profile picture set failed ---")
                    else:
                        print("--- Photo upload confirm failed ---")
                else:
                    print("--- Photo upload failed ---")
            else:
                print("--- Timeline fetch failed ---")
        else:
            print("--- Cover photo publish failed ---")
    else:
        print("--- Cover photo upload failed ---")

if __name__ == "__main__":
    main()
