import json

# SCOPE = "MarketData ReadAccount Trade OptionsSpreads Matrix openid offline_access profile email"
# CRED_FILE = "secret/ts_tokens.json"

with open('config') as f:
    config = json.load(f)

SCOPE = (config["client_key"],
                       config["client_secret"],
                       config["call_back_domain"])
