from web3 import Web3

API_URL = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3 =  Web3( Web3.HTTPProvider(API_URL))

def getGasPrices():
    try:
        gasPrices={}
        gweiPrices={}
        etherPrices={}
        dollarPrices={}
        euroPrices={}

        gasPrices["current"] = web3.eth.gas_price

        gasPrices["safe"] = int(gasPrices["current"] * 0.9)  
        gasPrices["average"] = int(gasPrices["current"] * 1.0)   
        gasPrices["fast"] = int(gasPrices["current"] * 1.1)     
        gasPrices["fastest"] = int(gasPrices["current"] * 1.2)   
        
        # TA2: Convert gas prices from Wei to Gwei
        gweiPrices["current"] = web3.from_wei(gasPrices["current"], 'gwei')
        gweiPrices["safe"] = web3.from_wei(gasPrices["safe"], 'gwei')
        gweiPrices["average"] = web3.from_wei(gasPrices["average"], 'gwei')
        gweiPrices["fast"] = web3.from_wei(gasPrices["fast"], 'gwei')
        gweiPrices["fastest"] = web3.from_wei(gasPrices["fastest"], 'gwei')
        
        # SA2: Conversion of gas price into ether
        etherPrices["current"] = web3.from_wei(gasPrices["current"], 'ether')
        etherPrices["safe"] = web3.from_wei(gasPrices["safe"], 'ether')
        etherPrices["average"] = web3.from_wei(gasPrices["average"], 'ether')
        etherPrices["fast"] = web3.from_wei(gasPrices["fast"], 'ether')
        etherPrices["fastest"] = web3.from_wei(gasPrices["fastest"], 'ether')

        
        # SA2: Conversion of gas price into ether to dollars
        conversionRate = 1826.33
        dollarPrices["current"] = etherPrices["current"] * int(conversionRate)
        dollarPrices["safe"] = etherPrices["safe"] * int(conversionRate)
        dollarPrices["average"] = etherPrices["average"] * int(conversionRate)
        dollarPrices["fast"] = etherPrices["fast"] * int(conversionRate)
        dollarPrices["fastest"] =  etherPrices["fastest"] * int(conversionRate)
        print(dollarPrices)

         # AA1: Conversion of gas price into ether to euro
        conversionRateE = 1671
        euroPrices["current"] = etherPrices["current"] * int(conversionRateE)
        euroPrices["safe"] = etherPrices["safe"] * int(conversionRateE)
        euroPrices["average"] = etherPrices["average"] * int(conversionRateE)
        euroPrices["fast"] = etherPrices["fast"] * int(conversionRateE)
        euroPrices["fastest"] =  etherPrices["fastest"] * int(conversionRateE)
        print(euroPrices)

        return gasPrices, gweiPrices, etherPrices, dollarPrices, euroPrices
    
        
    except Exception as e:
        print(f"Error: {e}")
        return None, None, None
    

