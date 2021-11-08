from os import environ
from pathlib import Path
from tempfile import gettempdir

PROTOCOL_VERSION = 2

def get_pool_genesis_txn_path(pool_name):
    path_temp = Path(gettempdir()).joinpath("bbutestnet")
    path = path_temp.joinpath("{{}}.txn".format(pool_name))
    save_pool_genesis_txn_file(path)
    return path

def pool_genesis_txn_data():
    pool_ip = environ.get("TEST_POOL_IP", "127.0.0.1")

    return "\n".join([
        '{{"reqSignature":{{}},"txn":{{"data":{{"data":{{"alias":"usaabbudev01","blskey":"2KHfHgVce3r8p3vequA3vwkSwZdAMt2ub2jEAYJLJsFvpPAAp69ZqjTgo3bNUUzKrC2HidxKexFCbRcJJ8fYxmMQxFNfTKjs8jUd9ynQsxcoWNcZ18zmziRwmc6zPHswjB4BTiSLcECn1P5kU8nkqqpxwgBGmz1MQo7rpSqkksvtoJc","blskey_pop":"Qs3kRWV7fqKMyZNMUioGX2WuTmW5dZ1s9TmYdnhJWu82PDq3bHdiBb9hdW7ezqZ8RBTCz4W8JjuXuwzC8wWXyyTsXXecpJr3wQzY6sdrB6EtjonNwUQFH2EgrbBPmGu88ep4knVnQqU3ZRyitrm4sVuPie7LgtcNfjSWiem5AbS8Qf","client_ip":"167.24.233.22","client_port":"9702","node_ip":"167.24.233.22","node_port":"9701","services":["VALIDATOR"]}},"dest":"HjjsLjNykfjwrT7FJot2jDCCNuQ3s4TVagAaU5GrE2uG"}},"metadata":{{"from":"JxzRZq3gTwNSBd53AoYYDz"}},"type":"0"}},"txnMetadata":{{"seqNo":1,"txnId":"3853f7a5e29f9d8bdc6cd4b3e554508fb8d66248dcc9402d16f9dd902c094b0a"}},"ver":"1"}},{{"reqSignature":{{}},"txn":{{"data":{{"data":{{"alias":"doan_bbudev","blskey":"2256UhVAxdefJfy7NwJQUXtWbKyJPKdF27G6FSzr4BW7eFK6aKD9wCHBWhvWae3qVxu8pKVM9Yvxgdi4B7U616V61cDuBZixtDMZkEEvTSJYBi8PXhYrWSfomFWVwGdXXdgPdimQM1UHtBpAgSbPGxbWBzRULmvkHiund8ewAkjyh26","blskey_pop":"RYExo9UX177W88PPzVoSvGLHj7Y5zpxXmcczqrvvxvsGZZdk5zxbdcefkvGPECcZwLzQQFyMegSENfiRKurMSiRMZC1BxJECS4pEcnAcYUkFGfMEEDYhKnYi8eGEJwKSLvSYKbneW3LeeGJzw5NsBLfh8L6odDb2jgurrfWX6Lwcs1","client_ip":"54.89.69.97","client_port":"9702","node_ip":"54.89.69.97","node_port":"9701","services":["VALIDATOR"]}},"dest":"BWbhtN3ae5uNqpWqKHDnaCzgmTKGXCmtKUt6TjC3i25v"}},"metadata":{{"from":"2Lf1gAyNLEwiwXa7M1savw"}},"type":"0"}},"txnMetadata":{{"seqNo":2,"txnId":"4304653a406fcd312f7a3390956f1c997ce955f64d4c5f8504693b5a4bd07e29"}},"ver":"1"}},{{"reqSignature":{{}},"txn":{{"data":{{"data":{{"alias":"brlumedictst","blskey":"x8GdL7MES1rWiRQAEN4pqac9jKnQYxzZiCDqMAN488Fm9WkJyEPdNBkhEsQqVrSZXgvKjCTfYnDEDVnBxzX47WmdzZUCaQRSpfgxTqPZtvjz15uYMRHVqMDyfVHxEnCPZvhBFCJQwHPsvTpBodVcqu25min6PUinWe5PPdcDSt54gf","blskey_pop":"R11kHfLrNU1KrA3A2fSPKtub2LuLWQrQiSBonaTCuumJEMRSTwHzSzCUeLcpxpxqY1pYomM3TEUrQrqjxLanahQfUdCGFNGvz478FpFN7jnqBs6hYBSFvCrndJgWpiF82R2PtqyVNpDUd8ceBkUtWk5ftcgocRh1LVai7NZJvc78xF","client_ip":"52.148.178.37","client_port":"9702","node_ip":"52.148.178.4","node_port":"9701","services":["VALIDATOR"]}},"dest":"HKsBgfsm44SQy8XQFJo6iEzFdxrLiEJDHeNwnCUhjKB7"}},"metadata":{{"from":"5Wn8egUoAAwm3unVz8pKcH"}},"type":"0"}},"txnMetadata":{{"seqNo":3,"txnId":"bd93d709efefaabc8fe7321c464cbea6286f444e3aa6ef88f896598bd386b5e9"}},"ver":"1"}},{{"reqSignature":{{}},"txn":{{"data":{{"data":{{"alias":"IBMBedrockNodeDev","blskey":"3qZUfFGxboiWxFWrs12khKs2u5Cyg4vmUd2itQVfWX5ziEmkDeMnGz61b1Kzk69v8sjQpLKgZx2UZTw5b8cxH7U7W97iumWtxGQQDrvY6aSNy9a7iL8tVTKf1evSufxooPFY6pdFR1t4PX98pv2Gf41tK6owjG5HsFezf7vvCDPspF3","blskey_pop":"Qq7YWf4Pd63U7S35PE8FyjuQE1DfCSQhnVPzvFUrkQBukJk2uQENDTWZ2oHyPsGSi1meZs1dZrS8zCRwLmzdmvLmutanp4XXiM8cXmmMD1XcZwvpTmTJoLBravq3LFeEvpwRqvEoMsN6ogVcEEzZVbDS8Lnwz969hCD8k1ojpHW1xb","client_ip":"169.48.68.221","client_port":"9702","node_ip":"169.48.68.220","node_port":"9701","services":["VALIDATOR"]}},"dest":"AnRViMVPh5qbtYGaFe5nZryBMujePMwXodXAwufhjwo"}},"metadata":{{"from":"7iufBnrWcAiyJY6eestxZb"}},"type":"0"}},"txnMetadata":{{"seqNo":4,"txnId":"011165472c1b356d8aca33fa753bcd9280e4c7fdd75ab33dcd74424f227c037d"}},"ver":"1"}}'

    ])

def save_pool_genesis_txn_file(path):
    data = pool_genesis_txn_data()
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(str(path), "w+") as f:
        f.writelines(data)

