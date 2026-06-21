import numpy as np

from fuzzywuzzy import fuzz

def extract_features(q1,q2):
    q1_len=len(q1)
    q2_len=len(q2)

    q1_words=len(q1.split())
    q2_words=len(q2.split())

    q1_set=set(q1.split())
    q2_set=set(q2.split())


    common_words=len(q1_set.intersection(q2_set))

    total_unique_words=len(q1_set.union(q2_set))

    word_share=common_words/(total_unique_words+1e-6)

    len_diff=abs(q1_len-q2_len)

    fuzz_ratio=fuzz.ratio(q1,q2)

    partial_ratio=fuzz.partial_ratio(q1,q2)

    #placeholder

    tfidf_cosine_similarity=0

    features=np.array([[
         q1_len,
        q2_len,
        q1_words,
        q2_words,
        common_words,
        total_unique_words,
        word_share,
        len_diff,
        fuzz_ratio,
        partial_ratio,
        tfidf_cosine_similarity
    ]])

    return features