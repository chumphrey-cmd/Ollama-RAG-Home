**NOTE: Utilized personal laptop with 1 NVIDIA RTX 3080**
References:
- https://medium.com/@mbrazel/open-source-self-hosted-rag-llm-server-with-chromadb-docker-ollama-7e6c6913da7a

Pre-requisites:
1. Install Linux on Windows with WSL [HERE](https://learn.microsoft.com/en-us/windows/wsl/install)
2. Install CUDA Tooling for Ubuntu on WSL2 [HERE](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local)
3. Verify drivers are properly installed
   > nvidia-smi

Installing and Running Models w/ Ollama:
Open WSL terminaal and run the following to download Ollama:
> curl -fsSL https://ollama.com/install.sh | sh

From terminal, download the model of your choice from [HERE](https://ollama.com/library)
> ollama run <insert model of your choice here>

1. Deployed WSL2 on machine, initiated CUDA installation on WSL2, Docker package download from WSL2
2. Initiated Docker Deployment from personal laptop
3. $ sudo docker run -p 8000:8000 chromadb/chroma 
4. Initialize the vector database containing your documents.python chroma_client.py (to initialize the vector database)
5. rag_query.py (to begin RAG system)
