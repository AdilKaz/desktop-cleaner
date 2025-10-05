    # 🧹 Desktop Cleaner

    A simple Python tool to organize your messy desktop by automatically sorting files into categorized folders (e.g., **Images**, **Documents**, **Videos**, etc.).

    ---

    ## ✨ Features

    - 📁 Automatically sorts files into folders by type  
    - 💻 Works on Windows, macOS, and Linux  
    - ⚙️ Customizable file categories  
    - ⚡ Lightweight and easy to use  

    ---

    ## 🚀 Installation

    ```bash
    git clone https://github.com/AdilKaz/desktop-cleaner.git
    cd desktop-cleaner
    pip install -r requirements.txt
    ```
    ---

    ## 🧠 Usage
    
    Run the script in your terminal:
    python cleaner.py

    After running, your desktop will be neatly organized into folders like:
    
    Desktop/
    ├── Images/
    ├── Documents/
    ├── Videos/
    └── Others/

    ---

    ## 🧩 Example Configuration (optional)

    You can customize file categories inside cleaner.py:
    extension = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv'],
        'Music': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
        'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
        'Others': []
    }
    Feel free to add or remove file types as you like.

    ---

    ## 🌟 Show Your Support

    If you like this project, please give it a ⭐ on GitHub - it helps a lot!