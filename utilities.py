DICT_FILE = 'engmix.txt'
PAD = 'q'

'______________________________________________________________________________'

def get_base(base_type):
    """
    ----------------------------------------------------
    Parameters:   base_type (str) 
    Return:       result (str)
    Description:  Return a base string containing a subset of ASCII charactes
                  Defined base types:
                  lower, upper, alpha, lowernum, uppernum, alphanum, special, nonalpha, B6, BA, all
                      lower: lower case characters
                      upper: upper case characters
                      alpha: upper and lower case characters
                      lowernum: lower case and numerical characters
                      uppernum: upper case and numerical characters
                      alphanum: upper, lower and numerical characters
                      special: punctuations and special characters (no white space)
                      nonalpha: special and numerical characters
                      B6: num, lower, upper, space and newline
                      BA: upper + lower + num + special + ' \n'
                      all: upper, lower, numerical and special characters
    Errors:       if invalid base type, print error msg, return empty string
    ---------------------------------------------------
    """
    lower = "".join([chr(ord('a')+i) for i in range(26)])
    upper = lower.upper()
    num = "".join([str(i) for i in range(10)])
    special = ''
    for i in range(ord('!'),127):
        if not chr(i).isalnum():
            special+= chr(i)
            
    result = ''
    if base_type == 'lower':
        result = lower
    elif base_type == 'upper':
        result = upper
    elif base_type == 'alpha':
        result = upper + lower
    elif base_type == 'lowernum':
        result = lower + num
    elif base_type == 'uppernum':
        result = upper + num
    elif base_type == 'alphanum':
        result = upper + lower + num
    elif base_type == 'special':
        result = special
    elif base_type == 'nonalpha':
        result = special + num
    elif base_type == 'B6': #64 symbols
        result = num + lower + upper + ' ' + '\n'
    elif base_type == 'BA': #96 symbols
        result = upper + lower + num + special + ' \n'
    elif base_type == 'all':
        result = upper + lower + num + special
    else:
        print('Error(get_base): undefined base type')
        result = ''
    return result

'______________________________________________________________________________'

def get_language_freq(language='English'):
    """
    ----------------------------------------------------
    Parameters:   language (str): default = English 
    Return:       freq (list of floats) 
    Description:  Return frequencies of characters in a given language
                  Current implementation supports English language
                  If unsupported language --> print error msg and return []
    ---------------------------------------------------
    """
    if language == 'English':
        return [0.08167,0.01492,0.02782, 0.04253, 0.12702,0.02228, 0.02015,
                0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
                0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
                0.00978, 0.0236, 0.0015, 0.01974, 0.00074]
    else:
        print('Error(get_language_freq): unsupported language')
        return []
    
'______________________________________________________________________________'

def file_to_text(filename):
    """
    ----------------------------------------------------
    Parameters:   filename (str)
    Return:       contents (str)
    Description:  Utility function to read contents of a file
                  Can be used to read plaintext or ciphertext
    Asserts:      filename is a valid name
    ---------------------------------------------------
    """
    # Check if file name is valid
    # Open file
    # Return contents 

    assert is_valid_filename(filename), "Error (file_to_text): invalid input"
    f = open(filename, 'r')
    contents = f.read()
    f.close()
    return contents

'______________________________________________________________________________'

def text_to_file(text, filename):
    """
    ----------------------------------------------------
    Parameters:   text (str)
                  filename (str)            
    Return:       no returns
    Description:  Utility function to write any given text to a file
                  If file already exist, previous contents will be erased
    Asserts:      text is a string and filename is a valid filename
    ---------------------------------------------------
    """
    # Handle Asserts
    # Write contents to a file 
    # Close the file

    assert is_valid_filename(filename), "Error (file_to_text): invalid input"
    assert isinstance(text, str), "Error (file_to_text): invalid input"
    f = open(filename, 'w')
    f.write(text)
    f.close()
    return

'______________________________________________________________________________'

def is_valid_filename(filename):
    """
    ----------------------------------------------------
    Parameters:   filename (str)
    Return:       True/False
    Description:  Checks if given input is a valid filename 
                  a filename should have at least 3 characters
                  and contains a single dot that is not the first or last character
    ---------------------------------------------------
    """
    bool = True 
    if len(filename) < 3 or filename.count(".") != 1 or filename[0] == "." or filename[-1] == ".":
        bool = False      
    return bool

'______________________________________________________________________________'
   
def load_dictionary(dict_file=None):
    """
    ----------------------------------------------------
    Parameters:   dict_file (str): filename
                        default value = None
    Return:       dict_list (list): 2D list
    Description:  Reads a given dictionary file
                  dictionary is assumed to be formatted as each word in a separate line
                  Returns a list of lists, list 0 contains all words starting with 'a'
                  list 1 all words starting with 'b' and so forth.
                  if no parameter given, use default file (DICT_FILE)
    Errors:       if invalid filename, print error msg, return []
    ---------------------------------------------------
    """
    # Open file 
    # Loop through each line and check if new starting letter appears 
    # Add new contents accordingly

    if(dict_file != None and not is_valid_filename(dict_file)):
        print("Error (load_dictionary): invalid input")

    if dict_file == None: 
        dict_file = DICT_FILE

    f = open(dict_file, 'r', encoding="ISO-8859-15")
    dict_list = [[]]
    last_letter = "a"
    index = 0 

    for lines in f:
        line = lines.strip() 
        current_letter = lines[0] 
        if current_letter == last_letter: # Check to see if we're on the same letter
            dict_list[index].append(line) # Append to that letter's dict
        else:
            index += 1                    # If not, add a new letter to the dict and append the file line there
            dict_list.append([line])
        last_letter = current_letter
    
    f.close()

    return dict_list

'______________________________________________________________________________'

def text_to_words(text):
    """
    ----------------------------------------------------
    Parameters:   text (str)
    Return:       word_list (list)
    Description:  Reads a given text
                  Returns a list of strings, each pertaining to a word in the text
                  Words are separated by a white space (space, tab or newline)
                  Gets rid of all special characters at the start and at the end
    Asserts:      text is a string
    ---------------------------------------------------
    """
    assert isinstance(text, str)

    special = get_base("special")
    word_list1 = text.split()
    word_list = []
    string = ""


    for element in word_list1:
        string = element
        for character in element:
           if (character in special and character != "-"):
               if(len(string) != 1):
                   string = string.replace(character,"")
        if (len(string) > 0):
            word_list.append(string)

                

    return word_list

'______________________________________________________________________________'

def analyze_text(text, dict_list):
    """
    ----------------------------------------------------
    Parameters:   text (str)
                  dict_list (list)
    Return:       matches (int)
                  mismatches (int)
    Description:  Reads a given text, checks if each word appears in given dictionary
                  Returns number of matches and mismatches.
                  Words are compared in lowercase
                  Assumes a proper dict_list
    Asserts:      text is a string and dict_list is a list
    ---------------------------------------------------
    """
    # split up all the words in text using the helper function defined earlier 
    # traverse through text_list and see if eeach word is in the dict list
    #  while keeping count of how many are and how many aren't
    assert isinstance(text,str)
    assert isinstance(dict_list,list)

    matches = 0
    mismatches = 0
    word_list = text_to_words(text)

    for word in word_list:
        first_letter = word[0].lower()
        ascii_val = ord(first_letter)
        if  ascii_val < 97 or ascii_val > 122: 
            mismatches +=1 
        else:
            first_letter_index = ord(first_letter) - 97

            if word.lower() in dict_list[first_letter_index]:
                matches += 1
            else:
                mismatches += 1

    return matches, mismatches

'______________________________________________________________________________'

def is_plaintext(text, dict_list, threshold=0.9):
    """
    ----------------------------------------------------
    Parameters:   text (str)
                  dict_list (list): dictionary list
                  threshold (float): number between 0 to 1
                      default value = 0.9
    Return:       True/False
    Description:  Check if a given file is a plaintext
                  If #matches/#words >= threshold --> True
                      otherwise --> False
                  If invalid threshold, set to default value of 0.9
                  An empty text should return False
                  Assumes a valid dict_list is passed
    ---------------------------------------------------
    """
    if (threshold > 1 or threshold < 0):
        threshold = 0.9

    boolean = False 
    if (len(text) > 0):
        matches, mismatches = analyze_text(text,dict_list)
        word_list = text_to_words(text)
        if (matches/len(word_list) >= threshold):
            boolean = True
   
    return boolean

'______________________________________________________________________________'

def new_matrix(r,c,fill):
    """
    ----------------------------------------------------
    Parameters:   r: #rows (int)
                  c: #columns (int)
                  fill (str,int,double)
    Return:       matrix (2D List)
    Description:  Create an empty matrix of size r x c
                  All elements initialized to fill
                  minimum #rows and #columns = 2
                  If invalid value given, set to 2
    ---------------------------------------------------
    """
    if (r < 2):
        r = 2
    if (c < 2): 
        c = 2 

    matrix = [[fill for i in range(c)] for j in range(r)]

    return matrix

'______________________________________________________________________________'

def print_matrix(matrix):
    """
    ----------------------------------------------------
    Parameters:   matrix (2D List)
    Return:       -
    Description:  prints a matrix each row in a separate line
                  items separated by a tab
                  Assumes given parameter is a valid matrix
    ---------------------------------------------------
    """

    for i in range(len(matrix)): 
        for j in range(len(matrix[i])):
            print("{}".format(matrix[i][j]),end="	")
        print("")

    return

'______________________________________________________________________________'

def index_2d(input_list,item):
    """
    ----------------------------------------------------
    Parameters:   input_list (list): 2D list
                  item (?)
    Return:       i (int): row number
                  j (int): column number
    Description:  Performs linear search on input list to find "item"
                  returns i,j, where i is the row number and j is the column number
                  if not found returns -1,-1
    Asserts:      input_list is a list
    ---------------------------------------------------
    """
    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            if (input_list[i][j] == item):
                return i,j 

    return -1,-1
'______________________________________________________________________________'

def shift_string(s,n,d='l'):
    """
    ----------------------------------------------------
    Parameters:   text (string): input string
                  shifts (int): number of shifts
                  direction (str): 'l' or 'r'
    Return:       update_text (str)
    Description:  Shift a given string by given number of shifts (circular shift)
                  If shifts is a negative value, direction is changed
                  If no direction is given or if it is not 'l' or 'r' set to 'l'
    Asserts:      text is a string and shifts is an integer
    ---------------------------------------------------
    """
    assert isinstance(s, str)
    assert isinstance(n, int)

    if (d != 'l' and d != 'r'): # Deal with bad input
        d = 'l'
    if (d == 'l' and n<0): # Deal with negatives 
        d = 'r'
        n *= -1 
    if (d == 'r' and n<0):
        d = 'l'
        n *= -1 
    
    updated_text = ""
    index = n % len(s)

    if (d == "r"):
        updated_text = s[-index:] + s[:-index]
    else: 
        updated_text = s[index:] + s[:index]


    return updated_text

'______________________________________________________________________________'

def matrix_to_string(matrix):
    """
    ----------------------------------------------------
    Parameters:   matrix (2D List)
    Return:       text (string)
    Description:  convert a 2D list of characters to a string
                  from top-left to right-bottom
                  Assumes given matrix is a valid 2D character list
    ---------------------------------------------------
    """
    text = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            text += matrix[i][j] 
    return text

'______________________________________________________________________________'

def get_positions(text,base):
    """
    ----------------------------------------------------
    Parameters:   text (str): input string
                  base (str):  stream of unique characters
    Return:       positions (2D list)
    Description:  Analyzes a given text for any occurrence of base characters
                  Returns a 2D list with characters and their respective positions
                  format: [[char1,pos1], [char2,pos2],...]
                  Example: get_positions('I have 3 cents.','c.h') -->
                      [['h',2],['c',9],['.',14]]
                  items are ordered based on their occurrence in the text
    Asserts:      text and base are strings
    ---------------------------------------------------
    """
    positions = []
    index = 0 
    
    for element in text: 
        if element in base: 
            positions.append([element, index])
        index += 1
    return positions

'______________________________________________________________________________'

def clean_text(text,base):
    """
    ----------------------------------------------------
    Parameters:   text (str)
                  base (str)
    Return:       updated_text (str)
    Description:  Constructs and returns a new text which has
                  all characters in original text after removing base characters
    Asserts:      text and base are strings
    ---------------------------------------------------
    """
    assert isinstance(text, str)
    assert isinstance(base, str)

    updated_text = ""
    for character in text:
        if character not in base:
            updated_text += character

    return updated_text

'______________________________________________________________________________'

def insert_positions(text, positions):
    """
    ----------------------------------------------------
    Parameters:   text (str)
                  positions (list): [[char1,pos1],[char2,pos2],...]]
    Return:       updated_text (str)
    Description:  Inserts all characters in the positions 2D list (generated by get_positions)
                  into their respective locations
                  Assumes a valid positions 2d list is given
    Asserts:      text is a string and positions is a list
    ---------------------------------------------------
    """
    assert isinstance(text, str)
    assert isinstance(positions, list)

    updated_text = "" 
    p_index = 0
    t_index = 0

    for i in range(len(text) + len(positions)): 
        if (p_index < len(positions) and positions[p_index][1] == i):
            updated_text += positions[p_index][0]
            p_index += 1
        else:
            updated_text += text[t_index]
            t_index += 1

    return updated_text

'______________________________________________________________________________'

def text_to_blocks(text,b_size,padding = False,pad =PAD):
    """
    ----------------------------------------------------
    Parameters:   text (str): input string
                  block_size (int)
                  padding (bool): False(default) = no padding, True = padding
                  pad (str): padding character, default = PAD
    Return:       blocks (list)
    Description:  Create a list containing strings each of given block size
                  if padding flag is set, pad empty blocks using given padding character
                  if no padding character given, use global PAD
    Asserts:      text is a string and block_size is a positive integer
    ---------------------------------------------------
    """
    assert isinstance(text, str)
    assert isinstance(b_size, int)
    assert b_size > 0

    blocks = []
    counter = 0
    i = 0 
    s = ""

    for character in text:
        s += character 
        counter += 1 
        if (counter == b_size):
            blocks.append(s)
            counter = 0 
            s = ""
        elif (i+1 == len(text)): # Reached last element of the string and could use some padding
            blocks.append(s)
        i += 1
    
    if (padding == True and counter != 0): # Pad if required
        blocks[-1] += pad*(b_size-counter)

    return blocks

'______________________________________________________________________________'

def blocks_to_baskets(blocks):
    """
    ----------------------------------------------------
    Parameters:   blocks (list): list of equal size strings
    Return:       baskets: (list): list of equal size strings
    Description:  Create k baskets, where k = block_size
                  basket[i] contains the ith character from each block
    Errors:       if blocks are not strings or are of different sizes -->
                    print 'Error(blocks_to_baskets): invalid blocks', return []
    ----------------------------------------------------
    """
    if not isinstance(blocks,list):
        print("Error(blocks_to_baskets): invalid blocks")
        return []
    for m in range(len(blocks)):
        if (not isinstance(blocks[m],str) or len(blocks[m]) != len(blocks[0])):
            print("Error(blocks_to_baskets): invalid blocks")
            return []

    k = len(blocks[0])
    baskets = ['' for string in range(k)]

    for i in range(k):
        for j in range(len(blocks)):
            baskets[i] += blocks[j][i]

    return baskets
'______________________________________________________________________________'

def compare_texts(text1,text2):
    """
    ----------------------------------------------------
    Parameters:   text1 (str)
                  text2 (str)
    Return:       matches (int)
    Description:  Compares two strings and returns number of matches
                  Comparison is done over character by character
    Assert:       text1 and text2 are strings
    ----------------------------------------------------
    """
    assert isinstance(text1, str)
    assert isinstance(text2, str)

    matches = 0
    
    if (len(text1) >= len(text2)):
        r = len(text2)
    else:
        r = len(text1)

    for i in range(r):
        if (text1[i] == text2[i]):
            matches += 1
    return matches 
'______________________________________________________________________________'

def get_freq(text,base = ''):
    """
    ----------------------------------------------------
    Parameters:   text (str)
                  base (str): default = ''
    Return:       count_list (list of floats) 
    Description:  Finds character frequencies (count) in a given text
                  Default is English language (counts both upper and lower case)
                  Otherwise returns frequencies of characters defined in base
    Assert:       text is a string
    ----------------------------------------------------
    """
    assert isinstance(text,str)

    if (base == None): # Deafult base ie upper and lower case letters  
        base = get_base('alpha')
    
    count_list = [0 for character in base]
    index = 0
    for character in text: 
        if character in base:
            index = base.find(character)
            count_list[index] += 1
    return count_list

'______________________________________________________________________________'

def is_binary(b):
    """
    ----------------------------------------------------
    Parameters:   b (str): binary number
    Return:       True/False
    Description:  Checks if given input is a string that represent a valid
                  binary number
                  An empty string, or a string that contains other than 0 or 1
                  should return False
    ---------------------------------------------------
    """
    bool = True
    if (b == "" or not isinstance(b,str)):
        bool = False 
    else: 
        index = 0 
        while(index < len(b)):
            if (b[index] != "1" and b[index] != "0"):
                bool = False
                index = len(b)
            else:
                index += 1
    return bool

'______________________________________________________________________________'

def bin_to_dec(b):
    """
    ----------------------------------------------------
    Parameters:   b (str): binary number
    Return:       decimal (int)
    Description:  Converts a binary number into corresponding integer
    Errors:       if not a valid binary number: 
                      print 'Error(bin_to_dec): invalid input' and return empty string
    ---------------------------------------------------
    """
    decimal = ""
    if (not is_binary(b)):
        print("Error(bin_to_dec): invalid input")
    else: 
        decimal = int(b,2)
    return decimal

'______________________________________________________________________________'

def dec_to_bin(decimal,size=None):
    """
    ----------------------------------------------------
    Parameters:   decimal (int): input decimal number
                  size (int): number of bits in output binary number
                      default size = None
    Return:       binary (str): output binary number
    Description:  Converts any integer to binary
                  Result is to be represented in size bits
                  pre-pad with 0's to fit the output in the given size
                  If no size is given, no padding is done 
    Asserts:      decimal is an integer
    Errors:       if an invalid size:
                      print 'Error(dec_to_bin): invalid size' and return ''
                  if size is too small to fit output binary number:
                      print 'Error(dec_to_bin): integer overflow' and return ''
    ---------------------------------------------------
    """
    assert isinstance(decimal, int)

    binary = "" 
    t_val = "{0:b}".format(decimal)

    if (not isinstance(size, int) and size != None):
        print("Error(dec_to_bin): invalid size")
    elif (size != None and size < 1):
        print("Error(dec_to_bin): invalid size")
    elif (size != None and size < len(t_val)):
        print("Error(dec_to_bin): integer overflow")
    else: 
        if (size == None or size == len(t_val)):
            binary = t_val
        else:
            padding = size - len(t_val)
            binary += "0"*padding + t_val 

    return binary 

'______________________________________________________________________________'

def xor(a,b):
    """
    ----------------------------------------------------
    Parameters:   a (str): binary number
                  b (str): binary number
    Return:       decimal (int)
    Description:  Apply xor operation on a and b
    Errors:       if a or b is not a valid binary number 
                      print 'Error(xor): invalid input' and return ''
                  if a and b have different lengths:
                       print 'Error(xor): size mismatch' and return ''
    ---------------------------------------------------
    """
    decimal = ""
    if (not is_binary(a) or not is_binary(b)):
        print("Error(xor): invalid input")
    elif (len(a) != len(b)):
        print("Error(xor): size mismatch")
    else: 
        for i in range(len(a)):
            if (a[i] == b[i]):
                decimal += "0"
            else: 
                decimal += "1"
        decimal = int(decimal)

    return decimal

'______________________________________________________________________________'

def encode(c,code_type):
    """
    ----------------------------------------------------
    Parameters:   c (str): a character
                  code_type (str): ASCII or B6
    Return:       b (str): corresponding binary number
    Description:  Encodes a given character using the given encoding scheme
                  Current implementation supports only ASCII and B6 encoding
    Errors:       If c is not a single character:
                    print 'Error(encode): invalid input' and return ''
                  If unsupported encoding type:
                    print 'Error(encode): Unsupported Coding Type' and return ''
    ---------------------------------------------------
    """
    b = ""
    if (not isinstance(c, str) or len(c) != 1): 
        print("Error(encode): invalid input")
    elif (code_type != "ASCII" and code_type !="B6"):
        print("Error(encode): Unsupported coding type")
    elif (code_type == "ASCII"):
        ascii_dec = ord(c)
        b = dec_to_bin(ascii_dec, 8)
    else:
        base = get_base("B6")
        b6_dec = base.index(c)
        b = dec_to_bin(b6_dec,6) 

    return b

'______________________________________________________________________________'

def decode(b,code_type):
    """
    ----------------------------------------------------
    Parameters:   b (str): a binary number
                  code_type (str): ASCII or B6
    Return:       c (str): corresponding character
    Description:  Encodes a given character using the given encoding scheme
                  Current implementation supports only ASCII and B6 encoding
    Errors:       If b is not a binary number:
                    print 'Error(decode): invalid input' and return ''
                  If unsupported encoding type:
                    print 'Error(decode): unsupported Coding Type' and return ''
    ---------------------------------------------------
    """
    c = "" 
    if (not is_binary(b) or (len(b) != 8 and len(b) != 6)):
        if (b == "0100000"):
            print("Error(decode_B6): invalid input")
        else:
            print("Error(decode): invalid input")
    elif (code_type != "ASCII" and code_type !="B6"):
        print("Error(decode): unsupported coding type")
    else:
        decimal = bin_to_dec(b)
        if (code_type == "ASCII"):
            c = chr(decimal)
        else: 
            base = get_base("B6")
            c = base[decimal]
             
    return c
