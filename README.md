# Coursera-Introduction-to-Retrieval-Augmented-Generation--RAG-
Coursera - Introduction to Retrieval Augmented Generation (RAG)

1. Project Overview: This introductory reading material.
2. Hands-on Project: The hands on project that we will work on together
3. Graded Quiz: The final assignment that you need to pass in order to finish the project successfully.
4. Learner Survey: Tell us what you thought about this guided project! 


## 1. Project Overview: This introductory reading material.
### Key Terms
**Retrieval augmented generation (RAG):** A technique in AI where a large language model accesses new or recent data outside its training set to provide better answers and improved results.  
**Vector database:** A search engine or database that stores vectorized documents, enabling more accurate information retrieval for AI models.  
**Embeddings:** Representations of text data as vectors in a high-dimensional space, allowing similarity comparisons between different pieces of text.  
**Azure AI Search:** Microsoft's cloud-based search service (formerly Azure Cognitive Services Search) that offers retrieval augmentation capabilities for large language models.  
**Comma separated value (CSV):** A common data format where values are separated by commas, used in this transcript to demonstrate RAG implementation with a vector database.  
**Pandas library:** A Python library used for data manipulation and analysis, particularly useful when working with CSV files.  
~**Qdrant:** Software used for creating an in-memory vector database search, enabling efficient text retrieval and embedding storage.  
~**Sentence transformers:** A tool to encode sentences into numerical representations (embeddings) that can be compared using cosine similarity or other distance metrics.  
**Cosine distance:** A measure of similarity between two non-zero vectors in a multi-dimensional space, often used in text analysis and information retrieval.  

---
## 2. Hands-on Project: The hands on project that we will work on together
### Managing Data for RAG Application (Wine Dataset Example)

- The example uses a **CSV file** containing wines with columns like **name**, **region**, **variety**, **rating**, and **notes**.
- The dataset has **1,365 entries**, filtered to only include wines rated **96 points and above**.
- **Python** and the **Pandas** library are used to load and manipulate the CSV.
- After loading, the data is **converted into a list of dictionaries** using the `to_dict('records')` method.
- Each dictionary maps the column names to their respective values for each wine.
- This structure (list of dicts) is necessary to **prepare data for a vector database**, where embeddings will later be created and stored for retrieval.
- The importance of using `'records'` is highlighted — without it, the format would incorrectly index data, making it unusable for the database.
---
### Building and Searching a Vector Database for Wines

- Loaded the **wine CSV** into **Pandas**, **dropping null values** to clean the dataset before serialization.
- Introduced **Qdrant** as the **vector database**, **sentence-transformers** for **embedding** (using model `all-MiniLM-L6-v2`), and **qdrant-client** for database interaction.
- Created a **collection** in Qdrant named **Top Wines**, setting **cosine distance** for similarity search, and **uploaded ~1,300 embeddings** (name, region, variety, notes).
- Noted that uploading large datasets can take time (e.g., 54 seconds for 1,300 records).
- **Performed semantic search** by encoding a query and searching the vector database, returning top matches based on the notes.
- Example searches showed relevant results like a **Cabernet Sauvignon from Napa Valley** and a **wine from Mendoza, Argentina**.
- Highlighted that this setup enables **natural language** querying and **retrieval augmentation** for large language model applications.
---
### Final Setup: Using Vector Database with LLM for Wine Recommendations

- **Loaded wines CSV again** using **Pandas**, **reduced dataset** to **700 entries** for faster upload into the database.
- Re-imported necessary libraries: **pandas**, **qdrant-client**, and **sentence-transformers** for encoding.
- **Created a new Qdrant collection** named **store-wines** and **uploaded embeddings** (~700 records), completing in **34 seconds**.
- **Defined a query**: *"Suggest me an amazing Malbec wine from Argentina"* and **searched** the vector database.
- Connected the application to a **local LLaMA-based model** (or could use OpenAI/ChatGPT/Azure APIs similarly).
- **System prompt** set the assistant persona as a **wine specialist** guiding users.
- Combined the **search results** from the vector database with **user query** and **system instructions** to generate a **final answer**.
- Example result: Recommended **Bodega Colomé Altura Máxima Malbec** from **Salta, Argentina**, rated **96**, based on retrieved vector data.
---