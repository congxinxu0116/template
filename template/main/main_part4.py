# This is part 4 of the main procedure that calculate the similarity between
# two sources 

# %% library
import pandas
import sklearn.feature_extraction.text
import sklearn.metrics.pairwise
# %% 
data = pandas.read_csv('twitter_clean.csv')
data.columns = ["DocumentID", "CoachID", 
              "Cleaned_Vectorized_Document",
              "Cleaned_Vectorized_Document_Length"]
data.head()
#%% 
count_vectorizer = sklearn.feature_extraction.text.CountVectorizer()
count_matrix = count_vectorizer.\
               fit_transform(data.Cleaned_Vectorized_Document)
#%% 
x = sklearn.metrics.pairwise.cosine_similarity(count_matrix[0:1], 
                                                 count_matrix,
                                                 dense_output = True)

# %%
df = pandas.DataFrame(data = x.reshape(len(x[0]), 1))
df.columns = ['cos_sim']
df.head()
# %%
# Function: doc_sim

# Input:
# - script1, 
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
def placeholder_remove_stop_words(x):
    return(x)

def placeholder_lemmatize(x):
    return(x)

def placeholder_tfidf(x):
    return(x)

def placeholder_lsa(x):
    return(x)

def placeholder_word_embedding(x):
    return(x)

def doc_sim(script1, script2, mode = 'normal', method = 'cosine', 
    remove_stop_words = True, lemmatize = True, tfidf = True, lsa = True, 
    word_embedding = True):

    # Check if each input has the correct type
    if mode not in ('normal', 'pairwise','cross'):
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
    
    if mode == 'normal':
        # Preprocessing: 
        if remove_stop_words:
            script1 = placeholder_remove_stop_words(script1)
            script2 = placeholder_remove_stop_words(script2)
        if lemmatize:
            script1 = placeholder_lemmatize(script1)
            script2 = placeholder_lemmatize(script2)
        if tfidf:
            script1 = placeholder_tfidf(script1)
            script2 = placeholder_tfidf(script2)
        if lsa:
            script1 = placeholder_lsa(script1)
            script2 = placeholder_lsa(script2)
        if word_embedding:
            script1 = placeholder_word_embedding(script1)
            script2 = placeholder_word_embedding(script2)

        # Vectorize 
        count_vectorizer = sklearn.feature_extraction.text.CountVectorizer()
        count_matrix = count_vectorizer.\
               fit_transform(data.Cleaned_Vectorized_Document)


    # Calculate the Similiarty Scores: 
    return 42





#%% 





doc_sim([1,2,3], [1,2,3], remove_stop_words = "0")

# %%
import pandas 

data = pandas.read_csv('https://github.com/congxinxu0116/Capstone-NLP-Edu-Interventions/blob/master/Duplicate_DocSim/corpus_clean1.csv')
data.head()
# %%
