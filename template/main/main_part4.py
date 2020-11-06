# This is part 4 of the main procedure that calculate the similarity between
# two sources 

# %%
# Function: doc_sim
# Library
import pandas
import sklearn.feature_extraction.text
import sklearn.metrics.pairwise
# Input:
# - document_matrix, 
# - script2,
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

def average_similarity(document_matrix, mode = 'normal'):
    # Get the last column of the document_matrix
    scores = document_matrix[document_matrix.columns[-1]] 

    # Check to see if the type of tmp is 
    if scores.dtype != float:
        raise SystemExit("Incorrect 'document_matrix' used. \
            Make sure the last column of the `document_matrix` \
            is the similarity_score.")

    # Compute the average similiarty
    # We subtract 1 from the total score because the similarity score 
    #   of the first script withitself is always 1
    if mode == 'normal':
        return((sum(scores) - 1) / (len(scores) - 1))
    if mode == 'pairwise':
        return scores.mean()

def doc_sim(document_matrix, mode = 'normal', method = 'cosine', 
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
    
    # NLP Preprocessing: 
    if remove_stop_words:
        document_matrix = placeholder_remove_stop_words(document_matrix)
    if lemmatize:
        document_matrix = placeholder_lemmatize(document_matrix)
    if tfidf:
        document_matrix = placeholder_tfidf(document_matrix)
    if lsa:
        document_matrix = placeholder_lsa(document_matrix)
    if word_embedding:
        document_matrix = placeholder_word_embedding(document_matrix)

    # Main Section:
    if mode == 'normal':
               
        # Vectorize the last column of the document_matrix
        # Here the assumption is that the last column of the document_matrix
        #   contains the cleaned words
        count_vectorizer = sklearn.feature_extraction.text.CountVectorizer()
        count_matrix = count_vectorizer.\
            fit_transform(document_matrix[document_matrix.columns[-1]])
            
        # Calculate the Similarity Score
        if method == 'cosine':           
            similarity_score = sklearn.metrics.pairwise.\
                               cosine_similarity(count_matrix[0:1],
                                                 count_matrix,
                                                 dense_output = True)
            document_matrix['similarity_score'] = \
                similarity_score.reshape(-1, 1)

            # Return the output data frame
            return(document_matrix)
    
    if mode == 'pairwise':
        # Create an empty list to store the average pairwise similarity score
        scores = pandas.Series()

        # Vectorize the last column of the document_matrix
        # Here the assumption is that the last column of the document_matrix
        #   contains the cleaned words
        count_vectorizer = sklearn.feature_extraction.text.CountVectorizer()
        count_matrix = count_vectorizer.\
            fit_transform(document_matrix[document_matrix.columns[-1]])
            
        # Calculate the Similarity Score
        if method == 'cosine':
            for index, row in document_matrix.iterrows():          
                similarity_score = sklearn.metrics.pairwise.\
                                   cosine_similarity(count_matrix[index],
                                                     count_matrix,
                                                     dense_output = True)
                
                scores.at[index] = average_similarity(
                    pandas.DataFrame(similarity_score.reshape(-1, 1))
                )

                document_matrix['similarity_score'] = scores
            # Return the output data frame
            return(document_matrix)

# %% Normal Scenario Benchmark Script vs. Session Script
data = pandas.read_csv('twitter_clean.csv')
data.columns = ["DocumentID", "CoachID", 
              "Cleaned_Vectorized_Document",
              "Cleaned_Vectorized_Document_Length"]
data = data[["DocumentID", "CoachID", "Cleaned_Vectorized_Document"]]
data = doc_sim(data.iloc[0:2,])
data.head()

# %% Average Script Similarity of top 1000
data = pandas.read_csv('twitter_clean.csv')
data.columns = ["DocumentID", "CoachID", 
              "Cleaned_Vectorized_Document",
              "Cleaned_Vectorized_Document_Length"]
data = data[["DocumentID", "CoachID", "Cleaned_Vectorized_Document"]]
data = doc_sim(data.iloc[0:1000,])
average_similarity(data)

# %% Average Pairwise Similarity
data = pandas.read_csv('twitter_clean.csv')
data.columns = ["DocumentID", "CoachID", 
              "Cleaned_Vectorized_Document",
              "Cleaned_Vectorized_Document_Length"]
data = data[["DocumentID", "CoachID", "Cleaned_Vectorized_Document"]]
data = doc_sim(data.iloc[0:10000,], mode = 'pairwise') # ~ 2 mins
data.head()

# %% Within Study Transcript Similarity Average
data = pandas.read_csv('twitter_clean.csv')
data.columns = ["DocumentID", "CoachID", 
              "Cleaned_Vectorized_Document",
              "Cleaned_Vectorized_Document_Length"]
data = data[["DocumentID", "CoachID", "Cleaned_Vectorized_Document"]]
data = doc_sim(data.iloc[0:100,], mode = 'pairwise')
average_similarity(data, mode = 'pairwise')
# %% Across Study Transcript Similarity
