import requests
import re
import json
import base64
import uuid
import os,random


tok= input(' Enter FB token: ')
id= input(' Put FB uid: ')
input(' prress enter to Continue....')
os.system("clear")
ip = random.choice([
    "192.168.0.100",
    "192.168.1.101",
    "192.168.43.1",
    "10.0.0.2",
    "172.20.10.1",
    "192.168.178.20"
])


url = input("Enter Facebook post URL: ").strip()

fetch_headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    'upgrade-insecure-requests': "1",
    'dnt': "1",
    'x-requested-with': "mark.via.gp",
    'sec-fetch-site': "none",
    'sec-fetch-mode': "navigate",
    'sec-fetch-user': "?1",
    'sec-fetch-dest': "document",
    'dpr': "2",
    'viewport-width': "980",
    'sec-ch-ua': "\"Android WebView\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
    'sec-ch-ua-mobile': "?1",
    'sec-ch-ua-platform': "\"Android\"",
    'sec-ch-ua-platform-version': "\"\"",
    'sec-ch-ua-model': "\"\"",
    'sec-ch-ua-full-version-list': "",
    'sec-ch-prefers-color-scheme': "dark",
    'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
    'priority': "u=0, i"
}

print("Fetching page...")

response = requests.get(url, headers=fetch_headers, timeout=10)
if response.status_code == 200:
    html_content = response.text
    
    feedback_pattern = r'"feedback":\s*{\s*"id":\s*"([^"]+)"'
    matches = re.findall(feedback_pattern, html_content)
    
    if matches:
        feedback_id = matches[0]
        print(f"Extracted Feedback ID: {feedback_id}")
    else:
        post_id_pattern = r'"post_id"\s*:\s*"(\d+)"'
        post_matches = re.findall(post_id_pattern, html_content)
        if post_matches:
            post_id = post_matches[0]
            feedback_id = base64.b64encode(f"feedback:{post_id}".encode()).decode()
            print(f"Extracted Post ID: {post_id}")
            print(f"Encoded Feedback ID: {feedback_id}")
        else:
            print("Could not find post ID")
            feedback_id = None
else:
    print(f"Failed to fetch page: {response.status_code}")
    feedback_id = None

if feedback_id:
    comment_text = input("Enter comment text: ").strip()
    print(53*"-")
    if not comment_text:
        print("Comment text is empty")
        exit()
    
    graphql_url = "https://graph-fallback.facebook.com/graphql?_nc_eh=2,fa4ec4cac7cfad9e97a291f7f6296edd,AUmQwZXUKu2SMpV3i5ibFHAgeBiDWGkHjfn-Tu77v3F6dwZ9_ZtAV7fDEr5GMSoi70I"
    
    payload = {
        'method': "post",
        'pretty': "false",
        'format': "json",
        'server_timestamps': "true",
        'locale': "en_GB",
        'fb_api_req_friendly_name': "CommentCreateMutation",
        'fb_api_caller_class': "graphservice",
        'client_doc_id': "847448982477392474615269160",
        'fb_api_client_context': json.dumps({"is_background": False}),
        'variables': json.dumps({
            "group_member_action_source": "GROUP_COMMENT",
            "image_medium_height": 2048,
            "enable_comment_identity_badge": True,
            "image_high_height": 2048,
            "image_medium_width": 360,
            "profile_pic_media_type": "image/x-auto",
            "size_style": "contain-fit",
            "profile_image_size": 80,
            "input": {
                "tracking": [
                    "{\"qid\":\"-7821779205627894801\",\"mf_story_key\":\"-8732996071543502680\",\"top_level_post_id\":\"1354157592847767\",\"content_owner_id_new\":\"100091893762082\",\"page_id\":\"119768761085825\",\"src\":22,\"originated_from_recommendation\":\"1\",\"story_location\":5,\"story_attachment_style\":\"video_autoplay\",\"view_time\":1765226324,\"filter\":\"h_nor\",\"video_id\":\"1354157592847767\",\"sty\":128,\"story_set_type\":19,\"mf_objid\":\"812936511779467\",\"ent_attachement_type\":\"VideoAttachment\",\"app_id\":\"6628568379\",\"viewstate_id\":\"-8732996071543502680\",\"pos\":4,\"page_insights\":{\"100091893762082\":{\"page_id\":\"100091893762082\",\"page_id_type\":\"page\",\"actor_id\":\"100091893762082\",\"dm\":{\"isShare\":0,\"originalPostOwnerID\":0,\"sharedMediaID\":0,\"sharedMediaOwnerID\":0},\"psn\":\"EntVideoCreationStory\",\"post_context\":{\"object_fbtype\":1,\"publish_time\":1764875182,\"story_name\":\"EntVideoCreationStory\",\"story_fbid\":[\"1354157592847767\"]},\"role\":1,\"sl\":5,\"targets\":[{\"actor_id\":\"100091893762082\",\"page_id\":\"100091893762082\",\"post_id\":\"1354157592847767\",\"role\":1,\"share_id\":0}]}},\"profile_relationship_type\":6,\"recommendation_item_source\":8532,\"recommendation_item_trigger_source\":\"809839811804956\",\"actrs\":\"100091893762082\",\"is_creator_profile_plus\":\"1\",\"join_key_from_recagg\":\"J118,100082394817366,-7821779205769029979,812936511779467,IFR,S3\",\"tds_flgs\":3}",
                    "{\"image_loading_state\":0,\"time_since_fetched\":54096,\"radio_type\":\"wifi-ethernet\",\"client_viewstate_position\":1,\"enabled_features\":\"[\\\"ZR\\\"]\",\"feed_unit_trace_info\":\"{\\\"state\\\":544,\\\"is_seen\\\":false,\\\"real_time_seen_state\\\":false,\\\"is_cache_enabled\\\":true,\\\"is_from_previous_session\\\":false,\\\"content_source\\\":\\\"NETWORK\\\",\\\"select_time\\\":1765226333247,\\\"network_fetch_time\\\":1765226323891,\\\"session_time\\\":1765226323871,\\\"network_response_time\\\":1765226328256,\\\"time_to_select_from_sess_start\\\":9376,\\\"time_to_net_rec_from_sess_start\\\":4385,\\\"time_since_network\\\":-1765226328256,\\\"network_pos\\\":5,\\\"network_latency\\\":4365,\\\"organic_pos\\\":2,\\\"time_since_select\\\":-1765226333247,\\\"category\\\":\\\"ENGAGEMENT\\\",\\\"fetch_age\\\":-1765226328234,\\\"story_age_at_vend_secs\\\":5.013,\\\"fetch_time_since_app_start\\\":1326376,\\\"rank_score\\\":\\\"1622234.00000\\\",\\\"client_weight\\\":\\\"3135912862234.00000\\\",\\\"is_instant_feed_cached_story\\\":false,\\\"is_see_first\\\":false,\\\"connection_quality\\\":3,\\\"connection_quality_by_bandwidth\\\":3,\\\"connection_quality_by_latency\\\":4,\\\"connection_quality_by_network_type\\\":3,\\\"is_from_background_prefetch\\\":\\\"false\\\",\\\"gql_position\\\":\\\"4\\\",\\\"did_show_ranking_debug_info_header\\\":false,\\\"story_class\\\":\\\"Story\\\",\\\"is_partial_story\\\":false,\\\"min_gap_type\\\":\\\"14\\\",\\\"groups_tab_feed_unit_type_name\\\":\\\"Story\\\",\\\"groups_tab_story_is_crf\\\":2}\",\"feed_unit_trace_info\":\"{}\"}",
                    "{\"conversation_guide_shown\":\"none\"}"
                ],
                "privacy_type": "DEFAULT_PRIVACY",
                "vod_video_timestamp": 12,
                "downstream_share_session_id": None,
                "downstream_share_session_start_time": None,
                "downstream_share_session_origin_uri": None,
                "nectar_module": "newsfeed_ufi",
#                "actor_id": "100082394817366",
                "actor_id":f"{id}",
                "attribution_id_v2": "FeedbackFragment,story_feedback_flyout,tap_footer_comment,1765226382.655,177208575,,,,1765226382.655;NewsFeedFragment,native_newsfeed,,1765226324.584,264004470,,301,,1765226324.584;LoginSuccessFragment,,,1765226265.732,241410581,,301,,1765226323.862",
                "feedback_source": "feedback_comments",
                "message": {
                    "text": comment_text,
                    "ranges": []
                },
                "feedback_referrer": "native_newsfeed",
                "feedback_id": feedback_id,
                "idempotence_token": str(uuid.uuid4()),
                "entry_point": "TAP_FOOTER_COMMENT",
                "downstream_share_navigation_events_count": [
                    {"name": "APP_BACKGROUNDED", "count": 0},
                    {"name": "APP_FOREGROUNDED", "count": 0}
                ],
                "action_timestamp": 1765226404
            },
            "nt_context": {
                "using_white_navbar": True,
                "styles_id": "079fde6dea01e71e4916c66f4e668826",
                "pixel_ratio": 2,
                "is_push_on": True,
                "debug_tooling_metadata_token": None,
                "is_flipper_enabled": False,
                "theme_params": [
                    {
                        "value": ["BLUEPRINT_TEST_GUTTER"],
                        "design_system_name": "FDS"
                    }
                ],
                "bloks_version": "11ed8f9f9ba3210acffda8a3b7e8ff5e1bc0dd59a8fe2f089aa58f16601d5bc3"
            },
            "enable_participation_questionnaire": True,
            "image_low_height": 2048,
            "enable_comment_shares": True,
            "enable_user_signals_in_comments": True,
            "enable_story_ring": True,
            "feedback_source": "NEWS_FEED",
            "fetch_presence_eligible": True,
            "fetch_privacy_value_for_pending_approval_comment": True,
            "image_high_width": 720,
            "enable_reactions_dock_message": True,
            "fetch_privacy_value_for_declined_comment": True,
            "media_type": "image/x-auto",
            "should_fetch_pinned_comment": True,
            "image_low_width": 240,
            "enable_add_friend_in_comments": True,
            "should_fetch_comments_downvote_fields": True,
            "query_for_can_be_invited_by_viewer": True,
            "enable_gen_ai_content_transparency_in_comments": True
        }),
        'fb_api_analytics_tags': json.dumps([
            "visitation_id=null",
            "nav_attribution_id_v2=FeedbackFragment,story_feedback_flyout,tap_footer_comment,1765226382.655,177208575,,,,1765226382.655;NewsFeedFragment,native_newsfeed,,1765226324.584,264004470,,301,,1765226324.584;LoginSuccessFragment,,,1765226265.732,241410581,,301,,1765226323.862",
            "surface_hierarchy=FeedbackFragment,story_feedback_flyout,null;SimpleUFIPopoverFragment,story_feedback_flyout,null;NewsFeedFragment,native_newsfeed,null;FbChromeFragment,unknown,null;FbMainTabActivity,native_newsfeed,null;FbCdsBottomSheetFragment,native_cds_fragment_screen_uninitialized,null;FbExperimentalLoggedOutBloksActivity,unknown,null;FbCdsBottomSheetFragment,native_cds_fragment_screen_uninitialized,null;FbExperimentalLoggedOutBloksActivity,unknown,null;LoginFragmentController,null,null",
            "GraphServices",
            "session_id=UFS-491ea055-15cd-c03f-d748-25d2c64f50d5-fg-6"
        ]),
        'client_trace_id': str(uuid.uuid4())
    }

    headers = {
        'User-Agent': "[FBAN/FB4A;FBAV/534.0.0.56.76;FBBV/803095644;FBDM/{density=2.0,width=720,height=1504};FBLC/en_GB;FBRV/0;FBCR/CHINA UNICOM;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katanb;FBDV/23106RN0DA;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
 #       'Accept-Encoding': "zstd, gzip, deflate",
        'x-fb-request-analytics-tags': json.dumps({
            "network_tags": {
                "product": "350685531728",
                "request_category": "graphql",
                "purpose": "none",
                "retry_attempt": "0"
            },
            "application_tags": "graphservice"
        }),
        'x-fb-rmd': "state=URL_MODIFIED;v=1;ip="+str(ip)+";tkn=76feebca9c5b95cb3c83878c968668b8;reqTime=208489;recvTime=208489;rn=TIMER_EXPIRED;if=Wifi;fbn=2;fbu=1;fbr=2",
        'x-fb-friendly-name': "CommentCreateMutation",
        'x-zero-f-device-id': "1beaf9e6-0fe6-4f88-b320-114add7b2da2",
        'x-graphql-client-library': "graphservice",
        'x-fb-appnetsession-sid': "853929c00cb32a6c21d2f1f399c39ac8",
        'x-fb-sim-hni': "46001",
        'x-fb-device-group': "5130",
        'x-zero-eh': "2,fa4ec4cac7cfad9e97a291f7f6296edd,AUmQwZXUKu2SMpV3i5ibFHAgeBiDWGkHjfn-Tu77v3F6dwZ9_ZtAV7fDEr5GMSoi70I",
        'x-fb-network-properties': "Wifi;Validated;",
  #      'content-encoding': "gzip",
        'x-fb-net-hni': "46001",
        'app-scope-id-header': "1beaf9e6-0fe6-4f88-b320-114add7b2da2",
        'x-fb-connection-type': "WIFI.ETHERNET",
        'x-fb-appnetsession-nid': "2f3a52395fc7aeb9add240b5bd34249e,Wifi",
#        'authorization': "OAuth EAAAAUaZA8jlABQPdpv4VRouEPXhzEhCCfPpKEYX8Vp5ky8xqCjf3FgahG0VfrCufodhUuMBYtZC2E8xt4CJC3dz4td0t2cONjZC8lDXqw1lo53eOTB63bSnFQra8ucMjrZCRiV2Dp21jQtEAQIYR1EZCBkdpTti9QjJHLRl0IxdGuvZB4XqgYNzjPij4JS6pwO6lHOSwZDZD",
        'authorization': f"OAuth {tok}",
#        'authorization': "OAuth EAAAAUaZA8jlABQCKHWCN5IdBufZAfpxh2YhGNCVjcJ1vWzYrZBUzj7ZBQZARq05Tir8kbFEnGy4Kp5X3IgIogxSZAyH5ii2afzLnipJX92xK4Ds7mZB71ETejikzUu0hhr1KGlbrHxrye4NcfltuwmT8kHuGBgbvOARPp6X3hbFLxSWaBN7Ll2fhhhpA3hsAIC2mzvJZBQZDZD",
        'x-fb-session-id': "nid=2blIxzomztP2;tid=1290;nc=0;fc=0;bc=0",
        'x-tigon-is-retry': "False",
        'priority': "u=3, i",
        'x-fb-qpl-active-flows-json': json.dumps({
            "schema_version": "v3",
            "inprogress_qpls": [],
            "snapshot_attributes": {}
        }),
        'x-fb-congestion-signal': "0",
        'x-meta-enable-tasos-ss-bwe': "1",
        'x-fb-http-engine': "Tigon/Liger",
        'x-fb-client-ip': "True",
        'x-fb-server-cluster': "True",
        'x-fb-conn-uuid-client': "6eccb01eafde5b732870df356a9e8a72"
    }

    print("Posting comment...")
    response = requests.post(graphql_url, data=payload, headers=headers)
    
    if response.status_code == 200:
        try:
            response_json = response.json()
            if 'data' in response_json and 'comment_create' in response_json['data']:
                if 'comment' in response_json['data']['comment_create']:
                    if 'id' in response_json['data']['comment_create']['comment']:
                        print("Comment posted successfully")
                        comment_id = response_json['data']['comment_create']['comment']['id']
                        print(f"Comment ID: {comment_id}")
        except:
            print("Error parsing response")
    else:
        print(f"Failed to post comment: {response.status_code}")
        print(response.text)
