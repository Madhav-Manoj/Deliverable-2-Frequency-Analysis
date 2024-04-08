import string


alphabet = string.ascii_lowercase 

def decrypt():


    message = "Wt vs vor obmhvwbu qcbtwrsbhwoz hc gom, vs kfchs wh wb qwdvsf, hvoh wg, pm gc qvobuwbu hvs cfrsf ct hvs zshhsfg ct hvs ozdvopsh, hvoh bch o kcfr qcizr ps aors cih"
    message.strip()
   
    for key in range(len(alphabet)):
     decrypted_message = ""

     for c in message:

         if c in alphabet:
             position = alphabet.find(c)
             new_position = (position - key) % 26
             new_character = alphabet[new_position]
             decrypted_message += new_character
         else:
             decrypted_message += c

    
      if 'the' in decrypted_message: 
       print(decrypted_message)
          
        

decrypt()