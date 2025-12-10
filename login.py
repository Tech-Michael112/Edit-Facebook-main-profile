import requests
import json
import re
import os
import time
import sys
os.system('clear')
def get_2fa_code(key):
    clean_key = key.replace(" ", "")
    url = f"https://2fa.live/tok/{clean_key}"

    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Mobile Safari/537.36",
        'sec-ch-ua-platform': "\"Android\"",
        'x-requested-with': "XMLHttpRequest",
        'sec-ch-ua': "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
        'sec-ch-ua-mobile': "?1",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://2fa.live/",
        'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
        'if-none-match': "W/\"12-vXdg77AvGuh1AEGm8GJbb3NdhpA\"",
        'priority': "u=1, i",
        'Cookie': "_gcl_au=1.1.1804570901.1765244060; _gid=GA1.2.330686978.1765244061; _ga=GA1.2.564353774.1765244061; _ga_R2SB88WPTD=GS2.1.s1765274399$o2$g1$t1765274508$j60$l0$h0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            code = data.get("token")
            if code and len(code) == 6:
                return code
    except:
        pass
    return None

def get_two_step_verification_context(user_id, password):
    url = "https://b-graph.facebook.com/graphql"

    timestamp = int(time.time())
    encrypted_password = f"#PWD_FB4A:0:{timestamp}:{password}"

    payload_data = {
        "params": {
            "params": json.dumps({
                "params": json.dumps({
                    "client_input_params": {
                        "aac": json.dumps({"aac_init_timestamp": timestamp}),
                        "sim_phones": [],
                        "aymh_accounts": [],
                        "network_bssid": None,
                        "secure_family_device_id": "de9c140c-8796-478c-9195-5cfcdcd1a4cf",
                        "attestation_result": {"errorMessage": "KeyAttestationException: No key found!"},
                        "has_granted_read_contacts_permissions": 0,
                        "auth_secure_device_id": "",
                        "has_whatsapp_installed": 0,
                        "password": encrypted_password,
                        "sso_token_map_json_string": "",
                        "block_store_machine_id": "",
                        "cloud_trust_token": None,
                        "event_flow": "login_manual",
                        "password_contains_non_ascii": "false",
                        "sim_serials": [],
                        "client_known_key_hash": "",
                        "encrypted_msisdn": "",
                        "has_granted_read_phone_permissions": 0,
                        "app_manager_id": "",
                        "should_show_nested_nta_from_aymh": 0,
                        "device_id": "efd96a84-ae23-457a-bcd5-314a14f31c33",
                        "zero_balance_state": "",
                        "login_attempt_count": 1,
                        "machine_id": "",
                        "flash_call_permission_status": {"READ_PHONE_STATE": "DENIED", "READ_CALL_LOG": "DENIED", "ANSWER_PHONE_CALLS": "DENIED"},
                        "accounts_list": [],
                        "family_device_id": "efd96a84-ae23-457a-bcd5-314a14f31c33",
                        "fb_ig_device_id": [],
                        "device_emails": [],
                        "try_num": 1,
                        "lois_settings": {"lois_token": ""},
                        "event_step": "home_page",
                        "headers_infra_flow_id": "",
                        "openid_tokens": {},
                        "contact_point": str(user_id)
                    },
                    "server_params": {
                        "should_trigger_override_login_2fa_action": 0,
                        "is_vanilla_password_page_empty_password": 0,
                        "is_from_logged_out": 0,
                        "should_trigger_override_login_success_action": 0,
                        "login_credential_type": "none",
                        "server_login_source": "login",
                        "waterfall_id": "d86e3bef-8755-4f2f-9fce-c0bf4e5a7124",
                        "two_step_login_type": "one_step_login",
                        "login_source": "Login",
                        "is_platform_login": 0,
                        "pw_encryption_try_count": 1,
                        "INTERNAL__latency_qpl_marker_id": 36707139,
                        "is_from_aymh": 0,
                        "offline_experiment_group": "caa_iteration_v6_perf_fb_2",
                        "is_from_landing_page": 0,
                        "left_nav_button_action": "NONE",
                        "password_text_input_id": "rl6t26:100",
                        "is_from_empty_password": 0,
                        "is_from_msplit_fallback": 0,
                        "ar_event_source": "login_home_page",
                        "username_text_input_id": "rl6t26:99",
                        "layered_homepage_experiment_group": None,
                        "device_id": "efd96a84-ae23-457a-bcd5-314a14f31c33",
                        "INTERNAL__latency_qpl_instance_id": 1.66817628600416E14,
                        "reg_flow_source": "login_home_native_integration_point",
                        "is_caa_perf_enabled": 1,
                        "credential_type": "password",
                        "is_from_password_entry_page": 0,
                        "caller": "gslr",
                        "family_device_id": "efd96a84-ae23-457a-bcd5-314a14f31c33",
                        "is_from_assistive_id": 0,
                        "access_flow_version": "pre_mt_behavior",
                        "is_from_logged_in_switcher": 0
                    }
                })
            }),
            "bloks_versioning_id": "3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5",
            "app_id": "com.bloks.www.bloks.caa.login.async.send_login_request"
        },
        "scale": "2",
        "nt_context": {
            "using_white_navbar": True,
            "styles_id": "cfe75e13b386d5c54b1de2dcca1bee5a",
            "pixel_ratio": 2,
            "is_push_on": True,
            "debug_tooling_metadata_token": None,
            "is_flipper_enabled": False,
            "theme_params": [],
            "bloks_version": "3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5"
        }
    }

    payload = {
        'method': "post",
        'pretty': "false",
        'format': "json",
        'server_timestamps': "true",
        'locale': "en_GB",
        'purpose': "fetch",
        'fb_api_req_friendly_name': "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
        'fb_api_caller_class': "graphservice",
        'client_doc_id': "119940804214876861379510865434",
        'variables': json.dumps(payload_data),
        'fb_api_analytics_tags': json.dumps(["GraphServices"]),
        'client_trace_id': "5306c4e6-4ff3-4c17-b0ce-b62f6a77ce28"
    }

    headers = {
        'User-Agent': "[FBAN/FB4A;FBAV/486.0.0.66.70;FBBV/653066364;FBDM/{density=2.0,width=720,height=1504};FBLC/en_GB;FBRV/0;FBCR/CHINA UNICOM;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.mahos;FBDV/23106RN0DA;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
        'x-fb-connection-type': "WIFI.ETHERNET",
        'x-tigon-is-retry': "False",
        'x-fb-device-group': "2265",
        'x-graphql-request-purpose': "fetch",
        'x-fb-privacy-context': "3643298472347298",
        'x-fb-friendly-name': "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
        'x-graphql-client-library': "graphservice",
        'x-fb-net-hni': "46001",
        'x-fb-sim-hni': "46001",
        'authorization': "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
        'x-fb-request-analytics-tags': json.dumps({"network_tags": {"product": "350685531728", "purpose": "fetch", "request_category": "graphql", "retry_attempt": "0"}, "application_tags": "graphservice"}),
        'x-fb-http-engine': "Tigon/Liger",
        'x-fb-client-ip': "True",
        'x-fb-server-cluster': "True"
    }

    try:
        response = requests.post(url, data=payload, headers=headers, timeout=15)
        if response.status_code == 200:
            raw_response = response.text
            context_patterns = [
                r'two_step_verification_context[\\\"]*:[\\\"]*([A-Za-z0-9+/=_-]+)',
                r'\"two_step_verification_context\"\s*:\s*\"([A-Za-z0-9+/=_-]+)\"',
                r'two_step_verification_context\\\\\\\":\\\\\\\"([A-Za-z0-9+/=_-]+)',
                r'(AR[A-Za-z0-9+/=_-]{400,})'
            ]

            for pattern in context_patterns:
                matches = re.findall(pattern, raw_response)
                if matches:
                    return matches[0]
    except:
        pass
    return None

def send_verify_code_request(code, two_step_verification_context):
    url = "https://b-graph.facebook.com/graphql"

    params_data = {
        "client_input_params": {
            "auth_secure_device_id": "",
            "block_store_machine_id": "",
            "code": code,
            "should_trust_device": 1,
            "family_device_id": "efd96a84-ae23-457a-bcd5-314a14f31c33",
            "device_id": "efd96a84-ae23-457a-bcd5-314a14f31c33",
            "cloud_trust_token": None,
            "network_bssid": None,
            "machine_id": "QFs3aY-k0uEvfJGxpwXZ3-yf"
        },
        "server_params": {
            "INTERNAL__latency_qpl_marker_id": 36707139,
            "block_store_machine_id": None,
            "device_id": "efd96a84-ae23-457a-bcd5-314a14f31c33",
            "spectra_reg_login_data": None,
            "cloud_trust_token": None,
            "challenge": "totp",
            "machine_id": "QFs3aY-k0uEvfJGxpwXZ3-yf",
            "INTERNAL__latency_qpl_instance_id": 1.67249268400124E14,
            "two_step_verification_context": two_step_verification_context,
            "flow_source": "two_factor_login"
        }
    }

    payload_data = {
        "params": {
            "params": json.dumps({"params": json.dumps(params_data)}),
            "bloks_versioning_id": "3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5",
            "app_id": "com.bloks.www.two_step_verification.verify_code.async"
        },
        "scale": "2",
        "nt_context": {
            "using_white_navbar": True,
            "styles_id": "cfe75e13b386d5c54b1de2dcca1bee5a",
            "pixel_ratio": 2,
            "is_push_on": True,
            "debug_tooling_metadata_token": None,
            "is_flipper_enabled": False,
            "theme_params": [],
            "bloks_version": "3711cb070fe0ab5acd59ae663b1ae4dc75db6f0c463d26a232fd9d72a63fb3e5"
        }
    }

    payload = {
        'method': "post",
        'pretty': "false",
        'format': "json",
        'server_timestamps': "true",
        'locale': "en_GB",
        'purpose': "fetch",
        'fb_api_req_friendly_name': "FbBloksActionRootQuery-com.bloks.www.two_step_verification.verify_code.async",
        'fb_api_caller_class': "graphservice",
        'client_doc_id': "119940804214876861379510865434",
        'variables': json.dumps(payload_data),
        'fb_api_analytics_tags': json.dumps(["GraphServices"]),
        'client_trace_id': "0efc2be6-2df0-40c1-b4b0-fe6ea2942db2"
    }

    headers = {
        'User-Agent': "[FBAN/FB4A;FBAV/486.0.0.66.70;FBBV/653066364;FBDM/{density=2.0,width=720,height=1504};FBLC/en_GB;FBRV/0;FBCR/CHINA UNICOM;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.mahos;FBDV/23106RN0DA;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
        'x-fb-connection-type': "WIFI.ETHERNET",
        'x-tigon-is-retry': "False",
        'x-fb-device-group': "2265",
        'x-graphql-request-purpose': "fetch",
        'x-fb-privacy-context': "3643298472347298",
        'x-fb-friendly-name': "FbBloksActionRootQuery-com.bloks.www.two_step_verification.verify_code.async",
        'x-graphql-client-library': "graphservice",
        'x-fb-net-hni': "46001",
        'x-fb-sim-hni': "46001",
        'authorization': "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
        'x-fb-request-analytics-tags': json.dumps({"network_tags": {"product": "350685531728", "purpose": "fetch", "request_category": "graphql", "retry_attempt": "0"}, "application_tags": "graphservice"}),
        'x-fb-http-engine': "Tigon/Liger",
        'x-fb-client-ip': "True",
        'x-fb-server-cluster': "True"
    }

    try:
        response = requests.post(url, data=payload, headers=headers, timeout=15)
        return response.text
    except:
        return ""

def extract_token_and_id(response_text):
    access_token = None
    user_id = None

    access_token_patterns = [
        r'\"access_token\\\\\\\":\\\\\\\"([A-Za-z0-9]+)\\\\\\\"',
        r'\"access_token\"\s*:\s*\"([A-Za-z0-9]+)\"',
        r'access_token[\\\"]*:[\\\"]*([A-Za-z0-9]+)'
    ]

    user_id_patterns = [
        r'\"uid\\\\\\\":([0-9]+)',
        r'\"uid\"\s*:\s*([0-9]+)',
        r'uid[\\\"]*:[\\\"]*([0-9]+)'
    ]

    for pattern in access_token_patterns:
        matches = re.findall(pattern, response_text)
        if matches:
            access_token = matches[0]
            break

    for pattern in user_id_patterns:
        matches = re.findall(pattern, response_text)
        if matches:
            user_id = matches[0]
            break

    return access_token, user_id

def process_single_account(user_id, password, twofa_key):
    two_step_verification_context = get_two_step_verification_context(user_id, password)

    if not two_step_verification_context:
        return user_id, None, None, "Failed to get context"

    code = get_2fa_code(twofa_key)

    if not code:
        return user_id, None, None, "Failed to get 2FA code"

    result = send_verify_code_request(code, two_step_verification_context)
    access_token, extracted_user_id = extract_token_and_id(result)

    if access_token and extracted_user_id:
        return user_id, access_token, extracted_user_id, "Success"
    else:
        return user_id, None, None, "Login failed"

def load_accounts_from_file(file_path):
    accounts = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    if '|' in line:
                        parts = line.split('|')
                        if len(parts) >= 3:
                            user_id = parts[0].strip()
                            password = parts[1].strip()
                            twofa_key = parts[2].strip()
                            accounts.append((user_id, password, twofa_key))
    except Exception as e:
        print(f"Error reading file: {e}")
    return accounts

def display_menu():
    print("\n" + "-"*50)
    print(" LOGIN AUTOMATION")
    print("-"*50)
    print("1. Single Account")
    print("2. Load from File (format: id|pass|2fa_key)")
    print("3. Exit")
    print("-"*50)

    while True:
        try:
            choice = int(input("\nSelect option (1-3): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Invalid choice! Please enter 1-3")
        except ValueError:
            print("Invalid input! Please enter a number")

def print_progress(total, current, success, failed, start_time):
    elapsed = time.time() - start_time
    percent = (current / total * 100) if total > 0 else 0
    sys.stdout.write(f"\r[STATUS] Processed: {current}/{total} | Success: {success} | Failed: {failed} | Elapsed: {elapsed:.1f}s")
    sys.stdout.flush()

def process_accounts(accounts, wait_time):
    total = len(accounts)
    success = 0
    failed = 0
    results = []

    print(f"\nProcessing {total} accounts...")
    print(f"Waiting {wait_time} seconds between accounts")
    print("-" * 60)

    start_time = time.time()

    print_progress(total, 0, success, failed, start_time)

    for i, (user_id, password, twofa_key) in enumerate(accounts, 1):
        try:
            result_user_id, access_token, extracted_user_id, status = process_single_account(user_id, password, twofa_key)

            if access_token and extracted_user_id:
                success += 1
                results.append((user_id, password, twofa_key, access_token, extracted_user_id, "SUCCESS"))
                print(f"\n\033[32m{user_id}|{password}|{access_token[:50]}...\033[0m")
            else:
                failed += 1
                results.append((user_id, password, twofa_key, None, None, status))
                print(f"\n\033[91m[FAILED] {user_id}|{password}|R:{status}\033[0m")

        except Exception as e:
            failed += 1
            results.append((user_id, password, twofa_key, None, None, f"Error: {str(e)}"))
            print(f"\n[ERROR] {user_id} | {str(e)}")

        print_progress(total, i, success, failed, start_time)
        
        if i < total:
            print(f"\nWaiting {wait_time} seconds before next account...")
            time.sleep(wait_time)

    print()
    return results, total, success, failed

def save_results(results, filename="results.txt"):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("ID|PASS|2FA_KEY|ACCESS_TOKEN|USER_ID|STATUS\n")
            for user_id, password, key, token, extracted_id, status in results:
                token_str = token if token else ""
                extracted_id_str = extracted_id if extracted_id else ""
                file.write(f"{user_id}|{password}|{key}|{token_str}|{extracted_id_str}|{status}\n")
        print(f"\n Results saved to: {filename}")
    except Exception as e:
        print(f"\n Error saving results: {e}")

def main():
    while True:
        choice = display_menu()

        if choice == 1:
            print("\nEnter account details:")
            user_id = input("User ID: ").strip()
            password = input("Password: ").strip()
            twofa_key = input("2FA Key: ").strip()

            if user_id and password and twofa_key:
                print("\nProcessing account...")
                result_user_id, token, extracted_id, status = process_single_account(user_id, password, twofa_key)

                print("\n" + "-"*60)
                if token and extracted_id:
                    print("\033[32m Successful!\033[0m")
                    print(f"User ID: {extracted_id}")
                    print(f"\033[96mAccess Token: {token}\033[0m")
                else:
                    print("\033[91m FAILED\033[0m")
                    print(f"Status: {status}")
                print("-"*60)

        elif choice == 2:
            file_path = input("\nEnter file path: ").strip()
            if os.path.exists(file_path):
                accounts = load_accounts_from_file(file_path)
                if accounts:
                    wait_time = input("\nEnter wait time between accounts (seconds): ").strip()
                    try:
                        wait_time = int(wait_time)
                        if wait_time < 0:
                            wait_time = 10
                    except:
                        wait_time = 10
                    
                    print(f"\nLoaded {len(accounts)} accounts from file")
                    
                    print("\n" + "-" * 60)
                    results, total, success, failed = process_accounts(accounts, wait_time)

                    print("\n" + "-"*60)
                    print("FINAL RESULTS")
                    print("-"*60)
                    print(f"Total: {total}")
                    print(f"\033[32mSuccessfully: {success}\033[0m")
                    print(f"\033[91mFailed: {failed}\033[0m")
                    print("-"*60)

                    save_results(results)
                else:
                    print("No valid accounts found in file!")
            else:
                print("File not found!")

        elif choice == 3:
            print("\nGoodbye!")
            break

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main() 
