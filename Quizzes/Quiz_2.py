#Create the following purchases data. Using the Apriori - FB Growth Algorithms find the association rules with support 20% confidence 70% and lift > 1 The table: 
#Trans ID [101, 102, 103, 104, 105, 106, 107, 108, 109,110] Items Purchased [(milk, bread, eggs), 
#(milk, juice), (juice, butter), (milk, bread, eggs), (coffee, eggs), (coffee), (coffee, juice), (milk, bread, cookies, eggs), (cookies, butter), (milk, bread)]

# Import Important Packages
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Create a DataFrame for the purchase transactions
data = {
    'Trans ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Items Purchased': [['milk', 'bread', 'eggs'], ['milk', 'juice'], ['juice', 'butter'],
                        ['milk', 'bread', 'eggs'], ['coffee', 'eggs'], ['coffee'],
                        ['coffee', 'juice'], ['milk', 'bread', 'cookies', 'eggs'],
                        ['cookies', 'butter'], ['milk', 'bread']]
}

df = pd.DataFrame(data)

# Convert items into one-hot encoded format
te = TransactionEncoder()
te_ary = te.fit(df['Items Purchased']).transform(df['Items Purchased'])
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

# Find frequent itemsets with Apriori algorithm
frequent_itemsets = apriori(df_encoded, min_support=0.2, use_colnames=True)

# Find association rules meeting the criteria
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
rules = rules[rules['lift'] > 1]

print("Association Rules:")
print(rules)