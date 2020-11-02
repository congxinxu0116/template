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
#   - Default: True, use stop words
#   - False, does not remove stop words
# - lemmatize, binary
#   - Default: True, lemmatize all words
#   - False, disable lemmatize
# - tfidf: Term frequency-inverse document-frequency 
#   - Default: True, enable tfidf
#   - False, disable tfidf 
# - lsa: Latent Semantic Analysis
#   -- Default: True, enable lsa
#   - False, disable lsa 
# - word_embedding: Word Embedding
#   -- Default: True, enable word_embedding
#   - False, disable word_embedding 

# Output: float value from 0 to 1
# 
# Dependency:
# - Package: 
#   
# - Other functions


def doc_sim(script1, script2, mode = 'normal', method = 'cosine', 
    remove_stop_words = True, lemmatize = True, tfidf = True, lsa = True, 
    word_embedding = True):

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

    # Check if the method is coded correctly
    if method not in ('cosine'):
        raise SystemExit("Incorrect 'method' used. Use 'cosine'")
    
    # Check Hyperparameter settings: 
    if remove_stop_words not in (True, False):
        raise SystemExit("Incorrect 'remove_stop_words' used. \
                          Use True or False")
    if lemmatize not in (True, False):
        raise SystemExit("Incorrect 'lemmatize' used. Use True or False")
    if tfidf not in (True, False):
        raise SystemExit("Incorrect 'tfidf' used. Use True or False")
    if lsa not in (True, False):
        raise SystemExit("Incorrect 'lsa' used. Use True or False")
    if word_embedding not in (True, False):
        raise SystemExit("Incorrect 'word_embedding' used. Use True or False")
    
    # Preprocessing: 
    
    
    return 42





#%% 





doc_sim([1,2,3], [1,2,3], remove_stop_words = "0")

# %%
remove_stop_words = 1
remove_stop_words not in (True, False)
# %%
