import pandas as pd  
from sklearn.model_selection import train_test_split  # this impots a function that splits ur datset into two parts : 1.trainnig(learning) 2. testing(checking accuracy)
from sklearn.linear_model import LinearRegression  #import a ML model(LinearRegression) that learns relationships between 
from sklearn.metrics import mean_squared_error  # imports a function to measure how wrong the predictions are(smaller=better)

# Load dataset  
df = pd.read_csv('house_data.csv') # df -->  table like structure  (Example CSV with columns: area, bedrooms, location, price  inputs and output)
# Convert categorical data  
df.columns=df.columns.str.strip().str.lower()
print(list(df.columns))
df = pd.get_dummies(df, columns=['location'], drop_first=True) # get_dummies--> used for convert words--> numbers because ML model can only work with numbers and  drop_first=True-> this is for we drop one location column to avoid duplicate information
# Features & Target  
X = df.drop('price',axis=1)  # drops the price column from the data and axis=1--> means remove a column not a row  # x = input features
y = df['price']   # y= target/output value
# Split data    
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # 80%--> training and 20% --> testing,random_state=42 --> menas i run the code 1sr time it shows some value and again i run the same code it shows the same output again (unique)
# Train model  
model = LinearRegression()  
model.fit(X_train, y_train) #  The model fits(learns) from the training data
# Predict  
predictions = model.predict(X_test)  
print("MSE:", mean_squared_error(y_test, predictions))
