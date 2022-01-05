import sqlite3

conn = sqlite3.connect('Vocabulary.db')


print("Opened database successfully")


conn.execute('''CREATE TABLE VOCABULARY
         (ID INT PRIMARY KEY     NOT NULL,
         WORDS           TEXT    NOT NULL,
         MEANING         TEXT    NOT NULL
         );''')


conn.execute("INSERT INTO VOCABULARY (ID,WORDS,MEANING) \
      VALUES (1, 'Determined', 'निर्धारित')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS,MEANING) \
      VALUES (2, 'Unconquerable', 'अजेय')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (3, 'Turmoil', 'खलबली/घबराहट')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (4, 'Burden', 'बोझ')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS,MEANING) \
      VALUES (5, 'Antics', 'हरकतों')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS,MEANING) \
      VALUES (6, 'Obstacle', 'बाधा/रुकावट/अवरोध')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (7, 'Cultivation', 'खेती/खेती करना/कृषि')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (8, 'Civilize', 'सभ्य बनाना')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (9, 'Possessed', 'अधीन/प्राप्त')");

conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (10, 'Sprouted', 'अंकुरित')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (11, 'Misery','कष्ट/विपत्ति/मुसीबत')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (12, 'Assured', 'आश्वासन दिया/भरोसा दिलाना')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (13, 'Curse', 'कोसना/अपशब्द/शाप/अभिशाप')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (14, 'Innocent', 'मासूम/निर्दोष/बेकसूर')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (15, 'Scream', 'चीख/चिल्लाना/शोर मचाना')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (16, 'Symphony', 'स्वर का मिलान')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (17, 'Proverb', 'कहावत/लोकोक्ति')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (18, 'Clutches', 'चंगुल/क़ब्ज़ा करना/पकड़ना')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (19, 'Conceive', 'विचार करना/कल्पना करना')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (20, 'Shattered', 'टुकड़े टुकड़े होना/तोड़ना/')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (21, 'Grief', 'शोक/क्लेश/अफ़सोस')");

conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (22, 'Wondered', 'आश्चर्य')");	
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (23, 'Chores', 'घर का काम/रोज़ाना-काम')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (24, 'Approached', 'प्रस्ताव करना/निकट आना/पहुंचना')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (25, 'Narrated', 'वर्णित/बयान करना')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (26, 'Considered', 'विचार करना/समझना/सोचना')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (27, 'Poverty', 'गरीबी/कमी/तंगी')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (28, 'Declined', 'अस्वीकार करना/इंकार कर दिया/झुकना')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (29, 'Venture', 'व्यापार/कार्य/जोखिम का काम/सट्टेबाज़ी')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (30, 'Destiny', 'भाग्य/नियति/तक़दीर')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (31, 'Decades', 'दशक')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (32, 'Desire', 'इच्छा/अभिलाषा/तमन्ना/कामना करना')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (33, 'Beyond', 'के परे/से बाहर/से ऊपर')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (34, 'Disciple', 'शिष्य/विद्यार्थी/चेला/छात्र')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (35, 'Annoyed', 'नाराज/परेशान/हैरान')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (36, 'Keenly', 'गौर से')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (37, 'Humbly', 'विनम्रतापूर्वक/')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (38, 'Ditch', 'खाई/गड्ढा/')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (39, 'Drizzle', 'बूंदा बांदी/फुहार पड़ना')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (40, 'Drowsy', 'सुस्त/नींद से भरा हुआ')");

conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (41, 'Curtain', 'परदा')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (42, 'Interpret', 'व्याख्या')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (43, 'Exert', 'परिश्रम करना/बल लगाना')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (44, 'Flee', 'भाग जाना/चंपत हो जाना')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (45, 'Reservoir', 'जलाशय/तालाब/संग्रह')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (46, 'Undertaken', 'कार्य शुरू/आरंभ किया हुआ')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (47, 'Precision', 'शुद्धता/')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (48, 'Iconic', 'प्रतिष्ठित')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (49, 'Rural', 'ग्रामीण/देहाती')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (50, 'Asset', 'संपत्ति')");

conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (51, 'Gigantic', 'विशाल/बहुत बड़ा/महाकाय/भीमकाय')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (52, 'Pavement', 'फुटपाथ/रास्ते का फर्श')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (53, 'Whopping', 'भारी/मरम्मत/ठुकाई/हार')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (54, 'Tremendous', 'अद्भुत/भयंकर/डरावना')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (55, 'Demise', 'मृत्यु/निधन/वसीयत करना')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (56, 'Frenzy', 'पागलपन/बावलापन/आवेश')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (57, 'Upsurge', 'चढ़ाव/उन्नति/तरक़्क़ी')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (58, 'Prop', 'सहारा/आधार/खंभा')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (59, 'Infamous', 'बदनाम/कुख्यात/निर्लज्ज')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (60, 'Enormous', 'विशाल/बहुत बड़ा/असाधारण')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (61, 'Established', 'स्थापना/प्रमाणित/स्थापित')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (62, 'Emerge', 'निकलना/प्रकट होना/उभरना')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (63, 'Guise', 'भेष/वेष/पहनावा')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (64, 'Scenic', 'सुंदर/तमाशा या नाटक सम्बंधी/बनावटी')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (65, 'Portfolio', 'निवेश सूची/खुले पत्र')");

conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (66, 'Captivating', 'मनोरम/लुभावना/मोहन')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (67, 'Evolved', 'विकसित/प्रस्तुत/प्रकट करना')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (68, 'Leases', 'पट्टों')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (69, 'Bustling', 'हलचल')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (70, 'Ambition', 'महत्वाकांक्षा/अभिलाषा/लालसा')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (71, 'Greedy', 'लालची ')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (72, 'Worth', 'लायक/योग्य ')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (73, 'Revenge', 'बदला लेना')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (74, 'Satisfied', 'संतुष्ट/तृप्त')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (75, 'Dissatisfied', 'असंतुष्ट/नाखुश')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (76, 'Still', 'अभी तक/अभी भी')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (77, 'Know', 'जानना/मालूम होना')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (78, 'Tough', 'कठिन/कठोर/सख्त')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (79, 'a lot of', 'बहुत')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (80, 'Goal', 'लक्ष्य/उदेश्य')");

conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (81, 'Particular', 'विशेष/खास')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (82, 'Sensible', 'समझदार/अक्लमंद')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (83, 'Admire', 'तारीफ करना/सराहना करना')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (84, 'Constraints', 'अड़चन होती है/दबाव')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (85, 'Opportunity', 'मौका/अवसर')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (86, 'Hurry up', 'जल्दी करना/जल्दी करो')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (87, 'Interfere', 'दखल देना/हस्तक्षेप करना')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (88, 'Irritate', 'चिढाना/उकसाना/जलन पैदा करना')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (89, 'Intention', 'इरादा/नीयत/प्रयोजन/मुद्दा')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (90, 'Fellow', 'साथी/सदस्य/व्यक्ति/सहचर(मित्र)')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (91, 'vague', 'अस्पष्ट/अनिश्चित')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (92, 'Pride', 'गौरव/दिखाव/घमंड/गर्व करना/अभिमान')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (93, 'Assistance', 'सहायता/सहाय/')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (94, 'Casual', 'अनौपचारिक/यदाकदा/इत्तिफ़ाक़ का/')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (95, 'Defeat', 'हार/विफल करना/पराजित करना')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (96, 'Broods', 'अंडे सेना')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (97, 'Attitude', 'रवैया/मनोभाव')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (98, 'Gaiety', 'आमोद-प्रमोद/उल्लास/खुशी/आनंद')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (99, 'Spirit', 'आत्मा')");
conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
      VALUES (100, 'Obsessed', 'दिमाग़ में घर कर लेना/जुनू')");

# conn.execute("INSERT INTO VOCABULARY (ID,WORDS, MEANING) \
#       VALUES ()");

conn.commit()



#------------------------------------------------------------------------------------------------------------------------
# cursor = conn.execute("SELECT id, words, meaning from VOCABULARY")

# cursor = conn.execute("SELECT id, words, meaning from VOCABULARY ORDER BY RANDOM() LIMIT 1")

# for row in cursor:
#    print("ID = ", row[0])
#    print("WORDS = ", row[1])
#    print("MEANING = ", row[2], "\n")
print("Operation done successfully")