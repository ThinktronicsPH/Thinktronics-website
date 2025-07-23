# 📝 Contract Generator API

A Flask-based API that generates `.docx` contract agreements dynamically based on user input. Ideal for research project developers, academic capstones, and freelance teams who need structured contracts with detailed project feature breakdowns.

---

## 🚀 Features

- 🔧 Fillable contract using `{{placeholders}}`
- 📄 Exports to `.docx` with dynamic content
- ✅ Supports nested project features (e.g. parent + sub-feature bullets)
- 🔒 No external service required
- 🔁 Future-proof: Easily extend with new fields

---

## 🗂️ Project Structure

project_root/
├── run.py
├── app/
│ ├── service.py # Generates and fills .docx
│ ├── generated_docs/ # Output folder for generated contracts
│ └── doc_templates/
│ └── Contract-Template.docx # Main .docx template with placeholders
| └──


## How to Run

```bash
pip install -r requirements.txt
python run.py
```

## API Test

Visit: `http://127.0.0.1:5000/ping` -> should return `{ "message": "pong" }`



## Testing Request

/generate_contract

**POST** `/generate-contract`

**Request Body Example (JSON):**

```json
{
  "agreement_date": "August 5, 2025",
  "client_names": "Carlos Tan",
  "service_providers": "Engr. Santos",
  "project_title": "Smart Farming System",
  "total_cost": "₱80,000",
  "down_payment": "₱40,000",
  "remaining_cost": "₱40,000",
  "deadline_date": "October 1, 2025",
  "project_description": [
    {
      "title": "Sensor System",
      "features": ["Soil moisture", "Temperature", "Humidity"]
    },
    {
      "title": "Water Pump Control",
      "features": ["Auto schedule", "Manual override via app"]
    },
    {
      "title": "Mobile Dashboard",
      "features": ["Live sensor feed", "Pump controls", "Warning alerts"]
    }
  ]
}
```


