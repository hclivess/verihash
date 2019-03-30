import requests

hashes_to_test = ["hash1","hash2"]
hashes_to_test_raw = ';'.join(hashes_to_test)
api_result = requests.get(f"http://127.0.0.1:9091/all/{hashes_to_test_raw}").text
print(api_result)


