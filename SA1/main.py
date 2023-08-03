# Write code to understand what is difficuly level in blockchain and Print the hash.
import hashlib
import random

# SA1: User input
difficultyLevel = int(input("Set Difficulty Level: "))

# Loop to generate random hashes until a hash with the desired condition is found
while True:
    # Generate a random string
    randomString = str(random.random()).encode('utf-8')

    # Create a hash object
    hashObject = hashlib.sha256()

    # Update the hash object with the random string
    hashObject.update(randomString)

    # Get the hexadecimal representation of the hash
    hashResult = hashObject.hexdigest()

    # Check if the first two characters of the hash are "0"
    if hashResult[:difficultyLevel] == "0" * difficultyLevel:
        
        print(hashResult)
        # Exit the loop if the condition is met
        break


# Activity Flow : 
'''
The student will write code to achieve the difficulty level
The student will add the random string to the block 
( As they know from the previous learning because of avalanche effect the minimal change in the input will make a drastic change to the output ) Using method they will calculate the hash
Once they achieve the difficulty level break the loop and make the Transaction successful
'''