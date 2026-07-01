# 😊 AI Face Emotion Detector

A real-time facial emotion recognition system built using **Python**, **OpenCV**, and **DeepFace**. The application captures live video from a webcam, detects faces, and classifies emotions such as **Happy, Sad, Angry, Fear, Surprise, Neutral,** and **Disgust** using CNN-based deep learning models.

---

## 🚀 Features

- 🎥 Real-time webcam emotion detection
- 😀 Detects multiple facial emotions
- 🧠 CNN-based emotion recognition using DeepFace
- 👤 Face detection with OpenCV
- ⚡ Fast and low-latency inference
- 🖥️ Displays detected emotion directly on the video feed

---

## 🛠️ Tech Stack

- Python
- OpenCV
- DeepFace
- NumPy

---

## 📂 Project Structure

```
AI-Face-Emotion-Detector/
│── ai_face_emotion.py
│── requirements.txt
│── README.md
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Face-Emotion-Detector.git
cd AI-Face-Emotion-Detector
```

### 2. Create a virtual environment (Optional)

```bash
python -m venv venv
```

Activate it

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install opencv-python deepface numpy
```

---

## ▶️ Run the Project

```bash
python ai_face_emotion.py
```

Allow webcam access when prompted.

---

## 🎯 How It Works

1. Captures live video from the webcam.
2. Detects faces in each frame using OpenCV.
3. Passes the detected face to the DeepFace emotion recognition model.
4. Predicts the dominant emotion.
5. Displays the emotion label above the detected face in real time.

---

## 📸 Demo

Add screenshots or a GIF of the application here.

Example:

```
images/demo.gif
```

---

## 📈 Future Improvements

- Detect multiple faces simultaneously
- Improve performance using GPU acceleration
- Display confidence scores
- Save emotion logs
- Build a Streamlit or Flask web interface
- Add emotion trend analytics

---

## 🤝 Contributing

Contributions are welcome!

Feel free to fork the repository, create a feature branch, and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Sarbani Kundu**

If you found this project useful, consider giving it a ⭐ on GitHub!
