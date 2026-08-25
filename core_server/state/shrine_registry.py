shrine_data = {
    "somnath": {
        "name": "Shree Somnath Jyotirlinga",
        "city": "Prabhas Patan, Veraval",
        "image": "/static/assets/shrines/somnath.jpg",
        "coords": [20.8880, 70.4012],
        "headcount": 3480,
        "wait_time": "25 mins",
        "zones": {
            "Sanctum_Exit": {"name": "Sanctum Exit", "density": 5.2, "status": "Critical", "risk": "Red", "coords": [20.8880, 70.4012]},
            "Corridor_A": {"name": "Corridor A", "density": 3.8, "status": "Caution", "risk": "Yellow", "coords": [20.8875, 70.4018]},
            "Gate_1": {"name": "Gate 1 (Accessible)", "density": 1.2, "status": "Safe", "risk": "Green", "coords": [20.8885, 70.4005]}
        }
    },
    "dwarka": {
        "name": "Dwarkadhish Temple (Jagat Mandir)",
        "city": "Dwarka",
        "image": "/static/assets/shrines/dwarka.jpg",
        "coords": [22.2442, 68.9685],
        "headcount": 4210,
        "wait_time": "35 mins",
        "zones": {
            "Moksha_Dwar": {"name": "Moksha Dwar", "density": 4.6, "status": "Critical", "risk": "Red", "coords": [22.2442, 68.9685]},
            "Swarga_Dwar": {"name": "Swarga Dwar", "density": 2.1, "status": "Safe", "risk": "Green", "coords": [22.2447, 68.9690]}
        }
    },
    "ambaji": {
        "name": "Shree Ambaji Mata Temple",
        "city": "Banaskantha",
        "image": "/static/assets/shrines/ambaji.jpg",
        "coords": [24.3323, 72.8504],
        "headcount": 2890,
        "wait_time": "15 mins",
        "zones": {
            "Gabbar_Pathway": {"name": "Gabbar Steps Pathway", "density": 3.2, "status": "Caution", "risk": "Yellow", "coords": [24.3323, 72.8504]},
            "Main_Plaza": {"name": "Main Temple Plaza", "density": 1.4, "status": "Safe", "risk": "Green", "coords": [24.3330, 72.8510]}
        }
    },
    "pavagadh": {
        "name": "Mahakali Temple (Pavagadh Hill)",
        "city": "Panchmahal",
        "image": "/static/assets/shrines/pavagadh.jpg",
        "coords": [22.4608, 73.5284],
        "headcount": 5120,
        "wait_time": "45 mins",
        "zones": {
            "Ropeway_Chokepoint": {"name": "Ropeway Base Queue", "density": 5.8, "status": "Critical", "risk": "Red", "coords": [22.4608, 73.5284]},
            "Machi_Plateau": {"name": "Machi Staging Plateau", "density": 2.9, "status": "Caution", "risk": "Yellow", "coords": [22.4620, 73.5300]}
        }
    }
}

wristbands = {
    "TM-101": {"child": "Aarav Sharma", "guardian": "Ramesh Sharma", "phone": "+91-9876543210"}
}