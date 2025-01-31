### **README.md**

# 🎙️ Speech-to-Text Transcription App

This project is a **Streamlit web app** that allows users to upload an audio file (e.g., `.mp3`, `.wav`, `.m4a`) and convert it into text using a **Whisper API**. The app is interactive and displays the transcribed text, making it easy to process audio recordings.

---

## 📋 **What the Code Does**
- The app takes an uploaded audio file and sends it to a Speech-to-Text API (such as Whisper or any similar transcription service).
- The API processes the audio and returns the transcribed text.
- The app displays the transcribed text on the web interface, with options for user review.

---

## 🚀 **How to Use It (Step by Step)**
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/speech-to-text-app.git
    cd speech-to-text-app
    ```

2. **Install dependencies:**
    Make sure you have Python installed. Then, create a virtual environment and install dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Set up the `secrets.toml` file:**
    Create a `secrets.toml` file in the root directory and add the following:
    ```toml
    [default]
    api_url = "YOUR_API_URL"
    api_key = "YOUR_API_KEY"
    ```

4. **Run the app:**
    ```bash
    streamlit run app.py
    ```

5. **Upload an audio file:**  
    Use the app interface to upload an audio file and receive the transcription.

---

## 🔍 **What Happens in Each Step**

### **1. User Uploads Audio File**
- The app’s **file uploader** lets the user select an audio file (supported formats: `.mp3`, `.wav`, `.m4a`).
- The uploaded file is shown in the interface using Streamlit’s audio player.

### **2. API Request**
- Once the user uploads the file, the app sends it to the transcription API using an HTTP POST request.
- The request includes the audio file and necessary API headers for authentication.

### **3. API Processing**
- The API processes the file and returns the transcribed text as a JSON response.
  
### **4. Displaying Results**
- If the API call is successful, the transcribed text is displayed in a text area.
- If the API call fails, an error message is shown with details of the issue.

---

## 📂 **Project Structure**
```plaintext
speech-to-text-app/
│
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies for the project
├── secrets.toml            # Contains API URL and API key (do not share publicly)
├── README.md               # Project documentation
└── .gitignore              # Ignore unnecessary files in the repo
```

---

### 📄 **Explanation of Each File**
- **`app.py`**: Main application logic. Handles user input, sends API requests, and displays the results.
- **`requirements.txt`**: Lists the required Python libraries such as Streamlit and Requests.
- **`secrets.toml`**: Stores sensitive data like API URL and API key, making it safer to manage configurations.
- **`.gitignore`**: Ensures that unnecessary files like virtual environments and sensitive secrets are not pushed to the repository.
- **`README.md`**: Documentation to help others understand and use the project.

---

## 📸 **Screenshots**
![Screenshot 2025-01-30 224207](https://github.com/user-attachments/assets/2bea5459-eb4c-49b0-a660-e0b8d80760af)


## 🤝 **Contributions**
Feel free to fork the repository and submit pull requests!
