# Ollama RAG

**NOTE: Utilized personal laptop with 1 NVIDIA RTX 3080 in a Windows Environment**

## Prerequisites

1. **Install Linux on Windows with WSL**  
   Follow the instructions [HERE](https://learn.microsoft.com/en-us/windows/wsl/install)

2. **Install CUDA Tooling for Ubuntu on WSL2**  
   Follow the instructions [HERE](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local)

3. **Verify Drivers Installation**

   ```sh
   nvidia-smi

4. **Set Up Python Virtual Environment**
- Open VSCode
- Create and activate a Python 3.10+ virtual environment

   ```sh
   pip install -r requirements.txt

## Installing and Running Models with Ollama
1. Download Ollama
- Open WSL terminal and run the following command:

   ```sh
   curl -fsSL https://ollama.com/install.sh | sh

2. Download the Model of Your Choice
- From WSL terminal, download a model from [HERE](https://ollama.com/library)

   ```sh
   ollama run "name_of_your_model"

3. Verify Downloaded Model
- Verify the model and note its syntax (e.g., mistral:latest)

   ```sh
   ollama list

4. Determine WSL IP Address
- From WSL terminal, determine your WSL IP address (look under the **eth#** interface)

   ```sh
   ip a

## Setting Up Ollama RAG

1. Upload Data
- Open your preferred IDE, upload, and save PDFs into the data directory.

2. Modify Configuration Files
- Open VSCode and modify **chroma_client.py**:
   - Replace **"YOUR_WSL_IP_GOES_HERE"** with your WSL IP.

- Modify rag_query.py:
   - Replace **"YOUR_WSL_IP_GOES_HERE"** with your WSL IP.
   - Replace **"YOUR_OLLAMA_MODEL_GOES_HERE"** with your downloaded Ollama model.
  
3. Save All Changes

## Running the Project

1. **Initialize Docker Container**
   - Pull and initiate `chromadb/chroma` container from Docker

     ```sh
     sudo docker run -p 8000:8000 chromadb/chroma
     ```

2. **Create Vector Database**
   - Initialize the data directory containing your documents to create a vector database

     ```sh
     python chroma_client.py
     ```
   - **Note:** Each time you modify the documents in the `data` directory, re-run `chroma_client.py`.

3. **Launch Interactive RAG System**

   ```sh
   python rag_query.py

## References/Inspiration

- [Open Source Self-Hosted RAG LLM Server with ChromaDB Docker Ollama](https://medium.com/@mbrazel/open-source-self-hosted-rag-llm-server-with-chromadb-docker-ollama-7e6c6913da7a)

