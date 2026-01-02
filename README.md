# startup-policy-copilot

A Retrieval-Augmented Generation (RAG) powered FastAPI tool is to help users query and understand Indian startup policies quickly and accurately. It uses LangChain, ChromaDB, HuggingFace embeddings, and PyTorch to perform semantic search and provide answers with source citations.

---

 Table of Contents

- Demo
- Features
- Architecture
- Tech Stack
- Project Structure
- How to Run
- API Endpoint
- Evaluation
- Author

---

 Demo

 [Watch Demo Video](https://www.loom.com/share/c43b02a7f4f8441b917138c0a9ba11fa)  

---

 Features

-  PDF Parsing: Automatically extracts text from Indian government policy PDFs.
-  Semantic Search:Uses embeddings to retrieve relevant content.
-  FastAPI Backend: Simple API for querying the documents.
-  LangChain Integration: Efficient document retrieval pipeline.
-  Evaluation Notebook: Accuracy metrics included.
-  Dockerized: Easy to build and run anywhere.

---

Architecture

  User   <---> FastAPI Endpoint   <---> LangChain Agent <--->  ChromaDB    
          
                                                ⬇
                                           HuggingFace Embeddings


Tech Stack
-Python 3.10
-FastAPI
-LangChain
-ChromaDB
-HuggingFace Transformers
-PyTorch (CPU)
-Docker



Project Structure

startup-policy-copilot/
│
├── app/                  # FastAPI app code
├── data/                 # PDF texts & Chroma vector DB
├── eval/                 # Evaluation and metrics
├── notebooks/            # Dev notebooks for loading, indexing, and evaluation
│
├── rag_api.py            # Main FastAPI app
├── requirements.txt      # Python dependencies
├── Dockerfile            # For containerizing the app
├── README.md             # You're reading this
└── LICENSE

 How to Run
 Docker (Recommended)
# Step 1: Build the image
docker build -t rag-api .

# Step 2: Run the container
docker run -p 8000:8000 rag-api
Then visit: http://127.0.0.1:8000/docs for Swagger UI.



API Endpoint

POST /ask
Query the system using a JSON payload like:
{
  "query": "What is the seed fund scheme?"
}
Successful Response:
{
  "answer": "Ministry of Commerce and Industry... \n\nSource: Guidelines for Startup India Seed Fund Scheme.txt"
}


Evaluation
The system was evaluated on 20 user queries from actual policy questions.

Metric	Value
Accuracy	90%
Citation Correctness	100%
Avg. Latency	< 1 sec/query
Fail Cases	3/20


Author
Nivedita Sharma
ICT Engineering | Passionate about AI for Public Good
niveditasharma28

License
This project is licensed under the MIT License.

 
Acknowledgements
Thanks to the Maarga Systems Internship Team and the creators of LangChain, FastAPI, and ChromaDB for enabling this learning opportunity.




