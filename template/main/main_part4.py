# This is part 4 of the main procedure that calculate the similarity between
# two sources 

# Function: doc_sim

# Input:
# - script1, list
# - script2, list
# - mode:
#   - Default: 'normal'
#   - pairwise
#   - cross
# - method:
#   - Default: 'cosine'
#   - more can be added
# - remove_stop_words, binary
#   - Default: 1, use stop words
#   - 0, does not remove stop words
# - lemmatize, binary
#   - Default: 1, lemmatize all words
#   - 0, disable lemmatize


# Output: float value from 0 to 1
# 
# Dependency:
# - Package: 
#   
# - Other functions


def doc_sim(script1, script2, mode = 'normal', method = 'cosine'):

    # Check if each input has the correct type
    if mode == 'normal':
        if type(script1) is not list:
            raise SystemExit("Incorrect Type for Script 1. Use 'list'")
        if type(script2) is not list:    
            raise SystemExit("Incorrect Type for Script 2. Use 'list'")
    else if mode == 'pairwise':
        if type(script1) is not list:
            raise SystemExit("Incorrect Type for Script 1. Use 'list'")
        if type(script2) is not dict:    
            raise SystemExit("Incorrect Type for Script 2. Use 'dict'")
    else if mode == 'cross':
        if type(script1) is not dict:
            raise SystemExit("Incorrect Type for Script 1. Use 'dict'")
        if type(script2) is not dict:    
            raise SystemExit("Incorrect Type for Script 2. Use 'dict'")
    else:
        raise SystemExit("Incorrect 'mode' used. \
            Choose 'normal' or 'pairwise' or 'cross'")

    if method == 'cosine':
        return 42
    else:
        raise SystemExit("Incorrect 'method' used. Use 'cosine'")




#%% 
def doc_sim(script1, script2, mode = 'normal', method = 'cosine'):

    # Check if each input has the correct type
    if mode == 'normal':
        if type(script1) is not list:
            raise SystemExit("Incorrect Type for Script 1. Use 'list'")
        if type(script2) is not list:    
            raise SystemExit("Incorrect Type for Script 2. Use 'list'")
    elif mode == 'pairwise':
        if type(script1) is not list:
            raise SystemExit("Incorrect Type for Script 1. Use 'list'")
        if type(script2) is not dict:    
            raise SystemExit("Incorrect Type for Script 2. Use 'dict'")
    elif mode == 'cross':
        if type(script1) is not dict:
            raise SystemExit("Incorrect Type for Script 1. Use 'dict'")
        if type(script2) is not dict:    
            raise SystemExit("Incorrect Type for Script 2. Use 'dict'")
    else:
        raise SystemExit("Incorrect 'mode' used. \
            Choose 'normal' or 'pairwise' or 'cross'")

    if method == 'cosine':
        return 42
    else:
        raise SystemExit("Incorrect 'method' used. Use 'cosine'")

doc_sim(dict(),dict(), mode = 'cross', method = 'sin')


# %%
