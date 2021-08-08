import pandas as pd

# Load train.jsonl, dev_seen.jsonl, dev_unseen.jsonl, test_seen.jsonl, test_unseen.jsonl
train_df = pd.read_json('train.jsonl', lines=True)
dev_seen_df = pd.read_json('dev_seen.jsonl', lines=True)
dev_unseen_df = pd.read_json('dev_unseen.jsonl', lines=True)
test_seen_df = pd.read_json('test_seen.jsonl', lines=True)
test_unseen_df = pd.read_json('test_unseen.jsonl', lines=True)

# Split label 0 and label 1
def split(df):
    print(len(df[df['label'] == 0]), len(df[df['label'] == 1]))
    return df[df['label'] == 0], df[df['label'] == 1]

train_0_df, train_1_df = split(train_df)
dev_s_0_df, dev_s_1_df = split(dev_seen_df)
dev_u_0_df, dev_u_1_df = split(dev_unseen_df)
test_s_0_df, test_s_1_df = split(test_seen_df)
test_u_0_df, test_u_1_df = split(test_unseen_df)

# Merge label 0 dfs togerther as well as label 1 dfs
data_0_df = train_0_df.merge(dev_s_0_df, how='outer').merge(dev_u_0_df, how='outer').merge(test_s_0_df, how='outer').merge(test_u_0_df, how='outer')
data_1_df = train_1_df.merge(dev_s_1_df, how='outer').merge(dev_u_1_df, how='outer').merge(test_s_1_df, how='outer').merge(test_u_1_df, how='outer')

print(f'{len(data_0_df)} label 0; {len(data_1_df)} label 1')

# Export to data.jsonl
data_df = data_0_df.merge(data_1_df, how='outer')
data_df['id'] = data_df['id'].apply(lambda x: str(x).zfill(5))
data_df.to_json('data_test.jsonl', orient='records', lines=True)