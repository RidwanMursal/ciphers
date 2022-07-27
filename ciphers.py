import utilities

class Columnar_Transposition:
    """
    ----------------------------------------------------
    Cipher name: Columnar Transposition Cipher
    Key:         (str) a keyword
    Type:        Transposition Cipher
    Description: Constructs a table from plaintext, 
                 #columns = len(keyword)
                 Rearrange columns based on keyword order
                 Read the text vertically
                 Applies to all characters except whitespaces
    ----------------------------------------------------
    """
    
    DEFAULT_PAD = 'q'
    DEFAULT_PASSWORD = 'abcd'
    
    def __init__(self,key=DEFAULT_PASSWORD,pad=DEFAULT_PAD):
        """
        ----------------------------------------------------
        Parameters:   _key (str): default = abcd
                      _pad (str): a character, default = q
        Description:  Columnar Transposition constructor
                      sets _key and _pad
        ---------------------------------------------------
        """
        self.key = key 
        self.pad = pad 

        if self.key != self.DEFAULT_PASSWORD : self.set_key(key)
        if self.pad != self.DEFAULT_PAD : self.set_pad(pad)

        return
            
    def get_key(self):
        """
        ----------------------------------------------------
        Parameters:   -
        Return:       key (str)
        Description:  Returns a copy of columnar transposition key
        ---------------------------------------------------
        """
        return self.key 
    
    def set_key(self,key):
        """
        ----------------------------------------------------
        Parameters:   key (str): keyword
        Return:       success: True/False
        Description:  Sets key to given key
                      if invalid key --> set to default key
        ---------------------------------------------------
        """
        boolean = True 
        if (not self.valid_key(key)):
            boolean = False
            key = self.DEFAULT_PASSWORD 
        
        self.key = key 
        
        return boolean

    def __str__(self):
        """
        ----------------------------------------------------
        Parameters:   -
        Return:       output (str)
        Description:  Constructs and returns a string representation of 
                      Columnar Transposition object
                      output format:
                      Columnar Transposition Cipher:
                      key = <key>, pad = <pad>
        ---------------------------------------------------
        """
        output = "Columnar Transposition Cipher:\nkey = {}, pad = {}".format(self.key, self.pad)
        return output 
        
    def get_pad(self):
        """
        ----------------------------------------------------
        Parameters:   -
        Return:       pad (str): current padding character
        Description:  Returns a copy of current padding character
        ---------------------------------------------------
        """ 
        return self.pad
    
    def set_pad(self,pad):
        """
        ----------------------------------------------------
        Parameters:   pad (str): a padding character
        Return:       success: True/False
        Description:  Sets pad to given character
                      a pad should be a single character
                      if invalid pad, set to default value
        ---------------------------------------------------
        """
        boolean = True 
        if (not isinstance(pad, str) or len(pad) != 1):
            boolean = False 
            pad = self.DEFAULT_PAD 
        
        self.pad = pad
        return boolean 

    @staticmethod
    def valid_key(key):
        """
        ----------------------------------------------------
        Static Method
        Parameters:   key (?): an arbitrary input
        Returns:      True/False
        Description:  Check if given input is a valid Columnar Transposition key
                      A valid key is a string consisting of at least two unique chars
        ---------------------------------------------------
        """
        ascii_min = 32
        asci_max = 126
        if not isinstance(key, str) or len(key) < 2: return False 

        for i in range(len(key)-1):
            a1 = ord(key[i])
            if a1 < ascii_min or a1 > asci_max : return False 
            if key[i] != key[i+1] : return True 
        
        return 

    
    @staticmethod
    def key_order(key):
        """
        ----------------------------------------------------
        Static Method
        Parameters:   key (str)           
        Return:       key_order (list)
        Description:  Returns key order
                      Example: [mark] --> akmr --> [1,3,0,2]
                      If invalid key --> return []
                      Applies to all ASCII characters from space to ~
                      Discards duplicate characters
        ----------------------------------------------------
        """
        d = {} 
        base = " " + utilities.get_base('all') 
        new_key = ""
        # First go through text and clean duplicates 
        for element in key: 
            if element not in new_key: 
                new_key += element

        # Now populate hashmap so that it holds the index of each element as well as the order they appear in 
        for index, element in enumerate(new_key):
            d[base.index(element)] = index 
        
        # Sort the hashmap by it's key so you can extract the index
        sorted_dict = sorted(d.items())

        # Extract indexes and put them in an array 
        a = [element[1] for element in sorted_dict]

        return a

    def encrypt(self,plaintext):
        """
        ----------------------------------------------------
        Parameters:   plaintext (str)
        Return:       ciphertext (list)
        Description:  Encryption using Columnar Transposition Cipher
                      Does not include whitespaces in encryption
                      Uses padding
        Asserts:      plaintext is a string
        ----------------------------------------------------
        """
        # Clean plaintext of spaces and keep track of their indicies so you can insert them back later 
        positions_of_white_spaces = utilities.get_positions(plaintext, " ")
        plaintext = utilities.clean_text(plaintext, " ")

        # Get the amount of rows and columns needed
        length = len(plaintext)
        key_order = self.key_order(self.key) 
        col = len(key_order)
        rows = (length // col) +1

        # Populate matrix
        matrix = utilities.new_matrix(rows, col, self.pad)
        count = 0
        for i in range(rows):
            if count == len(plaintext) : break 
            for j in range(col): 
                if count < len(plaintext): 
                    matrix[i][j] = plaintext[count]
                    count += 1 
        
        # Encrypt the string
        ciphertext = "" 
        col_counter = 0 
        while col_counter < col: 
            index = key_order[col_counter]
            row_counter = 0
            while(row_counter < rows): 
                ciphertext += matrix[row_counter][index] 
                row_counter += 1
            col_counter += 1

        # Insert the spaces back into the cipher text 
        ciphertext = utilities.insert_positions(ciphertext,positions_of_white_spaces)

        return ciphertext

    def decrypt(self,ciphertext):
        """
        ----------------------------------------------------
        Parameters:   ciphertext (str)
        Return:       plaintext (list)
        Description:  Decryption using Columnar Transposition Cipher
        Asserts:      ciphertext is a string
        ----------------------------------------------------
        """
        # Clean ciphertext of spaces and keep track of their indicies so you can insert them back later 
        positions_of_white_spaces = utilities.get_positions(ciphertext, " ")
        ciphertext = utilities.clean_text(ciphertext, " ")
        
        # Get the amount of rows and columns needed
        length = len(ciphertext)
        key_order = self.key_order(self.key) 
        col = len(key_order)
        rows = length // col

        # Populate matrix and decrypt the string
        matrix = utilities.new_matrix(rows, col, self.pad)
        col_counter = 0
        string_count = 0  
        while col_counter < col and string_count < length: 
            index = key_order[col_counter]
            row_counter = 0
            while(row_counter < rows and string_count < length): 
                matrix[row_counter][index] = ciphertext[string_count]
                row_counter += 1
                string_count += 1
            col_counter += 1

        # Turn matrix into string counterpart 
        matrix[-1] = [element for element in matrix[-1] if element != self.pad]
        plaintext = utilities.matrix_to_string(matrix)

        # Insert the spaces back into the cipher text 
        plaintext = utilities.insert_positions(plaintext,positions_of_white_spaces)

        
        return plaintext

        

class Polybius:
    """
    ----------------------------------------------------
    Cipher name: Polybius Square Cipher (205-123 BC)
    Key:         tuple(start_char,size)
    Type:        Substitution Cipher
    Description: Substitutes every character with two digit number [row#][column#]
                 Implementation allows different square sizes with customized start ASCII char
                 Default square is 5x5 starting at 'a' and ending in 'y' (z not encrypted)
                 Encrypts/decrypts only characters defined in the square
    ----------------------------------------------------
    """
    
    DEFAULT_KEY = ('a',5)

    def __init__(self,key=DEFAULT_KEY):
        """
        ----------------------------------------------------
        Parameters:   _key (str): default = ('a',5)
        Description:  Polybius Cipher constructor
                      sets _key
        ---------------------------------------------------
        """
        self.key = self.DEFAULT_KEY 
        if key != self.DEFAULT_KEY : self.set_key(key)
        return

    def get_key(self):
        """
        ----------------------------------------------------
        Parameters:   -
        Returns:      key (tuple)
        Description:  Returns a copy of current key
        ---------------------------------------------------
        """
        return self.key 
    
    @staticmethod
    def valid_key(key):
        """
        ----------------------------------------------------
        Static Method
        Parameters:   key (?): an arbitrary input
        Returns:      True/False
        Description:  Check if given input is a valid Polybius key
                      A valid key is a tuple with two elements
                      First element (start_char) is a single ASCII character
                      Second element (size) is an integer
                      The start_char should be an ASCII value between space and ~
                      The size should be an integer in the range [2,9]
                      The combination of start_char and size should not result in
                      a string that is beyond the ASCII range of [' ', '~']
        ---------------------------------------------------
        """
        boolean = False
        if (len(key) == 2 and isinstance(key, tuple) and isinstance(key[0], str) and isinstance(key[1], int)):
            if (len(key[0]) == 1 and ord(key[0]) in range(32,127) and key[1] in range(2,10)): 
                if ord(key[0]) + (key[1]**2 - 1) <= 126: 
                    boolean = True 

        return boolean
    
    def get_square(self,mode='list'):
        """
        ----------------------------------------------------
        Parameters:   mode(str)= 'list' or 'string'
        Returns:      square (2D list)
        Description:  Constructs Polybius square from key
                      Square can be returned as a 2D list or
                      as a string formatted as a matrix
        Errors:       if mode is not 'list' or 'string'
                          print error_msg: 'Error(Polybius.get_square): undefined mode'
                          return empty string
        ---------------------------------------------------
        """
        if mode != "list" and mode != "string" :
            print("Error(Polybius.get_square): undefined mode")
            return 

        square = utilities.new_matrix(self.key[1],self.key[1],0)
        ascii = ord(self.key[0]) 
        string = ""

        for i in range(len(square)):
            for j in range(len(square[i])):
                square[i][j] = chr(ascii)
                ascii += 1
                if mode == "string":
                    string += square[i][j]
                    string +=  "  " 
                    if j == len(square[i]) - 1 and i != len(square) - 1: string += "\n"
            
        # Turn into string representation if mode is set to string
        if mode == "string" : square = string

        return square 
        
    
    def _get_base(self):
        """
        ----------------------------------------------------
        A private helper function that returns the characters defined
        in the Polybius square as a single string
        String begins with start_char and ends with key*key subsequent chars
        ---------------------------------------------------
        """ 
        square = self.get_square("list")
        return utilities.matrix_to_string(square)
        
    
    def set_key(self,key):
        """
        ----------------------------------------------------
        Parameters:   key (tuple)
        Returns:      success (True/False)
        Description:  Sets Polybius object key to given key
                      Does not update key if invalid key
                      Returns success status: True/False
        ---------------------------------------------------
        """
        boolean = True 
        if not self.valid_key(key): 
            boolean = False
        else: 
            self.key = key  
        return boolean
    
    def __str__(self):
        """
        ----------------------------------------------------
        Parameters:   -
        Return:       output (str): string representation
        Description:  Returns a string representation of polybius
                      Format:
                      Polybius Cipher:
                      key = <key>
                      <polybius_square in matrix format>
        ---------------------------------------------------
        """
        matrix = self.get_square("string")
        output = "Polybius Cipher:\nkey = {}\n{}".format(self.key, matrix)
        return output
    
    def encode(self,plainchar):
        """
        -------------------------------------------------------
        Parameters:   plainchar(str): single character
        Return:       cipher(str): two digit number
        Description:  Substitutes a character with corresponding two numbers
                          using the defined Polybius square
                      If character is not defined in square return ''
        Errors:       if input is not a single character --> 
                         msg: 'Error(Polybius.encode): invalid input'
                         return empty string
        -------------------------------------------------------
        """
        # Handle error cases 
        base = self._get_base()
        if plainchar not in base : return ""
        if len(plainchar) != 1 : 
            print("Error(Polybius.encode): invalid input")
            return ""
        
        # Find character in square and do correct substitution 
        square = self.get_square("list")
        i1,i2 = utilities.index_2d(square, plainchar)

        return str(i1+1) + str(i2+1)

    def decode(self,cipher):
        """
        -------------------------------------------------------
        Parameters:   cipher(str): two digit number
        Return:       plainchar(str): a single character
        Description:  Substitutes a two digit number with a corresponding char
                          using the defined Polybius square
                      If invalid two digit number return empty string
        Errors:       if input is not string composing of two digits  --> 
                         msg: 'Error(Polybius.decode): invalid input'
                         return empty string
        -------------------------------------------------------
        """
        # Handle first possible Error 
        if (not isinstance(cipher, str) or len(cipher) != 2 or not cipher.isnumeric()): 
            print("Error(Polybius.decode): invalid input")
            return "" 

        # Get square as well as valid boundries for ciphertext
        square = self.get_square("list")
        rows = len(square)
        col = len(square[0])
        i = int(cipher[0])
        j = int(cipher[1])

        # Handle second possible error
        if (i not in range(1,rows+1) or j not in range(1,col+1)) : return ""

        # Do something
        plainchar = square[i-1][j-1]

        return plainchar        
    
    def encrypt(self,plaintext):
        """
        ----------------------------------------------------
        Parameters:   plaintext (str)
        Return:       ciphertext (list)
        Description:  Encryption using Polybius cipher
                      Encrypts only characters defined in the square
        Asserts:      plaintext is a string
        ----------------------------------------------------
        """
        base = self._get_base()
        ciphertext = "" 
        for element in plaintext:
            if element in base: 
                ciphertext += self.encode(element)
            else:
                ciphertext += element 

        return ciphertext 

    def decrypt(self,ciphertext):
        """
        ----------------------------------------------------
        Parameters:   ciphertext (str)
        Return:       plaintext (list)
        Description:  decryption using Polybius cipher
                        decrypts only 2 digit numbers
        Asserts:      ciphertext is a string
        ----------------------------------------------------
        """
        plaintext = "" 
        index = 0 

        while index < len(ciphertext) - 1:
            decode_val = ciphertext[index:index+2] 
            if decode_val.isnumeric(): 
                plaintext += self.decode(decode_val)
                index += 2 
            else: 
                plaintext += ciphertext[index]
                index += 1 

        if index < len(ciphertext): 
            plaintext += ciphertext[index]  

        return plaintext 

    @staticmethod
    def cryptanalyze(ciphertext,args=['',0,0,None,0.93]):
        """
        ----------------------------------------------------
        Static method
        Parameters:   ciphertext (string)
                      args (list):
                            start_char: (str): default = ''
                            min_size: (int): default = 0
                            max_size: (int): default = 0
                            dictionary_file (str): default = None
                            threshold (float): default = 0.93
        Return:       key,plaintext
        Description:  Cryptanalysis of Polybius Cipher
                      Returns plaintext and key (start_char,size)
                      Assumes user passes a valid args list
                      Uses bruteforce for the sizes is in range [min_size,max_size]
                      The square is always located between [' ', '~'] ASCII characters
        ---------------------------------------------------
        """
        # Load dict and tester 
        args[3] = utilities.load_dictionary("engmix.txt")
        analyze = Polybius()
        if args[1] == 0 : args[1] = 2 
        if args[2] == 0 : args[2] = 9

        # Case in which size of square is known 
        if (args[1] == args[2]):
            analyze.set_key((args[0],args[1]))
            if (args[0] != ""):
                plaintext = analyze.decrypt(ciphertext) 
                return (args[0],args[1]),plaintext  

            else:
                max_start_char = 126 - (args[1]**2)
                min_start_char = 32 
                possible_start_chars = range(min_start_char, max_start_char + 1)
                for element in possible_start_chars: 
                    analyze.set_key((chr(element), args[1]))
                    plaintext = analyze.decrypt(ciphertext)
                    if utilities.is_plaintext(plaintext, args[3], args[4]) : return analyze.get_key(), plaintext
        
        else:
            if args[0] != "":  
                for i in range(args[1], args[2]+1): 
                    analyze.set_key((args[0], i)) 
                    plaintext = analyze.decrypt(ciphertext)
                    if utilities.is_plaintext(plaintext, args[3], args[4]) : return analyze.get_key(), plaintext 
            else: 
               for i in range(args[1], args[2]+1): 
                    max_start_char = 126 - (i*i)
                    min_start_char = 32 
                    possible_start_chars = range(min_start_char, max_start_char + 1)

                    for element in possible_start_chars: 
                        analyze.set_key((chr(element), i))
                        plaintext = analyze.decrypt(ciphertext)
                        if utilities.is_plaintext(plaintext, args[3], args[4]) : return analyze.get_key(), plaintext


        print("Polybius.cryptanalyze: cryptanalysis failed")
        return "", ""

class Simple_Substitution:
    """
    ----------------------------------------------------
    Cipher name: Simple Substitution Cipher
    Key:         tuple(keyword(str),base(str))
    Type:        Substitution Cipher
    Description: The base is a stream of unique characters
                 Only characters defined in the base are substituted
                 The base is case insensitive
                 The keyword is a random arrangement of the base, or some of its characters
                 The substitution string is the keyword, then all base characters
                     not in keyword, while maintaining their order in the base
                 The case of characters should be preserved whenever possible
    ----------------------------------------------------
    """
    DEFAULT_KEY = ('frozen','abcdefghijklmnopqrstuvwxyz')

    def __init__(self,key=DEFAULT_KEY):
        """
        ----------------------------------------------------
        Parameters:   _key (str)
        Description:  Simple Substitution Cipher constructor
                      sets _key
        ---------------------------------------------------
        """
        self.key = self.DEFAULT_KEY 
        if key != self.DEFAULT_KEY : self.set_key()
        return

    def get_key(self):
        """
        ----------------------------------------------------
        Parameters:   -
        Returns:      key (tuple)
        Description:  Returns a copy of current key
        ---------------------------------------------------
        """
        return self.key 
    
    @staticmethod
    def valid_key(key):
        """
        ----------------------------------------------------
        Static Method
        Parameters:   key (?): an arbitrary input
        Returns:      True/False
        Description:  Check if given input is a valid Simple Substitution key
                      The key is a tuple composing of two strings
                      The base should contain at least two unique characters
                      The keyword should have at least two unique characters defined in the base
        ---------------------------------------------------
        """
        if not isinstance(key, tuple) or len(key) != 2 or not isinstance(key[0], str) or not isinstance(key[1], str) : return False 
        if len(key[1]) < 2 or (len(key[1]) == 2 and key[1][0] == key[1][1]) : return False
        
        a = []
        for element in key[0].lower():
            if element in key[1].lower() and element not in a:
                a.append(element)
            if len(a) >= 2 : return True

        return False 
    
    def get_table(self):
        """
        ----------------------------------------------------
        Parameters:   -
        Returns:      [base,sub]
        Description:  Constructs a substitution table
                      First element is the base string
                      Second element is the substitution string 
        ---------------------------------------------------
        """
        base = self.key[1] 
        keyword = self.key[0]
        cleaned_base = utilities.clean_text(base, keyword)
        sub = keyword + cleaned_base 

        return [base, sub]
    
    def set_key(self,key):
        """
        ----------------------------------------------------
        Parameters:   key (tuple(str,str))
        Returns:      success (True/False)
        Description:  Sets Simple Substitution key to given key
                      Does not update key if invalid key
                      Stores key without duplicates in lower case
                          duplicates in base are removed
                          duplicates in keyword are removed
                          keyword chars not in base are removed
                      Returns success status: True/False
        ---------------------------------------------------
        """
        boolean = True 
        if (not self.valid_key(key)):
            boolean = False
        else: 
            new_keyword = self._remove_duplicates(key[0],key[1])
            new_base = self._remove_duplicates(key[1],key[1])
            self.key = (new_keyword, new_base)
        return boolean 

    def _remove_duplicates(self, string, base):
        """
        Private helper function which removes duplicates in a particular string 
        """
        new_string = ""
        for element in string.lower(): 
            if element not in new_string and element in base.lower():
                new_string += element 
        return new_string.lower()
    
    def __str__(self):
        """
        ----------------------------------------------------
        Parameters:   -
        Return:       output (str): string representation
        Description:  Returns a string representation of Simple Substitution
                      Format:
                      Simple Substitution Cipher:
                      keyword = <keyword>
                      <base string>
                      <sub string>
        ---------------------------------------------------
        """
        a = self.get_table()
        output = "Simple Substitution Cipher:\nkey = {}\n{}\n{}".format(self.key[0],a[0],a[1])
        return output 
    
    def encrypt(self,plaintext):
        """
        ----------------------------------------------------
        Parameters:   plaintext (str)
        Return:       ciphertext (list)
        Description:  Encryption using Simple Substitution Cipher
                      Encrypts only characters defined in base
                      Preserves the case of characters
        Asserts:      plaintext is a string
        ----------------------------------------------------
        """
        ciphertext = ""
        table = self.get_table()[1]
        for element in plaintext:
            if element.lower() not in self.key[1]:
                ciphertext += element
            else:
                is_capital = element.isupper()
                index = self.key[1].index(element.lower())

                if is_capital:
                    ciphertext += table[index].upper()
                else:
                    ciphertext += table[index]
        return ciphertext

        

    def decrypt(self,ciphertext):
        """
        ----------------------------------------------------
        Parameters:   ciphertext (str)
        Return:       plaintext (list)
        Description:  decryption using Simple Substitution Cipher
                      Decrypts only characters defined in base
                      Preserves the case of characters
        Asserts:      ciphertext is a string
        ----------------------------------------------------
        """
        plaintext = ""
        table = self.get_table()[1]
        for element in ciphertext:
            if element.lower() not in self.key[1]:
                plaintext += element
            else:
                is_capital = element.isupper()
                index = table.index(element.lower())

                if is_capital:
                    plaintext += self.key[1][index].upper()
                else:
                    plaintext += self.key[1][index]
        return plaintext

class Vigenere:
    """
    ----------------------------------------------------
    Cipher name: Vigenere Cipher
    Key:         (str): a character or a keyword
    Type:        Polyalphabetic Substitution Cipher
    Description: if key is a single characters, uses autokey method
                    Otherwise, it uses a running key
                 In autokey: key = autokey + plaintext (except last char)
                 In running key: repeat the key
                 Substitutes only alpha characters (both upper and lower)
                 Preserves the case of characters
    ----------------------------------------------------
    """
    
    DEFAULT_KEY = 'k'
    
    def __init__(self,key=DEFAULT_KEY):
        """
        ----------------------------------------------------
        Parameters:   _key (str): default value: 'k'
        Description:  Vigenere constructor
                      sets _key
                      if invalid key, set to default key
        ---------------------------------------------------
        """
        self._key = key 
        if self._key != self.DEFAULT_KEY: 
            self.set_key(key)
        return
    
    def get_key(self):
        """
        ----------------------------------------------------
        Parameters:   -
        Return:       key (str)
        Description:  Returns a copy of the Vigenere key
        ---------------------------------------------------
        """
        return self._key
       
    def set_key(self,key):
        """
        ----------------------------------------------------
        Parameters:   key (str): non-empty string
        Return:       success: True/False
        Description:  Sets Vigenere cipher key to given key
                      All non-alpha characters are removed from the key
                      key is converted to lower case
                      if invalid key --> set to default key
        ---------------------------------------------------
        """ 
        boolean = True
        if not self.valid_key(key): 
            boolean = False 
            key = self.DEFAULT_KEY
        
        key = utilities.clean_text(key, utilities.get_base("nonalpha") + " ")
        self._key = key.lower()
        return boolean
    
    def __str__(self):
        """
        ----------------------------------------------------
        Parameters:   -
        Return:       output (str)
        Description:  Constructs and returns a string representation of 
                      Vigenere object. Used for testing
                      output format:
                      Vigenere Cipher:
                      key = <key>
        ---------------------------------------------------
        """
        output = "Vigenere Cipher:\nkey = {}".format(self.get_key())
        return output
    
    @staticmethod
    def valid_key(key):
        """
        ----------------------------------------------------
        Static Method
        Parameters:   key (?):
        Returns:      True/False
        Description:  Checks if given key is a valid Vigenere key
                      A valid key is a string composing of at least one alpha char
        ---------------------------------------------------
        """
        if type(key) == str:
            for element in key: 
                if element.isalpha(): 
                    return True 
        return False

    @staticmethod
    def get_square():
        """
        ----------------------------------------------------
        static method
        Parameters:   -
        Return:       vigenere_square (list of string)
        Description:  Constructs and returns vigenere square
                      The square contains a list of strings
                      element 1 = "abcde...xyz"
                      element 2 = "bcde...xyza" (1 shift to left)
        ---------------------------------------------------
        """
        base = utilities.get_base("lower")
        string = base
        vigenere_square = []

        for element in base: 
            vigenere_square.append(string)
            string = utilities.shift_string(string, 1, "l")

        return vigenere_square

    def encrypt(self,plaintext):
        """
        ----------------------------------------------------
        Parameters:   plaintext (str)
        Return:       ciphertext (str)
        Description:  Encryption using Vigenere Cipher
                      May use an auto character or a running key
        Asserts:      plaintext is a string
        ---------------------------------------------------
        """
        assert type(plaintext) == str, 'invalid plaintext'
        
        if len(self._key) == 1:
            return self._encrypt_auto(plaintext)
        else:
            return self._encrypt_run(plaintext)

    def _encrypt_auto(self,plaintext):
        """
        ----------------------------------------------------
        Parameters:   plaintext (str)
        Return:       ciphertext (str)
        Description:  Private helper function
                      Encryption using Vigenere Cipher Using an autokey
        ---------------------------------------------------
        """
        # your code here
        return ''

    def _encrypt_run(self,plaintext):
        """
        ----------------------------------------------------
        Parameters:   plaintext (str)
        Return:       ciphertext (str)
        Description:  Private helper function
                      Encryption using Vigenere Cipher Using a running key
        ---------------------------------------------------
        """
        # First take out all non alpha characters for encryption 
        base = utilities.get_base("nonalpha") + " " + "\n"
        positions = utilities.get_positions(plaintext, base)
        plaintext = utilities.clean_text(plaintext,base)

        # Formulate key of proper length
        x = len(plaintext) // len(self._key)
        r = len(plaintext) % len(self._key)
        key_stream = self._key*x + self._key[0:r+1]

        # Encrypt
        test = ""
        vsquare = self.get_square()
        ciphertext = "" 
        key_pt = 0
        base = utilities.get_base("lower")
        for element in plaintext:
            test += element
            flag = element.isupper() 
            if element.lower() in base:
                col = base.index(element.lower())
                row = base.index(key_stream[key_pt])
                value = vsquare[row][col] 
                if flag : value = value.upper()
                ciphertext += value
                key_pt += 1  
            else: 
                ciphertext += element
                
        # Add back non alpha characters 
        ciphertext = utilities.insert_positions(ciphertext, positions)
        
        return ciphertext
    
    def decrypt(self,ciphertext):
        """
        ----------------------------------------------------
        Parameters:   ciphertext (str)
        Return:       plaintext (str)
        Description:  Decryption using Vigenere Cipher
                      May use an auto character or a running key
        Asserts:      ciphertext is a string
        ---------------------------------------------------
        """
        assert type(ciphertext) == str, 'invalid input'
        
        if len(self._key) == 1:
            return self._decryption_auto(ciphertext)
        else:
            return self._decryption_run(ciphertext)

    def _decryption_auto(self,ciphertext):
        """
        ----------------------------------------------------
        Parameters:   ciphertext (str)
        Return:       plaintext (str)
        Description:  Private Helper method
                      Decryption using Vigenere Cipher Using autokey
        ---------------------------------------------------
        """
        # your code here
        return ''

    def _decryption_run(self,ciphertext):
        """
        ----------------------------------------------------
        Parameters:   ciphertext (str)
        Return:       plaintext (str)
        Description:  Private Helper method
                      Decryption using Vigenere Cipher Using running key
        ---------------------------------------------------
        """
        # First take out all non alpha characters for encryption 
        base = utilities.get_base("nonalpha") + " " + "\n"
        positions = utilities.get_positions(ciphertext, base)
        ciphertext = utilities.clean_text(ciphertext,base)

        # Formulate key of proper length
        x = len(ciphertext) // len(self._key)
        r = len(ciphertext) % len(self._key)
        key_stream = self._key*x + self._key[0:r+1]

        # decrypt
        vsquare = self.get_square()
        plaintext = "" 
        key_pt = 0
        base = utilities.get_base("lower")

        for element in ciphertext:
            #test += element
            flag = element.isupper() 
            if element.lower() in base:
                row = base.index(key_stream[key_pt])
                index = vsquare[row].index(element.lower())
                value = base[index] 
                if flag : value = value.upper()
                plaintext += value
                key_pt += 1  
            else: 
                plaintext += element 
        
        # Add back non alpha characters 
        plaintext = utilities.insert_positions(plaintext, positions)

        return plaintext

class Ceaser_Cipher():
    _base = utilities.get_base("lower")

    def __init__(self, key): 
        self._key = key 

    def get_shifted_base(self): 
        return utilities.shift_string(self._base, self._key, "l")
    
    def encrypt(self, plaintext):
        shifted_base = self.get_shifted_base()
        print("this is the shifted base", shifted_base) 
        ciphertext = ""
        for element in plaintext: 
            ciphertext += shifted_base[self._base.find(element)]
        return ciphertext
    
    def decrypt(self, ciphertext):
        shifted_base = self.get_shifted_base()
        print("this is the shifted base", shifted_base) 
        plaintext = ""
        for element in ciphertext: 
            plaintext += self._base[shifted_base.find(element)]
        return plaintext
            



    