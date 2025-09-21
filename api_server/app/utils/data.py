import os
from app.utils.image_utils import get_image_as_base64
from app.utils.config_reader import ConfigReader

config = ConfigReader()
IMAGE_BASE_PATH = config.get_image_base_path()

unified_trip_data = [
    {
  "city": "सूरत से राजस्थान",
  "dates": "22 अक्टूबर → 30 अक्टूबर",
  "locations": "जयपुर, जोधपुर, उदयपुर, जैसलमेर, पुष्कर और 8 अन्य स्थान",
  "notes": "हिलक्स में 5 मित्रों के साथ शाही राजस्थान की यादगार यात्रा",
  "tripDescription": {
    "title": "आपकी राजस्थान रोड ट्रिप - राजाओं की भूमि में 9 दिन की शाही यात्रा",
    "content": "राजस्थान की इस अविस्मरणीय यात्रा में आपको मिलेगा रेगिस्तान का सुनहरा रंग, महलों की भव्यता, और भारतीय संस्कृति का असली स्वाद। सूरत से शुरू होकर जयपुर के गुलाबी शहर से लेकर जैसलमेर के सुनहरी रेत के टीलों तक, यह यात्रा आपको राजस्थान के हर कोने की खूबसूरती दिखाएगी। हर दिन नई जगह, नया अनुभव और नई यादें। आपके हिलक्स में बैठकर राजस्थान के राजमार्गों पर दौड़ते हुए आप देखेंगे हवेलियों की नक्काशी, किलों की मजबूती, और स्थानीय बाजारों की रंगबिरंगी दुनिया। दाल बाटी चूरमा से लेकर लाल मांस तक, राजस्थानी व्यंजनों का स्वाद आपको जीवन भर याद रहेगा। रात में रेगिस्तान में सितारों को देखना और सुबह महलों में सूर्योदय का नजारा - यही तो है राजस्थान की असली पहचान।"
  },
  "tabs": [
    "Overview",
    "Itinerary",
    "Food",
    "Bookings",
    "Suggestions",
    "Locations",
    "Weather",
    "Packing",
    "Documents",
    "Budget",
    "Timelines",
    "Notifications"
  ],
  "tabContent": {
    "Overview": [
      {
        "type": "paragraph",
        "content": "राजस्थान भारत का सबसे रंगबिरंगा और शाही राज्य है। यहां आपको मिलेंगे भव्य किले, खूबसूरत महल, सुनहरे रेत के टीले और स्वादिष्ट राजस्थानी खाना। अक्टूबर का मौसम घूमने के लिए सबसे अच्छा है।"
      },
      {
        "type": "list",
        "title": "मुख्य आकर्षण:",
        "items": [
          "ऐतिहासिक किले और महल",
          "सुनहरे रेगिस्तान में कैमल सफारी",
          "रंग-बिरंगे स्थानीय बाजार",
          "प्रामाणिक राजस्थानी व्यंजन"
        ]
      },
      {
        "type": "departure",
        "days": "9",
        "time": "06:00:00"
      }
    ],





    # "Itinerary": [
    #   {
    #     "type": "dailyItinerary",
    #     "days": [
    #       {
    #         "date": "बुधवार, 22 अक्टूबर",
    #         "activities": [
    #           {
    #             "time": "06:00",
    #             "description": "सूरत से प्रस्थान",
    #             "type": "start"
    #           },
    #           {
    #             "time": "07:00",
    #             "description": "उदयपुर की ओर रवाना (315 किमी)",
    #             "details": "अनुमानित दूरी: 315 किमी\nअनुमानित समय: 6 घंटे",
    #             "action": "टोल प्लाजा के लिए कैश तैयार रखें",
    #             "type": "travel",
    #             "longDescription": "सुबह जल्दी निकलकर उदयपुर पहुंचने का फायदा यह है कि आप दिन में ही शहर देख सकेंगे। रास्ते में खूबसूरत अरावली पहाड़ियों का नजारा मिलेगा।"
    #           },
    #           {
    #             "time": "10:30",
    #             "description": "नाश्ता - अहमदाबाद हाईवे पर",
    #             "type": "food"
    #           },
    #           {
    #             "time": "14:00",
    #             "description": "उदयपुर पहुंचना और होटल चेक-इन",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "16:00",
    #             "description": "पिछोला झील बोट राइड",
    #             "type": "activity",
    #             "longDescription": "झील पर बोटिंग करते हुए जग मंदिर और लेक पैलेस का खूबसूरत नजारा देखें।"
    #           },
    #           {
    #             "time": "19:00",
    #             "description": "सिटी पैलेस घूमना",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "20:30",
    #             "description": "स्थानीय रेस्टोरेंट में रात का खाना",
    #             "type": "food"
    #           }
    #         ],
    #         "dailyCost": {
    #           "amount": "3500",
    #           "currency": "₹",
    #           "details": "ईंधन: ₹1500, टोल: ₹300, होटल: ₹1200, खाना: ₹500"
    #         }
    #       },
    #       {
    #         "date": "गुरुवार, 23 अक्टूबर",
    #         "activities": [
    #           {
    #             "time": "08:00",
    #             "description": "सहेलियों की बाड़ी और फतेह सागर झील",
    #             "type": "activity",
    #             "longDescription": "खूबसूरत गार्डन और फव्वारों का आनंद लें।"
    #           },
    #           {
    #             "time": "12:00",
    #             "description": "जोधपुर की ओर प्रस्थान (250 किमी)",
    #             "type": "travel"
    #           },
    #           {
    #             "time": "14:00",
    #             "description": "रानकपुर जैन मंदिर रुकना",
    #             "type": "activity",
    #             "longDescription": "1444 खंभों वाला यह मंदिर अद्भुत वास्तुकला का नमूना है।"
    #           },
    #           {
    #             "time": "17:30",
    #             "description": "जोधपुर पहुंचना और होटल चेक-इन",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "19:00",
    #             "description": "घंटा घर बाजार की सैर",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "20:30",
    #             "description": "मक्खनिया लस्सी और मिर्ची बड़ा",
    #             "type": "food"
    #           }
    #         ],
    #         "dailyCost": {
    #           "amount": "3200",
    #           "currency": "₹",
    #           "details": "ईंधन: ₹1200, होटल: ₹1200, खाना: ₹600, एंट्री फीस: ₹200"
    #         }
    #       },
    #       {
    #         "date": "शुक्रवार, 24 अक्टूबर",
    #         "activities": [
    #           {
    #             "time": "09:00",
    #             "description": "मेहरानगढ़ किला",
    #             "type": "activity",
    #             "longDescription": "राजस्थान के सबसे भव्य किलों में से एक, जहां से पूरे नीले शहर का नजारा दिखता है।"
    #           },
    #           {
    #             "time": "12:30",
    #             "description": "जसवंत थड़ा",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "14:00",
    #             "description": "जैसलमेर की ओर प्रस्थान (285 किमी)",
    #             "type": "travel"
    #           },
    #           {
    #             "time": "19:00",
    #             "description": "जैसलमेर पहुंचना",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "20:00",
    #             "description": "होटल चेक-इन और आराम",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "21:00",
    #             "description": "स्थानीय रेस्टोरेंट में डिनर",
    #             "type": "food"
    #           }
    #         ],
    #         "dailyCost": {
    #           "amount": "3800",
    #           "currency": "₹",
    #           "details": "ईंधन: ₹1400, होटल: ₹1500, खाना: ₹700, एंट्री फीस: ₹200"
    #         }
    #       },
    #       {
    #         "date": "शनिवार, 25 अक्टूबर",
    #         "activities": [
    #           {
    #             "time": "09:00",
    #             "description": "जैसलमेर किला (सोनार किला)",
    #             "type": "activity",
    #             "longDescription": "दुनिया का एकमात्र जीवित किला जहां आज भी लोग रहते हैं।"
    #           },
    #           {
    #             "time": "11:30",
    #             "description": "पटवों की हवेली",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "13:00",
    #             "description": "दोपहर का भोजन",
    #             "type": "food"
    #           },
    #           {
    #             "time": "15:00",
    #             "description": "सैम सैंड ड्यून्स के लिए प्रस्थान",
    #             "type": "travel"
    #           },
    #           {
    #             "time": "16:30",
    #             "description": "कैमल राइड और डेजर्ट सफारी",
    #             "type": "activity",
    #             "longDescription": "रेगिस्तान में ऊंट की सवारी और खूबसूरत सूर्यास्त का नजारा।"
    #           },
    #           {
    #             "time": "19:00",
    #             "description": "रेगिस्तान में राजस्थानी लोक संगीत",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "20:30",
    #             "description": "डेजर्ट कैंप में डिनर",
    #             "type": "food"
    #           },
    #           {
    #             "time": "22:00",
    #             "description": "रात्रि विश्राम - रेगिस्तान कैंप",
    #             "type": "activity"
    #           }
    #         ],
    #         "dailyCost": {
    #           "amount": "4200",
    #           "currency": "₹",
    #           "details": "कैमल सफारी: ₹1500, कैंप स्टे: ₹1800, खाना: ₹700, एंट्री फीस: ₹200"
    #         }
    #       },
    #       {
    #         "date": "रविवार, 26 अक्टूबर",
    #         "activities": [
    #           {
    #             "time": "06:00",
    #             "description": "रेगिस्तान में सूर्योदय",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "08:00",
    #             "description": "नाश्ता और जैसलमेर वापसी",
    #             "type": "food"
    #           },
    #           {
    #             "time": "11:00",
    #             "description": "जयपुर की ओर प्रस्थान (557 किमी)",
    #             "type": "travel"
    #           },
    #           {
    #             "time": "14:00",
    #             "description": "रास्ते में दोपहर का खाना",
    #             "type": "food"
    #           },
    #           {
    #             "time": "21:00",
    #             "description": "जयपुर पहुंचना और होटल चेक-इन",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "22:00",
    #             "description": "आराम",
    #             "type": "activity"
    #           }
    #         ],
    #         "dailyCost": {
    #           "amount": "3000",
    #           "currency": "₹",
    #           "details": "ईंधन: ₹1500, होटल: ₹1000, खाना: ₹500"
    #         }
    #       },
    #       {
    #         "date": "सोमवार, 27 अक्टूबर",
    #         "activities": [
    #           {
    #             "time": "08:00",
    #             "description": "आमेर किला",
    #             "type": "activity",
    #             "longDescription": "हाथी की सवारी और शीश महल का दर्शन।"
    #           },
    #           {
    #             "time": "11:00",
    #             "description": "हवा महल",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "13:00",
    #             "description": "दाल बाटी चूरमा लंच",
    #             "type": "food"
    #           },
    #           {
    #             "time": "15:00",
    #             "description": "सिटी पैलेस और जंतर मंतर",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "17:30",
    #             "description": "जोहरी बाजार में खरीदारी",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "20:00",
    #             "description": "चोखी ढाणी में राजस्थानी डिनर",
    #             "type": "food"
    #           }
    #         ],
    #         "dailyCost": {
    #           "amount": "3500",
    #           "currency": "₹",
    #           "details": "एंट्री फीस: ₹800, खाना: ₹1000, खरीदारी: ₹1200, चोखी ढाणी: ₹500"
    #         }
    #       },
    #       {
    #         "date": "मंगलवार, 28 अक्टूबर",
    #         "activities": [
    #           {
    #             "time": "09:00",
    #             "description": "पुष्कर की ओर प्रस्थान (145 किमी)",
    #             "type": "travel"
    #           },
    #           {
    #             "time": "11:30",
    #             "description": "पुष्कर झील और ब्रह्मा मंदिर",
    #             "type": "activity",
    #             "longDescription": "दुनिया का एकमात्र ब्रह्मा मंदिर और पवित्र पुष्कर झील।"
    #           },
    #           {
    #             "time": "13:00",
    #             "description": "पुष्कर में दोपहर का भोजन",
    #             "type": "food"
    #           },
    #           {
    #             "time": "15:00",
    #             "description": "सावित्री मंदिर (रोपवे)",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "17:00",
    #             "description": "पुष्कर बाजार में खरीदारी",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "19:00",
    #             "description": "अजमेर शरीफ दरगाह",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "22:00",
    #             "description": "जयपुर वापसी और होटल आराम",
    #             "type": "travel"
    #           }
    #         ],
    #         "dailyCost": {
    #           "amount": "2800",
    #           "currency": "₹",
    #           "details": "ईंधन: ₹800, खाना: ₹600, खरीदारी: ₹1000, एंट्री फीस: ₹400"
    #         }
    #       },
    #       {
    #         "date": "बुधवार, 29 अक्टूबर",
    #         "activities": [
    #           {
    #             "time": "08:00",
    #             "description": "नाहरगढ़ किला",
    #             "type": "activity",
    #             "longDescription": "जयपुर शहर का सबसे खूबसूरत नजारा।"
    #           },
    #           {
    #             "time": "11:00",
    #             "description": "जयगढ़ किला",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "13:00",
    #             "description": "दोपहर का भोजन",
    #             "type": "food"
    #           },
    #           {
    #             "time": "15:00",
    #             "description": "गलताजी मंदिर (बंदर मंदिर)",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "17:00",
    #             "description": "अंतिम मिनट की खरीदारी",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "20:00",
    #             "description": "विदाई डिनर पार्टी",
    #             "type": "food"
    #           }
    #         ],
    #         "dailyCost": {
    #           "amount": "2500",
    #           "currency": "₹",
    #           "details": "एंट्री फीस: ₹400, खाना: ₹800, खरीदारी: ₹1000, पेट्रोल: ₹300"
    #         }
    #       },
    #       {
    #         "date": "गुरुवार, 30 अक्टूबर",
    #         "activities": [
    #           {
    #             "time": "08:00",
    #             "description": "होटल चेक-आउट और नाश्ता",
    #             "type": "food"
    #           },
    #           {
    #             "time": "10:00",
    #             "description": "सूरत वापसी की यात्रा शुरू",
    #             "type": "start"
    #           },
    #           {
    #             "time": "14:00",
    #             "description": "रास्ते में दोपहर का खाना",
    #             "type": "food"
    #           },
    #           {
    #             "time": "22:00",
    #             "description": "सूरत पहुंचना",
    #             "type": "activity",
    #             "longDescription": "यादगार राजस्थान यात्रा की समाप्ति।"
    #           }
    #         ],
    #         "dailyCost": {
    #           "amount": "2000",
    #           "currency": "₹",
    #           "details": "ईंधन: ₹1200, खाना: ₹500, टोल: ₹300"
    #         }
    #       }
    #     ]
    #   }
    # ]
    
    "Itinerary": [
  {
    "type": "dailyItinerary",
    "days": [
      {
        "date": "बुधवार, 22 अक्टूबर",
        "activities": [
          { "time": "06:00", "description": "सूरत से प्रस्थान", "type": "start" },
          { "time": "07:00", "description": "उदयपुर की ओर रवाना (315 किमी)", "details": "अनुमानित दूरी: 315 किमी\nअनुमानित समय: 6 घंटे", "action": "टोल प्लाजा के लिए कैश तैयार रखें", "type": "travel", "longDescription": "सुबह जल्दी निकलकर उदयपुर पहुंचने का फायदा यह है कि आप दिन में ही शहर देख सकेंगे। रास्ते में खूबसूरत अरावली पहाड़ियों का नजारा मिलेगा।" },
          { "time": "10:30", "description": "नाश्ता - अहमदाबाद हाईवे पर", "type": "food" },
          { "time": "14:00", "description": "उदयपुर पहुंचना और होटल चेक-इन", "type": "activity" },
          { "time": "16:00", "description": "पिछोला झील बोट राइड", "type": "activity", "longDescription": "झील पर बोटिंग करते हुए जग मंदिर और लेक पैलेस का खूबसूरत नजारा देखें।" },
          { "time": "19:00", "description": "सिटी पैलेस घूमना", "type": "activity" },
          { "time": "20:30", "description": "स्थानीय रेस्टोरेंट में रात का खाना", "type": "food" }
        ],
        "dailyCost": { "amount": "3500", "currency": "₹", "details": "ईंधन: ₹1500, टोल: ₹300, होटल: ₹1200, खाना: ₹500" },
        "locations": [
          { "latitude": 24.572, "longitude": 73.679, "name": "Lake Pichola" },
          { "latitude": 24.5764, "longitude": 73.6835, "name": "City Palace Udaipur" }
        ]
      },
      {
        "date": "गुरुवार, 23 अक्टूबर",
        "activities": [
          { "time": "08:00", "description": "सहेलियों की बाड़ी और फतेह सागर झील", "type": "activity", "longDescription": "खूबसूरत गार्डन और फव्वारों का आनंद लें।" },
          { "time": "12:00", "description": "जोधपुर की ओर प्रस्थान (250 किमी)", "type": "travel" },
          { "time": "14:00", "description": "रानकपुर जैन मंदिर रुकना", "type": "activity", "longDescription": "1444 खंभों वाला यह मंदिर अद्भुत वास्तुकला का नमूना है।" },
          { "time": "17:30", "description": "जोधपुर पहुंचना और होटल चेक-इन", "type": "activity" },
          { "time": "19:00", "description": "घंटा घर बाजार की सैर", "type": "activity" },
          { "time": "20:30", "description": "मक्खनिया लस्सी और मिर्ची बड़ा", "type": "food" }
        ],
        "dailyCost": { "amount": "3200", "currency": "₹", "details": "ईंधन: ₹1200, होटल: ₹1200, खाना: ₹600, एंट्री फीस: ₹200" },
        "locations": [
          { "latitude": 24.6051, "longitude": 73.6847, "name": "Saheliyon ki Bari" },
          { "latitude": 25.0456, "longitude": 73.4602, "name": "Ranakpur Jain Temple" },
          { "latitude": 26.2921, "longitude": 73.0479, "name": "Ghanta Ghar, Jodhpur" }
        ]
      },
      {
        "date": "शुक्रवार, 24 अक्टूबर",
        "activities": [
          { "time": "09:00", "description": "मेहरानगढ़ किला", "type": "activity", "longDescription": "राजस्थान के सबसे भव्य किलों में से एक, जहां से पूरे नीले शहर का नजारा दिखता है।" },
          { "time": "12:30", "description": "जसवंत थड़ा", "type": "activity" },
          { "time": "14:00", "description": "जैसलमेर की ओर प्रस्थान (285 किमी)", "type": "travel" },
          { "time": "19:00", "description": "जैसलमेर पहुंचना", "type": "activity" },
          { "time": "20:00", "description": "होटल चेक-इन और आराम", "type": "activity" },
          { "time": "21:00", "description": "स्थानीय रेस्टोरेंट में डिनर", "type": "food" }
        ],
        "dailyCost": { "amount": "3800", "currency": "₹", "details": "ईंधन: ₹1400, होटल: ₹1500, खाना: ₹700, एंट्री फीस: ₹200" },
        "locations": [
          { "latitude": 26.2986, "longitude": 73.0186, "name": "Mehrangarh Fort" },
          { "latitude": 26.2978, "longitude": 73.0196, "name": "Jaswant Thada" }
        ]
      },
      {
        "date": "शनिवार, 25 अक्टूबर",
        "activities": [
          { "time": "09:00", "description": "जैसलमेर किला (सोनार किला)", "type": "activity", "longDescription": "दुनिया का एकमात्र जीवित किला जहां आज भी लोग रहते हैं।" },
          { "time": "11:30", "description": "पटवों की हवेली", "type": "activity" },
          { "time": "13:00", "description": "दोपहर का भोजन", "type": "food" },
          { "time": "15:00", "description": "सैम सैंड ड्यून्स के लिए प्रस्थान", "type": "travel" },
          { "time": "16:30", "description": "कैमल राइड और डेजर्ट सफारी", "type": "activity", "longDescription": "रेगिस्तान में ऊंट की सवारी और खूबसूरत सूर्यास्त का नजारा।" },
          { "time": "19:00", "description": "रेगिस्तान में राजस्थानी लोक संगीत", "type": "activity" },
          { "time": "20:30", "description": "डेजर्ट कैंप में डिनर", "type": "food" },
          { "time": "22:00", "description": "रात्रि विश्राम - रेगिस्तान कैंप", "type": "activity" }
        ],
        "dailyCost": { "amount": "4200", "currency": "₹", "details": "कैमल सफारी: ₹1500, कैंप स्टे: ₹1800, खाना: ₹700, एंट्री फीस: ₹200" },
        "locations": [
          { "latitude": 26.9124, "longitude": 70.9129, "name": "Jaisalmer Fort" },
          { "latitude": 26.9167, "longitude": 70.9152, "name": "Patwon Ki Haveli" },
          { "latitude": 26.9412, "longitude": 70.7716, "name": "Sam Sand Dunes" }
        ]
      },
      {
        "date": "रविवार, 26 अक्टूबर",
        "activities": [
          { "time": "06:00", "description": "रेगिस्तान में सूर्योदय", "type": "activity" },
          { "time": "08:00", "description": "नाश्ता और जैसलमेर वापसी", "type": "food" },
          { "time": "11:00", "description": "जयपुर की ओर प्रस्थान (557 किमी)", "type": "travel" },
          { "time": "14:00", "description": "रास्ते में दोपहर का खाना", "type": "food" },
          { "time": "21:00", "description": "जयपुर पहुंचना और होटल चेक-इन", "type": "activity" },
          { "time": "22:00", "description": "आराम", "type": "activity" }
        ],
        "dailyCost": { "amount": "3000", "currency": "₹", "details": "ईंधन: ₹1500, होटल: ₹1000, खाना: ₹500" },
        "locations": [
          { "latitude": 26.9124, "longitude": 70.9129, "name": "Jaisalmer" },
          { "latitude": 26.9124, "longitude": 75.7873, "name": "Jaipur" }
        ]
      },
      {
        "date": "सोमवार, 27 अक्टूबर",
        "activities": [
          { "time": "08:00", "description": "आमेर किला", "type": "activity", "longDescription": "हाथी की सवारी और शीश महल का दर्शन।" },
          { "time": "11:00", "description": "हवा महल", "type": "activity" },
          { "time": "13:00", "description": "दाल बाटी चूरमा लंच", "type": "food" },
          { "time": "15:00", "description": "सिटी पैलेस और जंतर मंतर", "type": "activity" },
          { "time": "17:30", "description": "जोहरी बाजार में खरीदारी", "type": "activity" },
          { "time": "20:00", "description": "चोखी ढाणी में राजस्थानी डिनर", "type": "food" }
        ],
        "dailyCost": { "amount": "3500", "currency": "₹", "details": "एंट्री फीस: ₹800, खाना: ₹1000, खरीदारी: ₹1200, चोखी ढाणी: ₹500" },
        "locations": [
          { "latitude": 26.9855, "longitude": 75.8507, "name": "Amer Fort" },
          { "latitude": 26.9239, "longitude": 75.8267, "name": "Hawa Mahal" },
          { "latitude": 26.9257, "longitude": 75.8236, "name": "City Palace Jaipur" }
        ]
      },
      {
        "date": "मंगलवार, 28 अक्टूबर",
        "activities": [
          { "time": "09:00", "description": "पुष्कर की ओर प्रस्थान (145 किमी)", "type": "travel" },
          { "time": "11:30", "description": "पुष्कर झील और ब्रह्मा मंदिर", "type": "activity", "longDescription": "दुनिया का एकमात्र ब्रह्मा मंदिर और पवित्र पुष्कर झील।" },
          { "time": "13:00", "description": "पुष्कर में दोपहर का भोजन", "type": "food" },
          { "time": "15:00", "description": "सावित्री मंदिर (रोपवे)", "type": "activity" },
          { "time": "17:00", "description": "पुष्कर बाजार में खरीदारी", "type": "activity" },
          { "time": "19:00", "description": "अजमेर शरीफ दरगाह", "type": "activity" },
          { "time": "22:00", "description": "जयपुर वापसी और होटल आराम", "type": "travel" }
        ],
        "dailyCost": { "amount": "2800", "currency": "₹", "details": "ईंधन: ₹800, खाना: ₹600, खरीदारी: ₹1000, एंट्री फीस: ₹400" },
        "locations": [
          { "latitude": 26.4876, "longitude": 74.5518, "name": "Pushkar Lake" },
          { "latitude": 26.4874, "longitude": 74.5526, "name": "Brahma Temple, Pushkar" },
          { "latitude": 26.4499, "longitude": 74.6382, "name": "Ajmer Sharif Dargah" }
        ]
      },
      {
        "date": "बुधवार, 29 अक्टूबर",
        "activities": [
          { "time": "08:00", "description": "नाहरगढ़ किला", "type": "activity", "longDescription": "जयपुर शहर का सबसे खूबसूरत नजारा।" },
          { "time": "11:00", "description": "जयगढ़ किला", "type": "activity" },
          { "time": "13:00", "description": "दोपहर का भोजन", "type": "food" },
          { "time": "15:00", "description": "गलताजी मंदिर (बंदर मंदिर)", "type": "activity" },
          { "time": "17:00", "description": "अंतिम मिनट की खरीदारी", "type": "activity" },
          { "time": "20:00", "description": "विदाई डिनर पार्टी", "type": "food" }
        ],
        "dailyCost": { "amount": "2500", "currency": "₹", "details": "एंट्री फीस: ₹400, खाना: ₹800, खरीदारी: ₹1000, पेट्रोल: ₹300" },
        "locations": [
          { "latitude": 26.9390, "longitude": 75.8127, "name": "Nahargarh Fort" },
          { "latitude": 26.9573, "longitude": 75.8006, "name": "Jaigarh Fort" },
          { "latitude": 26.9367, "longitude": 75.8566, "name": "Galtaji Temple" }
        ]
      },
      {
        "date": "गुरुवार, 30 अक्टूबर",
        "activities": [
          { "time": "08:00", "description": "होटल चेक-आउट और नाश्ता", "type": "food" },
          { "time": "10:00", "description": "सूरत वापसी की यात्रा शुरू", "type": "start" },
          { "time": "14:00", "description": "रास्ते में दोपहर का खाना", "type": "food" },
          { "time": "22:00", "description": "सूरत पहुंचना", "type": "activity", "longDescription": "यादगार राजस्थान यात्रा की समाप्ति।" }
        ],
        "dailyCost": { "amount": "2000", "currency": "₹", "details": "ईंधन: ₹1200, खाना: ₹500, टोल: ₹300" },
        "locations": [
          { "latitude": 21.1702, "longitude": 72.8311, "name": "Surat" }
        ]
      }
    ]
  }
]

    
    
    
    
    
    
    ,
    "Food": [
      {
        "type": "heading",
        "content": "राजस्थान के मुख्य व्यंजन"
      },
      {
        "type": "item",
        "name": "दाल बाटी चूरमा",
        "description": "राजस्थान का सबसे प्रसिद्ध व्यंजन। कुरकुरी बाटी के साथ दाल और मीठा चूरमा।",
        "recommendation": "जयपुर में चोखी ढाणी में जरूर ट्राई करें।"
      },
      {
        "type": "item",
        "name": "लाल मांस",
        "description": "राजस्थानी मसालों के साथ बना हुआ मांस का तीखा व्यंजन।",
        "recommendation": "जोधपुर में मिलता है सबसे अच्छा।"
      },
      {
        "type": "item",
        "name": "गट्टे की सब्जी",
        "description": "बेसन के गट्टों से बनी हुई तीखी सब्जी।",
        "recommendation": "हर जगह उपलब्ध है।"
      },
      {
        "type": "item",
        "name": "मिर्ची बड़ा",
        "description": "मिर्च के अंदर आलू भरकर बेसन में फ्राई किया हुआ।",
        "recommendation": "जोधपुर में स्पेशल मिलता है।"
      },
      {
        "type": "item",
        "name": "प्याज की कचोरी",
        "description": "जयपुर की प्रसिद्ध कचोरी।",
        "recommendation": "सुबह के नाश्ते में बेस्ट।"
      },
      {
        "type": "item",
        "name": "मक्खनिया लस्सी",
        "description": "जोधपुर की फेमस मलाई वाली लस्सी।",
        "recommendation": "घंटा घर के पास मिलती है।"
      }
    ],
    "Bookings": [
      {
        "type": "heading",
        "content": "आपकी वर्तमान बुकिंग स्थिति"
      },
      {
        "type": "booking",
        "service": "होटल उदयपुर",
        "details": "लेक व्यू होटल (22-23 अक्टूबर)",
        "status": "बुक करना है",
        "bookingId": "HOTEL001"
      },
      {
        "type": "booking",
        "service": "होटल जोधपुर",
        "details": "हवेली रूम्स (23-24 अक्टूबर)",
        "status": "बुक करना है",
        "bookingId": "HOTEL002"
      },
      {
        "type": "booking",
        "service": "डेजर्ट कैंप",
        "details": "सैम सैंड ड्यून्स कैंप (25-26 अक्टूबर)",
        "status": "बुक करना है",
        "bookingId": "CAMP001"
      },
      {
        "type": "packageBooking",
        "service": "कैमल सफारी पैकेज",
        "details": "जैसलमेर डेजर्ट सफारी व कल्चरल शो",
        "status": "बुक करना है",
        "bookingId": "PKG001",
        "savings": {
          "amount": "500",
          "currency": "₹"
        },
        "message": "ग्रुप बुकिंग पर ₹500 की छूट मिल सकती है!"
      },
      {
        "type": "bookingConfirmation",
        "confirmedMessage": "होटल बुकिंग यात्रा से पहले करना सुनिश्चित करें!",
        "referenceNo": "RAJASTHAN2025",
        "emailMessage": "पीक सीजन के कारण होटल जल्दी बुक हो सकते हैं।"
      }
    ],
    "Suggestions": [
      {
        "type": "heading",
        "content": "आपके लिए व्यक्तिगत सुझाव"
      },
      {
        "type": "suggestion",
        "title": "रणथम्भोर नेशनल पार्क",
        "description": "अगर समय हो तो टाइगर सफारी का मजा लें।",
        "category": "वाइल्डलाइफ"
      },
      {
        "type": "suggestion",
        "title": "माउंट आबू",
        "description": "राजस्थान का एकमात्र हिल स्टेशन।",
        "category": "हिल स्टेशन"
      },
      {
        "type": "suggestion",
        "title": "कुंभलगढ़ किला",
        "description": "चीन की दीवार के बाद दूसरी सबसे लंबी दीवार।",
        "category": "ऐतिहासिक"
      },
      {
        "type": "suggestion",
        "title": "बीकानेर",
        "description": "भुजिया और ऊंट के लिए प्रसिद्ध।",
        "category": "फूड एंड कल्चर"
      }
    ],
    "Locations": [
      {
        "type": "heading",
        "content": "मुख्य गंतव्य स्थान"
      },
      {
        "type": "location",
        "name": "उदयपुर",
        "description": "झीलों का शहर, लेक पैलेस और सिटी पैलेस के लिए प्रसिद्ध।",
        "coordinates": "24.5854° N, 73.7125° E"
      },
      {
        "type": "location",
        "name": "जोधपुर",
        "description": "नीला शहर, मेहरानगढ़ किले के लिए प्रसिद्ध।",
        "coordinates": "26.2389° N, 73.0243° E"
      },
      {
        "type": "location",
        "name": "जैसलमेर",
        "description": "सुनहरा शहर, रेगिस्तान और सोनार किले के लिए प्रसिद्ध।",
        "coordinates": "26.9157° N, 70.9083° E"
      },
      {
        "type": "location",
        "name": "जयपुर",
        "description": "गुलाबी शहर, हवा महल और आमेर किले के लिए प्रसिद्ध।",
        "coordinates": "26.9124° N, 75.7873° E"
      },
      {
        "type": "location",
        "name": "पुष्कर",
        "description": "पवित्र शहर, ब्रह्मा मंदिर और पुष्कर झील के लिए प्रसिद्ध।",
        "coordinates": "26.4899° N, 74.5511° E"
      }
    ],
    "Weather": [
      {
        "type": "heading",
        "content": "अक्टूबर 2025 मौसम पूर्वानुमान"
      },
      {
        "type": "weather",
        "city": "उदयपुर",
        "icon": "☀️",
        "temperature": "21-31°C"
      },
      {
        "type": "weather",
        "city": "जोधपुर",
        "icon": "☀️",
        "temperature": "22-34°C"
      },
      {
        "type": "weather",
        "city": "जैसलमेर",
        "icon": "☀️",
        "temperature": "24-35°C"
      },
      {
        "type": "weather",
        "city": "जयपुर",
        "icon": "☀️",
        "temperature": "23-33°C"
      }
    ],
    "Packing": [
      {
        "type": "heading",
        "content": "राजस्थान यात्रा के लिए पैकिंग चेकलिस्ट"
      },
      {
        "type": "item",
        "name": "सूती कपड़े (दिन के लिए)",
        "checked": "false"
      },
      {
        "type": "item",
        "name": "गर्म कपड़े (रात के लिए)",
        "checked": "false"
      },
      {
        "type": "item",
        "name": "सनग्लासेज और सनस्क्रीन",
        "checked": "false"
      },
      {
        "type": "item",
        "name": "आरामदायक चप्पल/जूते",
        "checked": "false"
      },
      {
        "type": "item",
        "name": "टोपी या स्कार्फ",
        "checked": "false"
      },
      {
        "type": "item",
        "name": "पावर बैंक और चार्जर",
        "checked": "false"
      },
      {
        "type": "item",
        "name": "पानी की बोतल",
        "checked": "false"
      },
      {
        "type": "item",
        "name": "कैमरा",
        "checked": "false"
      },
      {
        "type": "item",
        "name": "फर्स्ट एड किट",
        "checked": "false"
      },
      {
        "type": "item",
        "name": "नकद पैसे",
        "checked": "false"
      }
    ],
    "Documents": [
      {
        "type": "heading",
        "content": "जरूरी दस्तावेज"
      },
      {
        "type": "document",
        "name": "ड्राइविंग लाइसेंस",
        "icon": "🚗"
      },
      {
        "type": "document",
        "name": "RC बुक (हिलक्स)",
        "icon": "📄"
      },
      {
        "type": "document",
        "name": "इंश्योरेंस पेपर",
        "icon": "📄"
      },
      {
        "type": "document",
        "name": "होटल बुकिंग वाउचर",
        "icon": "🏨"
      },
      {
        "type": "document",
        "name": "आधार कार्ड",
        "icon": "📄"
      },
      {
        "type": "document",
        "name": "इमरजेंसी कॉन्टैक्ट लिस्ट",
        "icon": "📞"
      }
    ],
    "Budget": [
      {
        "type": "heading",
        "content": "बजट ट्रैकर (प्रति व्यक्ति)"
      },
      {
        "type": "budget",
        "spent": "0",
        "total": "15000",
        "currency": "₹"
      },
      {
        "type": "paragraph",
        "content": "प्रमुख खर्च: होटल (₹4000), ईंधन और टोल (₹3500), खाना (₹3500), एंट्री फीस (₹2000), खरीदारी (₹2000)"
      }
    ],
    "Timelines": [
      {
        "type": "heading",
        "content": "दैनिक ड्राइविंग समय"
      },
      {
        "type": "timeline",
        "items": [
          "दिन 1: सूरत-उदयपुर (6 घंटे)",
          "दिन 2: उदयपुर-जोधपुर (4 घंटे)",
          "दिन 3: जोधपुर-जैसलमेर (5 घंटे)",
          "दिन 5: जैसलमेर-जयपुर (10 घंटे)",
          "दिन 9: जयपुर-सूरत (12 घंटे)"
        ]
      }
    ],
    "Notifications": [
      {
        "type": "heading",
        "content": "महत्वपूर्ण सूचनाएं"
      },
      {
        "type": "notification",
        "items": [
          "रेगिस्तान में मोबाइल नेटवर्क कम हो सकता है",
          "हमेशा पानी साथ रखें",
          "स्थानीय गाइड रुपये 500-800 प्रति दिन",
          "होटल एडवांस बुकिंग जरूरी",
          "टोल पेमेंट के लिए FASTag रखें",
          "इमरजेंसी नंबर: 100 (पुलिस), 108 (एम्बुलेंस)"
        ]
      }
    ]
  }
},
    
    
    
    {
  "city": "Pune, India",
  "dates": "Oct 2 → Oct 10",
  "locations": "Kochi, Munnar, Thekkady, Alleppey, Trivandrum & 8 more",
  "notes": "Religious temples, elephant experiences, sunrise views, party spots - all using public transport",
  "tripDescription": {
    "title": "Your spiritual and adventurous journey to Kerala from Pune",
    "content": "Experience the perfect blend of spirituality and excitement in God's Own Country. This 9-day Kerala adventure combines sacred temple visits at Guruvayur and Padmanabhaswamy temples with thrilling elephant encounters in Thekkady and Munnar. Watch magnificent sunrises over Alleppey backwaters from traditional houseboats, explore vibrant nightlife in Kochi's Fort area, and witness majestic elephants at training centers and wildlife sanctuaries. Travel entirely by public transport using Kerala's excellent KSRTC bus network, trains, and ferries - making it both budget-friendly and authentic. From spiritual temple ceremonies to party nights in Kochi, elephant bathing experiences to serene backwater cruises, this itinerary offers the complete Kerala experience while maintaining your budget under ₹15,000 per person."
  },
  "tabs": [
    "Overview",
    "Itinerary",
    "Food",
    "Bookings",
    "Suggestions",
    "Locations",
    "Weather",
    "Packing",
    "Documents",
    "Budget",
    "Timelines",
    "Notifications"
  ],
  "tabContent": {
    "Overview": [
      {
        "type": "paragraph",
        "content": "Kerala in October offers the perfect post-monsoon weather with clear skies, pleasant temperatures (24-28°C), and lush green landscapes. This itinerary combines religious experiences at ancient temples, elephant encounters in wildlife sanctuaries, magical sunrises over backwaters, and vibrant nightlife in Kochi - all accessible through Kerala's excellent public transport network."
      },
      {
        "type": "list",
        "title": "Key Highlights:",
        "items": [
          "Sacred temples: Guruvayur Krishna Temple and Padmanabhaswamy Temple",
          "Elephant experiences: Thekkady wildlife sanctuary and Kodanad training center",
          "Sunrise views: Alleppey houseboat and backwater cruises",
          "Party scenes: Kochi nightlife and beach parties in Kovalam",
          "Public transport: KSRTC buses, trains, ferries - budget under ₹15,000"
        ]
      },
      {
        "type": "departure",
        "days": "9",
        "time": "22:50:00"
      }
    ],



    # "Itinerary": [
    #   {
    #     "type": "dailyItinerary",
    #     "days": [
    #       {
    #         "date": "Wednesday, Oct 2",
    #         "activities": [
    #           {
    #             "time": "22:50",
    #             "description": "Depart from Pune Junction by train",
    #             "details": "Board Poorna Express (11097) to Kochi\nJourney: 28 hours\nFare: ₹620 (Sleeper class)",
    #             "action": "Book tickets in advance",
    #             "type": "travel",
    #             "longDescription": "Begin your Kerala adventure with an overnight train journey from Pune to Kochi aboard the famous Poorna Express. The 28-hour journey offers scenic views of the Western Ghats and coastal plains."
    #           }
    #         ],
    #         "dailyCost": {
    #           "amount": "700",
    #           "currency": "₹",
    #           "details": "Train ticket: ₹620, Meals: ₹80"
    #         }
    #       },
    #       {
    #         "date": "Friday, Oct 4",
    #         "activities": [
    #           {
    #             "time": "03:15",
    #             "description": "Arrive at Ernakulam Junction, Kochi",
    #             "type": "start"
    #           },
    #           {
    #             "time": "09:00",
    #             "description": "Check into budget accommodation in Fort Kochi",
    #             "details": "Backpacker hostels: ₹800-1200 per night",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "11:00",
    #             "description": "Explore Fort Kochi heritage sites",
    #             "details": "Chinese Fishing Nets, Dutch Palace, Jewish Synagogue\nWalking tour of colonial architecture",
    #             "type": "activity",
    #             "longDescription": "Discover the rich colonial heritage of Fort Kochi with its iconic Chinese fishing nets, historic Dutch Palace with beautiful murals, and the ancient Jewish Synagogue with its blue and white tiles."
    #           },
    #           {
    #             "time": "13:00",
    #             "description": "Traditional Kerala lunch at local restaurant",
    #             "type": "food"
    #           },
    #           {
    #             "time": "15:00",
    #             "description": "Visit Marine Drive and local markets",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "19:00",
    #             "description": "Kathakali dance performance",
    #             "details": "Kerala Kathakali Center\nTicket: ₹150",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "21:30",
    #             "description": "Experience Kochi nightlife",
    #             "details": "Sky Grill Lounge or Clubb 18 for party atmosphere",
    #             "type": "activity"
    #           }
    #         ],
    #         "dailyCost": {
    #           "amount": "2200",
    #           "currency": "₹",
    #           "details": "Accommodation: ₹1000, Food: ₹600, Activities: ₹400, Local transport: ₹200"
    #         }
    #       },
    #       {
    #         "date": "Saturday, Oct 5",
    #         "activities": [
    #           {
    #             "time": "08:00",
    #             "description": "Travel to Guruvayur by KSRTC bus",
    #             "details": "Distance: 90km, Time: 2.5 hours\nBus fare: ₹80",
    #             "type": "travel",
    #             "longDescription": "Take a comfortable KSRTC bus from Kochi to the temple town of Guruvayur, famous for its Krishna temple and elephant sanctuary."
    #           },
    #           {
    #             "time": "11:00",
    #             "description": "Visit Guruvayur Krishna Temple",
    #             "details": "Dress code: Traditional attire mandatory\nMen: Dhoti, Women: Saree/Salwar",
    #             "type": "activity",
    #             "longDescription": "Experience the divine atmosphere at one of Kerala's most important Krishna temples. The temple opens at 3 AM for Nirmalya darshan and offers a deeply spiritual experience."
    #           },
    #           {
    #             "time": "13:00",
    #             "description": "Visit Punnathur Kotta Elephant Sanctuary",
    #             "details": "Entry: ₹30, 60+ temple elephants\nElephant feeding and interaction",
    #             "type": "activity",
    #             "longDescription": "Visit India's largest elephant sanctuary within the temple compound, home to over 60 temple elephants decorated for festivals. Watch elephant training and feeding sessions."
    #           },
    #           {
    #             "time": "15:00",
    #             "description": "Traditional Kerala vegetarian meal",
    #             "type": "food"
    #           },
    #           {
    #             "time": "17:00",
    #             "description": "Return to Kochi by bus",
    #             "type": "travel"
    #           },
    #           {
    #             "time": "20:00",
    #             "description": "Dinner at Mattancherry area",
    #             "type": "food"
    #           }
    #         ],
    #         "dailyCost": {
    #           "amount": "1800",
    #           "currency": "₹",
    #           "details": "Transport: ₹160, Temple entry: ₹30, Food: ₹500, Accommodation: ₹1000, Misc: ₹110"
    #         }
    #       },
    #       {
    #         "date": "Sunday, Oct 6",
    #         "activities": [
    #           {
    #             "time": "08:00",
    #             "description": "Travel to Munnar by KSRTC bus",
    #             "details": "Distance: 130km, Time: 4 hours\nFare: ₹120",
    #             "type": "travel",
    #             "longDescription": "Journey through scenic hill roads to Munnar, Kerala's famous hill station known for tea plantations and elephant sightings."
    #           },
    #           {
    #             "time": "13:00",
    #             "description": "Check into budget accommodation in Munnar",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "14:30",
    #             "description": "Lunch and rest",
    #             "type": "food"
    #           },
    #           {
    #             "time": "16:00",
    #             "description": "Visit Mattupetty Dam and elephant spotting",
    #             "details": "Entry: ₹20, Boating: ₹50\nWild elephant sightings common",
    #             "type": "activity",
    #             "longDescription": "Explore the scenic Mattupetty Dam area known for frequent wild elephant sightings. The area's natural salt licks attract elephants, especially during evening hours."
    #           },
    #           {
    #             "time": "18:30",
    #             "description": "Visit tea gardens and museum",
    #             "details": "Tea Museum entry: ₹100\nTea plantation tour",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "20:00",
    #             "description": "Dinner at local restaurant",
    #             "type": "food"
    #           }
    #         ],
    #         "dailyCost": {
    #           "amount": "2100",
    #           "currency": "₹",
    #           "details": "Transport: ₹120, Accommodation: ₹1200, Food: ₹500, Activities: ₹170, Local transport: ₹110"
    #         }
    #       },
    #       {
    #         "date": "Monday, Oct 7",
    #         "activities": [
    #           {
    #             "time": "06:00",
    #             "description": "Early morning sunrise viewing at Anamudi Peak viewpoint",
    #             "details": "Best sunrise views in Kerala hills\nLocal transport: ₹100",
    #             "type": "activity",
    #             "longDescription": "Experience breathtaking sunrise views from the highest peak viewpoint in South India. The early morning mist and golden light create magical photography opportunities."
    #           },
    #           {
    #             "time": "09:00",
    #             "description": "Travel to Thekkady by bus",
    #             "details": "Distance: 110km, Time: 3 hours\nFare: ₹100",
    #             "type": "travel"
    #           },
    #           {
    #             "time": "13:00",
    #             "description": "Check into accommodation near Periyar Wildlife Sanctuary",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "15:00",
    #             "description": "Periyar Wildlife Sanctuary boat safari",
    #             "details": "Entry: ₹45, Boat ride: ₹300\nElephant spotting from boat",
    #             "type": "activity",
    #             "longDescription": "Enjoy a boat safari on Periyar Lake within the wildlife sanctuary. The lake shores are frequented by wild elephants, offering excellent viewing opportunities from the safety of the boat."
    #           },
    #           {
    #             "time": "17:30",
    #             "description": "Visit Elephant Junction for close encounters",
    #             "details": "Packages: ₹400-6000\n1-hour program includes feeding and photos",
    #             "type": "activity",
    #             "longDescription": "Experience close elephant interactions including feeding, bathing, and photo sessions. Choose from various duration packages based on your interest and budget."
    #           },
    #           {
    #             "time": "20:00",
    #             "description": "Dinner with local entertainment",
    #             "type": "food"
    #           }
    #         ],
    #         "dailyCost": {
    #           "amount": "2300",
    #           "currency": "₹",
    #           "details": "Transport: ₹200, Accommodation: ₹1100, Activities: ₹745, Food: ₹500, Local transport: ₹100"
    #         }
    #       },
    #       {
    #         "date": "Tuesday, Oct 8",
    #         "activities": [
    #           {
    #             "time": "08:00",
    #             "description": "Travel to Alleppey by bus",
    #             "details": "Distance: 140km, Time: 4 hours\nFare: ₹130",
    #             "type": "travel"
    #           },
    #           {
    #             "time": "13:00",
    #             "description": "Check into houseboat for overnight stay",
    #             "details": "Deluxe houseboat: ₹4000-6000\nIncludes all meals and AC rooms",
    #             "action": "Book in advance",
    #             "type": "activity",
    #             "longDescription": "Board a traditional Kerala houseboat for an overnight cruise through the famous Alleppey backwaters. The floating hotel includes comfortable AC rooms, local meals, and stunning water views."
    #           },
    #           {
    #             "time": "14:00",
    #             "description": "Lunch on houseboat while cruising",
    #             "type": "food"
    #           },
    #           {
    #             "time": "16:00",
    #             "description": "Backwater cruise through canals and lakes",
    #             "details": "Visit Punnamada Lake, C Block, village areas\nWatch local life along waterways",
    #             "type": "activity",
    #             "longDescription": "Cruise through the intricate network of canals, lakes, and rivers. Pass by coconut groves, paddy fields, and traditional village life along the water's edge."
    #           },
    #           {
    #             "time": "18:30",
    #             "description": "Sunset viewing from houseboat deck",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "20:00",
    #             "description": "Traditional Kerala dinner on houseboat",
    #             "type": "food"
    #           },
    #           {
    #             "time": "22:00",
    #             "description": "Overnight stay anchored in peaceful backwaters",
    #             "type": "activity"
    #           }
    #         ],
    #         "dailyCost": {
    #           "amount": "5200",
    #           "currency": "₹",
    #           "details": "Transport: ₹130, Houseboat: ₹5000 (includes meals), Local transport: ₹70"
    #         }
    #       },
    #       {
    #         "date": "Wednesday, Oct 9",
    #         "activities": [
    #           {
    #             "time": "06:00",
    #             "description": "Magical sunrise over Alleppey backwaters",
    #             "details": "Wake up to golden sunrise reflecting on water\nBreakfast served while cruising",
    #             "type": "activity",
    #             "longDescription": "Experience one of Kerala's most beautiful sunrise views as golden light dances across the still backwaters. Traditional breakfast is served on deck as you cruise through morning mist."
    #           },
    #           {
    #             "time": "08:00",
    #             "description": "Morning cruise through SNDP canal and villages",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "09:00",
    #             "description": "Check out from houseboat at Alleppey",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "10:30",
    #             "description": "Travel to Trivandrum by train",
    #             "details": "Distance: 160km, Time: 3.5 hours\nFare: ₹100",
    #             "type": "travel"
    #           },
    #           {
    #             "time": "14:30",
    #             "description": "Check into accommodation in Trivandrum",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "16:00",
    #             "description": "Visit Padmanabhaswamy Temple",
    #             "details": "Dress code: Traditional attire\nOne of richest temples in world",
    #             "type": "activity",
    #             "longDescription": "Visit the famous Padmanabhaswamy Temple, dedicated to Lord Vishnu. This ancient temple is known for its intricate architecture and is considered one of the richest temples in the world."
    #           },
    #           {
    #             "time": "18:00",
    #             "description": "Explore Trivandrum city and markets",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "20:00",
    #             "description": "Dinner at local restaurant",
    #             "type": "food"
    #           }
    #         ],
    #         "dailyCost": {
    #           "amount": "1900",
    #           "currency": "₹",
    #           "details": "Transport: ₹100, Accommodation: ₹1000, Food: ₹500, Activities: ₹200, Local transport: ₹100"
    #         }
    #       },
    #       {
    #         "date": "Thursday, Oct 10",
    #         "activities": [
    #           {
    #             "time": "09:00",
    #             "description": "Visit Kovalam Beach",
    #             "details": "Distance: 16km by bus\nFare: ₹30",
    #             "type": "travel"
    #           },
    #           {
    #             "time": "10:00",
    #             "description": "Beach activities and water sports",
    #             "details": "Surfing, parasailing available\nBeach entry free",
    #             "type": "activity",
    #             "longDescription": "Enjoy the golden sands and clear waters of Kovalam Beach. Try water sports or simply relax on the beach before your evening departure."
    #           },
    #           {
    #             "time": "13:00",
    #             "description": "Seafood lunch at beach restaurant",
    #             "type": "food"
    #           },
    #           {
    #             "time": "15:00",
    #             "description": "Return to Trivandrum",
    #             "type": "travel"
    #           },
    #           {
    #             "time": "16:30",
    #             "description": "Last-minute shopping at Chalai Market",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "19:00",
    #             "description": "Travel to railway station",
    #             "type": "travel"
    #           },
    #           {
    #             "time": "20:30",
    #             "description": "Board train back to Pune",
    #             "details": "Kanyakumari Express (16381)\nJourney: 28 hours",
    #             "type": "travel",
    #             "longDescription": "Board the overnight train back to Pune, carrying wonderful memories of Kerala's temples, elephants, sunrises, and backwater experiences."
    #           }
    #         ],
    #         "dailyCost": {
    #           "amount": "1400",
    #           "currency": "₹",
    #           "details": "Transport: ₹700, Food: ₹400, Activities: ₹200, Shopping: ₹100"
    #         }
    #       }
    #     ]
    #   }
    # ],



  "Itinerary": [
    {
      "type": "dailyItinerary",
      "days": [
        {
          "date": "Wednesday, Oct 2",
          "activities": [
            {
              "time": "22:50",
              "description": "Depart from Pune Junction by train",
              "details": "Board Poorna Express (11097) to Kochi\nJourney: 28 hours\nFare: ₹620 (Sleeper class)",
              "action": "Book tickets in advance",
              "type": "travel",
              "longDescription": "Begin your Kerala adventure with an overnight train journey from Pune to Kochi aboard the famous Poorna Express. The 28-hour journey offers scenic views of the Western Ghats and coastal plains."
            }
          ],
          "dailyCost": {
            "amount": "700",
            "currency": "₹",
            "details": "Train ticket: ₹620, Meals: ₹80"
          },
          "locations": [
            { "latitude": 18.5289, "longitude": 73.8743, "name": "Pune Junction Railway Station" }
          ]
        },
        {
          "date": "Friday, Oct 4",
          "activities": [
            {
              "time": "03:15",
              "description": "Arrive at Ernakulam Junction, Kochi",
              "type": "start"
            },
            {
              "time": "09:00",
              "description": "Check into budget accommodation in Fort Kochi",
              "details": "Backpacker hostels: ₹800-1200 per night",
              "type": "activity"
            },
            {
              "time": "11:00",
              "description": "Explore Fort Kochi heritage sites",
              "details": "Chinese Fishing Nets, Dutch Palace, Jewish Synagogue\nWalking tour of colonial architecture",
              "type": "activity",
              "longDescription": "Discover the rich colonial heritage of Fort Kochi with its iconic Chinese fishing nets, historic Dutch Palace with beautiful murals, and the ancient Jewish Synagogue with its blue and white tiles."
            },
            {
              "time": "13:00",
              "description": "Traditional Kerala lunch at local restaurant",
              "type": "food"
            },
            {
              "time": "15:00",
              "description": "Visit Marine Drive and local markets",
              "type": "activity"
            },
            {
              "time": "19:00",
              "description": "Kathakali dance performance",
              "details": "Kerala Kathakali Center\nTicket: ₹150",
              "type": "activity"
            },
            {
              "time": "21:30",
              "description": "Experience Kochi nightlife",
              "details": "Sky Grill Lounge or Clubb 18 for party atmosphere",
              "type": "activity"
            }
          ],
          "dailyCost": {
            "amount": "2200",
            "currency": "₹",
            "details": "Accommodation: ₹1000, Food: ₹600, Activities: ₹400, Local transport: ₹200"
          },
          "locations": [
            { "latitude": 9.9699, "longitude": 76.2908, "name": "Ernakulam Junction" },
            { "latitude": 9.9658, "longitude": 76.2421, "name": "Fort Kochi" }
          ]
        },
        {
          "date": "Saturday, Oct 5",
          "activities": [
            {
              "time": "08:00",
              "description": "Travel to Guruvayur by KSRTC bus",
              "details": "Distance: 90km, Time: 2.5 hours\nBus fare: ₹80",
              "type": "travel",
              "longDescription": "Take a comfortable KSRTC bus from Kochi to the temple town of Guruvayur, famous for its Krishna temple and elephant sanctuary."
            },
            {
              "time": "11:00",
              "description": "Visit Guruvayur Krishna Temple",
              "details": "Dress code: Traditional attire mandatory\nMen: Dhoti, Women: Saree/Salwar",
              "type": "activity",
              "longDescription": "Experience the divine atmosphere at one of Kerala's most important Krishna temples. The temple opens at 3 AM for Nirmalya darshan and offers a deeply spiritual experience."
            },
            {
              "time": "13:00",
              "description": "Visit Punnathur Kotta Elephant Sanctuary",
              "details": "Entry: ₹30, 60+ temple elephants\nElephant feeding and interaction",
              "type": "activity",
              "longDescription": "Visit India's largest elephant sanctuary within the temple compound, home to over 60 temple elephants decorated for festivals. Watch elephant training and feeding sessions."
            },
            {
              "time": "15:00",
              "description": "Traditional Kerala vegetarian meal",
              "type": "food"
            },
            {
              "time": "17:00",
              "description": "Return to Kochi by bus",
              "type": "travel"
            },
            {
              "time": "20:00",
              "description": "Dinner at Mattancherry area",
              "type": "food"
            }
          ],
          "dailyCost": {
            "amount": "1800",
            "currency": "₹",
            "details": "Transport: ₹160, Temple entry: ₹30, Food: ₹500, Accommodation: ₹1000, Misc: ₹110"
          },
          "locations": [
            { "latitude": 10.5946, "longitude": 76.0390, "name": "Guruvayur Krishna Temple" }
          ]
        },
        {
          "date": "Sunday, Oct 6",
          "activities": [
            {
              "time": "08:00",
              "description": "Travel to Munnar by KSRTC bus",
              "details": "Distance: 130km, Time: 4 hours\nFare: ₹120",
              "type": "travel",
              "longDescription": "Journey through scenic hill roads to Munnar, Kerala's famous hill station known for tea plantations and elephant sightings."
            },
            {
              "time": "13:00",
              "description": "Check into budget accommodation in Munnar",
              "type": "activity"
            },
            {
              "time": "14:30",
              "description": "Lunch and rest",
              "type": "food"
            },
            {
              "time": "16:00",
              "description": "Visit Mattupetty Dam and elephant spotting",
              "details": "Entry: ₹20, Boating: ₹50\nWild elephant sightings common",
              "type": "activity",
              "longDescription": "Explore the scenic Mattupetty Dam area known for frequent wild elephant sightings. The area's natural salt licks attract elephants, especially during evening hours."
            },
            {
              "time": "18:30",
              "description": "Visit tea gardens and museum",
              "details": "Tea Museum entry: ₹100\nTea plantation tour",
              "type": "activity"
            },
            {
              "time": "20:00",
              "description": "Dinner at local restaurant",
              "type": "food"
            }
          ],
          "dailyCost": {
            "amount": "2100",
            "currency": "₹",
            "details": "Transport: ₹120, Accommodation: ₹1200, Food: ₹500, Activities: ₹170, Local transport: ₹110"
          },
          "locations": [
            { "latitude": 10.0892, "longitude": 77.0597, "name": "Munnar Hill Station" },
            { "latitude": 10.1060, "longitude": 77.1240, "name": "Mattupetty Dam" }
          ]
        },
        {
          "date": "Monday, Oct 7",
          "activities": [
            {
              "time": "06:00",
              "description": "Early morning sunrise viewing at Anamudi Peak viewpoint",
              "details": "Best sunrise views in Kerala hills\nLocal transport: ₹100",
              "type": "activity",
              "longDescription": "Experience breathtaking sunrise views from the highest peak viewpoint in South India. The early morning mist and golden light create magical photography opportunities."
            },
            {
              "time": "09:00",
              "description": "Travel to Thekkady by bus",
              "details": "Distance: 110km, Time: 3 hours\nFare: ₹100",
              "type": "travel"
            },
            {
              "time": "13:00",
              "description": "Check into accommodation near Periyar Wildlife Sanctuary",
              "type": "activity"
            },
            {
              "time": "15:00",
              "description": "Periyar Wildlife Sanctuary boat safari",
              "details": "Entry: ₹45, Boat ride: ₹300\nElephant spotting from boat",
              "type": "activity",
              "longDescription": "Enjoy a boat safari on Periyar Lake within the wildlife sanctuary. The lake shores are frequented by wild elephants, offering excellent viewing opportunities from the safety of the boat."
            },
            {
              "time": "17:30",
              "description": "Visit Elephant Junction for close encounters",
              "details": "Packages: ₹400-6000\n1-hour program includes feeding and photos",
              "type": "activity",
              "longDescription": "Experience close elephant interactions including feeding, bathing, and photo sessions. Choose from various duration packages based on your interest and budget."
            },
            {
              "time": "20:00",
              "description": "Dinner with local entertainment",
              "type": "food"
            }
          ],
          "dailyCost": {
            "amount": "2300",
            "currency": "₹",
            "details": "Transport: ₹200, Accommodation: ₹1100, Activities: ₹745, Food: ₹500, Local transport: ₹100"
          },
          "locations": [
            { "latitude": 9.6031, "longitude": 77.1615, "name": "Thekkady" },
            { "latitude": 9.5775, "longitude": 77.1800, "name": "Periyar Wildlife Sanctuary" }
          ]
        },
        {
          "date": "Tuesday, Oct 8",
          "activities": [
            {
              "time": "08:00",
              "description": "Travel to Alleppey by bus",
              "details": "Distance: 140km, Time: 4 hours\nFare: ₹130",
              "type": "travel"
            },
            {
              "time": "13:00",
              "description": "Check into houseboat for overnight stay",
              "details": "Deluxe houseboat: ₹4000-6000\nIncludes all meals and AC rooms",
              "action": "Book in advance",
              "type": "activity",
              "longDescription": "Board a traditional Kerala houseboat for an overnight cruise through the famous Alleppey backwaters. The floating hotel includes comfortable AC rooms, local meals, and stunning water views."
            },
            {
              "time": "14:00",
              "description": "Lunch on houseboat while cruising",
              "type": "food"
            },
            {
              "time": "16:00",
              "description": "Backwater cruise through canals and lakes",
              "details": "Visit Punnamada Lake, C Block, village areas\nWatch local life along waterways",
              "type": "activity",
              "longDescription": "Cruise through the intricate network of canals, lakes, and rivers. Pass by coconut groves, paddy fields, and traditional village life along the water's edge."
            },
            {
              "time": "18:30",
              "description": "Sunset viewing from houseboat deck",
              "type": "activity"
            },
            {
              "time": "20:00",
              "description": "Traditional Kerala dinner on houseboat",
              "type": "food"
            },
            {
              "time": "22:00",
              "description": "Overnight stay anchored in peaceful backwaters",
              "type": "activity"
            }
          ],
          "dailyCost": {
            "amount": "5200",
            "currency": "₹",
            "details": "Transport: ₹130, Houseboat: ₹5000 (includes meals), Local transport: ₹70"
          },
          "locations": [
            { "latitude": 9.5021, "longitude": 76.3511, "name": "Alleppey Backwaters" }
          ]
        },
        {
          "date": "Wednesday, Oct 9",
          "activities": [
            {
              "time": "06:00",
              "description": "Magical sunrise over Alleppey backwaters",
              "details": "Wake up to golden sunrise reflecting on water\nBreakfast served while cruising",
              "type": "activity",
              "longDescription": "Experience one of Kerala's most beautiful sunrise views as golden light dances across the still backwaters. Traditional breakfast is served on deck as you cruise through morning mist."
            },
            {
              "time": "08:00",
              "description": "Morning cruise through SNDP canal and villages",
              "type": "activity"
            },
            {
              "time": "09:00",
              "description": "Check out from houseboat at Alleppey",
              "type": "activity"
            },
            {
              "time": "10:30",
              "description": "Travel to Trivandrum by train",
              "details": "Distance: 160km, Time: 3.5 hours\nFare: ₹100",
              "type": "travel"
            },
            {
              "time": "14:30",
              "description": "Check into accommodation in Trivandrum",
              "type": "activity"
            },
            {
              "time": "16:00",
              "description": "Visit Padmanabhaswamy Temple",
              "details": "Dress code: Traditional attire\nOne of richest temples in world",
              "type": "activity",
              "longDescription": "Visit the famous Padmanabhaswamy Temple, dedicated to Lord Vishnu. This ancient temple is known for its intricate architecture and is considered one of the richest temples in the world."
            },
            {
              "time": "18:00",
              "description": "Explore Trivandrum city and markets",
              "type": "activity"
            },
            {
              "time": "20:00",
              "description": "Dinner at local restaurant",
              "type": "food"
            }
          ],
          "dailyCost": {
            "amount": "1900",
            "currency": "₹",
            "details": "Transport: ₹100, Accommodation: ₹1000, Food: ₹500, Activities: ₹200, Local transport: ₹100"
          },
          "locations": [
            { "latitude": 8.5241, "longitude": 76.9366, "name": "Thiruvananthapuram (Trivandrum)" },
            { "latitude": 8.4828, "longitude": 76.9464, "name": "Padmanabhaswamy Temple" }
          ]
        },
        {
          "date": "Thursday, Oct 10",
          "activities": [
            {
              "time": "09:00",
              "description": "Visit Kovalam Beach",
              "details": "Distance: 16km by bus\nFare: ₹30",
              "type": "travel"
            },
            {
              "time": "10:00",
              "description": "Beach activities and water sports",
              "details": "Surfing, parasailing available\nBeach entry free",
              "type": "activity",
              "longDescription": "Enjoy the golden sands and clear waters of Kovalam Beach. Try water sports or simply relax on the beach before your evening departure."
            },
            {
              "time": "13:00",
              "description": "Seafood lunch at beach restaurant",
              "type": "food"
            },
            {
              "time": "15:00",
              "description": "Return to Trivandrum",
              "type": "travel"
            },
            {
              "time": "16:30",
              "description": "Last-minute shopping at Chalai Market",
              "type": "activity"
            },
            {
              "time": "19:00",
              "description": "Travel to railway station",
              "type": "travel"
            },
            {
              "time": "20:30",
              "description": "Board train back to Pune",
              "details": "Kanyakumari Express (16381)\nJourney: 28 hours",
              "type": "travel",
              "longDescription": "Board the overnight train back to Pune, carrying wonderful memories of Kerala's temples, elephants, sunrises, and backwater experiences."
            }
          ],
          "dailyCost": {
            "amount": "1400",
            "currency": "₹",
            "details": "Transport: ₹700, Food: ₹400, Activities: ₹200, Shopping: ₹100"
          },
          "locations": [
            { "latitude": 8.3895, "longitude": 76.9756, "name": "Kovalam Beach" }
          ]
        }
      ]
    }
  ],
    "Food": [
      {
        "type": "heading",
        "content": "Traditional Kerala Cuisine Experiences"
      },
      {
        "type": "item",
        "name": "Kerala Sadya",
        "description": "Traditional vegetarian feast served on banana leaf with over 20 dishes including sambar, rasam, aviyal, and payasam.",
        "recommendation": "Must try at temple festivals or traditional restaurants."
      },
      {
        "type": "item",
        "name": "Karimeen Fish Curry",
        "description": "Pearl spot fish cooked in coconut milk with Kerala spices, a backwater specialty.",
        "recommendation": "Best enjoyed on houseboats in Alleppey."
      },
      {
        "type": "item",
        "name": "Appam with Stew",
        "description": "Fermented rice pancakes served with vegetable or meat stew in coconut milk.",
        "recommendation": "Perfect breakfast option available everywhere."
      },
      {
        "type": "item",
        "name": "Puttu and Kadala Curry",
        "description": "Steamed rice cake served with spicy black chickpea curry.",
        "recommendation": "Traditional breakfast, best at local eateries."
      },
      {
        "type": "item",
        "name": "Kerala Parotta with Beef Curry",
        "description": "Flaky layered bread served with spicy beef curry, a popular dinner combination.",
        "recommendation": "Available at local restaurants and street food stalls."
      }
    ],
    "Bookings": [
      {
        "type": "heading",
        "content": "Essential Bookings for Your Kerala Trip"
      },
      {
        "type": "booking",
        "service": "Train",
        "details": "Pune to Kochi - Poorna Express (11097), Oct 2, 22:50",
        "status": "To be booked",
        "bookingId": "TRAIN001"
      },
      {
        "type": "booking",
        "service": "Train",
        "details": "Trivandrum to Pune - Kanyakumari Express (16381), Oct 10, 20:30",
        "status": "To be booked",
        "bookingId": "TRAIN002"
      },
      {
        "type": "booking",
        "service": "Houseboat",
        "details": "Alleppey Overnight Houseboat, Oct 8-9",
        "status": "To be booked",
        "bookingId": "BOAT001"
      },
      {
        "type": "packageBooking",
        "service": "Elephant Experience Package",
        "details": "Thekkady Elephant Junction 1-hour program",
        "status": "To be booked",
        "bookingId": "ELEPHANT001",
        "savings": {
          "amount": "200",
          "currency": "₹"
        },
        "message": "Book combined temple and elephant sanctuary tour to save ₹200!"
      },
      {
        "type": "bookingConfirmation",
        "confirmedMessage": "Public transport tickets can be booked on arrival for flexibility!",
        "referenceNo": "KERALA2024",
        "emailMessage": "KSRTC buses don't require advance booking for most routes"
      }
    ],
    "Suggestions": [
      {
        "type": "heading",
        "content": "Additional Experiences to Consider"
      },
      {
        "type": "suggestion",
        "title": "Thrissur Pooram Festival (if timing aligns)",
        "description": "Witness Kerala's most spectacular temple festival with decorated elephants and traditional music.",
        "category": "Cultural Experience"
      },
      {
        "type": "suggestion",
        "title": "Ayurvedic Massage on Houseboat",
        "description": "Add rejuvenating traditional massage service during your backwater cruise.",
        "category": "Wellness"
      },
      {
        "type": "suggestion",
        "title": "Sunrise Kayaking in Alleppey",
        "description": "Early morning kayaking through narrow canals for intimate backwater experience.",
        "category": "Adventure"
      },
      {
        "type": "suggestion",
        "title": "Kochi Water Metro Experience",
        "description": "Use Kerala's modern water transport system to explore Kochi's islands.",
        "category": "Transportation"
      },
      {
        "type": "suggestion",
        "title": "Local Cooking Class",
        "description": "Learn to prepare traditional Kerala dishes with local families.",
        "category": "Cultural Experience"
      }
    ],
    "Locations": [
      {
        "type": "heading",
        "content": "Key Destinations on Your Kerala Journey"
      },
      {
        "type": "location",
        "name": "Guruvayur Krishna Temple",
        "description": "Ancient temple dedicated to Lord Krishna, famous for its spiritual significance and elephant sanctuary.",
        "coordinates": "10.5918° N, 76.0362° E"
      },
      {
        "type": "location",
        "name": "Periyar Wildlife Sanctuary, Thekkady",
        "description": "Premier wildlife sanctuary known for elephant sightings during boat safaris on Periyar Lake.",
        "coordinates": "9.4647° N, 77.2553° E"
      },
      {
        "type": "location",
        "name": "Alleppey Backwaters",
        "description": "Venice of the East, famous for houseboat cruises and sunrise views over interconnected waterways.",
        "coordinates": "9.4981° N, 76.3388° E"
      },
      {
        "type": "location",
        "name": "Fort Kochi",
        "description": "Historic area with colonial architecture, Chinese fishing nets, and vibrant nightlife scene.",
        "coordinates": "9.9649° N, 76.2479° E"
      },
      {
        "type": "location",
        "name": "Mattupetty Hills, Munnar",
        "description": "Hill station known for tea plantations, dam, and frequent wild elephant sightings.",
        "coordinates": "10.0889° N, 77.0595° E"
      },
      {
        "type": "location",
        "name": "Padmanabhaswamy Temple, Trivandrum",
        "description": "Ancient temple dedicated to Lord Vishnu, known for its architectural grandeur and spiritual importance.",
        "coordinates": "8.4823° N, 76.9475° E"
      }
    ],
    "Weather": [
      {
        "type": "heading",
        "content": "October Weather in Kerala"
      },
      {
        "type": "weather",
        "city": "Kochi",
        "icon": "☀️",
        "temperature": "24-28°C"
      },
      {
        "type": "weather",
        "city": "Munnar",
        "icon": "🌤️",
        "temperature": "15-22°C"
      },
      {
        "type": "weather",
        "city": "Thekkady",
        "icon": "☁️",
        "temperature": "20-26°C"
      },
      {
        "type": "weather",
        "city": "Alleppey",
        "icon": "☀️",
        "temperature": "25-29°C"
      },
      {
        "type": "weather",
        "city": "Trivandrum",
        "icon": "⛅",
        "temperature": "24-30°C"
      }
    ],
    "Packing": [
      {
        "type": "heading",
        "content": "Kerala Trip Packing Checklist"
      },
      {
        "type": "item",
        "name": "Traditional attire (Dhoti/Saree for temples)",
        "checked": "false"
      },
      {
        "type": "item",
        "name": "Comfortable walking shoes",
        "checked": "false"
      },
      {
        "type": "item",
        "name": "Light cotton clothes",
        "checked": "false"
      },
      {
        "type": "item",
        "name": "Rain jacket (just in case)",
        "checked": "false"
      },
      {
        "type": "item",
        "name": "Sunscreen and hat",
        "checked": "false"
      },
      {
        "type": "item",
        "name": "Camera with waterproof cover",
        "checked": "false"
      },
      {
        "type": "item",
        "name": "Power bank",
        "checked": "false"
      },
      {
        "type": "item",
        "name": "Personal medications",
        "checked": "false"
      },
      {
        "type": "item",
        "name": "Mosquito repellent",
        "checked": "false"
      },
      {
        "type": "item",
        "name": "Quick-dry towel",
        "checked": "false"
      }
    ],
    "Documents": [
      {
        "type": "heading",
        "content": "Required Documents"
      },
      {
        "type": "document",
        "name": "Train Tickets (PDF)",
        "icon": "🚂"
      },
      {
        "type": "document",
        "name": "Hotel Booking Confirmations",
        "icon": "🏨"
      },
      {
        "type": "document",
        "name": "ID Proof (Aadhar/Passport)",
        "icon": "📄"
      },
      {
        "type": "document",
        "name": "Houseboat Booking Voucher",
        "icon": "🛥️"
      },
      {
        "type": "document",
        "name": "Travel Insurance (recommended)",
        "icon": "📄"
      },
      {
        "type": "document",
        "name": "Emergency Contact Numbers",
        "icon": "📞"
      }
    ],
    "Budget": [
      {
        "type": "heading",
        "content": "Total Trip Budget Breakdown"
      },
      {
        "type": "budget",
        "spent": "0",
        "total": "18000",
        "currency": "₹"
      },
      {
        "type": "paragraph",
        "content": "Budget breakdown per person: Transportation (₹1,540), Accommodation (₹7,300), Food (₹3,500), Activities (₹2,660), Houseboat (₹5,000). Total estimated cost: ₹18,000 per person for 9 days including all major experiences."
      }
    ],
    "Timelines": [
      {
        "type": "heading",
        "content": "Pre-trip Preparation Timeline"
      },
      {
        "type": "timeline",
        "items": [
          "3 weeks before: Book train tickets (Pune-Kochi, Trivandrum-Pune)",
          "2 weeks before: Reserve Alleppey houseboat for overnight stay",
          "1 week before: Download KSRTC bus app and check routes",
          "3 days before: Pack traditional clothes for temple visits",
          "1 day before: Check weather forecast and local transportation"
        ]
      }
    ],
    "Notifications": [
      {
        "type": "heading",
        "content": "Important Travel Reminders"
      },
      {
        "type": "notification",
        "items": [
          "Temple dress code strictly enforced - carry traditional attire",
          "Elephant activities weather dependent - have backup plans",
          "Houseboat sunrise views best in clear weather - check forecast",
          "KSRTC buses don't require advance booking for most routes",
          "Keep ID proof for train travel and hotel check-ins"
        ]
      }
    ]
  }
},{
  "city": "Pune to Konkan, Maharashtra",
  "dates": "Sep 20 → Sep 30",
  "locations": "Alibaug, Ganpatipule, Ratnagiri, Tarkarli, Malvan, Harihareshwar, Dapoli & 8 more",
  "notes": "Monsoon season ending - expect scattered showers but lush green landscapes. Pack rain gear and waterproof bags. Perfect time for waterfalls and scenic beauty.",
  "tripDescription": {
    "title": "Your Epic 10-Day Konkan Coast Boys Adventure - Maharashtra's Coastal Paradise",
    "content": "Experience the ultimate coastal adventure along Maharashtra's stunning Konkan coastline! This carefully crafted 10-day boys trip combines pristine beaches, historic sea forts, thrilling water sports, authentic Malvani cuisine, and unforgettable memories. From the serene temples of Ganpatipule to the adventure paradise of Tarkarli, explore hidden gems, indulge in fresh seafood, trek to ancient forts, and experience the raw beauty of monsoon-kissed landscapes. With a perfect mix of relaxation, adventure, culture, and camaraderie, this journey promises to be the ultimate coastal escape with your squad. The post-monsoon season offers the best of both worlds - lush green surroundings and clearing skies for perfect beach days and water activities."
  },
  "tabs": ["Overview", "Itinerary", "Food", "Bookings", "Suggestions", "Locations", "Weather", "Packing", "Documents", "Budget", "Timelines", "Notifications"],
  "tabContent": {
    "Overview": [
      {
        "type": "paragraph",
        "content": "This 10-day Konkan adventure is perfectly timed for late September when the monsoon is receding, leaving behind lush landscapes and perfect weather for exploration. You'll journey through Maharashtra's most stunning coastal destinations, from the popular beaches of Alibaug to the pristine waters of Tarkarli."
      },
      {
        "type": "list",
        "title": "Key Highlights:",
        "items": [
          "Historic sea forts of Murud-Janjira and Sindhudurg",
          "Pristine beaches and crystal clear waters",
          "Authentic Malvani seafood and Konkani cuisine",
          "Water sports and scuba diving at Tarkarli",
          "Sacred temples and cultural experiences",
          "Post-monsoon waterfalls and lush greenery"
        ]
      },
      {
        "type": "departure",
        "days": 10,
        "time": "06:30:00"
      }
    ],






    # "Itinerary": [
    #   {
    #     "type": "dailyItinerary",
    #     "days": [
    #       {
    #         "date": "Friday, Sep 20",
    #         "activities": [
    #           {
    #             "time": "06:30 am",
    #             "description": "Departure from Pune",
    #             "type": "start"
    #           },
    #           {
    #             "time": "",
    #             "description": "Drive to Alibaug via NH48 and SH92",
    #             "details": "Approx Distance: 150 Km\nApprox Time: 3.5 hrs\nPrivate AC Bus/Tempo Traveller",
    #             "action": "Book vehicle in advance",
    #             "type": "travel",
    #             "longDescription": "Start your Konkan adventure with a scenic drive through Maharashtra's countryside. The route takes you through rolling hills and rural landscapes before reaching the coastal town of Alibaug, your first stop on this epic journey."
    #           },
    #           {
    #             "time": "11:00 am",
    #             "description": "Check-in at group accommodation in Alibaug",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "12:30 pm",
    #             "description": "Lunch at local restaurant - try Konkani fish thali",
    #             "type": "food"
    #           },
    #           {
    #             "time": "02:00 pm",
    #             "description": "Visit Kolaba Fort (accessible during low tide)",
    #             "type": "activity",
    #             "longDescription": "Explore this historic sea fort built in 1662 by Chhatrapati Shivaji Maharaj. Walk across the water during low tide and discover ancient cannons, temples, and stunning sea views."
    #           },
    #           {
    #             "time": "04:30 pm",
    #             "description": "Alibaug Beach relaxation and beach volleyball",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "07:00 pm",
    #             "description": "Beachside dinner with fresh seafood",
    #             "type": "food"
    #           },
    #           {
    #             "time": "09:00 pm",
    #             "description": "Beach bonfire and group activities",
    #             "type": "activity"
    #           }
    #         ]
    #       },
    #       {
    #         "date": "Saturday, Sep 21",
    #         "activities": [
    #           {
    #             "time": "08:00 am",
    #             "description": "Breakfast and checkout",
    #             "type": "food"
    #           },
    #           {
    #             "time": "09:30 am",
    #             "description": "Visit Kihim Beach and explore Nagaon Beach",
    #             "type": "activity",
    #             "longDescription": "Experience the pristine beauty of Kihim Beach with its black sand and coconut groves, followed by the popular Nagaon Beach known for water sports."
    #           },
    #           {
    #             "time": "12:00 pm",
    #             "description": "Drive to Harihareshwar",
    #             "details": "Distance: 24 Km\nTime: 45 minutes",
    #             "type": "travel"
    #           },
    #           {
    #             "time": "01:00 pm",
    #             "description": "Lunch and check-in at Harihareshwar",
    #             "type": "food"
    #           },
    #           {
    #             "time": "03:00 pm",
    #             "description": "Visit Harihareshwar Temple (Dakshin Kashi)",
    #             "type": "activity",
    #             "longDescription": "Explore this ancient Shiva temple known as the 'Kashi of the South'. The temple complex offers spiritual tranquility and stunning coastal views."
    #           },
    #           {
    #             "time": "05:00 pm",
    #             "description": "Harihareshwar Beach and sunset viewing",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "07:30 pm",
    #             "description": "Dinner at local homestay",
    #             "type": "food"
    #           }
    #         ]
    #       },
    #       {
    #         "date": "Sunday, Sep 22",
    #         "activities": [
    #           {
    #             "time": "08:00 am",
    #             "description": "Breakfast and checkout",
    #             "type": "food"
    #           },
    #           {
    #             "time": "09:30 am",
    #             "description": "Drive to Dapoli",
    #             "details": "Distance: 65 Km\nTime: 1.5 hrs",
    #             "type": "travel"
    #           },
    #           {
    #             "time": "11:30 am",
    #             "description": "Visit Keshavraj Temple and explore Dapoli town",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "01:00 pm",
    #             "description": "Lunch at local restaurant",
    #             "type": "food"
    #           },
    #           {
    #             "time": "02:30 pm",
    #             "description": "Visit Anjarle Beach and possible dolphin spotting",
    #             "type": "activity",
    #             "longDescription": "Experience the untouched beauty of Anjarle Beach. During post-monsoon season, there's a good chance of spotting dolphins in the waters."
    #           },
    #           {
    #             "time": "05:00 pm",
    #             "description": "Check-in at Dapoli accommodation",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "07:00 pm",
    #             "description": "Group dinner with Konkani specialties",
    #             "type": "food"
    #           }
    #         ]
    #       },
    #       {
    #         "date": "Monday, Sep 23",
    #         "activities": [
    #           {
    #             "time": "08:00 am",
    #             "description": "Breakfast and checkout",
    #             "type": "food"
    #           },
    #           {
    #             "time": "09:30 am",
    #             "description": "Drive to Ganpatipule",
    #             "details": "Distance: 55 Km\nTime: 1.5 hrs",
    #             "type": "travel"
    #           },
    #           {
    #             "time": "11:30 am",
    #             "description": "Visit Swayambhu Ganpatipule Temple",
    #             "type": "activity",
    #             "longDescription": "Visit this 400-year-old temple with its self-manifested Ganesha idol. The temple is situated right on the beach, offering a unique spiritual experience by the sea."
    #           },
    #           {
    #             "time": "01:00 pm",
    #             "description": "Lunch at beachside restaurant",
    #             "type": "food"
    #           },
    #           {
    #             "time": "02:30 pm",
    #             "description": "Ganpatipule Beach activities and water sports",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "04:30 pm",
    #             "description": "Visit Prachin Konkan Museum",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "06:00 pm",
    #             "description": "Check-in at group accommodation",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "07:30 pm",
    #             "description": "Beachside dinner and evening relaxation",
    #             "type": "food"
    #           }
    #         ]
    #       },
    #       {
    #         "date": "Tuesday, Sep 24",
    #         "activities": [
    #           {
    #             "time": "09:00 am",
    #             "description": "Breakfast at accommodation",
    #             "type": "food"
    #           },
    #           {
    #             "time": "10:30 am",
    #             "description": "Visit Aare Ware Beach",
    #             "type": "activity",
    #             "longDescription": "Explore this secluded twin beach formed by mountain meeting the sea. Perfect for photography and peaceful moments away from crowds."
    #           },
    #           {
    #             "time": "12:30 pm",
    #             "description": "Visit Jaigad Fort and Lighthouse",
    #             "type": "activity",
    #             "longDescription": "Explore this 14th-century fort built on a cliff offering magnificent views of the Arabian Sea. The lighthouse provides panoramic coastal views."
    #           },
    #           {
    #             "time": "02:00 pm",
    #             "description": "Lunch at local dhaba",
    #             "type": "food"
    #           },
    #           {
    #             "time": "03:30 pm",
    #             "description": "Return to Ganpatipule for beach time",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "07:00 pm",
    #             "description": "Group dinner at accommodation",
    #             "type": "food"
    #           },
    #           {
    #             "time": "08:30 pm",
    #             "description": "Beach bonfire and music session",
    #             "type": "activity"
    #           }
    #         ]
    #       },
    #       {
    #         "date": "Wednesday, Sep 25",
    #         "activities": [
    #           {
    #             "time": "08:00 am",
    #             "description": "Breakfast and checkout",
    #             "type": "food"
    #           },
    #           {
    #             "time": "09:30 am",
    #             "description": "Drive to Ratnagiri",
    #             "details": "Distance: 25 Km\nTime: 45 minutes",
    #             "type": "travel"
    #           },
    #           {
    #             "time": "10:30 am",
    #             "description": "Visit Ratnadurg Fort",
    #             "type": "activity",
    #             "longDescription": "Explore this 16th-century fort that later became part of Shivaji's empire. The fort offers historical significance and coastal views."
    #           },
    #           {
    #             "time": "12:30 pm",
    #             "description": "Visit Thibaw Palace and Tilak Smarak",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "02:00 pm",
    #             "description": "Lunch featuring famous Alphonso mangoes (if in season)",
    #             "type": "food"
    #           },
    #           {
    #             "time": "03:30 pm",
    #             "description": "Bhatye Beach relaxation",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "05:30 pm",
    #             "description": "Check-in at Ratnagiri accommodation",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "07:00 pm",
    #             "description": "Dinner at coastal restaurant",
    #             "type": "food"
    #           }
    #         ]
    #       },
    #       {
    #         "date": "Thursday, Sep 26",
    #         "activities": [
    #           {
    #             "time": "07:30 am",
    #             "description": "Early breakfast and checkout",
    #             "type": "food"
    #           },
    #           {
    #             "time": "08:30 am",
    #             "description": "Drive to Tarkarli via Malvan",
    #             "details": "Distance: 225 Km\nTime: 5 hrs with breaks",
    #             "type": "travel",
    #             "longDescription": "Long but scenic drive through the Western Ghats and coastal roads. Multiple breaks for refreshments and sightseeing."
    #           },
    #           {
    #             "time": "02:00 pm",
    #             "description": "Arrival in Tarkarli and lunch",
    #             "type": "food"
    #           },
    #           {
    #             "time": "03:30 pm",
    #             "description": "Check-in at beach resort/homestay",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "04:30 pm",
    #             "description": "First taste of Tarkarli Beach",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "06:00 pm",
    #             "description": "Sunset watching and beach photography",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "07:30 pm",
    #             "description": "Welcome dinner with fresh Malvani seafood",
    #             "type": "food"
    #           }
    #         ]
    #       },
    #       {
    #         "date": "Friday, Sep 27",
    #         "activities": [
    #           {
    #             "time": "08:00 am",
    #             "description": "Breakfast at accommodation",
    #             "type": "food"
    #           },
    #           {
    #             "time": "09:30 am",
    #             "description": "Scuba Diving session at Tarkarli",
    #             "type": "activity",
    #             "longDescription": "Experience the underwater world of Tarkarli with professional instructors. See colorful coral reefs, tropical fish, and marine life in crystal clear waters."
    #           },
    #           {
    #             "time": "12:00 pm",
    #             "description": "Water sports - Parasailing, Jet Skiing, Banana Boat",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "02:00 pm",
    #             "description": "Lunch break at beach shack",
    #             "type": "food"
    #           },
    #           {
    #             "time": "03:30 pm",
    #             "description": "Visit to Sindhudurg Fort by boat",
    #             "type": "activity",
    #             "longDescription": "Take a boat ride to this magnificent sea fort built by Chhatrapati Shivaji Maharaj. Explore the fort's architecture and learn about Maratha naval history."
    #           },
    #           {
    #             "time": "06:30 pm",
    #             "description": "Return and rest time",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "08:00 pm",
    #             "description": "Group dinner with local Malvani specialties",
    #             "type": "food"
    #           }
    #         ]
    #       },
    #       {
    #         "date": "Saturday, Sep 28",
    #         "activities": [
    #           {
    #             "time": "09:00 am",
    #             "description": "Breakfast and leisurely morning",
    #             "type": "food"
    #           },
    #           {
    #             "time": "10:30 am",
    #             "description": "Visit Devbaugh Beach and backwaters",
    #             "type": "activity",
    #             "longDescription": "Explore the serene backwaters where the Karli River meets the Arabian Sea. Perfect for peaceful boat rides and bird watching."
    #           },
    #           {
    #             "time": "12:30 pm",
    #             "description": "Tsunami Island visit for more water sports",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "02:00 pm",
    #             "description": "Lunch at island restaurant",
    #             "type": "food"
    #           },
    #           {
    #             "time": "03:30 pm",
    #             "description": "Beach volleyball and group games",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "05:00 pm",
    #             "description": "Shopping for local souvenirs and cashew nuts",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "07:30 pm",
    #             "description": "Farewell dinner with cultural program",
    #             "type": "food"
    #           },
    #           {
    #             "time": "09:00 pm",
    #             "description": "Beach party and memories session",
    #             "type": "activity"
    #           }
    #         ]
    #       },
    #       {
    #         "date": "Sunday, Sep 29",
    #         "activities": [
    #           {
    #             "time": "09:00 am",
    #             "description": "Breakfast and checkout",
    #             "type": "food"
    #           },
    #           {
    #             "time": "10:30 am",
    #             "description": "Start return journey to Pune",
    #             "details": "Distance: 530 Km\nTime: 10-11 hrs with stops",
    #             "type": "travel",
    #             "longDescription": "Long journey back home with multiple stops for meals, rest, and sightseeing. Consider overnight halt at Kolhapur or Sangli if needed."
    #           },
    #           {
    #             "time": "01:00 pm",
    #             "description": "Lunch break in Kolhapur",
    #             "type": "food"
    #           },
    #           {
    #             "time": "04:00 pm",
    #             "description": "Tea break and rest",
    #             "type": "food"
    #           },
    #           {
    #             "time": "09:00 pm",
    #             "description": "Arrival in Pune",
    #             "type": "end"
    #           }
    #         ]
    #       }
    #     ]
    #   }
    # ]
    

    "Itinerary": [
  {
    "type": "dailyItinerary",
    "days": [
      {
        "date": "Friday, Sep 20",
        "activities": [
          {
            "time": "06:30 am",
            "description": "Departure from Pune",
            "type": "start"
          },
          {
            "time": "",
            "description": "Drive to Alibaug via NH48 and SH92",
            "details": "Approx Distance: 150 Km\nApprox Time: 3.5 hrs\nPrivate AC Bus/Tempo Traveller",
            "action": "Book vehicle in advance",
            "type": "travel",
            "longDescription": "Start your Konkan adventure with a scenic drive through Maharashtra's countryside. The route takes you through rolling hills and rural landscapes before reaching the coastal town of Alibaug, your first stop on this epic journey."
          },
          {
            "time": "11:00 am",
            "description": "Check-in at group accommodation in Alibaug",
            "type": "activity"
          },
          {
            "time": "12:30 pm",
            "description": "Lunch at local restaurant - try Konkani fish thali",
            "type": "food"
          },
          {
            "time": "02:00 pm",
            "description": "Visit Kolaba Fort (accessible during low tide)",
            "type": "activity",
            "longDescription": "Explore this historic sea fort built in 1662 by Chhatrapati Shivaji Maharaj. Walk across the water during low tide and discover ancient cannons, temples, and stunning sea views."
          },
          {
            "time": "04:30 pm",
            "description": "Alibaug Beach relaxation and beach volleyball",
            "type": "activity"
          },
          {
            "time": "07:00 pm",
            "description": "Beachside dinner with fresh seafood",
            "type": "food"
          },
          {
            "time": "09:00 pm",
            "description": "Beach bonfire and group activities",
            "type": "activity"
          }
        ],
        "locations": [
          { "latitude": 18.5204, "longitude": 73.8567, "name": "Pune City" },
          { "latitude": 18.6411, "longitude": 72.8758, "name": "Alibaug" },
          { "latitude": 18.6485, "longitude": 72.8725, "name": "Kolaba Fort" },
          { "latitude": 18.6412, "longitude": 72.8722, "name": "Alibaug Beach" }
        ]
      },
      {
        "date": "Saturday, Sep 21",
        "activities": [
          {
            "time": "08:00 am",
            "description": "Breakfast and checkout",
            "type": "food"
          },
          {
            "time": "09:30 am",
            "description": "Visit Kihim Beach and explore Nagaon Beach",
            "type": "activity",
            "longDescription": "Experience the pristine beauty of Kihim Beach with its black sand and coconut groves, followed by the popular Nagaon Beach known for water sports."
          },
          {
            "time": "12:00 pm",
            "description": "Drive to Harihareshwar",
            "details": "Distance: 24 Km\nTime: 45 minutes",
            "type": "travel"
          },
          {
            "time": "01:00 pm",
            "description": "Lunch and check-in at Harihareshwar",
            "type": "food"
          },
          {
            "time": "03:00 pm",
            "description": "Visit Harihareshwar Temple (Dakshin Kashi)",
            "type": "activity",
            "longDescription": "Explore this ancient Shiva temple known as the 'Kashi of the South'. The temple complex offers spiritual tranquility and stunning coastal views."
          },
          {
            "time": "05:00 pm",
            "description": "Harihareshwar Beach and sunset viewing",
            "type": "activity"
          },
          {
            "time": "07:30 pm",
            "description": "Dinner at local homestay",
            "type": "food"
          }
        ],
        "locations": [
          { "latitude": 18.7950, "longitude": 72.8977, "name": "Kihim Beach" },
          { "latitude": 18.5676, "longitude": 72.9061, "name": "Nagaon Beach" },
          { "latitude": 17.9963, "longitude": 73.0166, "name": "Harihareshwar" },
          { "latitude": 17.9986, "longitude": 73.0161, "name": "Harihareshwar Temple" },
          { "latitude": 17.9972, "longitude": 73.0182, "name": "Harihareshwar Beach" }
        ]
      },
      {
        "date": "Sunday, Sep 22",
        "activities": [
          {
            "time": "08:00 am",
            "description": "Breakfast and checkout",
            "type": "food"
          },
          {
            "time": "09:30 am",
            "description": "Drive to Dapoli",
            "details": "Distance: 65 Km\nTime: 1.5 hrs",
            "type": "travel"
          },
          {
            "time": "11:30 am",
            "description": "Visit Keshavraj Temple and explore Dapoli town",
            "type": "activity"
          },
          {
            "time": "01:00 pm",
            "description": "Lunch at local restaurant",
            "type": "food"
          },
          {
            "time": "02:30 pm",
            "description": "Visit Anjarle Beach and possible dolphin spotting",
            "type": "activity",
            "longDescription": "Experience the untouched beauty of Anjarle Beach. During post-monsoon season, there's a good chance of spotting dolphins in the waters."
          },
          {
            "time": "05:00 pm",
            "description": "Check-in at Dapoli accommodation",
            "type": "activity"
          },
          {
            "time": "07:00 pm",
            "description": "Group dinner with Konkani specialties",
            "type": "food"
          }
        ],
        "locations": [
          { "latitude": 17.7570, "longitude": 73.1865, "name": "Dapoli" },
          { "latitude": 17.7716, "longitude": 73.2071, "name": "Keshavraj Temple" },
          { "latitude": 17.8383, "longitude": 73.0964, "name": "Anjarle Beach" }
        ]
      },
      {
        "date": "Monday, Sep 23",
        "activities": [
          {
            "time": "08:00 am",
            "description": "Breakfast and checkout",
            "type": "food"
          },
          {
            "time": "09:30 am",
            "description": "Drive to Ganpatipule",
            "details": "Distance: 55 Km\nTime: 1.5 hrs",
            "type": "travel"
          },
          {
            "time": "11:30 am",
            "description": "Visit Swayambhu Ganpatipule Temple",
            "type": "activity",
            "longDescription": "Visit this 400-year-old temple with its self-manifested Ganesha idol. The temple is situated right on the beach, offering a unique spiritual experience by the sea."
          },
          {
            "time": "01:00 pm",
            "description": "Lunch at beachside restaurant",
            "type": "food"
          },
          {
            "time": "02:30 pm",
            "description": "Ganpatipule Beach activities and water sports",
            "type": "activity"
          },
          {
            "time": "04:30 pm",
            "description": "Visit Prachin Konkan Museum",
            "type": "activity"
          },
          {
            "time": "06:00 pm",
            "description": "Check-in at group accommodation",
            "type": "activity"
          },
          {
            "time": "07:30 pm",
            "description": "Beachside dinner and evening relaxation",
            "type": "food"
          }
        ],
        "locations": [
          { "latitude": 17.1473, "longitude": 73.2653, "name": "Ganpatipule" },
          { "latitude": 17.1450, "longitude": 73.2709, "name": "Swayambhu Ganpati Temple" },
          { "latitude": 17.1446, "longitude": 73.2672, "name": "Ganpatipule Beach" },
          { "latitude": 17.1492, "longitude": 73.2707, "name": "Prachin Konkan Museum" }
        ]
      },
      {
        "date": "Tuesday, Sep 24",
        "activities": [
          {
            "time": "09:00 am",
            "description": "Breakfast at accommodation",
            "type": "food"
          },
          {
            "time": "10:30 am",
            "description": "Visit Aare Ware Beach",
            "type": "activity",
            "longDescription": "Explore this secluded twin beach formed by mountain meeting the sea. Perfect for photography and peaceful moments away from crowds."
          },
          {
            "time": "12:30 pm",
            "description": "Visit Jaigad Fort and Lighthouse",
            "type": "activity",
            "longDescription": "Explore this 14th-century fort built on a cliff offering magnificent views of the Arabian Sea. The lighthouse provides panoramic coastal views."
          },
          {
            "time": "02:00 pm",
            "description": "Lunch at local dhaba",
            "type": "food"
          },
          {
            "time": "03:30 pm",
            "description": "Return to Ganpatipule for beach time",
            "type": "activity"
          },
          {
            "time": "07:00 pm",
            "description": "Group dinner at accommodation",
            "type": "food"
          },
          {
            "time": "08:30 pm",
            "description": "Beach bonfire and music session",
            "type": "activity"
          }
        ],
        "locations": [
          { "latitude": 17.1078, "longitude": 73.2506, "name": "Aare Ware Beach" },
          { "latitude": 17.3051, "longitude": 73.2201, "name": "Jaigad Fort" },
          { "latitude": 17.3061, "longitude": 73.2188, "name": "Jaigad Lighthouse" }
        ]
      },
      {
        "date": "Wednesday, Sep 25",
        "activities": [
          {
            "time": "08:00 am",
            "description": "Breakfast and checkout",
            "type": "food"
          },
          {
            "time": "09:30 am",
            "description": "Drive to Ratnagiri",
            "details": "Distance: 25 Km\nTime: 45 minutes",
            "type": "travel"
          },
          {
            "time": "10:30 am",
            "description": "Visit Ratnadurg Fort",
            "type": "activity",
            "longDescription": "Explore this 16th-century fort that later became part of Shivaji's empire. The fort offers historical significance and coastal views."
          },
          {
            "time": "12:30 pm",
            "description": "Visit Thibaw Palace and Tilak Smarak",
            "type": "activity"
          },
          {
            "time": "02:00 pm",
            "description": "Lunch featuring famous Alphonso mangoes (if in season)",
            "type": "food"
          },
          {
            "time": "03:30 pm",
            "description": "Bhatye Beach relaxation",
            "type": "activity"
          },
          {
            "time": "05:30 pm",
            "description": "Check-in at Ratnagiri accommodation",
            "type": "activity"
          },
          {
            "time": "07:00 pm",
            "description": "Dinner at coastal restaurant",
            "type": "food"
          }
        ],
        "locations": [
          { "latitude": 16.9944, "longitude": 73.3006, "name": "Ratnagiri" },
          { "latitude": 16.9898, "longitude": 73.2828, "name": "Ratnadurg Fort" },
          { "latitude": 16.9875, "longitude": 73.3158, "name": "Thibaw Palace" },
          { "latitude": 16.9937, "longitude": 73.3179, "name": "Tilak Smarak" },
          { "latitude": 16.9946, "longitude": 73.3073, "name": "Bhatye Beach" }
        ]
      },
      {
        "date": "Thursday, Sep 26",
        "activities": [
          {
            "time": "07:30 am",
            "description": "Early breakfast and checkout",
            "type": "food"
          },
          {
            "time": "08:30 am",
            "description": "Drive to Tarkarli via Malvan",
            "details": "Distance: 225 Km\nTime: 5 hrs with breaks",
            "type": "travel",
            "longDescription": "Long but scenic drive through the Western Ghats and coastal roads. Multiple breaks for refreshments and sightseeing."
          },
          {
            "time": "02:00 pm",
            "description": "Arrival in Tarkarli and lunch",
            "type": "food"
          },
          {
            "time": "03:30 pm",
            "description": "Check-in at beach resort/homestay",
            "type": "activity"
          },
          {
            "time": "04:30 pm",
            "description": "First taste of Tarkarli Beach",
            "type": "activity"
          },
          {
            "time": "06:00 pm",
            "description": "Sunset watching and beach photography",
            "type": "activity"
          },
          {
            "time": "07:30 pm",
            "description": "Welcome dinner with fresh Malvani seafood",
            "type": "food"
          }
        ],
        "locations": [
          { "latitude": 16.0392, "longitude": 73.4627, "name": "Tarkarli Beach" },
          { "latitude": 16.0598, "longitude": 73.4753, "name": "Malvan" }
        ]
      },
      {
        "date": "Friday, Sep 27",
        "activities": [
          {
            "time": "08:00 am",
            "description": "Breakfast at accommodation",
            "type": "food"
          },
          {
            "time": "09:30 am",
            "description": "Scuba Diving session at Tarkarli",
            "type": "activity",
            "longDescription": "Experience the underwater world of Tarkarli with professional instructors. See colorful coral reefs, tropical fish, and marine life in crystal clear waters."
          },
          {
            "time": "12:00 pm",
            "description": "Water sports - Parasailing, Jet Skiing, Banana Boat",
            "type": "activity"
          },
          {
            "time": "02:00 pm",
            "description": "Lunch break at beach shack",
            "type": "food"
          },
          {
            "time": "03:30 pm",
            "description": "Visit to Sindhudurg Fort by boat",
            "type": "activity",
            "longDescription": "Take a boat ride to this magnificent sea fort built by Chhatrapati Shivaji Maharaj. Explore the fort's architecture and learn about Maratha naval history."
          },
          {
            "time": "06:30 pm",
            "description": "Return and rest time",
            "type": "activity"
          },
          {
            "time": "08:00 pm",
            "description": "Group dinner with local Malvani specialties",
            "type": "food"
          }
        ],
        "locations": [
          { "latitude": 16.0409, "longitude": 73.4629, "name": "Tarkarli" },
          { "latitude": 16.0130, "longitude": 73.4682, "name": "Sindhudurg Fort" }
        ]
      },
      {
        "date": "Saturday, Sep 28",
        "activities": [
          {
            "time": "09:00 am",
            "description": "Breakfast and leisurely morning",
            "type": "food"
          },
          {
            "time": "10:30 am",
            "description": "Visit Devbaugh Beach and backwaters",
            "type": "activity",
            "longDescription": "Explore the serene backwaters where the Karli River meets the Arabian Sea. Perfect for peaceful boat rides and bird watching."
          },
          {
            "time": "12:30 pm",
            "description": "Tsunami Island visit for more water sports",
            "type": "activity"
          },
          {
            "time": "02:00 pm",
            "description": "Lunch at island restaurant",
            "type": "food"
          },
          {
            "time": "03:30 pm",
            "description": "Beach volleyball and group games",
            "type": "activity"
          },
          {
            "time": "05:00 pm",
            "description": "Shopping for local souvenirs and cashew nuts",
            "type": "activity"
          },
          {
            "time": "07:30 pm",
            "description": "Farewell dinner with cultural program",
            "type": "food"
          },
          {
            "time": "09:00 pm",
            "description": "Beach party and memories session",
            "type": "activity"
          }
        ],
        "locations": [
          { "latitude": 16.0337, "longitude": 73.4902, "name": "Devbaugh Beach" },
          { "latitude": 16.0316, "longitude": 73.4954, "name": "Tsunami Island" }
        ]
      },
      {
        "date": "Sunday, Sep 29",
        "activities": [
          {
            "time": "09:00 am",
            "description": "Breakfast and checkout",
            "type": "food"
          },
          {
            "time": "10:30 am",
            "description": "Start return journey to Pune",
            "details": "Distance: 530 Km\nTime: 10-11 hrs with stops",
            "type": "travel",
            "longDescription": "Long journey back home with multiple stops for meals, rest, and sightseeing. Consider overnight halt at Kolhapur or Sangli if needed."
          },
          {
            "time": "01:00 pm",
            "description": "Lunch break in Kolhapur",
            "type": "food"
          },
          {
            "time": "04:00 pm",
            "description": "Tea break and rest",
            "type": "food"
          },
          {
            "time": "09:00 pm",
            "description": "Arrival in Pune",
            "type": "end"
          }
        ],
        "locations": [
          { "latitude": 16.7050, "longitude": 74.2433, "name": "Kolhapur" },
          { "latitude": 17.0527, "longitude": 74.4910, "name": "Sangli" },
          { "latitude": 18.5204, "longitude": 73.8567, "name": "Pune" }
        ]
      }
    ]
  }
]

    
    
    
    
    
    
    ,






    "Food": [
      {
        "type": "heading",
        "content": "Authentic Konkan & Malvani Culinary Experiences"
      },
      {
        "type": "item",
        "name": "Kombdi Vade",
        "description": "Traditional Malvani chicken curry served with fluffy fried bread (vade), onions, lemon, and sol kadhi. A signature dish of the region.",
        "recommendation": "Must try at Malvan or Tarkarli local restaurants."
      },
      {
        "type": "item",
        "name": "Fresh Seafood Thali",
        "description": "Complete meal featuring fish curry, fried fish, prawns, rice, bhakri, and sol kadhi. Different preparations available with pomfret, kingfish, or mackerel.",
        "recommendation": "Available at every coastal town - try different preparations."
      },
      {
        "type": "item",
        "name": "Sol Kadhi",
        "description": "Refreshing pink drink made from coconut milk and kokam fruit. Perfect coolant after spicy Malvani meals.",
        "recommendation": "Drink with every meal - aids digestion."
      },
      {
        "type": "item",
        "name": "Mori Masala (Shark Curry)",
        "description": "Spicy shark curry cooked in traditional Malvani style with coconut and red chilies. A coastal specialty.",
        "recommendation": "Try at specialized seafood restaurants in Malvan."
      },
      {
        "type": "item",
        "name": "Bangda Fry",
        "description": "Whole mackerel marinated in spices and shallow fried. Simple yet flavorful preparation popular throughout Konkan.",
        "recommendation": "Available at beach shacks and local eateries."
      },
      {
        "type": "item",
        "name": "Koliwada Prawns",
        "description": "Crispy fried prawns with spicy coating. Perfect snack with drinks by the beach.",
        "recommendation": "Best enjoyed fresh at beachside restaurants."
      }
    ],
    "Bookings": [
      {
        "type": "heading",
        "content": "Your Current Bookings"
      },
      {
        "type": "booking",
        "service": "Transport",
        "details": "Pune to Konkan AC Tempo Traveller (Sep 20-29)",
        "status": "To be confirmed",
        "bookingId": "TT-KON001"
      },
      {
        "type": "booking",
        "service": "Accommodation",
        "details": "Group Stay Alibaug (Sep 20-21)",
        "status": "Available",
        "bookingId": "ACC-ALB001"
      },
      {
        "type": "booking",
        "service": "Accommodation",
        "details": "Harihareshwar Homestay (Sep 21-22)",
        "status": "Available",
        "bookingId": "ACC-HAR002"
      },
      {
        "type": "booking",
        "service": "Accommodation",
        "details": "Dapoli Budget Hotel (Sep 22-23)",
        "status": "Available",
        "bookingId": "ACC-DAP003"
      },
      {
        "type": "booking",
        "service": "Accommodation",
        "details": "Ganpatipule Group Stay (Sep 23-25)",
        "status": "Available",
        "bookingId": "ACC-GAN004"
      },
      {
        "type": "booking",
        "service": "Accommodation",
        "details": "Ratnagiri Budget Hotel (Sep 25-26)",
        "status": "Available",
        "bookingId": "ACC-RAT005"
      },
      {
        "type": "booking",
        "service": "Accommodation",
        "details": "Tarkarli Beach Resort (Sep 26-29)",
        "status": "Available",
        "bookingId": "ACC-TAR006"
      },
      {
        "type": "packageBooking",
        "service": "Scuba Diving Package",
        "details": "Tarkarli Scuba Diving with Equipment & Training",
        "status": "Available for booking",
        "bookingId": "PKG-SCU007",
        "savings": {
          "amount": 500,
          "currency": "₹"
        },
        "message": "Group discount available for 10+ people!"
      },
      {
        "type": "bookingConfirmation",
        "confirmedMessage": "Booking Confirmed! Your coastal adventure begins on Sep 20, 2025.",
        "referenceNo": "KON2025",
        "emailMessage": "All itinerary details emailed to group leader"
      }
    ],
    "Suggestions": [
      {
        "type": "heading",
        "content": "Additional Experiences for Your Group"
      },
      {
        "type": "suggestion",
        "title": "Marleshwar Cave Temple Trek",
        "description": "Visit this unique cave temple with waterfall beside it. Perfect for adventure and spirituality combined.",
        "category": "Spiritual Adventure"
      },
      {
        "type": "suggestion",
        "title": "Dolphin Watching at Dapoli",
        "description": "Early morning boat rides offer chances to spot dolphins in their natural habitat during post-monsoon season.",
        "category": "Wildlife Experience"
      },
      {
        "type": "suggestion",
        "title": "Local Fishing Experience",
        "description": "Join local fishermen for early morning fishing trips and learn traditional coastal fishing methods.",
        "category": "Cultural Experience"
      },
      {
        "type": "suggestion",
        "title": "Cashew Factory Visit in Vengurla",
        "description": "Learn about cashew processing and buy fresh cashews directly from manufacturers.",
        "category": "Educational Tour"
      },
      {
        "type": "suggestion",
        "title": "Backwater Kayaking",
        "description": "Explore the serene backwaters of Tarkarli and Devbaugh by kayak for a peaceful water adventure.",
        "category": "Adventure Sport"
      }
    ],
    "Locations": [
      {
        "type": "heading",
        "content": "Key Destinations on Your Konkan Journey"
      },
      {
        "type": "location",
        "name": "Alibaug",
        "description": "Charming coastal town famous for Kolaba Fort, pristine beaches, and proximity to Mumbai.",
        "coordinates": "18.6414° N, 72.8722° E"
      },
      {
        "type": "location",
        "name": "Ganpatipule",
        "description": "Sacred coastal town with 400-year-old Ganesh temple, beautiful beaches, and cultural significance.",
        "coordinates": "17.1333° N, 73.2667° E"
      },
      {
        "type": "location",
        "name": "Tarkarli",
        "description": "Water sports paradise with crystal clear waters, coral reefs, and excellent scuba diving opportunities.",
        "coordinates": "15.9667° N, 73.4667° E"
      },
      {
        "type": "location",
        "name": "Harihareshwar",
        "description": "Known as 'Dakshin Kashi', famous for ancient Shiva temple and rocky coastline.",
        "coordinates": "17.9833° N, 73.0167° E"
      },
      {
        "type": "location",
        "name": "Sindhudurg Fort",
        "description": "Historic sea fort built by Chhatrapati Shivaji Maharaj, accessible by boat from Malvan.",
        "coordinates": "15.9667° N, 73.4500° E"
      },
      {
        "type": "location",
        "name": "Ratnagiri",
        "description": "Historic port city famous for Alphonso mangoes, forts, and Lokmanya Tilak's heritage.",
        "coordinates": "16.9944° N, 73.3006° E"
      }
    ],
    "Weather": [
      {
        "type": "heading",
        "content": "Weather Forecast for Your Trip Period"
      },
      {
        "type": "weather",
        "city": "Alibaug",
        "icon": "🌦️",
        "temperature": "24-30°C"
      },
      {
        "type": "weather",
        "city": "Ganpatipule",
        "icon": "☁️",
        "temperature": "23-29°C"
      },
      {
        "type": "weather",
        "city": "Tarkarli",
        "icon": "⛅",
        "temperature": "25-31°C"
      },
      {
        "type": "weather",
        "city": "Ratnagiri",
        "icon": "🌤️",
        "temperature": "24-30°C"
      }
    ],
    "Packing": [
      {
        "type": "heading",
        "content": "Essential Packing Checklist for Konkan Trip"
      },
      { "type": "item", "name": "Waterproof Rain Jacket", "checked": "false" },
      { "type": "item", "name": "Quick-dry Clothes", "checked": "false" },
      { "type": "item", "name": "Waterproof Bags for Electronics", "checked": "false" },
      { "type": "item", "name": "Comfortable Trekking Shoes", "checked": "false" },
      { "type": "item", "name": "Flip-flops for Beach", "checked": "false" },
      { "type": "item", "name": "Sunscreen (SPF 30+)", "checked": "false" },
      { "type": "item", "name": "Insect Repellent", "checked": "false" },
      { "type": "item", "name": "First Aid Kit", "checked": "false" },
      { "type": "item", "name": "Power Bank", "checked": "false" },
      { "type": "item", "name": "Camera with Waterproof Case", "checked": "false" },
      { "type": "item", "name": "Swimming Clothes", "checked": "false" },
      { "type": "item", "name": "Hat/Cap", "checked": "false" }
    ],
    "Documents": [
      {
        "type": "heading",
        "content": "Important Documents & Information"
      },
      { "type": "document", "name": "Group Travel Itinerary (PDF)", "icon": "📄" },
      { "type": "document", "name": "Emergency Contact Numbers", "icon": "📞" },
      { "type": "document", "name": "Hotel Booking Confirmations", "icon": "🏨" },
      { "type": "document", "name": "Transport Booking Voucher", "icon": "🚐" },
      { "type": "document", "name": "Travel Insurance Documents", "icon": "🛡️" },
      { "type": "document", "name": "Local Emergency Services Info", "icon": "🆘" }
    ],
    "Budget": [
      {
        "type": "heading",
        "content": "Budget Breakdown per Person"
      },
      {
        "type": "budget",
        "spent": 0,
        "total": 20000,
        "currency": "₹"
      }
    ],
    "Timelines": [
      {
        "type": "heading",
        "content": "Pre-Trip Timeline"
      },
      {
        "type": "timeline",
        "items": [
          { "date": "Sep 15", "task": "Confirm all bookings and group count", "status": "pending" },
          { "date": "Sep 17", "task": "Book transportation and first night accommodation", "status": "pending" },
          { "date": "Sep 18", "task": "Final packing and group coordination", "status": "pending" },
          { "date": "Sep 19", "task": "Check weather updates and prepare accordingly", "status": "pending" }
        ]
      }
    ],
    "Notifications": [
      {
        "type": "heading", 
        "content": "Important Reminders"
      },
      {
        "type": "notification",
        "message": "Weather Alert: Scattered showers expected Sep 20-22. Pack rain gear!",
        "priority": "high"
      },
      {
        "type": "notification", 
        "message": "Book scuba diving in advance at Tarkarli for group discounts",
        "priority": "medium"
      },
      {
        "type": "notification",
        "message": "Kolaba Fort accessible only during low tide - check tide timings",
        "priority": "medium"
      },
      {
        "type": "notification",
        "message": "Try to reach Sindhudurg Fort early to avoid crowds",
        "priority": "low"
      }
    ]
  }
}
,
{
  "city": "Shimla, India",
  "dates": "Sep 26 → Oct 1",
  "locations": "Mall Road, Jakhoo Hill, Kufri & 13 more",
  "notes": "Remember to carry light woolens and book train tickets in advance for best rates!",
  "tripDescription": {
    "title": "Your trip to Shimla - Scenic mountains and colonial charm",
    "content": "Enjoy a memorable 5-day group tour from Pune to Shimla, exploring breathtaking hills, historic temples, bustling bazaars, and adventure spots. Travel comfortably on a budget via India's public transport, stay at well-rated budget hotels near Mall Road, and savor local Himachali delicacies. This itinerary balances sightseeing, nature, and relaxation for groups and families."
  },
  "tabs": [
    "Overview",
    "Itinerary",
    "Food",
    "Bookings",
    "Suggestions",
    "Locations",
    "Weather",
    "Packing",
    "Documents",
    "Budget",
    "Timelines",
    "Notifications"
  ],
  "tabContent": {
    "Overview": [
      {
        "type": "paragraph",
        "content": "This group trip covers a scenic train and bus journey from Pune to Shimla via Chandigarh, with 4 nights in a central Shimla hotel. Experience Himalayan towns, colonial history, nature walks, panoramic viewpoints, shopping, and flavorful food in a compact and affordable itinerary."
      },
      {
        "type": "list",
        "title": "Key Highlights:",
        "items": [
          "Toy train or HRTC bus journey through the hills",
          "Historical sites: Jakhoo Temple, Christ Church, Viceregal Lodge",
          "Kufri adventure & Himalayan Bird Park",
          "Vibrant Mall Road shopping & cafes"
        ]
      },
      {
        "type": "departure",
        "days": 5,
        "time": "09:00:00"
      }
    ],




    # "Itinerary": [
    #   {
    #     "type": "dailyItinerary",
    #     "days": [
    #       {
    #         "date": "Friday, Sep 26",
    #         "activities": [
    #           {
    #             "time": "09:00 am",
    #             "description": "Take CDG Skranti Express from Pune Junction",
    #             "type": "start"
    #           },
    #           {
    #             "time": "",
    #             "description": "Board overnight train to Chandigarh",
    #             "details": "Departure: Pune Jn at 9:00 AM, Arrival: Chandigarh next day 3:45 PM, Cost: ₹745 (Sleeper)",
    #             "action": "Book ticket in advance",
    #             "type": "travel",
    #             "longDescription": "Enjoy India's diverse terrain on this scenic long-haul train journey to Chandigarh, your gateway to the Himalayas."
    #           }
    #         ]
    #       },
    #       {
    #         "date": "Saturday, Sep 27",
    #         "activities": [
    #           {
    #             "time": "03:45 pm",
    #             "description": "Arrive in Chandigarh, freshen up, HRTC bus to Shimla",
    #             "type": "travel"
    #           },
    #           {
    #             "time": "07:30 pm",
    #             "description": "Arrive in Shimla, check-in at hotel near Mall Road",
    #             "type": "checkin"
    #           },
    #           {
    #             "time": "08:30 pm",
    #             "description": "Stroll on Mall Road and sample street food",
    #             "type": "activity"
    #           }
    #         ]
    #       },
    #       {
    #         "date": "Sunday, Sep 28",
    #         "activities": [
    #           {
    #             "time": "09:30 am",
    #             "description": "Jakhoo Hill and Temple visit",
    #             "type": "activity",
    #             "longDescription": "Climb or cab-ride to the region's tallest hill, see the 33-meter Hanuman statue, panoramic valley views"
    #           },
    #           {
    #             "time": "01:00 pm",
    #             "description": "Lunch at Krishna Bakery, Mall Road",
    #             "type": "food"
    #           },
    #           {
    #             "time": "03:00 pm",
    #             "description": "The Ridge, Lakkar Bazaar shopping",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "05:00 pm",
    #             "description": "Indian Institute of Advanced Studies (Viceregal Lodge)",
    #             "type": "activity"
    #           }
    #         ]
    #       },
    #       {
    #         "date": "Monday, Sep 29",
    #         "activities": [
    #           {
    #             "time": "08:30 am",
    #             "description": "Day trip to Kufri - adventure park, yak rides, high-altitude zoo",
    #             "details": "Use local bus/taxi (₹80/₹120 one way)",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "12:30 pm",
    #             "description": "Lunch at a local dhaba in Kufri",
    #             "type": "food"
    #           },
    #           {
    #             "time": "03:30 pm",
    #             "description": "Himalayan Bird Park, Tara Devi Temple on return",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "07:00 pm",
    #             "description": "Dinner at Wake & Bake Café, Mall Road",
    #             "type": "food"
    #           }
    #         ]
    #       },
    #       {
    #         "date": "Tuesday, Sep 30",
    #         "activities": [
    #           {
    #             "time": "09:30 am",
    #             "description": "Pack, last-minute sightseeing or shopping near The Ridge",
    #             "type": "activity"
    #           },
    #           {
    #             "time": "01:30 pm",
    #             "description": "Take HRTC bus to Chandigarh",
    #             "type": "travel"
    #           },
    #           {
    #             "time": "05:30 pm",
    #             "description": "Board CDG Skranti Express train to Pune",
    #             "type": "travel"
    #           }
    #         ]
    #       }
    #     ]
    #   }
    # ]
    
    "Itinerary": [
  {
    "type": "dailyItinerary",
    "days": [
      {
        "date": "Friday, Sep 26",
        "activities": [
          {
            "time": "09:00 am",
            "description": "Take CDG Skranti Express from Pune Junction",
            "type": "start"
          },
          {
            "time": "",
            "description": "Board overnight train to Chandigarh",
            "details": "Departure: Pune Jn at 9:00 AM, Arrival: Chandigarh next day 3:45 PM, Cost: ₹745 (Sleeper)",
            "action": "Book ticket in advance",
            "type": "travel",
            "longDescription": "Enjoy India's diverse terrain on this scenic long-haul train journey to Chandigarh, your gateway to the Himalayas."
          }
        ],
        "locations": [
          { "latitude": 18.5289, "longitude": 73.8743, "name": "Pune Junction Railway Station" }
        ]
      },
      {
        "date": "Saturday, Sep 27",
        "activities": [
          {
            "time": "03:45 pm",
            "description": "Arrive in Chandigarh, freshen up, HRTC bus to Shimla",
            "type": "travel"
          },
          {
            "time": "07:30 pm",
            "description": "Arrive in Shimla, check-in at hotel near Mall Road",
            "type": "checkin"
          },
          {
            "time": "08:30 pm",
            "description": "Stroll on Mall Road and sample street food",
            "type": "activity"
          }
        ],
        "locations": [
          { "latitude": 30.7046, "longitude": 76.7179, "name": "Chandigarh Railway Station" },
          { "latitude": 31.1048, "longitude": 77.1734, "name": "Shimla Mall Road" }
        ]
      },
      {
        "date": "Sunday, Sep 28",
        "activities": [
          {
            "time": "09:30 am",
            "description": "Jakhoo Hill and Temple visit",
            "type": "activity",
            "longDescription": "Climb or cab-ride to the region's tallest hill, see the 33-meter Hanuman statue, panoramic valley views"
          },
          {
            "time": "01:00 pm",
            "description": "Lunch at Krishna Bakery, Mall Road",
            "type": "food"
          },
          {
            "time": "03:00 pm",
            "description": "The Ridge, Lakkar Bazaar shopping",
            "type": "activity"
          },
          {
            "time": "05:00 pm",
            "description": "Indian Institute of Advanced Studies (Viceregal Lodge)",
            "type": "activity"
          }
        ],
        "locations": [
          { "latitude": 31.1041, "longitude": 77.1855, "name": "Jakhoo Temple" },
          { "latitude": 31.1048, "longitude": 77.1734, "name": "Mall Road, Shimla" },
          { "latitude": 31.1045, "longitude": 77.1723, "name": "The Ridge, Shimla" },
          { "latitude": 31.0716, "longitude": 77.1515, "name": "Viceregal Lodge / Indian Institute of Advanced Studies" }
        ]
      },
      {
        "date": "Monday, Sep 29",
        "activities": [
          {
            "time": "08:30 am",
            "description": "Day trip to Kufri - adventure park, yak rides, high-altitude zoo",
            "details": "Use local bus/taxi (₹80/₹120 one way)",
            "type": "activity"
          },
          {
            "time": "12:30 pm",
            "description": "Lunch at a local dhaba in Kufri",
            "type": "food"
          },
          {
            "time": "03:30 pm",
            "description": "Himalayan Bird Park, Tara Devi Temple on return",
            "type": "activity"
          },
          {
            "time": "07:00 pm",
            "description": "Dinner at Wake & Bake Café, Mall Road",
            "type": "food"
          }
        ],
        "locations": [
          { "latitude": 31.0982, "longitude": 77.2674, "name": "Kufri" },
          { "latitude": 31.1000, "longitude": 77.1700, "name": "Himalayan Bird Park, Shimla" },
          { "latitude": 31.0599, "longitude": 77.1290, "name": "Tara Devi Temple" },
          { "latitude": 31.1048, "longitude": 77.1734, "name": "Wake & Bake Café, Mall Road" }
        ]
      },
      {
        "date": "Tuesday, Sep 30",
        "activities": [
          {
            "time": "09:30 am",
            "description": "Pack, last-minute sightseeing or shopping near The Ridge",
            "type": "activity"
          },
          {
            "time": "01:30 pm",
            "description": "Take HRTC bus to Chandigarh",
            "type": "travel"
          },
          {
            "time": "05:30 pm",
            "description": "Board CDG Skranti Express train to Pune",
            "type": "travel"
          }
        ],
        "locations": [
          { "latitude": 31.1045, "longitude": 77.1723, "name": "The Ridge, Shimla" },
          { "latitude": 30.7046, "longitude": 76.7179, "name": "Chandigarh Railway Station" },
          { "latitude": 18.5289, "longitude": 73.8743, "name": "Pune Junction Railway Station" }
        ]
      }
    ]
  }
]

    
    
    
    
    ,

    "Food": [
      {
        "type": "heading",
        "content": "Top Food Experiences in Shimla"
      },
      {
        "type": "item",
        "name": "Sidu",
        "description": "Traditional Himachali bread stuffed with walnuts and poppy seeds.",
        "recommendation": "Try at local dhabas."
      },
      {
        "type": "item",
        "name": "Madra",
        "description": "Punjab-influenced chickpea curry with rich Himachali spices.",
        "recommendation": "Taste authentic Madra at Krishna Bakery."
      },
      {
        "type": "item",
        "name": "Tibetan Momos",
        "description": "Steamed dumplings, vegetarian or chicken fillings.",
        "recommendation": "Street stalls on Mall Road, evening time."
      },
      {
        "type": "item",
        "name": "Chha Gosht",
        "description": "Marinated mutton curry local to Himachal.",
        "recommendation": "Try in small restaurants away from main tourist areas."
      }
    ],
    "Bookings": [
      {
        "type": "heading",
        "content": "Your Current Bookings"
      },
      {
        "type": "booking",
        "service": "Train",
        "details": "CDG Skranti Express, Pune to Chandigarh, Sep 26, 9:00 AM",
        "status": "Confirmed",
        "bookingId": "TRN123456"
      },
      {
        "type": "booking",
        "service": "Bus",
        "details": "HRTC Chandigarh to Shimla, Sep 27, 4:00 PM",
        "status": "Confirmed",
        "bookingId": "BUS654321"
      },
      {
        "type": "booking",
        "service": "Hotel",
        "details": "Hotel Silverine, Shimla (Sep 27 - Oct 1)",
        "status": "Confirmed",
        "bookingId": "HOT112233"
      }
    ],
    "Suggestions": [
      {
        "type": "heading",
        "content": "Suggestions for your group"
      },
      {
        "type": "suggestion",
        "title": "Try the Kalka-Shimla Toy Train",
        "description": "If time allows, experience the UNESCO-listed narrow gauge rail for views and nostalgia.",
        "category": "Scenic Journey"
      },
      {
        "type": "suggestion",
        "title": "Explore nearby Mashobra",
        "description": "Take a day trip to this peaceful, green village for forest walks and apple orchards.",
        "category": "Nature"
      },
      {
        "type": "suggestion",
        "title": "Evening at The Ridge",
        "description": "Unwind with great sunset views, live performances, and local snacks.",
        "category": "Relaxation"
      }
    ],
    "Locations": [
      {
        "type": "heading",
        "content": "Key Locations in Shimla"
      },
      {
        "type": "location",
        "name": "Mall Road",
        "description": "The heart of Shimla's shopping and social life; street food and cafes.",
        "coordinates": "31.1048° N, 77.1734° E"
      },
      {
        "type": "location",
        "name": "Jakhoo Hill",
        "description": "Highest peak, home to the Jakhoo temple and Hanuman statue.",
        "coordinates": "31.1084° N, 77.1817° E"
      },
      {
        "type": "location",
        "name": "Kufri",
        "description": "Hill station for adventure activities and stunning views.",
        "coordinates": "31.0982° N, 77.2674° E"
      },
      {
        "type": "location",
        "name": "Viceregal Lodge",
        "description": "Colonial-era building, now Institute of Advanced Studies.",
        "coordinates": "31.1044° N, 77.1270° E"
      }
    ],
    "Weather": [
      {
        "type": "heading",
        "content": "Weather Forecast"
      },
      {
        "type": "weather",
        "city": "Shimla",
        "icon": "🌤️",
        "temperature": "14–23°C (pleasant, crisp mornings)"
      },
      {
        "type": "weather",
        "city": "Kufri",
        "icon": "🌦️",
        "temperature": "10–18°C (carry light sweaters)"
      }
    ],
    "Packing": [
      {
        "type": "heading",
        "content": "Packing Checklist"
      },
      { "type": "item", "name": "Sweater/Light Woolen", "checked": "false" },
      { "type": "item", "name": "Comfortable Walking Shoes", "checked": "true" },
      { "type": "item", "name": "Umbrella/Raincoat", "checked": "false" },
      { "type": "item", "name": "Power Bank", "checked": "true" },
      { "type": "item", "name": "Reusable Water Bottle", "checked": "false" },
      { "type": "item", "name": "Sunscreen & Sunglasses", "checked": "false" },
      { "type": "item", "name": "ID Proof (Aadhaar/Passport)", "checked": "true" }
    ],
    "Documents": [
      {
        "type": "heading",
        "content": "Important Documents"
      },
      { "type": "document", "name": "Train E-Ticket (PDF)", "icon": "🚆" },
      { "type": "document", "name": "Bus Booking (PDF)", "icon": "🚌" },
      { "type": "document", "name": "Hotel Booking Confirmation", "icon": "🏨" },
      { "type": "document", "name": "Travel Insurance", "icon": "📄" }
    ],
    "Budget": [
      {
        "type": "heading",
        "content": "Budget Tracker"
      },
      {
        "type": "budget",
        "spent": 47450,
        "total": 50000,
        "currency": "₹"
      }
    ]
  }
}
]




trip_cards_data = [
  {
    "id": 1,
    "title": "My Europe Grand Tour",
    "description": "14 days, 7 cities, culture & cuisine across Europe.",
    "imageUrl": get_image_as_base64(os.path.join(IMAGE_BASE_PATH, "europe_trip.jpg"))
  },
  {
    "id": 2,
    "title": "Coastal California Road Trip",
    "description": "7 days of scenic drives and charming beach towns.",
    "imageUrl": get_image_as_base64(os.path.join(IMAGE_BASE_PATH, "california.jpg"))
  },
  {
    "id": 3,
    "title": "Japanese Cherry Blossom Adventure",
    "description": "10 days of ancient temples & modern Tokyo during cherry blossom season.",
    "imageUrl": get_image_as_base64(os.path.join(IMAGE_BASE_PATH, "japan_cherry_blosm.jpg"))
  }
]
