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
