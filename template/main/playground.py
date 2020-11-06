#%% 
documents = (
"The sky is blue",
"The sun is bright",
"The sun in the sky is bright",
"We can see the shining sun, the bright sun"
)
documents
# %%
from sklearn.feature_extraction.text \
    import CountVectorizer
import numpy
count_vectorizer = CountVectorizer()
count_matrix = count_vectorizer.fit_transform(documents)

# %%
def CalCosSim(set1, set2):
    # Create two empty lists to store 0, 1 values
    list1 = []
    list2 = [] 
    
    # Form a set containing unique words of both strings  
    set_union = set1.union(set2)  
    
    # Fill list1 and list2 with 0 and 1
    # if the word show up in set1, list1 will have a 1, 
    #   otherwise list1 will get a 0
    # if the word show up in set2, list2 will have a 1, 
    #   otherwise list2 will get a 0
    for w in set_union: 
        if w in set1: 
            list1.append(1)  
        else: 
            list1.append(0) 
        if w in set2: 
            list2.append(1) 
        else: 
            list2.append(0) 
    
    # initialize a variable store the total sum of product
    #   of each element in list1 and list2
    sum_of_product = 0

    # Get the sum of product of each element in list1 and list2
    for i in range(len(set_union)): 
        sum_of_product += list1[i] * list2[i]
    
    # Cosine formula 
    cosine = sum_of_product / float((sum(list1) * sum(list2)) ** 0.5) 
    
    # Return the cosine similarity with 4 significant digits.
    return(round(cosine, 4))

# set1 = {'david', 'likes', 'chocolate'}
# set2 = {'david', 'likes', 'dark', 'chocolate'}

# print(CalCosSim(set1, set2))
# %%

set1 = set(documents[0].split(' '))
set2 = set(documents[1].split(' '))
set3 = set(documents[2].split(' '))
set4 = set(documents[3].split(' '))

x = [CalCosSim(set1, set1),
    CalCosSim(set1, set2),
    CalCosSim(set1, set3),
    CalCosSim(set1, set4)]

# %%
from sklearn.metrics.pairwise import cosine_similarity
print('sklearn result:')
print(cosine_similarity(count_matrix[0:1], 
                        count_matrix,
                        dense_output = True))
print('hand calculation result')
print(x)
# %% Testing ---
# Create two empty lists to store 0, 1 values
list1 = []
list2 = [] 

# Form a set containing unique words of both strings  
set_union = set1.union(set3)  

# Fill list1 and list2 with 0 and 1
# if the word show up in set1, list1 will have a 1, 
#   otherwise list1 will get a 0
# if the word show up in set2, list2 will have a 1, 
#   otherwise list2 will get a 0
for w in set_union: 
    if w in set1: 
        list1.append(1)  
    else: 
        list1.append(0) 
    if w in set3: 
        list2.append(1) 
    else: 
        list2.append(0)


# %%
from scipy import sparse
A =  numpy.array([list1, list2])
A_sparse = sparse.csr_matrix(A)

similarities = cosine_similarity(A_sparse, dense_output=False)
print('pairwise dense output:\n {}\n'.format(similarities))
# %%
from scipy import sparse
A =  numpy.array([list1, list2])
A_sparse = sparse.csr_matrix(A)

similarities = cosine_similarity(A_sparse, dense_output=False)
print('pairwise dense output:\n {}\n'.format(similarities))
# %%


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