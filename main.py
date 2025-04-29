import pandas as pd
from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer

df = pd.read_csv('top_rated_wines.csv')
df = df[df['variety'].notna()] # remove any NaN values as it blows up serialization
data = df.to_dict('records')
df

encoder = SentenceTransformer('all-MiniLM-L6-v2') # Model to create embeddings
# create the vector database client
qdrant = QdrantClient(":memory:") # Create in-memory Qdrant instance

# Create collection to store books
qdrant.recreate_collection(
    collection_name="top_wines",
    vectors_config=models.VectorParams(
        size=encoder.get_sentence_embedding_dimension(), # Vector size is defined by used model
        distance=models.Distance.COSINE
    )
)


# vectorize!
# Note that for Coursera we use an older way of Qdrant doing the uploads using Records instead of Points
qdrant.upload_records(
    collection_name="top_wines",
    records=[
        models.Record(
            id=idx,
            vector=encoder.encode(doc["notes"]).tolist(),
            payload=doc
        ) for idx, doc in enumerate(data) # data is the variable holding all the wines
    ]
)

# Search time for awesome wines!

hits = qdrant.search(
    collection_name="top_wines",
    query_vector=encoder.encode("A wine from Mendoza Argentina").tolist(),
    limit=3
)
for hit in hits:
  print(hit.payload, "score:", hit.score)
