
import streamlit as st
import random
import html
from io import BytesIO

# Optional voice narration
try:
    from gtts import gTTS
    GTTS_AVAILABLE = True
except ImportError:
    GTTS_AVAILABLE = False


# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="ItihasQuest | Stories of Wisdom",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# VISUAL DESIGN
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700;800&family=Nunito:wght@400;500;600;700;800&display=swap');

:root {
    --gold: #f6c66b;
    --cream: #fff2d5;
    --ink: #281b32;
    --purple: #24172f;
}

.stApp {
    background:
        radial-gradient(ellipse at top left, #55314f 0%, transparent 38%),
        radial-gradient(ellipse at bottom right, #5a392c 0%, transparent 32%),
        linear-gradient(135deg, #171222, #28182e 55%, #211622);
    color: #fff5e7;
    font-family: 'Nunito', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

h1, h2, h3 {
    font-family: 'Cinzel', serif !important;
    color: #ffe2a0 !important;
}

p, label, li {
    color: #f8eadb;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #21142c, #302037);
    border-right: 1px solid #80613c;
}

[data-testid="stSidebar"] * {
    color: #fff0d8;
}

.hero {
    position: relative;
    overflow: hidden;
    padding: 44px 36px;
    border: 1px solid #d4a75e;
    border-radius: 28px;
    background:
        radial-gradient(circle at 85% 25%, #f4c87535, transparent 24%),
        linear-gradient(120deg, #49264c, #291a35 60%, #573526);
    box-shadow: 0 18px 55px #00000045;
    margin-bottom: 26px;
}

.hero:after {
    content: "✦  ☼  ✧  ॐ  ✧";
    position: absolute;
    right: 18px;
    bottom: 5px;
    font-size: 34px;
    letter-spacing: 12px;
    color: #ffdc8b;
    opacity: .20;
}

.eyebrow {
    color: #f4ca7b;
    text-transform: uppercase;
    letter-spacing: 4px;
    font-size: 12px;
    font-weight: 800;
}

.hero h1 {
    font-size: clamp(32px, 5vw, 60px);
    line-height: 1.12;
    margin: 14px 0;
}

.hero p {
    font-size: 17px;
    line-height: 1.8;
    max-width: 750px;
    color: #f9e9d5;
}

.section-label {
    text-transform: uppercase;
    letter-spacing: 3px;
    font-size: 11px;
    color: #e8bc75;
    font-weight: 800;
}

.story-card {
    min-height: 275px;
    border: 1px solid #c7a16a;
    border-radius: 22px;
    padding: 22px;
    background: linear-gradient(150deg, #fff0d8, #f3d7a6);
    color: #342139;
    box-shadow: 0 12px 28px #00000025;
    margin-bottom: 12px;
}

.story-card h3 {
    color: #48254b !important;
    font-size: 20px;
    margin-top: 8px;
}

.story-card p {
    color: #49384a;
    line-height: 1.6;
}

.story-art {
    font-size: 49px;
    line-height: 1.3;
}

.tag {
    display: inline-block;
    padding: 5px 11px;
    border-radius: 50px;
    background: #ead09a;
    color: #523548;
    font-size: 11px;
    font-weight: 800;
    margin: 4px 4px 4px 0;
}

.parchment {
    background:
        radial-gradient(circle at top right, #fff8d866, transparent 30%),
        linear-gradient(145deg, #fff0d0, #e7c58e);
    color: #38233c;
    padding: 30px;
    border-radius: 24px;
    border: 2px solid #bd8a4d;
    box-shadow: inset 0 0 35px #98663420, 0 16px 35px #00000035;
    margin: 15px 0;
}

.parchment h2, .parchment h3 {
    color: #512a4a !important;
}

.parchment p, .parchment li {
    color: #39283b;
    font-size: 17px;
    line-height: 1.9;
}

.chapter-number {
    color: #8b5c32;
    letter-spacing: 3px;
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
}

.moral {
    padding: 18px 20px;
    border-left: 5px solid #e3ad51;
    border-radius: 10px;
    background: #3a2543;
    color: #ffebba;
    line-height: 1.8;
    margin: 15px 0;
}

.info-panel {
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #8e6a4c;
    background: linear-gradient(135deg, #34233c, #402b38);
    min-height: 130px;
}

.info-panel h3 {
    font-size: 17px;
}

.info-panel p {
    font-size: 14px;
    line-height: 1.6;
}

div.stButton > button {
    border-radius: 12px;
    border: 1px solid #d9ac60;
    background: linear-gradient(135deg, #f6d18a, #dda654);
    color: #2b1930;
    font-weight: 800;
    min-height: 44px;
    transition: all .2s ease;
}

div.stButton > button:hover {
    border-color: #ffe7ae;
    transform: translateY(-2px);
    background: linear-gradient(135deg, #ffe5aa, #edbc69);
    color: #28172e;
}

div[data-testid="stProgressBar"] > div > div {
    background: linear-gradient(90deg, #cf8e4e, #ffe3a1);
}

div[data-testid="stMetric"] {
    background: #34233d;
    border: 1px solid #72523e;
    padding: 15px;
    border-radius: 16px;
}

div[data-testid="stMetric"] label {
    color: #e9c78e !important;
}

div[data-testid="stMetric"] [data-testid="stMetricValue"] {
    color: #fff0cc;
}

.stTextInput input, .stTextArea textarea {
    background: #fff1d9;
    color: #33223a;
    border-radius: 10px;
}

.stSelectbox div[data-baseweb="select"] > div {
    background: #fff1d9;
    color: #33223a;
}

hr {
    border-color: #75543f;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# STORY LIBRARY — ENGLISH + TELUGU
# =========================================================
STORIES = [
    {
        "id": "rama",
        "title": "Rama Keeps His Promise",
        "telugu_title": "రాముడు — మాట నిలబెట్టుకున్న మహానుభావుడు",
        "source": "Ramayana",
        "value": "Responsibility",
        "art": "🏹🌳👑",
        "color": "Forest Chronicles",
        "description": "A prince faces a difficult choice and teaches us the meaning of duty.",
        "chapters": [
            {
                "heading": "A Prince of Ayodhya",
                "en": """Long ago, in the beautiful kingdom of Ayodhya, Prince Rama was loved by everyone. He was brave, kind and respectful. One day, a promise made by King Dasharatha changed Rama's life. Rama was asked to leave the palace and spend fourteen years in the forest.""",
                "te": """పూర్వం అయోధ్య అనే అందమైన రాజ్యంలో రాముడు అనే యువరాజు ఉండేవాడు. అతను ధైర్యవంతుడు, దయగలవాడు, అందరినీ గౌరవించేవాడు. ఒక రోజు దశరథ మహారాజు ఇచ్చిన మాట కారణంగా రాముడు పద్నాలుగు సంవత్సరాలు అడవిలో గడపాల్సి వచ్చింది."""
            },
            {
                "heading": "The Difficult Decision",
                "en": """Rama could have argued for his royal position. Instead, he chose to honour his father's promise. Sita and Lakshmana decided to accompany him. Together, they left the comfort of the palace and began a new journey through the forest.""",
                "te": """రాముడు తన రాజ్యాధికారాన్ని కోరుకోవచ్చు. కానీ తండ్రి ఇచ్చిన మాటను నిలబెట్టడానికి అడవికి వెళ్లాలని నిర్ణయించుకున్నాడు. సీత, లక్ష్మణుడు కూడా అతనితో వెళ్లారు. ముగ్గురూ రాజభవనాన్ని విడిచి కొత్త ప్రయాణాన్ని ప్రారంభించారు."""
            },
            {
                "heading": "A Promise Remembered",
                "en": """Life in the forest brought challenges, but Rama continued to act with courage and responsibility. His choice reminds us that doing the right thing can sometimes be difficult. True character appears when a decision is not easy.""",
                "te": """అడవిలో ఎన్నో కష్టాలు ఎదురైనా రాముడు ధైర్యంగా, బాధ్యతతో ముందుకు సాగాడు. సరైన పని చేయడం కొన్నిసార్లు కష్టమైనా దాన్ని చేయాలని అతని జీవితం మనకు గుర్తు చేస్తుంది."""
            }
        ],
        "moral_en": "Keep your word and accept responsibility for your choices.",
        "moral_te": "ఇచ్చిన మాటను నిలబెట్టుకోండి. మీ నిర్ణయాలకు బాధ్యత వహించండి.",
        "application": "Keep a promise you made to a friend or complete a responsibility without being reminded."
    },
    {
        "id": "hanuman",
        "title": "Hanuman's Courageous Journey",
        "telugu_title": "హనుమంతుడు — ధైర్యానికి ప్రతీక",
        "source": "Ramayana",
        "value": "Courage",
        "art": "🐒⛰️🌊",
        "color": "Ocean of Courage",
        "description": "A mighty leap teaches us to trust our abilities and help others.",
        "chapters": [
            {
                "heading": "A Mission Across the Ocean",
                "en": """When Sita was missing, Rama's friends searched for her. Their journey brought them to the vast ocean. Across the water lay Lanka. The group needed someone courageous enough to cross the sea and search for Sita.""",
                "te": """సీతమ్మ జాడ కోసం రాముని మిత్రులు వెతుకుతూ సముద్రం దగ్గరకు చేరుకున్నారు. సముద్రానికి అవతల లంక ఉంది. సీతమ్మను వెతకడానికి సముద్రాన్ని దాటగల ధైర్యవంతుడు అవసరమయ్యాడు."""
            },
            {
                "heading": "Remembering His Strength",
                "en": """Hanuman was capable of extraordinary things, but he needed a reminder of his own strength. When he remembered his abilities and focused on his mission, his confidence returned. He prepared to make the great leap.""",
                "te": """హనుమంతుడికి అసాధారణ శక్తి ఉంది. కానీ తన శక్తిని గుర్తుచేసుకోవాల్సి వచ్చింది. తన సామర్థ్యాన్ని గుర్తించి లక్ష్యంపై దృష్టి పెట్టగానే అతనిలో ఆత్మవిశ్వాసం పెరిగింది."""
            },
            {
                "heading": "Courage in Action",
                "en": """Hanuman crossed the ocean, reached Lanka and searched carefully for Sita. His courage was not simply about being powerful; he used his abilities to help someone in need. His journey shows that courage grows when we focus on a meaningful purpose.""",
                "te": """హనుమంతుడు సముద్రాన్ని దాటి లంకకు చేరుకుని సీతమ్మను వెతికాడు. ధైర్యం అంటే కేవలం బలం కాదు; అవసరంలో ఉన్నవారికి సహాయం చేయడానికి మన శక్తిని ఉపయోగించడం కూడా ధైర్యమే."""
            }
        ],
        "moral_en": "Believe in your abilities and use them to help others.",
        "moral_te": "మీ సామర్థ్యాన్ని నమ్మండి. దానిని ఇతరులకు సహాయం చేయడానికి ఉపయోగించండి.",
        "application": "Try one difficult task today instead of giving up before you begin."
    },
    {
        "id": "krishna",
        "title": "Krishna Guides Arjuna",
        "telugu_title": "కృష్ణుడు — అర్జునుడికి మార్గదర్శి",
        "source": "Mahabharata",
        "value": "Wisdom",
        "art": "🦚🪈✨",
        "color": "Wisdom of the Gita",
        "description": "A moment of doubt becomes a lesson about duty, courage and clear thinking.",
        "chapters": [
            {
                "heading": "A Warrior's Doubt",
                "en": """On the battlefield of Kurukshetra, Arjuna looked at the people standing before him and felt overwhelmed. He was confused, worried and unsure what to do. Even a skilled warrior can experience doubt when a decision is difficult.""",
                "te": """కురుక్షేత్ర యుద్ధభూమిలో అర్జునుడు తన ఎదుట ఉన్నవారిని చూసి ఆందోళనకు గురయ్యాడు. ఏం చేయాలో అర్థంకాక సందిగ్ధంలో పడ్డాడు. కష్టమైన నిర్ణయాల సమయంలో నైపుణ్యం ఉన్నవారికి కూడా సందేహాలు రావచ్చు."""
            },
            {
                "heading": "The Guide Beside Him",
                "en": """Krishna listened and guided Arjuna through a deeper understanding of duty and action. He encouraged Arjuna to think carefully rather than be controlled by fear. Their conversation is remembered in the Bhagavad Gita.""",
                "te": """కృష్ణుడు అర్జునుడి మాటలను విని, కర్తవ్యం మరియు కార్యాచరణ గురించి వివరించాడు. భయానికి లోనుకాకుండా ఆలోచించి నిర్ణయం తీసుకోవాలని ప్రోత్సహించాడు. వారి సంభాషణ భగవద్గీతగా ప్రసిద్ధి చెందింది."""
            },
            {
                "heading": "Clarity Before Action",
                "en": """Arjuna gained a clearer understanding of his responsibility. The story reminds us to pause, seek wise guidance and consider our duties before making important decisions. Thoughtful action is better than action driven by panic.""",
                "te": """అర్జునుడికి తన బాధ్యతపై స్పష్టత వచ్చింది. ముఖ్యమైన నిర్ణయాల ముందు ఆగి ఆలోచించడం, మంచి సలహా తీసుకోవడం, మన కర్తవ్యాన్ని అర్థం చేసుకోవడం అవసరమని ఈ కథ చెబుతుంది."""
            }
        ],
        "moral_en": "Think clearly, seek wise advice and act responsibly.",
        "moral_te": "స్పష్టంగా ఆలోచించండి, మంచి సలహా తీసుకోండి, బాధ్యతతో వ్యవహరించండి.",
        "application": "When you feel confused about a decision, list your options and ask a trusted person for advice."
    },
    {
        "id": "truth",
        "title": "Yudhishthira and Truthfulness",
        "telugu_title": "యుధిష్ఠిరుడు — సత్యం యొక్క విలువ",
        "source": "Mahabharata",
        "value": "Honesty",
        "art": "📜⚖️🪔",
        "color": "Hall of Truth",
        "description": "Explore why honesty and thoughtful words matter, even under pressure.",
        "chapters": [
            {
                "heading": "Known for Truth",
                "en": """Yudhishthira, the eldest of the Pandavas, was known for valuing truth and fairness. People respected him because honesty was an important part of his character. Yet being honest did not mean every situation was simple.""",
                "te": """పాండవులలో పెద్దవాడైన యుధిష్ఠిరుడు సత్యానికి, న్యాయానికి ప్రాధాన్యత ఇచ్చేవాడు. నిజాయితీ అతని వ్యక్తిత్వంలో ముఖ్యమైన భాగం. అయితే ప్రతి పరిస్థితిలో నిజం చెప్పడం సులభం కాదు."""
            },
            {
                "heading": "The Weight of Words",
                "en": """The Mahabharata presents difficult moments in which truth, duty and the consequences of words must be considered carefully. The story invites us to think about how our statements affect other people and why careless words can cause harm.""",
                "te": """మహాభారతంలో సత్యం, కర్తవ్యం, మాటల వల్ల కలిగే పరిణామాల గురించి ఆలోచింపజేసే క్లిష్ట పరిస్థితులు ఉన్నాయి. మన మాటలు ఇతరులపై ఎలా ప్రభావం చూపుతాయో జాగ్రత్తగా ఆలోచించాలి."""
            },
            {
                "heading": "Honesty with Responsibility",
                "en": """Honesty builds trust, but wise communication matters too. We should speak truthfully, avoid misleading others and think about the consequences of our actions. Integrity means trying to do what is right even when it is uncomfortable.""",
                "te": """నిజాయితీ నమ్మకాన్ని పెంచుతుంది. నిజం చెప్పడం, ఇతరులను తప్పుదారి పట్టించకపోవడం, మన చర్యల ఫలితాలను ఆలోచించడం అవసరం. కష్టమైనప్పటికీ సరైన పని చేయడానికి ప్రయత్నించడమే నిజాయితీ."""
            }
        ],
        "moral_en": "Be truthful, fair and mindful of the effects of your words.",
        "moral_te": "నిజాయితీగా, న్యాయంగా ఉండండి. మీ మాటల ప్రభావాన్ని గుర్తించండి.",
        "application": "If you make a mistake, admit it honestly and think about how to correct it."
    },
    {
        "id": "rabbit",
        "title": "The Lion and the Clever Rabbit",
        "telugu_title": "సింహం మరియు తెలివైన కుందేలు",
        "source": "Panchatantra",
        "value": "Problem-solving",
        "art": "🦁🐇🌕",
        "color": "Forest of Clever Ideas",
        "description": "A small rabbit uses intelligence to face a much stronger opponent.",
        "chapters": [
            {
                "heading": "The Forest in Fear",
                "en": """In a forest, a powerful lion frightened the other animals. They were afraid to challenge him because he was much stronger. One day, a small rabbit was chosen to visit the lion.""",
                "te": """ఒక అడవిలో బలమైన సింహం ఇతర జంతువులను భయపెట్టేది. అది చాలా శక్తివంతమైనది కావడంతో జంతువులు ఎదిరించలేకపోయేవి. ఒక రోజు చిన్న కుందేలుకు సింహం దగ్గరకు వెళ్లే బాధ్యత వచ్చింది."""
            },
            {
                "heading": "A Clever Plan",
                "en": """The rabbit did not try to defeat the lion by strength. Instead, it thought carefully and used a clever plan involving the lion's own reflection in a well. The lion became angry when it saw what it believed was another lion.""",
                "te": """కుందేలు సింహాన్ని బలంతో ఓడించడానికి ప్రయత్నించలేదు. బదులుగా తెలివిగా ఆలోచించి, బావిలో కనిపించిన సింహం ప్రతిబింబాన్ని ఉపయోగించి ఒక ఉపాయం పన్నింది."""
            },
            {
                "heading": "Brains and Bravery",
                "en": """The traditional tale ends with the lion jumping into the well, believing its reflection was a rival. The animals were free from its threat. The story celebrates intelligence, but also reminds us to solve problems thoughtfully rather than through violence.""",
                "te": """ప్రతిబింబాన్ని మరో సింహంగా భావించిన సింహం బావిలోకి దూకిందని ఈ కథ చెబుతుంది. జంతువులకు భయం తొలగిపోయింది. బలంతోనే కాకుండా తెలివిగా ఆలోచించి సమస్యలను పరిష్కరించవచ్చని ఈ కథ నేర్పుతుంది."""
            }
        ],
        "moral_en": "A thoughtful plan can be more powerful than physical strength.",
        "moral_te": "శారీరక బలం కంటే తెలివైన ఆలోచన కొన్నిసార్లు గొప్పది.",
        "application": "When a problem appears, pause and think of at least two possible solutions."
    },
    {
        "id": "dove",
        "title": "The Dove and the Ant",
        "telugu_title": "పావురం మరియు చీమ",
        "source": "Traditional Fable",
        "value": "Kindness",
        "art": "🕊️🐜🌿",
        "color": "Garden of Kindness",
        "description": "A tiny act of kindness returns when it is needed most.",
        "chapters": [
            {
                "heading": "A Tiny Ant in Trouble",
                "en": """One day, an ant fell into a stream and struggled to stay above the water. A dove sitting on a nearby branch noticed the little creature and decided to help.""",
                "te": """ఒక రోజు చిన్న చీమ నీటిలో పడిపోయి బయటపడటానికి కష్టపడింది. దగ్గరలోని కొమ్మపై ఉన్న పావురం చీమను గమనించి సహాయం చేయాలని నిర్ణయించుకుంది."""
            },
            {
                "heading": "A Leaf Becomes a Lifeboat",
                "en": """The dove dropped a leaf near the ant. The ant climbed onto it and safely reached the bank. The small act of kindness saved the ant from danger.""",
                "te": """పావురం చీమ దగ్గర ఒక ఆకును పడవేసింది. చీమ ఆ ఆకుపైకి ఎక్కి సురక్షితంగా ఒడ్డుకు చేరుకుంది. చిన్న సహాయం చీమను ప్రమాదం నుంచి కాపాడింది."""
            },
            {
                "heading": "Kindness Returned",
                "en": """Later, a hunter approached the dove. The ant noticed the danger and bit the hunter's foot. The hunter was distracted, giving the dove a chance to fly away. This fable teaches that kindness matters and even a small creature can make a difference.""",
                "te": """తర్వాత ఒక వేటగాడు పావురం దగ్గరకు వచ్చాడు. ప్రమాదాన్ని గమనించిన చీమ వేటగాడి కాలిని కుట్టింది. వేటగాడు అటువైపు దృష్టి పెట్టడంతో పావురం ఎగిరిపోయింది. చిన్న జీవి కూడా గొప్ప సహాయం చేయగలదని ఈ కథ చెబుతుంది."""
            }
        ],
        "moral_en": "Be kind. Even a small act of help can make a big difference.",
        "moral_te": "దయతో ఉండండి. చిన్న సహాయం కూడా పెద్ద మార్పును తీసుకురాగలదు.",
        "application": "Help a classmate, listen to someone who feels sad or care for an animal."
    }
]


# =========================================================
# QUIZ BANK
# =========================================================
QUIZ = [
    {
        "q": "Which value is highlighted in Rama's decision?",
        "te": "రాముడి నిర్ణయం ఏ విలువను తెలియజేస్తుంది?",
        "options": ["Greed", "Responsibility", "Jealousy", "Carelessness"],
        "answer": "Responsibility",
        "explanation": "Rama accepts responsibility and honours his father's promise."
    },
    {
        "q": "What helped Hanuman complete his mission?",
        "te": "హనుమంతుడు తన లక్ష్యాన్ని సాధించడానికి ఏది సహాయపడింది?",
        "options": ["Giving up", "Anger alone", "Courage and confidence", "Avoiding the task"],
        "answer": "Courage and confidence",
        "explanation": "Hanuman remembers his abilities and uses them for a meaningful purpose."
    },
    {
        "q": "What did Krishna encourage Arjuna to do?",
        "te": "కృష్ణుడు అర్జునుడిని ఏమి చేయమని ప్రోత్సహించాడు?",
        "options": ["Act only from fear", "Think about duty and act wisely", "Ignore every problem", "Blame everyone"],
        "answer": "Think about duty and act wisely",
        "explanation": "The conversation in the Bhagavad Gita explores duty, wisdom and action."
    },
    {
        "q": "What is one lesson from the lion and rabbit story?",
        "te": "సింహం మరియు కుందేలు కథలోని ఒక పాఠం ఏమిటి?",
        "options": ["Strength solves every problem", "Never think", "Intelligence can solve problems", "Kindness is useless"],
        "answer": "Intelligence can solve problems",
        "explanation": "The rabbit uses careful thinking instead of physical strength."
    },
    {
        "q": "How did the dove help the ant?",
        "te": "పావురం చీమకు ఎలా సహాయం చేసింది?",
        "options": ["By dropping a leaf", "By hiding", "By chasing it away", "By doing nothing"],
        "answer": "By dropping a leaf",
        "explanation": "The leaf helped the ant reach safety."
    },
    {
        "q": "What builds trust between people?",
        "te": "వ్యక్తుల మధ్య నమ్మకాన్ని ఏది పెంచుతుంది?",
        "options": ["Dishonesty", "Honesty", "Rumours", "Broken promises"],
        "answer": "Honesty",
        "explanation": "Honest communication helps people trust each other."
    },
    {
        "q": "What should you do when a difficult decision confuses you?",
        "te": "క్లిష్టమైన నిర్ణయం తీసుకోవడంలో గందరగోళం ఉంటే ఏం చేయాలి?",
        "options": ["Panic immediately", "Never ask for help", "Think carefully and seek wise advice", "Choose randomly"],
        "answer": "Think carefully and seek wise advice",
        "explanation": "A pause and thoughtful advice can help you make a better decision."
    },
    {
        "q": "Which story teaches that a small act of kindness matters?",
        "te": "చిన్న సహాయం కూడా ముఖ్యమని ఏ కథ నేర్పుతుంది?",
        "options": ["The Dove and the Ant", "Rama Keeps His Promise", "Krishna Guides Arjuna", "The Lion and the Rabbit"],
        "answer": "The Dove and the Ant",
        "explanation": "The dove helps the ant, and later the ant helps the dove."
    },
    {
        "q": "What is a useful response to a problem?",
        "te": "సమస్య ఎదురైనప్పుడు ఉపయోగకరమైన స్పందన ఏది?",
        "options": ["Give up instantly", "Think of possible solutions", "Blame others first", "Ignore every detail"],
        "answer": "Think of possible solutions",
        "explanation": "Careful thinking can reveal better solutions."
    },
    {
        "q": "Why do stories teach values?",
        "te": "కథలు విలువలను ఎందుకు నేర్పుతాయి?",
        "options": ["Only to entertain", "To encourage reflection and good choices", "To prevent all questions", "To replace learning"],
        "answer": "To encourage reflection and good choices",
        "explanation": "Stories give examples that help us reflect on our own choices."
    }
]


# =========================================================
# SESSION STATE
# =========================================================
def init_state():
    defaults = {
        "page": "Home",
        "language": "English + తెలుగు",
        "selected_story": "rama",
        "chapter": 0,
        "completed_stories": [],
        "completed_values": [],
        "quiz_questions": random.sample(QUIZ, 5),
        "quiz_index": 0,
        "quiz_score": 0,
        "quiz_answered": False,
        "quiz_feedback": "",
        "quiz_finished": False,
        "quiz_selected": None,
        "quiz_attempts": 0,
        "reflections": {},
        "audio_bytes": None,
        "audio_story_id": None,
        "audio_chapter": None,
        "audio_language": None
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


init_state()


def current_story():
    return next(
        (s for s in STORIES if s["id"] == st.session_state.selected_story),
        STORIES[0]
    )


def get_story(story_id):
    return next((s for s in STORIES if s["id"] == story_id), STORIES[0])


def bilingual():
    return st.session_state.language == "English + తెలుగు"


def show_english():
    return st.session_state.language != "తెలుగు"


def show_telugu():
    return st.session_state.language != "English"


def go_to(page):
    st.session_state.page = page
    st.rerun()


def select_story(story_id):
    st.session_state.selected_story = story_id
    st.session_state.chapter = 0
    st.session_state.audio_bytes = None
    st.session_state.page = "Story Mode"
    st.rerun()


def complete_story(story_id):
    if story_id not in st.session_state.completed_stories:
        st.session_state.completed_stories.append(story_id)


def story_text(en, te):
    if show_english():
        st.markdown(en)
    if show_telugu():
        if bilingual():
            with st.expander("తెలుగులో చదవండి | Read in Telugu"):
                st.markdown(te)
        else:
            st.markdown(te)


# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:
    st.markdown(
        "<div style='text-align:center;font-size:50px;'>📜</div>"
        "<h2 style='text-align:center;margin-top:0;'>ItihasQuest</h2>"
        "<p style='text-align:center;color:#e9c78e;'>Stories • Values • Wisdom</p>",
        unsafe_allow_html=True
    )
    st.divider()

    st.session_state.language = st.selectbox(
        "🌐 Story Language",
        ["English + తెలుగు", "English", "తెలుగు"],
        index=["English + తెలుగు", "English", "తెలుగు"].index(
            st.session_state.language
        )
    )

    pages = [
        "Home",
        "Story Library",
        "Story Mode",
        "Quiz Arena",
        "Values Garden",
        "My Journey"
    ]

    selected_page = st.radio(
        "YOUR ADVENTURE",
        pages,
        index=pages.index(st.session_state.page)
    )
    st.session_state.page = selected_page

    st.divider()
    finished = len(st.session_state.completed_stories)
    st.markdown("**✨ Your Story Progress**")
    st.progress(finished / len(STORIES))
    st.caption(f"{finished} of {len(STORIES)} stories completed")

    st.markdown(
        "<div style='padding:12px;border:1px solid #7c5a45;"
        "border-radius:14px;text-align:center;margin-top:18px;'>"
        "<span style='font-size:26px;'>🪔</span><br>"
        "<b>Every story holds a light.</b><br>"
        "<span style='font-size:12px;'>Discover the wisdom within.</span>"
        "</div>",
        unsafe_allow_html=True
    )


# =========================================================
# HOME PAGE
# =========================================================
if st.session_state.page == "Home":
    st.markdown("""
    <div class="hero">
        <div class="eyebrow">✦ A Magical Journey Through Ancient Wisdom ✦</div>
        <h1>Every Story Has a<br>Little Spark of Magic.</h1>
        <p>
        Welcome to ItihasQuest — an interactive storybook where the worlds of
        the Ramayana, Mahabharata, Panchatantra and traditional tales come alive.
        Read, listen, explore values and discover the hero within you.
        </p>
        <div style="font-size:27px;letter-spacing:8px;margin-top:20px;">
            🏹 &nbsp; 🦚 &nbsp; 🪷 &nbsp; 🪈 &nbsp; 🪔
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="info-panel">
            <h3>📖 The Story Library</h3>
            <p>Explore timeless stories, chapter by chapter, in English and Telugu.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="info-panel">
            <h3>🎙️ Listen & Imagine</h3>
            <p>Listen to story narration and imagine every scene like a living book.</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="info-panel">
            <h3>🧠 Play & Discover</h3>
            <p>Answer story quizzes and collect values as you continue your journey.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## ✨ Choose Your First Adventure")
    st.caption("Each story has three chapters and a lesson to carry into everyday life.")

    cols = st.columns(3)
    for i, story in enumerate(STORIES[:3]):
        with cols[i]:
            st.markdown(f"""
            <div class="story-card">
                <div class="story-art">{story['art']}</div>
                <span class="tag">{story['source']}</span>
                <span class="tag">{story['value']}</span>
                <h3>{story['title']}</h3>
                <p>{story['description']}</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Open Story →", key=f"home_{story['id']}", use_container_width=True):
                select_story(story["id"])

    st.markdown("---")
    left, right = st.columns([1, 1])
    with left:
        st.markdown("### 🪷 Your Learning Quest")
        st.write("Read a story. Discover its value. Try a quiz. Use the lesson in real life.")
        st.progress(len(st.session_state.completed_stories) / len(STORIES))
        st.caption(f"{len(st.session_state.completed_stories)} stories completed")
    with right:
        if st.button("📚 Explore All Stories", use_container_width=True):
            go_to("Story Library")
        if st.button("🧠 Enter the Quiz Arena", use_container_width=True):
            go_to("Quiz Arena")


# =========================================================
# STORY LIBRARY
# =========================================================
elif st.session_state.page == "Story Library":
    st.markdown("## 📚 The Story Library")
    st.write("Choose a tale. Turn its pages. Discover a value you can use in your life.")

    search = st.text_input("🔍 Search by story, source or value", placeholder="Try courage, kindness, Ramayana...")
    source_filter = st.selectbox(
        "Filter by collection",
        ["All Collections"] + sorted(set(s["source"] for s in STORIES))
    )

    filtered = []
    for s in STORIES:
        search_text = (
            s["title"] + " " + s["telugu_title"] + " " +
            s["source"] + " " + s["value"] + " " + s["description"]
        ).lower()
        if search.lower() in search_text and (
            source_filter == "All Collections" or s["source"] == source_filter
        ):
            filtered.append(s)

    st.caption(f"{len(filtered)} story/stories found")

    if not filtered:
        st.info("No story found. Try another keyword.")
    else:
        for start in range(0, len(filtered), 2):
            cols = st.columns(2)
            for j, story in enumerate(filtered[start:start + 2]):
                with cols[j]:
                    done = story["id"] in st.session_state.completed_stories
                    st.markdown(f"""
                    <div class="story-card">
                        <div class="story-art">{story['art']}</div>
                        <span class="tag">{story['source']}</span>
                        <span class="tag">{story['value']}</span>
                        <h3>{story['title']}</h3>
                        <p>{story['description']}</p>
                        <p><b>తెలుగు:</b> {story['telugu_title']}</p>
                        <p>{'✅ Completed' if done else '📖 3 chapters • Story mode'}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button(
                        "Read This Story →",
                        key=f"library_{story['id']}",
                        use_container_width=True
                    ):
                        select_story(story["id"])


# =========================================================
# STORY MODE
# =========================================================
elif st.session_state.page == "Story Mode":
    st.markdown("## 📖 Story Mode")
    st.caption("Settle in, turn the pages and step into another world.")

    chosen = st.selectbox(
        "Choose your story",
        options=[s["id"] for s in STORIES],
        format_func=lambda x: get_story(x)["title"],
        index=[s["id"] for s in STORIES].index(st.session_state.selected_story)
    )
    if chosen != st.session_state.selected_story:
        st.session_state.selected_story = chosen
        st.session_state.chapter = 0
        st.session_state.audio_bytes = None
        st.rerun()

    story = current_story()
    total = len(story["chapters"])
    chapter_idx = min(st.session_state.chapter, total - 1)
    chapter = story["chapters"][chapter_idx]

    st.markdown(f"""
    <div class="hero" style="padding:28px;">
        <div class="eyebrow">{story['source']} • {story['color']}</div>
        <div style="font-size:48px;margin-top:12px;">{story['art']}</div>
        <h1 style="font-size:34px;">{story['title']}</h1>
        <p>{story['description']}</p>
        <span class="tag">Value: {story['value']}</span>
    </div>
    """, unsafe_allow_html=True)

    st.progress((chapter_idx + 1) / total)
    st.caption(f"CHAPTER {chapter_idx + 1} OF {total}")

    # Chapter parchment
    safe_heading = html.escape(chapter["heading"])
    st.markdown(f"""
    <div class="parchment">
        <div class="chapter-number">✦ THE ANCIENT STORYBOOK ✦</div>
        <h2>{safe_heading}</h2>
        <div style="font-size:27px;margin:14px 0;">{story['art']}</div>
    </div>
    """, unsafe_allow_html=True)

    # Render chapter text according to language preference
    if show_english():
        st.markdown(f"""
        <div class="parchment">
            <div class="chapter-number">ENGLISH EDITION</div>
            <p>{html.escape(chapter['en'])}</p>
        </div>
        """, unsafe_allow_html=True)

    if show_telugu():
        st.markdown(f"""
        <div class="parchment">
            <div class="chapter-number">తెలుగు కథ</div>
            <p>{html.escape(chapter['te'])}</p>
        </div>
        """, unsafe_allow_html=True)

    # Narration
    with st.expander("🎙️ Listen to this chapter"):
        if not GTTS_AVAILABLE:
            st.warning("Install gTTS using: py -m pip install gTTS")
        else:
            voice_choice = st.radio(
                "Narration language",
                ["English", "తెలుగు"],
                horizontal=True,
                key=f"voice_{story['id']}_{chapter_idx}"
            )
            if st.button("🔊 Generate Voice Narration", key=f"voice_btn_{story['id']}_{chapter_idx}"):
                voice_text = chapter["en"] if voice_choice == "English" else chapter["te"]
                voice_lang = "en" if voice_choice == "English" else "te"
                try:
                    with st.spinner("Preparing your story narration..."):
                        audio_file = BytesIO()
                        gTTS(text=voice_text, lang=voice_lang, slow=False).write_to_fp(audio_file)
                        st.session_state.audio_bytes = audio_file.getvalue()
                        st.session_state.audio_story_id = story["id"]
                        st.session_state.audio_chapter = chapter_idx
                        st.session_state.audio_language = voice_choice
                    st.success("Your narration is ready!")
                except Exception as e:
                    st.error("Voice generation needs an internet connection. Please try again.")
            if (
                st.session_state.audio_bytes
                and st.session_state.audio_story_id == story["id"]
                and st.session_state.audio_chapter == chapter_idx
            ):
                st.audio(st.session_state.audio_bytes, format="audio/mp3")

    st.markdown("### 🪔 Think About the Story")
    st.markdown(f"""
    <div class="moral">
        <b>🌟 The value of this chapter</b><br>
        {html.escape(story['moral_en'])}<br>
        <span style="font-size:15px;">{html.escape(story['moral_te'])}</span>
    </div>
    """, unsafe_allow_html=True)

    reflection_key = f"reflection_{story['id']}"
    reflection = st.text_area(
        "Your reflection: What would you do in this situation?",
        value=st.session_state.reflections.get(story["id"], ""),
        placeholder="Write your thoughts here...",
        key=reflection_key
    )
    st.session_state.reflections[story["id"]] = reflection

    st.caption("Real-life challenge: " + story["application"])

    st.markdown("---")
    prev_col, count_col, next_col = st.columns([1, 1, 1])

    with prev_col:
        if st.button("← Previous Page", disabled=(chapter_idx == 0), use_container_width=True):
            st.session_state.chapter = chapter_idx - 1
            st.session_state.audio_bytes = None
            st.rerun()

    with count_col:
        st.markdown(
            f"<p style='text-align:center;padding-top:10px;'>"
            f"📜 Page {chapter_idx + 1} / {total}</p>",
            unsafe_allow_html=True
        )

    with next_col:
        if chapter_idx < total - 1:
            if st.button("Next Page →", use_container_width=True):
                st.session_state.chapter = chapter_idx + 1
                st.session_state.audio_bytes = None
                st.rerun()
        else:
            if st.button("✨ Complete Story", use_container_width=True):
                complete_story(story["id"])
                if story["value"] not in st.session_state.completed_values:
                    st.session_state.completed_values.append(story["value"])
                st.success("Story completed! A new piece of wisdom joins your journey.")
                st.balloons()

    if story["id"] in st.session_state.completed_stories:
        st.success("🏅 This story is in your completed collection.")

    if st.button("🧠 Test What You Learned", use_container_width=True):
        go_to("Quiz Arena")


# =========================================================
# QUIZ ARENA
# =========================================================
elif st.session_state.page == "Quiz Arena":
    st.markdown("## 🧠 The Quiz Arena")
    st.write("Test your memory, understand the lessons and earn your wisdom score.")

    if not st.session_state.quiz_finished:
        questions = st.session_state.quiz_questions
        idx = st.session_state.quiz_index
        question = questions[idx]

        st.markdown(f"""
        <div class="hero" style="padding:25px;">
            <div class="eyebrow">✦ WISDOM CHALLENGE ✦</div>
            <h1 style="font-size:35px;">Question {idx + 1}</h1>
            <p>Think carefully before choosing your answer.</p>
        </div>
        """, unsafe_allow_html=True)

        st.progress((idx + 1) / len(questions))
        st.markdown(f"### {question['q']}")
        if show_telugu():
            st.markdown(f"**{question['te']}**")

        selected_answer = st.radio(
            "Choose one answer",
            question["options"],
            key=f"quiz_option_{idx}",
            index=None
        )

        if not st.session_state.quiz_answered:
            if st.button("Check My Answer ✨", use_container_width=True):
                if selected_answer is None:
                    st.warning("Choose an answer first.")
                else:
                    st.session_state.quiz_selected = selected_answer
                    st.session_state.quiz_attempts += 1
                    if selected_answer == question["answer"]:
                        st.session_state.quiz_score += 1
                        st.session_state.quiz_feedback = "correct"
                    else:
                        st.session_state.quiz_feedback = "incorrect"
                    st.session_state.quiz_answered = True
                    st.rerun()
        else:
            if st.session_state.quiz_feedback == "correct":
                st.success("🌟 Correct! Excellent thinking.")
            else:
                st.error(f"Not quite. The correct answer is: {question['answer']}")
            st.info(question["explanation"])

            if st.button(
                "Next Question →" if idx < len(questions) - 1 else "See My Results 🏆",
                use_container_width=True
            ):
                if idx < len(questions) - 1:
                    st.session_state.quiz_index += 1
                    st.session_state.quiz_answered = False
                    st.session_state.quiz_feedback = ""
                    st.session_state.quiz_selected = None
                    st.rerun()
                else:
                    st.session_state.quiz_finished = True
                    st.rerun()

    else:
        total = len(st.session_state.quiz_questions)
        score = st.session_state.quiz_score
        percentage = round(score / total * 100)

        st.markdown(f"""
        <div class="hero" style="text-align:center;">
            <div style="font-size:70px;">{'🏆' if percentage >= 80 else '🌟' if percentage >= 60 else '🪷'}</div>
            <div class="eyebrow">YOUR WISDOM REPORT</div>
            <h1>{score} / {total}</h1>
            <p>You scored {percentage}% in this challenge.</p>
        </div>
        """, unsafe_allow_html=True)

        st.progress(percentage / 100)

        if percentage >= 80:
            st.success("Amazing! You have a wonderful memory for the stories.")
        elif percentage >= 60:
            st.info("Good work! Revisit a story to strengthen your understanding.")
        else:
            st.info("Every attempt is a new beginning. Read the stories and try again.")

        a, b, c = st.columns(3)
        a.metric("Correct Answers", score)
        b.metric("Questions", total)
        c.metric("Score", f"{percentage}%")

        if st.button("🔄 Play a New Quiz", use_container_width=True):
            st.session_state.quiz_questions = random.sample(QUIZ, 5)
            st.session_state.quiz_index = 0
            st.session_state.quiz_score = 0
            st.session_state.quiz_answered = False
            st.session_state.quiz_feedback = ""
            st.session_state.quiz_finished = False
            st.session_state.quiz_selected = None
            st.session_state.quiz_attempts = 0
            st.rerun()

        if st.button("📖 Read Another Story", use_container_width=True):
            go_to("Story Library")


# =========================================================
# VALUES GARDEN
# =========================================================
elif st.session_state.page == "Values Garden":
    st.markdown("## 🌱 The Values Garden")
    st.write("Every story plants a seed. Every good action helps it grow.")

    values = [
        ("🌳", "Responsibility", "Keep your promises and do your part."),
        ("🔥", "Courage", "Try what is right, even when it feels difficult."),
        ("🦚", "Wisdom", "Pause, think and learn from good guidance."),
        ("🪔", "Honesty", "Speak truthfully and build trust."),
        ("🧩", "Problem-solving", "Look for thoughtful solutions."),
        ("🕊️", "Kindness", "Help others whenever you can.")
    ]

    cols = st.columns(3)
    for i, (emoji, value, meaning) in enumerate(values):
        with cols[i % 3]:
            earned = value in st.session_state.completed_values
            st.markdown(f"""
            <div class="story-card" style="min-height:190px;">
                <div class="story-art">{emoji}</div>
                <h3>{value}</h3>
                <p>{meaning}</p>
                <span class="tag">{'🌟 DISCOVERED' if earned else '🌱 READY TO GROW'}</span>
            </div>
            """, unsafe_allow_html=True)

            related = [s for s in STORIES if s["value"] == value]
            if related and st.button("Explore Lesson", key=f"value_{value}", use_container_width=True):
                select_story(related[0]["id"])

    st.markdown("### 🌼 Your Garden's Growth")
    discovered = len(st.session_state.completed_values)
    st.progress(discovered / len(values))
    st.write(f"You have discovered **{discovered} of {len(values)} values**.")

    st.info(
        "Garden tip: after finishing a story, think of one small action "
        "you can take today to practise its value."
    )


# =========================================================
# MY JOURNEY
# =========================================================
elif st.session_state.page == "My Journey":
    st.markdown("## 🏆 My Journey")
    st.write("Your personal record of stories explored and lessons discovered.")

    completed = st.session_state.completed_stories
    discovered = st.session_state.completed_values

    a, b, c = st.columns(3)
    a.metric("Stories Completed", f"{len(completed)} / {len(STORIES)}")
    b.metric("Values Discovered", len(discovered))
    c.metric("Reflections Written", sum(
        1 for v in st.session_state.reflections.values() if v.strip()
    ))

    st.markdown("### 📜 Your Story Collection")
    for story in STORIES:
        done = story["id"] in completed
        with st.container(border=True):
            left, middle, right = st.columns([1, 4, 1])
            with left:
                st.markdown(f"<div style='font-size:35px;'>{story['art']}</div>", unsafe_allow_html=True)
            with middle:
                st.markdown(f"**{story['title']}**")
                st.caption(f"{story['source']} • Value: {story['value']}")
            with right:
                st.write("✅ Done" if done else "📖 Unread")
                if st.button("Open", key=f"journey_{story['id']}"):
                    select_story(story["id"])

    st.markdown("### ✍️ My Reflections")
    has_reflections = False
    for story in STORIES:
        note = st.session_state.reflections.get(story["id"], "").strip()
        if note:
            has_reflections = True
            st.markdown(f"**{story['title']}**")
            st.write(note)
            st.divider()

    if not has_reflections:
        st.info("Your reflections will appear here after you write them in Story Mode.")

    if len(completed) == len(STORIES):
        st.balloons()
        st.success("🏆 Story Master! You have completed every story in this collection.")

    st.caption(
        "Progress is stored in this Streamlit session. Restarting the app or "
        "starting a fresh session may reset it."
    )


# =========================================================
# FOOTER
# =========================================================
st.markdown("---")
st.markdown("""
<div style="text-align:center;padding:12px;color:#d7b98d;">
    <div style="font-size:25px;">🪷 ✦ 🪔 ✦ 🪷</div>
    <b>ITIHASQUEST</b><br>
    <span style="font-size:13px;">
        Ancient stories • Timeless values • A wiser tomorrow
    </span>
</div>
""", unsafe_allow_html=True)