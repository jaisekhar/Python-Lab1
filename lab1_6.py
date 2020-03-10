import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import metrics
import seaborn as sns
sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")

#Reading dataset from the file
dataset = pd.read_csv('CC.csv')

#Handling NULL Values
nulls = pd.DataFrame(dataset.isnull().sum().sort_values(ascending=False)[:5])
nulls.columns  = ['Null Count']
nulls.index.name  = 'Feature'
print(nulls)

#Selecting only Required Features
x = dataset.iloc[:,1:-1]

#Replacing null values with mean value of the specific feature column
x=x.apply(lambda x: x.fillna(x.mean()),axis=0)

#elbow method
wcss = []
for i in range(1,7):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
print(wcss)
plt.plot(range(1,7),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

#Applying Standardization and PCA
scaler = StandardScaler()
scaler.fit(x)
x_scaler=scaler.transform(x)
pca = PCA(2)
x_pca = pca.fit_transform(x_scaler)

#From elbow method choose clusters as 3
km = KMeans(n_clusters=3)
km.fit(x_pca)
y_cluster_kmeans= km.predict(x_pca)

#Calculating silhouette score
score = metrics.silhouette_score(x_pca, y_cluster_kmeans)
print(score)

#Plotting cluster
plt.scatter(x_pca[:,0],x_pca[:,1],c=y_cluster_kmeans,cmap='rainbow')
plt.show()