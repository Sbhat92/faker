from .. import Provider as AddressProvider


class Provider(AddressProvider):
    # City and States names taken from wikipedia
    # Street format taken from some common famous places in India
    # Link for cities: https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population
    # Link for States: https://en.wikipedia.org/wiki/States_and_union_territories_of_India
    # Links for street name formats: https://www.mumbai77.com/city/3313/travel/old-new-street-names/

    city_formats = ("{{city_name}}",)

    street_name_formats = (
        "{{last_name}} Nagar",
        "{{last_name}} Zila",
        "{{last_name}} Street",
        "{{last_name}} Ganj",
        "{{last_name}} Road",
        "{{last_name}} Path",
        "{{last_name}} Marg",
        "{{last_name}} Chowk",
        "{{last_name}} Circle",
        "{{last_name}}",
    )

    street_address_formats = (
        "{{building_number}}, {{street_name}}",
        "{{building_number}}\n{{street_name}}",
    )

    address_formats = (
        "{{street_address}}\n{{city}} {{postcode}}",
        "{{street_address}}\n{{city}}-{{postcode}}",
        "{{street_address}}, {{city}} {{postcode}}",
        "{{street_address}}, {{city}}-{{postcode}}",
    )

    building_number_formats = ("H.No. ###", "###", "H.No. ##", "##", "##/##", "##/###")

    postcode_formats = ("######",)

    cities = (
        "Mumbai",
        "Delhi",
        "Kolkata",
        "Chennai",
        "Bangalore",
        "Hyderabad",
        "Ahmedabad",
        "Kanpur",
        "Pune",
        "Surat",
        "Jaipur",
        "Lucknow",
        "Nagpur",
        "Indore",
        "Bhopal",
        "Ludhiana",
        "Patna",
        "Visakhapatnam",
        "Vadodara",
        "Agra",
        "Thane",
        "Kalyan-Dombivli",
        "Varanasi",
        "Ranchi",
        "Nashik",
        "Dhanbad",
        "Faridabad",
        "Meerut",
        "Pimpri-Chinchwad",
        "Howrah",
        "Allahabad",
        "Ghaziabad",
        "Rajkot",
        "Amritsar",
        "Jabalpur",
        "Coimbatore",
        "Madurai",
        "Srinagar",
        "Aurangabad",
        "Solapur",
        "Vijayawada",
        "Jodhpur",
        "Gwalior",
        "Guwahati",
        "Chandigarh",
        "Hubli–Dharwad",
        "Mysore",
        "Tiruchirappalli",
        "Bareilly",
        "Jalandhar",
        "Navi Mumbai",
        "Salem",
        "Kota",
        "Vasai-Virar",
        "Aligarh",
        "Moradabad",
        "Bhubaneswar",
        "Gorakhpur",
        "Raipur",
        "Bhiwandi",
        "Kochi",
        "Jamshedpur",
        "Bhilai",
        "Amravati",
        "Cuttack",
        "Warangal",
        "Bikaner",
        "Mira-Bhayandar",
        "Guntur",
        "Bhavnagar",
        "Durgapur",
        "Kolhapur",
        "Ajmer",
        "Asansol",
        "Ulhasnagar",
        "Siliguri",
        "Jalgaon",
        "Saharanpur",
        "Jamnagar",
        "Bhatpara",
        "Sangli-Miraj & Kupwad",
        "Kozhikode",
        "Nanded",
        "Ujjain",
        "Dehradun",
        "Rourkela",
        "Gulbarga",
        "Tirunelveli",
        "Malegaon",
        "Akola",
        "Belgaum",
        "Mangalore",
        "Bokaro",
        "South Dumdum",
        "Udaipur",
        "Gaya",
        "Maheshtala",
        "Jhansi",
        "Nellore",
        "Jammu",
        "Thiruvananthapuram",
        "Davanagere",
        "Kollam",
        "Panihati",
        "Kurnool",
        "Tiruppur",
        "Dhule",
        "Bhagalpur",
        "Rajpur Sonarpur",
        "Kakinada",
        "Thrissur",
        "Bellary",
        "Muzaffarnagar",
        "Korba",
        "Rajahmundry",
        "Kamarhati",
        "Ambattur",
        "Berhampur",
        "Ahmednagar",
        "Muzaffarpur",
        "Noida",
        "Patiala",
        "Mathura",
        "New Delhi",
        "Latur",
        "Sambalpur",
        "Shahjahanpur",
        "Kulti",
        "Chandrapur",
        "Nizamabad",
        "Rohtak",
        "Bardhaman",
        "Rampur",
        "Bhilwara",
        "Firozabad",
        "Bilaspur",
        "Shimoga",
        "Agartala",
        "Gopalpur",
        "Darbhanga",
        "Panipat",
        "Bally",
        "Alwar",
        "Parbhani",
        "Ichalkaranji",
        "Anantapuram",
        "Baranagar",
        "Tumkur",
        "Ramagundam",
        "Jalna",
        "Durg",
        "Sagar",
        "Bihar Sharif",
        "Dewas",
        "Barasat",
        "Avadi",
        "Farrukhabad",
        "Aizawl",
        "Tirupati",
        "Bijapur",
        "Satara",
        "Satna",
        "Ratlam",
        "Imphal",
        "Pondicherry",
        "North Dumdum",
        "Anantapur",
        "Khammam",
        "Ozhukarai",
        "Bathinda",
        "Thoothukudi",
        "Thanjavur",
        "Naihati",
        "Sonipat",
        "Mau",
        "Tiruvottiyur",
        "Hapur",
        "Sri Ganganagar",
        "Karnal",
        "Etawah",
        "Nagercoil",
        "Raichur",
        "Raurkela Industrial Township",
        "Secunderabad",
        "Karimnagar",
        "Mirzapur",
        "Bharatpur",
        "Ambarnath",
        "Arrah",
        "Uluberia",
        "Serampore",
        "Dindigul",
        "Gandhinagar",
        "Burhanpur",
        "Nadiad",
        "Eluru",
        "Yamunanagar",
        "Kharagpur",
        "Munger",
        "Pali",
        "Katni",
        "Singrauli",
        "Tenali",
        "Sikar",
        "Silchar",
        "Rewa",
        "Sambhal",
        "Machilipatnam",
        "Vellore",
        "Alappuzha",
        "Bulandshahr",
        "Haridwar",
        "Vijayanagaram",
        "Erode",
        "Gurgaon",
        "Bidar",
        "Bhusawal",
        "Khandwa",
        "Purnia",
        "Haldia",
        "Chinsurah",
        "Bhiwani",
        "Raebareli",
        "Junagadh",
        "Bahraich",
        "Gandhidham",
        "Mango",
        "Raiganj",
        "Amroha",
        "Sultan Pur Majra",
        "Hospet",
        "Bidhannagar",
        "Malda",
        "Sirsa",
        "Berhampore",
        "Jaunpur",
        "Surendranagar Dudhrej",
        "Madhyamgram",
        "Kirari Suleman Nagar",
        "Bhind",
        "Nandyal",
        "Chittoor",
        "Bhalswa Jahangir Pur",
        "Fatehpur",
        "Morena",
        "Nangloi Jat",
        "Ongole",
        "Karawal Nagar",
        "Shivpuri",
        "Morbi",
        "Unnao",
        "Pallavaram",
        "Kumbakonam",
        "Shimla",
        "Mehsana",
        "Panchkula",
        "Orai",
        "Ambala",
        "Dibrugarh",
        "Guna",
        "Danapur",
        "Sasaram",
        "Anand",
        "Kottayam",
        "Hazaribagh",
        "Kadapa",
        "Saharsa",
        "Nagaon",
        "Loni",
        "Hajipur",
        "Dehri",
        "Bettiah",
        "Katihar",
        "Deoghar",
        "Jorhat",
        "Siwan",
        "Panvel",
        "Hosur",
        "Tinsukia",
        "Bongaigaon",
        "Motihari",
        "Jamalpur",
        "Suryapet",
        "Begusarai",
        "Miryalaguda",
        "Proddatur",
        "Karaikudi",
        "Kishanganj",
        "Phusro",
        "Buxar",
        "Tezpur",
        "Jehanabad",
        "Aurangabad",
        "Chapra",
        "Ramgarh",
        "Gangtok",
        "Adoni",
        "Amaravati",
        "Ballia",
        "Bhimavaram",
        "Dharmavaram",
        "Giridih",
        "Gudivada",
        "Guntakal",
        "Hindupur",
        "Kavali",
        "Khora ",
        "Ghaziabad",
        "Madanapalle",
        "Mahbubnagar",
        "Medininagar",
        "Narasaraopet",
        "Phagwara",
        "Pudukkottai",
        "Srikakulam",
        "Tadepalligudem",
        "Tadipatri",
        "Udupi",
    )

    states = (
        "Andhra Pradesh",
        "Arunachal Pradesh",
        "Assam",
        "Bihar",
        "Chhattisgarh",
        "Goa",
        "Gujarat",
        "Haryana",
        "Himachal Pradesh",
        "Jharkhand",
        "Karnataka",
        "Kerala",
        "Madhya Pradesh",
        "Maharashtra",
        "Manipur",
        "Meghalaya",
        "Mizoram",
        "Nagaland",
        "Odisha",
        "Punjab",
        "Rajasthan",
        "Sikkim",
        "Tamil Nadu",
        "Telangana",
        "Tripura",
        "Uttar Pradesh",
        "Uttarakhand",
        "West Bengal",
    )

    def city_name(self) -> str:
        return self.random_element(self.cities)

    def state_name(self) -> str:
        return self.random_element(self.states)

    def administrative_unit(self) -> str:
        return self.random_element(self.states)

    state = administrative_unit
