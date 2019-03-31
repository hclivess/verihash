# Verihash

**Work in progress**
**Proof of concept**

This is a lightweight Veriblock alternative which checks sets of hashes against the current Bitcoin hash for fork resolution. Instead of saving data to the Bitcoin blockchain, it simply compares individual hashes to the latest Bitcoin hash and returns the best candidate. _As of now, there is no protection against a 51% attack, which is the main goal of Veriblock. Such feature will likely require a form of data storage with some sort of authority management (like BTC chain) combined with time frames for entries in BTC block intervals. See issue https://github.com/hclivess/verihash/issues/1_

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
 ## Usecase:
 
 Verihash can be used to resolve network forks by comparing hashes of your favorite altcoin with security backed by Bitcoin hashrate. You can score hashes based on similarity to the Bitcoin main chain and easily evaluate the best candidate.
 
 
 ## Design aspects and considerations:
 
 #### Morphing
 Since this application currently uses only the most recent Bitcoin hash, the hash candidate order changes with every new Bitcoin block. Therefore, it is useful for estimation of the current block consensus, not for any historical verifications. Scanning Bitcoin hash history would open a possible bruteforce attack vector as miners could attempt to produce blocks that have the closest similarity ratio to a Bitcoin block at a particular block height.
  
 #### Bitcoin forking
As in case with Veriblock, a possible Bitcoin network split (forking) splits efficiency of this method by the number of forks.

 #### Disqualification
 Not all nodes will have all the possible hash candidates at all times, so this mechanism works in a way opposing that of Veriblock. Instead of qualifying blocks, it disqualifies them from a given number of candidates. Not all nodes will know all hashes at all times, but there is always a clear resolution from any given number of them, progressively leading to the only possible candidate.
  
 ## Notes:
 
 Unlike Veriblock, Verihash does not store any information onchain for Bitcoin or Veriblock and you do not have to pay any fees. Public blockchain.com API is used, but you can easily redirect it to your bitcoind to prevent a possible man-in-the middle attack or availability issues. 
 
 For your particular use, Verihash can be extended with data storage if needed, have hash rules linked to Bitcoin hashes of particular height with block time adjusted, etc. If you need any of these features, feel free to contact me at admin@bismuth.cz
 
