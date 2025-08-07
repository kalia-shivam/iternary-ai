## 🌍 One-Day Travel Itinerary + AI-Generated Images (via GPT + DALL·E 3)

This serverless Python API generates a **personalized one-day itinerary** for any city you provide, and then uses **DALL·E 3** to create beautiful images representing the morning, afternoon, and evening activities.

---

### 🔧 Features

* 🧭 Generates **3-part itineraries** (Morning, Afternoon, Evening) with GPT-4
* 🎨 Creates 3 **AI-generated images** (DALL·E 3) based on the itinerary
* ☁️ Deployed on **Google Cloud Run**
* 📦 Simple API endpoint: Send a city name and get back text + 3 images
* 🛫 Great for use in travel planning apps or tourism content generators

---

### 🧪 Sample Request

**POST** `/`

**Body (JSON):**

```json
{
  "city": "Toronto, Canada"
}
```

---

### 📦 Response

```json
{
  "itinerary": "Morning: Visit the Royal Ontario Museum... Afternoon: Distillery District... Evening: CN Tower...",
  "morning_image": "https://image-link.com/...",
  "afternoon_image": "https://image-link.com/...",
  "evening_image": "https://image-link.com/..."
}
```

---

### 🗂️ Tech Stack

* Python 3.12
* OpenAI GPT-4 + DALL·E 3
* Google Cloud Run
* Flask (via Functions Framework)
* Postman for testing
