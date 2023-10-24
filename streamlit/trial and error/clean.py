#### Cleaning function Kalpa:
def clean_the_text(text_1):  #input should be a series
    # Remove the unnecessary pattern starting from Û
    import re
    import pandas as pd
    import numpy as np
    new_text = []
    for j in range(len(text_1)):
        result = re.sub(r'\b[Û\\n]\w*\b', '', text_1[j].lower())
        new_text.append(result)
    
    ## Remove urls
    new_text_1 = []
    for j in range(len(new_text)):
        result = re.sub(r'http[s]?://\S+', '', new_text[j])
        new_text_1.append(result)
    
    
    ## Remove non-english 
    new_text_2 = []
    for j in range(len(new_text_1)):
        result = re.sub(r'[^\x00-\x7F]+', '', new_text_1[j])
        new_text_2.append(result)
    
    ## Remove => in text
    new_text_3 = []
    for j in range(len(new_text_2)):
        result = re.sub(r'[=>.]', '', new_text_2[j])
        new_text_3.append(result)
    
    
    ## Remove the word 'amp' which is a high frequency word in text
    new_text_4 = []
    for j in range(len(new_text_3)):
        result = re.sub(r'amp', '', new_text_3[j])
        new_text_4.append(result)

    return pd.Series(new_text_4)  ## return a series