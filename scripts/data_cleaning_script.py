import pandas as pd
import re
from typing import List

# ----------------------------------------------------------------------
#  Define Keyword Sets
# ----------------------------------------------------------------------

# Keywords indicating AI Creation, Management, or Advanced Use (Resilient/Growing Roles)
AI_ADOPTION_KEYWORDS: List[str] = [
    'machine learning', 'deep learning', 'generative ai', 'genai', 'llm', 'nlp', 
    'computer vision', 'neural networks', 'ai ethics', 'mlops', 'ai governance', 
    'tensorflow', 'pytorch', 'scikit-learn', 'hugging face', 'keras', 'aws sagemaker', 
    'azure ml', 'google ai platform', 'prompt engineering', 'data science', 
    'predictive modeling', 'algorithm development', 'feature engineering', 
    'big data architecture', 'statistical modeling', 'ai product manager', 
    'prompt engineer', 'ai/ml engineer', 'ai designer', 'ai specialist', 
    'chatGPT', 'gemini', 'RNN', 'rnn', 'CNN', 'cnn', 'Chatbot'
]

# Keywords indicating repetitive, rules-based tasks (Vulnerable/Changing Roles)
AUTOMATION_SUSCEPTIBILITY_KEYWORDS: List[str] = [
    'robotic process automation', 'rpa', 'uipath', 'blue prism', 'automation anywhere', 
    'process mapping','workflow automation', 'data entry', 
    'data cleaning', 'data manipulation', 'routine reporting', 'ticket resolution', 
    'l1/l2 support', 'standardized query', 'maintaining legacy systems', 
    'basic troubleshooting', 'compliance checklist', 'excel macro', 
    'standard documentation', 'status reporting', 'basic data gathering', 
    'invoice processing', 'expense reporting', 'automation'
]

def classify_job_description(description: str) -> str:
    """
    This function will analyzes a single job description string and classifies its AI impact.
    """
    if pd.isna(description):
        return 'Missing Description'
    
    # Convert description to lower case for case-insensitive matching
    description_lower = str(description).lower()
    
    # Use regular expressions to count keyword occurrences
    def count_keywords(text: str, keywords: List[str]) -> int:
        count = 0
        # Create a single pattern for efficient searching (using word boundaries \b)
        pattern = r'\b(' + '|'.join(re.escape(k) for k in keywords) + r')\b'
        count = len(re.findall(pattern, text))
        return count

    # Count keywords
    adoption_count = count_keywords(description_lower, AI_ADOPTION_KEYWORDS)
    susceptibility_count = count_keywords(description_lower, AUTOMATION_SUSCEPTIBILITY_KEYWORDS)
    
    # Determine the classification based on the counts
    if susceptibility_count > adoption_count:
        return 'Automation Affected'
    elif adoption_count > susceptibility_count:
        return 'AI Adoption Affected'
    else:
        # Includes cases where both are zero or both are equal non-zero
        return 'Low AI Impact'


    
def clean_data(df):
    ''' This function will clean the data'''
    
    #Removing Time Posted field, not required for further analysis
    df_new=df.drop('Time Posted',axis=1)
    
    #Removing Null values
    df_clean=df_new.dropna()
    
    #Removing duplicates from data
    df_final=df_clean.drop_duplicates()
    
    # Removing Job Description that is not required for further analysis
    df_Final=df_final.drop('Job Description',axis=1)
    
    return df_Final
    
df=pd.read_excel(r"C:\Users\dimpu\OneDrive\Desktop\Web_Scarping_project\data\web_scraped_data.xlsx")
df.loc[:, 'AI_Impact_Category'] = df['Job Description'].apply(classify_job_description)
df1=clean_data(df)
df1.to_csv('Final_data.csv',index=False)
print("Process complete, Data saved as Final_data.csv")


