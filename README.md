# Verihash

This is a lightweight Veriblock alternative which checks sets of hashes against the current Bitcoin hash for fork resolution. Instead of saving data to the Bitcoin blockchain, it simply compares individual hashes to the latest Bitcoin hash and returns the best candidate.

To run, simply start web.py
```python3 web.py```
This will start a restful API on your local machine, port ```9091```

To query the API with hash candidates, simply enter them into the URL in the following format, delimited with a semicolon

 ```
 http://127.0.0.1:9091/all/hash1;hash2;hash3
 ```
 The best candidate will be returned to you in the following format, returning the best candidate with the highest similarity rate and related Bitcoin block information
 ```
 [{"winner": "hash2", "similarity": 0.25}, {"btc_hash": "00000000000000000022f47cf1a1a0f232deb855997f61382106ec35bd0f3edc", "btc_time": 1553917566, "btc_height": 569409}]
 ```
 Test run:
  ```
  python3 main.py
  ```
 Programmic access:
 ```
 python3 programmic.py
 ```
 
 
 Unlike Veriblock, Verihash does not store any information onchain for Bitcoin or Veriblock and you do not have to pay any fees. Public blockchain.com API is used, but you can easily redirect it to your bitcoind.
 
