from flask import Flask, Response
import requests
import json
import random

# create our Flask app
app = Flask(__name__)

# Function to get the mapped token or handle meme tokens
def get_simple_price(token):
    token_map = {
        'ETH': 'ethereum',
        'SOL': 'solana',
        'BTC': 'bitcoin',
        'BNB': 'binancecoin',
        'ARB': 'arbitrum'
    }

    if token in token_map:
        return token_map[token]
    else:
        # This will handle meme tokens by retrieving the block height
        address = get_token_symbol_from_block_height(token)
        return get_token_price(address)  # Get the price using the token address


# Function to get the token's address using its block height
def get_token_symbol_from_block_height(block_height):
    # First API: Get token information by block height
    url = f'https://api.upshot.xyz/v2/allora/tokens-oracle/token/{block_height}'
    headers = {
        "accept": "application/json",
        "x-api-key": "UP-0d9ed54694abdac60fd23b74"  # Replace with your API key
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        address = data.get('data', {}).get('address')
        if address:
            return address
        else:
            raise ValueError("Token address not found")
    
    raise ValueError("Unsupported token")

# Function to get the price using the token's address
def get_token_price(address):
    # Second API: Get token price using the address from the first API
    url = f'https://api.geckoterminal.com/api/v2/simple/networks/base/token_price/{address}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Extract price from the response based on the given structure
        token_prices = data.get('data', {}).get('attributes', {}).get('token_prices', {})
        return token_prices.get(address)  # Use the address as the key to get the price

    raise ValueError("Price data not available for the token")


# Define the inference endpoint
# Define the inference endpoint
@app.route("/inference/<string:token>")
def get_inference(token):
    try:

        current_token = get_simple_price(token)  # Get either mapped token or meme token's price
        try:
          current_token = float(current_token)
        except (ValueError, TypeError):
          pass
          
        # If current_token is a price (for meme tokens), return it immediately
        if isinstance(current_token, (int, float)):            
            random_factor = random.uniform(0.99, 1.01)
            adjusted_price = current_token * random_factor
            formatted_price = f"{adjusted_price:.21f}"
            print(formatted_price)
            return Response(str(formatted_price), status=200, content_type='text/plain')

        return Response(str(2650), status=200, content_type='text/plain')

    except Exception as e:
        # Error handling, attempt to fetch price again
        return str(e)

# run our Flask app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
