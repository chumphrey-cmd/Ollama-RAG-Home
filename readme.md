**NOTE: Utilized personal laptop with 1 NVIDIA RTX 3080 in a Windows Environment**

Pre-requisites:
1. Install Linux on Windows with WSL [HERE](https://learn.microsoft.com/en-us/windows/wsl/install)
2. Install CUDA Tooling for Ubuntu on WSL2 [HERE](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local)
3. Verify drivers are properly installed
   > nvidia-smi

4. Open VSCode, create, and activate a python3.10+ virtual environment (NOTE: I've found that this eariler iteration works best for this project)
   > python -m venv "name_of_venv"
   > "name_of_venv"\Scripts\activate

Installing and Running Models w/ Ollama:
Open WSL terminal and run the following to download Ollama:
> curl -fsSL https://ollama.com/install.sh | sh

- From WSL terminal, download the model of your choice from [HERE](https://ollama.com/library)
> ollama run "name_of_your_model"

- Verify model you've downloaded and note the specific syntax of the model (e.g., **mistral:latest**) as it will be used to update our script later.
> ollama list

- From WSL terminal determine your WSL IP address and keep note of the IP as it will be used to update our script later (should be located under the **eth#** interface)
> ip a

3. Open IDE of your choice, upload, and save the PDFs into the **data** directory

4. Open VSCode and modify **chroma_client.py** by swapping **"YOUR_WSL_IP_GOES_HERE"** with your previous identified IP.

5. Modify **rag_query.py** by swapping **"YOUR_WSL_IP_GOES_HERE"** with your previous identified IP.

6. Modify **rag_query.py** by swapping **"YOUR_OLLAMA_MODEL_GOES_HERE"** with your previously downloaded Ollama model.

7. Save all changes

8. Pull and initiate chromadb/chroma container from Docker
   > sudo docker run -p 8000:8000 chromadb/chroma

9. Initialize the data directory containg your documents to create vector database
   > python chroma_client.py

NOTE: each time you open this RAG system or modify the documents within the "data" directory, you must re-run **chroma_client.py**

7. Launch interactive rag system.
   > rag_query.py


References/Inspiration:
- https://medium.com/@mbrazel/open-source-self-hosted-rag-llm-server-with-chromadb-docker-ollama-7e6c6913da7a
