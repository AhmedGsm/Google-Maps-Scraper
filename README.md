# 🌍 Places Finder - Google Maps Lead Scraper & Email Enricher
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![PySide6](https://img.shields.io/badge/PySide6-6.x-green.svg)](https://doc.qt.io/qtforpython/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-orange.svg)](https://www.selenium.dev/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-lightgrey.svg)](https://www.mysql.com/)
[![APIs](https://img.shields.io/badge/APIs-Hunter.io%20%7C%20Snov.io-purple.svg)](https://hunter.io)

> **Automate B2B lead generation with a powerful desktop application.** Scrape verified business listings from Google Maps, enrich them with professional emails via integrated APIs, and manage everything through a sleek, multi-language Qt6 interface. Built for sales teams, marketers, and data analysts.

---

## ✨ Key Features
| Feature | Description |
|---------|-------------|
| 🗺️ **Google Maps Scraping** | Extracts business name, address, phone, website, and direct Maps links with infinite scroll automation |
| 📧 **Email Enrichment** | Auto-finds verified contact emails via **Hunter.io** & **Snov.io** with intelligent fallback & rotation |
| 🖥️ **Modern Desktop GUI** | Built with **PySide6 (Qt6)** featuring a responsive dashboard, real-time results table, and live message logs |
| 🔐 **License & Credit System** | Remote validation, MAC address binding, trial limits, and per-query credit tracking |
| 🌐 **Multi-Language UI** | Supports English, French, and Arabic with dynamic `.qm` translation loading |
| 🌍 **Multi-Browser Engine** | Chrome, Firefox, and Edge support with memory-optimized fast-scraping profiles (images/plugins disabled) |
| 💾 **MySQL Integration** | Structured data storage, duplicate prevention, and optional upsert logic |
| 📥 **One-Click CSV Export** | Instantly download scraped & enriched lead lists to your system's Downloads folder |
| ⚡ **Threaded Execution** | Non-blocking UI with background Selenium threads and safe start/stop controls |

---

## 🏗️ Architecture & Workflow
```
User opens Places Finder Desktop App
        ↓
[Registration] → Validates via Remote API → Binds MAC Address → Grants Credits
        ↓
User enters Search Query & List Name → Clicks "Start Searching"
        ↓
[Selenium Engine] launches optimized browser → Navigates Google Maps
        ↓
[Scrollable Module] triggers infinite scroll → Extracts DOM elements
        ↓
[Data Extraction] → Name, Address, Phone, Website, Maps URL
        ↓
[Email Finder] → Queries Hunter.io → Fallback to Snov.io → Rotates API keys
        ↓
[MySQL Model] → Inserts/Updates records → Prevents duplicates
        ↓
[PySide6 UI] → Updates table in real-time → Logs progress → Decrements credits
        ↓
User clicks "Export List" → Saves to CSV → Ready for CRM/Outreach
```

---

## 🛠️ Tech Stack
| Layer | Technologies |
|-------|--------------|
| **GUI Framework** | PySide6 (Qt6), Qt Designer (`.ui`), `pyside6-uic` |
| **Scraping Engine** | Selenium 4.x, Custom `DriverManipulator`, DOM cleanup scripts |
| **Data Storage** | MySQL 8.0, `mysql-connector-python`, Structured schema |
| **Email Enrichment** | Hunter.io API, Snov.io API (OAuth2), Recursive key rotation |
| **Licensing & Auth** | Remote PHP/Node API, MAC address binding, Credit tracking |
| **Concurrency** | Python `threading`, Non-blocking Qt event loop |

---

## 📦 Installation & Setup

### 1️⃣ Prerequisites
- Python `3.8` or higher
- MySQL Server (running locally or remotely)
- Valid API keys for **Hunter.io** and/or **Snov.io**
- Browser drivers installed (`chromedriver`, `geckodriver`, or `msedgedriver`)

### 2️⃣ Quick Start
```bash
# Clone repository
git clone https://github.com/yourusername/places-finder.git
cd places-finder

# Create & activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install pyside6 selenium mysql-connector-python requests

# Run the desktop application
python main_window.py
```

### 3️⃣ Database Configuration
1. Create a MySQL database named `googlemaps`
2. Ensure the tables `places` and `localusers` exist (or let the app auto-create them on first run)
3. Update database credentials in `constants.py`:
```python
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "your_password"
MYSQL_DATABASE = "googlemaps"
```

### 4️⃣ API & Licensing Setup
- Add your Hunter.io/Snov.io keys to `HUNTER_API_KEYS_LIST` and `SNOV_API_KEYS_LIST` in `constants.py`
- Point `api_endpoint` in `constants.py` to your license management server
- The app handles MAC binding, credit deduction, and trial limits automatically

---

## 📁 Project Structure
```
places-finder/
├── main_window.py          # PySide6 entry point & main application logic
├── Ui_MainWindow.py        # Auto-generated Qt UI layout
├── Ui_DialogAbout.py       # Auto-generated "About" dialog
├── dialog_about.py         # About dialog controller
├── resources_rc.py         # Compiled Qt resources (icons, SVGs)
├── drivermanipulator.py    # Cross-browser Selenium setup & fast-scraping profiles
├── scrollable.py           # Infinite scroll automation & DOM memory cleanup
├── wsite.py                # Core scraping orchestrator, place extraction & CSV export
├── finder.py               # Hunter.io API wrapper with key rotation
├── snovio_finder.py        # Snov.io API wrapper with OAuth2 token handling
├── model.py                # MySQL connection pool, CRUD operations, duplicate handling
├── register_API.py         # User registration payload builder
├── requestAPI.py           # License manager client (check, update, delete)
├── license.py              # Local credit tracking & trial enforcement
├── constants.py            # Centralized config, timeouts, selectors, API keys
├── requirements.txt        # Python dependencies
├── UI/                     # Original Qt Designer files (.ui)
└── translations/           # Compiled .qm translation files (en, fr, ar)
```

---

## ⚙️ Configuration Reference

### Key Constants (`constants.py`)
| Constant | Purpose |
|----------|---------|
| `PARENT_SCROLLABLE_SELECTOR` | CSS selector for Google Maps infinite scroll container |
| `PLACE_CONTAINER_SELECTOR` | Selector for individual business cards in the results list |
| `WAIT_ELEMENT_To_APPEAR` | Selenium explicit wait timeout (seconds) |
| `SCRAPE_PLACES_INTERVAL` | Delay between processing each lead (prevents rate limits) |
| `FREE_CREDITS` | Default trial queries granted on first registration |
| `TABLE_WIDGET_SIZE` | Max rows allocated in the PySide6 results table |

### Database Schema (`googlemaps.places`)
Stores scraped & enriched leads:
```sql
project_name, place_url, short_url, name, address, phone, website,
email, email_type, email_confidence, first_name, last_name, position,
seniority, department, linkedin, twitter, phone_number, 
verification_date, email_status
```

---

## 🚀 Usage Guide

### 🔹 Step 1: Registration
1. Open the app → Navigate to the **Register** tab
2. Enter your **Name**, **Email**, and **Phone**
3. Click **Register** → App binds your MAC address and allocates initial credits
4. Switch to the **Search** tab to begin

### 🔹 Step 2: Running a Search
1. Enter a **List Name** (e.g., `Dentists_Paris`)
2. Enter your **Google Maps Query** (e.g., `Dentists in Paris`)
3. Click **Start Searching**
4. Watch real-time extraction in the results table & message log
5. Click **Stop Searching** anytime to safely terminate browsers

### 🔹 Step 3: Export & Manage
- **Export CSV:** Click the 💾 save icon → Choose location → Download lead list
- **Check Credits:** View remaining queries, license type, and expiration date in the user info panel
- **Change Language:** Use the top menu: `Languages → English / Français / العربية`

---

## 💡 Troubleshooting

| Issue | Solution |
|-------|----------|
| `Selenium WebDriverException` | Ensure browser drivers match your installed browser version. Run `pip install webdriver-manager` or manually update drivers. |
| `MySQL Connection Refused` | Verify `MYSQL_HOST`, `MYSQL_USER`, and `MYSQL_PASSWORD` in `constants.py`. Ensure MySQL service is running. |
| `No Emails Found` | Check Hunter.io/Snov.io API keys in `constants.py`. Ensure business has a valid website domain. |
| `License Expired / No Credits` | Contact your license provider to top up. The app auto-blocks scraping when credits hit `0`. |
| `UI Freezes During Scraping` | Normal behavior if thread isn't yielding. The app uses `QApplication.processEvents()` implicitly; avoid heavy operations on the main thread. |
| `DOM Memory Leak / Slowdown` | The `scrollable.py` module automatically deletes processed elements from the DOM. If issues persist, restart the app. |

---

## 🔐 Security & Best Practices
- ✅ **MAC Address Binding:** Prevents license sharing across devices
- ✅ **API Key Rotation:** Automatically cycles through multiple Hunter.io/Snov.io keys to avoid rate limits
- ✅ **Fast-Scraping Profiles:** Blocks images, plugins, and notifications to reduce bandwidth & fingerprinting
- ✅ **Input Validation:** RFC 5322 email validation, phone format checking, and sanitized SQL queries
- ✅ **Local Credential Storage:** Database credentials are centralized in `constants.py` (use `.env` in production)

> ⚠️ **Production Note:** For commercial deployment, move API keys and DB credentials to environment variables or a secure config manager. Never commit `constants.py` with live keys to public repositories.

---

## 🤝 Contributing
We welcome improvements! Please follow these steps:
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-idea`
3. Make changes and test locally
4. Commit with clear messages: `git commit -m 'feat: add export to JSON'`
5. Push and open a Pull Request

### Development Tips
- Edit UI in Qt Designer → Recompile with: `pyside6-uic main.ui -o Ui_MainWindow.py`
- Update translations: `lupdate *.py -ts translations/app_ar.ts` → `lrelease *.ts`
- Mock API responses during dev to avoid credit consumption

---

## 📄 License
Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

---

> 📬 **Support & Feedback**  
> Found a bug? Need custom API integrations or CRM sync?  
> → [Open an Issue](https://github.com/yourusername/places-finder/issues)  
> → Or reach out via email for enterprise licensing & support.

*Built for sales automation. Designed for precision. Powered by open-source tech.* 🌟
