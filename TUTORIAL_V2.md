# GenLayer Intelligent Contract Tutorial (V2)

## Overview
This guide explains how to deploy and test a simple Intelligent Contract on GenLayer.

## Steps
1. Connect wallet and add GenLayer testnet  
2. Get testnet GEN tokens  
3. Open GenLayer Studio  
4. Create a contract:

from genlayer import Contract  
class Contract(Contract):  
    def evaluate(self, input_text):  
        if "hello" in input_text.lower():  
            return "Greeting detected"  
        return "No greeting detected"

5. Deploy the contract  
6. Test with sample inputs  

## Example Prompts
- "hello world" → Greeting detected  
- "hi there" → No greeting detected  

## Common Issues
- Contract schema may fail if structure is incorrect  
- Studio error messages are limited, making debugging harder  

## Key Insight
GenLayer introduces non-deterministic execution where validator outputs may differ, requiring consensus based on agreement rather than exact replication.
