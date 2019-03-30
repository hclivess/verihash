from blockchain import blockexplorer
from difflib import SequenceMatcher
from hashlib import blake2b


def similar(a, b):
    print(f"Testing similarity between {a} and {b}")
    return SequenceMatcher(None, a, b, autojunk=False).ratio()

def compare (hash_candidates):
    winner = {}
    latest_btc_block = {}

    hash_winning = 0

    latest_block = blockexplorer.get_latest_block()
    latest_btc_block['btc_hash'] = latest_block.hash
    latest_btc_block['btc_time'] = latest_block.time
    latest_btc_block['btc_height'] = latest_block.height

    for hash_instance in hash_candidates:
        h = blake2b(digest_size=20)
        h.update(hash_instance.encode('utf8'))
        hashed_hash_instance = h.hexdigest().encode('utf-8')
        hashed_hash_instance_str = hashed_hash_instance.decode('utf-8')

        print(hash_instance, hashed_hash_instance_str)

        similarity = (similar(hashed_hash_instance_str, str(latest_block.hash)))

        if similarity > hash_winning:
            hash_winning = similarity
            winner['winner'] = hash_instance
            winner['similarity'] = similarity

    return winner,latest_btc_block

if __name__ == "__main__":
    print(compare(["test_hash_1","test_hash_2","test_hash_3"]))