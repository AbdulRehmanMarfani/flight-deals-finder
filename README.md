Alright — here’s your **full beginner-friendly README** with the complete setup instructions for **Sheety** and **Amadeus** included.

---

## **Flight Deals Finder**

### **Description**

Flight Deals Finder is a Python-based tool that helps users track and find cheap flights for specific destinations. It uses the **Sheety API** to store destination data and lowest prices, and the **Amadeus API** to retrieve IATA airport codes and search for the best available flight offers. The program compares real-time flight prices with a user-defined threshold and displays results in the terminal (with an option to send notifications).

---

### **Features**

* Retrieve and store destination data using **Sheety API**.
* Automatically fetch and update **IATA airport codes** for each destination.
* Search for the best available **round-trip flights** using the Amadeus API.
* Compare flight prices against a predefined lowest price.
* Display found deals with flight details in the console.
* Ready for integration with email or SMS notifications.

---

### **Prerequisites**

* Python 3.8 or above
* An Amadeus Developer account with **API key** and **API secret**
* A Sheety project with a Google Sheet for storing destinations and prices
* (Optional) Twilio account for SMS notifications
* Installed dependencies from `requirements.txt`

---

### **Installation**

1. Clone this repository:

```bash
git clone https://github.com/AbdulRehmanMarfani/flight-deals-finder.git
cd flight-deals-finder
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate      # For Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add:

```
AMADEUS_API_KEY=your_amadeus_api_key
AMADEUS_API_SECRET=your_amadeus_api_secret
SHEETY_TOKEN=your_sheety_token
```

---

### **Sheety Setup**

1. Go to [https://sheety.co](https://sheety.co) and log in with your Google account.
2. Create a new project linked to a Google Sheet.
3. Name the sheet `prices` and create the following columns:

   * **city** — Destination city name
   * **iataCode** — Leave blank initially (will be auto-filled by the program)
   * **lowestPrice** — Your price threshold for a good deal
4. In Sheety, enable authentication for your project and copy your **Bearer Token** into your `.env` file as `SHEETY_TOKEN`.
5. Copy your project’s API endpoint (looks like `https://api.sheety.co/xxxx/flightDeals/prices`) into the `sheety_endpoint` variable in `main.py`.

---

### **Amadeus API Setup**

1. Sign up at [https://developers.amadeus.com](https://developers.amadeus.com).
2. Create a new application in your Amadeus dashboard.
3. Set the environment to **Test** mode (for free use).
4. Copy your **API Key** and **API Secret** into your `.env` file:

```
AMADEUS_API_KEY=your_api_key_here
AMADEUS_API_SECRET=your_api_secret_here
```

5. The API endpoint for test mode is:

```
https://test.api.amadeus.com
```

---

### **Usage**

1. Make sure your `.env` file is configured correctly.
2. Run the program:

```bash
python main.py
```

3. The program will:

   * Retrieve your destination data from Sheety
   * Fetch and update missing IATA codes
   * Search for flights from Karachi to each destination
   * Print deals that are below your `lowestPrice`

---

### **Example Output**

```
Flight found from KHI to LHR for 320.00 GBP on 2025-09-14T08:15
Flight found from KHI to DXB for 150.00 GBP on 2025-10-01T05:30
```

---

### **File Structure**

```
flight-deals-finder/
│
├── main.py                 # Main program logic
├── data_manager.py         # Handles Sheety API requests
├── flight_data.py          # Gets IATA codes & API tokens from Amadeus
├── flight_search.py        # Searches for flights via Amadeus
├── notification_manager.py # Placeholder for notifications
├── requirements.txt        # Python dependencies
└── README.md               # Documentation
```

---

### **Future Improvements**

* Add Twilio SMS or email notifications for new deals
* Store flight search results in Google Sheets for history
* Add filters for airlines, number of stops, and travel class

