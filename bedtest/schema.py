"""
This sample is extensions of "write_schema_and_cred_def.py"

Shows how to issue a credential as a Trust Anchor which has created a Cred Definition
for an existing Schema.

After Trust Anchor has successfully created and stored a Cred Definition using Anonymous Credentials,
Prover's wallet is created and opened, and used to generate Prover's Master Secret.
After that, Trust Anchor generates Credential Offer for given Cred Definition, using Prover's DID
Prover uses Credential Offer to create Credential Request
Trust Anchor then uses Prover's Credential Request to issue a Credential.
Finally, Prover stores Credential in its wallet.
"""

import asyncio
import json
import pprint

from indy import pool, ledger, wallet, did, anoncreds
from indy.error import ErrorCode, IndyError

#from utils import open_wallet, get_pool_genesis_txn_path, PROTOCOL_VERSION

pool_name = 'testnet'
issuer_wallet_config = json.dumps({"id": "bubs"})
issuer_wallet_credentials = json.dumps({"key": "testkey"})
steward_did = 'JxzRzq3gTwNSBd53AoYYDz'
trust_anchor_did = '4DQfNnivcNee6v1bJmhWY1'
PROTOCOL_VERSION = '2'

def print_log(value_color="", value_noncolor=""):
    """set the colors for text."""
    HEADER = '\033[92m'
    ENDC = '\033[0m'
    print(HEADER + value_color + ENDC + str(value_noncolor))

async def issue_credential():
    try:

        # 2.
        print_log('\n2. Open pool ledger and get the handle from libindy\n')
        pool_handle = await pool.open_pool_ledger(config_name=pool_name, config=None)
        issuer_wallet_handle = await wallet.open_wallet(issuer_wallet_config, issuer_wallet_credentials)


        # 8.
        print_log('\n8. Issuer create Credential Schema\n')
        schema = {
            'name': 'usaa_credtest',
            'version': '1.0',
            'attributes': '["age", "sex", "height", "name"]'
        }
        issuer_schema_id, issuer_schema_json = await anoncreds.issuer_create_schema(steward_did, 
                                                                                schema['name'],
                                                                                schema['version'],
                                                                                schema['attributes'])
        print_log('Schema: ')
        pprint.pprint(issuer_schema_json)

        # 9.
        print_log('\n9. Build the SCHEMA request to add new schema to the ledger\n')
        schema_request = await ledger.build_schema_request(steward_did, issuer_schema_json)
        print_log('Schema request: ')
        pprint.pprint(json.loads(schema_request))

        # 10.
        print_log('\n10. Sending the SCHEMA request to the ledger\n')
        schema_response = \
            await ledger.sign_and_submit_request(pool_handle,
                                                 issuer_wallet_handle,
                                                 steward_did,
                                                 schema_request)
        print_log('Schema response:')
        pprint.pprint(json.loads(schema_response))

        # 11.
        print_log('\n11. Creating and storing Credential Definition using anoncreds as Trust Anchor, for the given Schema\n')
        cred_def_tag = 'TAG1'
        cred_def_type = 'CL'
        cred_def_config = json.dumps({"support_revocation": False})

        (cred_def_id, cred_def_json) = \
            await anoncreds.issuer_create_and_store_credential_def(issuer_wallet_handle,
                                                                   trust_anchor_did,
                                                                   issuer_schema_json,
                                                                   cred_def_tag,
                                                                   cred_def_type,
                                                                   cred_def_config)
        print_log('Credential definition: ')
        pprint.pprint(json.loads(cred_def_json))

    except IndyError as e:
        print('Error occurred: %s' % e)

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(issue_credential())
    loop.close()


if __name__ == '__main__':
    main()

