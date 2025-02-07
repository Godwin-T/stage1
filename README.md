# Number Analysis Toolkit 
**HNGx Stage One Project**

[![HNG Stage One](https://img.shields.io/badge/HNG-Stage%20One-blue)](https://hng.tech/internship)

A Python utility for performing various number analysis operations, developed for Stage One of the HNG12 Internship program.

## ✨ Features
- Check if a number is Armstrong
- Prime number verification
- Perfect number detection
- Digit sum calculation
- Odd/Even classification
- Fun facts about numbers

## 🚀 Installation
```bash
git clone https://github.com/yourusername/number-analysis-toolkit.git
cd number-analysis-toolkit
pip install -r requirements.txt
```

## 🌐 API Endpoint
`GET /api/analyze/{digit}`

**Example Request:**
```bash
curl http://localhost:5000/api/analyze/7
```

**Example Response:**
```json
{
    "armstrong": false,
    "even": false,
    "fun_fact": "7 is the number of days in a week",
    "number": 7, 
    "perfect": false,
    "prime": true,
    "sum_of_digits": 7
}
```

## 💻 Usage
```python
from main import main

# Get analysis for a single digit
result = main(7)
print(result)
```

## 📝 Function Overview
```python
def is_armstrong(n):      # Checks Armstrong number status
def is_prime(n):          # Verifies prime numbers  
def is_perfect_number(n): # Identifies perfect numbers
def sum_of_digits(n):     # Calculates digit sums
def is_odd_or_even(n):    # Determines parity
def get_funfact(digit):   # Returns interesting facts
```

## 🤝 Contributing
This project is part of the [HNG Internship](https://hng.tech/internship). For stage one contributions, please follow the program guidelines.

## 📄 License
MIT License © 2025 HNGx Internship Program
