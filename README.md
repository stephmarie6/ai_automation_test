import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Sample task dataset
data = {'Task': ['Prepare presentation', 'Reply to emails', 'Workout'],
        'Deadline': [2, 1, 5],  # Days left
        'Urgency': [5, 3, 2]}  # 1-5 scale
df = pd.DataFrame(data)

# Scaling features
scaler = StandardScaler()
X = scaler.fit_transform(df[['Deadline', 'Urgency']])

# Model (Train a simple classifier)
model = RandomForestClassifier()
y = [1, 2, 3]  # Priority ranking (1 = high)
model.fit(X, y)

# Predict task priority
df['Priority'] = model.predict(X)
print(df.sort_values('Priority'))
