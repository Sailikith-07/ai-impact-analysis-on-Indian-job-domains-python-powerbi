import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer


df=pd.read_csv(r'C:\Users\dimpu\OneDrive\Desktop\Web_Scarping_project\data\final_file.csv')
data=df.drop(['Job Title','Company Name','No of Applications'],axis='columns')  

location_filter=df.groupby('Location').agg({'AI_Impact_Category':'count'}).sort_values(by='AI_Impact_Category',ascending=False).reset_index().head(11)
location=location_filter['Location']
location.drop(6,inplace=True)

Industry_filter=df.groupby('Industry').agg({'AI_Impact_Category':'count'}).sort_values(by='AI_Impact_Category',ascending=False).reset_index().head(10)
industry=Industry_filter['Industry']

Experience_level_filter=df.groupby('Experience Level').agg({'AI_Impact_Category':'count'}).sort_values(by='AI_Impact_Category',ascending=False).reset_index().head(15)
experience=Experience_level_filter['Experience Level']

Domain_filter=df.groupby('Domain').agg({'AI_Impact_Category':'count'}).sort_values(by='AI_Impact_Category',ascending=False).reset_index().head(15)
domain=Domain_filter['Domain']

data_df=data[(data['Location'].isin(location)) & (data['Industry'].isin(industry)) & (data['Experience Level'].isin(experience)) & (data['Domain'].isin(domain))]



# For description extraction
df1=pd.read_excel(r'C:\Users\dimpu\OneDrive\Desktop\Web_Scarping_project\web_scraped_data_modified.xlsx')
# cleaning
df1.drop('Time Posted',axis='columns',inplace=True)
df_clean=df1.dropna()
df1_final=df_clean.drop_duplicates()

final=df1_final[(df1_final['Location'].isin(location)) & (df1_final['Industry'].isin(industry)) & (df1_final['Experience Level'].isin(experience)) & (df1_final['Domain'].isin(domain))]


x=final.drop(['Job Title','Company Name','No of Applications'],axis='columns')

le=LabelEncoder()
data_df['AI_Impact_Category_n']=le.fit_transform(data_df['AI_Impact_Category'])
y=data_df['AI_Impact_Category_n']



# Preprocessing and pipeline creation
CATEGORICAL_FEATURES = ['Domain', 'Location', 'Industry', 'Experience Level']
TEXT_FEATURE = 'Job Description'

preprocessor = ColumnTransformer(
    transformers=[
        # Transformer 1: Categorical Columns (use handle_unknown='ignore' to safely manage new, unseen categories)
        ('cat', OneHotEncoder(handle_unknown='ignore'), CATEGORICAL_FEATURES),
        
        # Transformer 2: Text Column (reuse your TF-IDF settings)
        ('tfidf', TfidfVectorizer(max_features=5000, stop_words='english'), TEXT_FEATURE)
    ],
    remainder='drop' # Drop any other columns not listed
)

#  Create the full pipeline (Preprocessing + Model)
full_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', DecisionTreeClassifier()) 
]) 


    
#Training Model
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42,stratify=y)

full_pipeline.fit(X_train, y_train)

# Check score
print("Pipeline Accuracy:", full_pipeline.score(X_test, y_test))    

    
# User Input
domain=input('Enter Domain :')
location=input('Enter preferred location :')
industry=input('Enter preferred Industry :')
experience=input('Experience Level :')
text_input = input(f'Describe about {domain} role (skills,tools or else paste Job Description). Max 500 Words :')
 
Domain = []
Domain.append(domain)
Location=[]
Location.append(location)
Industry=[]
Industry.append(industry)
Experience=[]
Experience.append(experience)
new_text_input=[]
new_text_input.append(text_input)


new_cat_data = {
    'Location': Location,
    'Experience Level': Experience,
    'Industry': Industry,
    'Domain': Domain,
    'Job Description' : new_text_input
}

# 3. Convert categorical data to a DataFrame
new_job_data = pd.DataFrame(new_cat_data)

prediction_array = full_pipeline.predict(new_job_data)

print(prediction_array)

