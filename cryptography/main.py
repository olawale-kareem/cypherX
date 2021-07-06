import re
from art import art


# cryptography logo
print(art)

#


# alphabet bank
alphabets_bank = 'abcdefghijklmnopqrstuvwxyz'

# validation
def validation(name):
    # max encryption level
    max_encrytption_level = 10

    # take the letter input and validate
    letter = input(f"Please input the word to {name}: ")
    letter_regex_pattern = '^[\w_\W]+$'
    validate_letter = re.match(letter_regex_pattern, letter)
    while  validate_letter == None :
        letter = input(f"Wrong input,Please input the alphabets (a-z) to {name}: ")
        validate_letter = re.match(letter_regex_pattern, letter)

    # take the letter input and validate
    print("""  
           
    """)

    key = input(f"Please enter the {name} key (1 - 10): ")
    key_base_value = 0
    
    # handle general edge case for key    
    key_regex_pattern = '^[0-9\s]*$'
    validate_key = re.match(key_regex_pattern, key)
    while validate_key == None and key > str(max_encrytption_level):
        key = input(f"Wrong input,Please numbers ( 1 - 10) as {name} key: ")      
        validate_key = re.match(key_regex_pattern, key)

    # make decision based on the validated key input
    space_enter_regex_pattern = '^[\s]*$'
    space_validation = re.match(space_enter_regex_pattern,key)

    if space_validation :
        key = str(key_base_value)

    return letter , key

# encode feature
def encode():
    # operation name
    operation_name = 'encode'
    # the max index and length of the alphabets bank
    max_index_of_alphabets_bank = len(alphabets_bank)  - 1
    max_length_of_alphabets_bank = len(alphabets_bank)  
    # encoded word list
    max_encrytption_level = 10
    encoded_list = []
    display_format = ""

    # call validation  and destructure  the correct letter and encode_key
    letter, encode_key = validation(operation_name)
    
    encode_key = int(encode_key)
    # convert the input string to list
    letter_list = list(letter)
    # collect the letter one at a time for  encodeing


    for letter in letter_list:

        filteration_regex = '^[A-Z0-9_\W]+$'
        validation_filteration_regex = re.match(filteration_regex, letter)

        if validation_filteration_regex:
            returned_letter = letter
            encoded_list.append(returned_letter)      
            
        else:
            # get the id of the word from alphabet bank
            for alphabet_index in range(0, len(alphabets_bank)):
                # handles lowercase letter decode
                if letter == alphabets_bank[alphabet_index]:
                    alphabet_id = alphabet_index 
                        # the new index of the string based on the encode key
                    final_alphabet_id = alphabet_id + encode_key
                    # process the final_alphabet_id to give the right decoded word
                    if final_alphabet_id <= max_index_of_alphabets_bank:
                        encoded_word = alphabets_bank[final_alphabet_id]
                        encoded_list.append(encoded_word)
                    else:
                        adjusted_alphabet_id = final_alphabet_id - max_length_of_alphabets_bank 
                        encoded_word = alphabets_bank[adjusted_alphabet_id]
                        encoded_list.append(encoded_word)

    final_encoded_word = display_format.join(encoded_list)
    print(f"The encoded word is: {final_encoded_word}")

# decode feature   
def decode():
    # operation name
    operation_name = 'decode'
     # the max index and length of the alphabets bank
    minimum_index_of_alphabets_bank = 0
    max_length_of_alphabets_bank = len(alphabets_bank)  
    # encoded word list
    decoded_list = []
    display_format = ""

    # call validation  and destructure  the correct letter and encode_key
    letter, decode_key = validation(operation_name)
    decode_key = int(decode_key)
    # convert the input string to list
    letter_list = list(letter)
    # collect the letter one at a time for  encodeing

    for letter in letter_list:

        filteration_regex = '^[A-Z0-9_\W]+$'
        validation_filteration_regex = re.match(filteration_regex, letter)

        # return special characters
        if validation_filteration_regex:
            returned_letter = letter
            decoded_list.append(returned_letter)
        else:
            # sort the lowercase letter
            # get the id of the word from alphabet bank
            for alphabet_index in range(0, len(alphabets_bank)):
                if letter == alphabets_bank[alphabet_index]:
                    alphabet_id = alphabet_index     
                    # the new index of the string based on the encode key
                    final_alphabet_id = alphabet_id - decode_key
                    # process the final_alphabet_id to give the right decoded word
                    if final_alphabet_id < minimum_index_of_alphabets_bank:
                        adjusted_alphabet_id = final_alphabet_id + max_length_of_alphabets_bank 
                        decoded_word = alphabets_bank[adjusted_alphabet_id]
                        decoded_list.append(decoded_word)
                    else:
                        decoded_word = alphabets_bank[final_alphabet_id]
                        decoded_list.append(decoded_word)
    # finally joined the individually encoded words together   
    final_encoded_word = display_format.join(decoded_list)
    print(f"The decoded word is: {final_encoded_word}")
# cryptography
def cryptography():
    print("""
    

       """)
    cryptography_operation = input("Please enter  enter 'encode' to encode or 'decode' to decode : ").lower()
    # validation of input
    while cryptography_operation != "encode" and cryptography_operation != "decode" :
        cryptography_operation = input("Wrong input,Please enter  enter 'encode' to encode or 'decode' to decode : ").lower()
        cryptography_operation = cryptography_operation

    # slection of operation
    if cryptography_operation == "encode":
        # encode operation
        print("""  
        
        
         """)
        encode()
        print(""" 
        
        
        
          """)
        continue_operation = input("""
        Would you like to perform another cryptographic operation?: 
        Enter 'yes' to perform another operation
        Enter 'no'  to cancel
        """)
        while continue_operation != "yes" and continue_operation != "no" :
            continue_operation = input("Wrong input,please enter 'yes' to perform another operation or enter 'no' to cancel: ")
            continue_operation = continue_operation

        if continue_operation == "yes":
            print(""" 
            
            
            """)
            cryptography()
        else:
            print(" Operation cancelled, Thank you for using the cryptography app ")
    else:
        # decode operation
        decode()
        print("   ")
        continue_operation = input("""
        Would you like to perform another cryptographic operation?: 
        Enter 'yes' to perform another operation
        Enter 'no'  to cancel
        """).lower()
        while continue_operation != "yes" and continue_operation != "no" :
            continue_operation = input("Wrong input,please enter 'yes' to perform another operation or enter 'no' to cancel: ").lower()
            continue_operation = continue_operation

        if continue_operation == "yes":
            cryptography()
        else:
            print(" Operation cancelled, Thank you for using the cryptography app ")




cryptography()