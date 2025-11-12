lexicon = {
    'chatgpt': {
        'continue_dialog': (
            "GIVE_SHORT_ANSWER"
            "You are English Dialog Bot 🇬🇧, a friendly and intelligent assistant. "
            "Chat warmly and naturally in English, using a motivating and supportive tone. "
            "Adapt language to the user's English level (A1–C2). "
            "Gently correct mistakes, suggest vocabulary and grammar improvements, "
            "introduce new words or phrases, and add interesting cultural or language facts when relevant. "
            "Consider previous feedback if available and continue the conversation coherently. "
            "Keep responses concise, engaging, and practical for learning. "
            "IGNORE NEXT_STEP - it is a separator. "
            "YOU ARE A FRIEND, NOT AN LLM OR PROFESSOR, JUST CHAT."
        ),
        'give_feedback': (
            "You are English Dialog Bot 🇬🇧, a kind and supportive assistant. "
            "Provide constructive feedback on the user's English. "
            "Point out areas to improve in vocabulary, grammar, and expression. "
            "Give actionable tips, short exercises, or useful phrases. "
            "Include small interesting facts about English language or British culture. "
            "Adapt feedback to the user's level (A1–C2) and consider previous feedback. "
            "Keep the tone friendly, motivating, and concise."
        ),
    },

    'buttons': {
        'ready': 'I am ready ✅',
    },

    'handlers': {
        'start': (
            "<b>Hello!</b> I am <b>English Dialog Bot 🇬🇧</b>.\n\n"
            "I am here to help you practice English in a fun and supportive way. "
            "We can chat on any topic, I will correct mistakes, and give helpful tips.\n\n"
            "<b>Why do we need your English level?</b>\n"
            "It helps me adapt messages to your knowledge:\n"
            "A1–A2: simple words and phrases\n"
            "B1–B2: normal conversation\n"
            "C1–C2: advanced expressions, idioms\n\n"
            "<b>Modes:</b>\n"
            "Relax 🐾 – longer dialogues, more guidance, slower pace\n"
            "Normal 🙂 – balanced pace and feedback (default)\n"
            "Hard ⚡ – short dialogues, quicker feedback, challenging exercises\n\n"
            "You can change name, level, or mode anytime, reset the conversation, "
            "or see your info. Let's improve English together! 🌟"
        ),
        'choose_name': "What should I call you? ✏️ Enter your name:",
        'choose_level': "Select your English level 🇬🇧: A1–C2. This helps me chat at the right difficulty 📝",
        'choose_mode': "Choose a mode: Relax 🐾 / Normal 🙂 / Hard ⚡. You can change anytime!",
        'completed': "<b>All set!</b> Let's start our first chat! I will guide and support you 🌟",
        'edit_name': "Enter your new name ✏️",
        'edit_lvl': "Select your new English level 🇬🇧",
        'edit_mode': "Select your new mode ⚡",
        'edit_done': "<b>Changes saved!</b> ✅",
        'wrong_name': "Hmm, that name seems invalid. Try another ✏️",
        'incorrect_input': "I didn't understand that. Please try again 🙂",
        'stop_spam': "Please wait a moment… ⏳",
        'ready_done': "<b>Ready!</b> Send your next message whenever you like 📝",
        'reset_dialog': "<b>Conversation reset</b> 🌟 Let's start fresh!",
        'thinking': "English Dialog Bot 🇬🇧 is thinking… ⏳ Please wait a moment!",
        'info': (
            "<b>About English Dialog Bot 🇬🇧</b>\n"
            "I am your assistant for practicing English.\n\n"
            "<b>Commands:</b>\n"
            "/start – Start chatting\n"
            "/edit_name – Change your name ✏️\n"
            "/edit_lvl – Change your English level 🇬🇧\n"
            "/edit_mode – Change dialogue mode ⚡\n"
            "/reset_dialog – Start conversation fresh 🔄\n"
            "/info – Show this info ℹ️"
        ),
    },

    'commands': {
        'reset_dialog': "Reset the conversation 🔄",
        'start': "Start chatting 📝",
        'edit_name': "Change your name ✏️",
        'edit_lvl': "Change English level 🇬🇧",
        'edit_mode': "Change mode ⚡",
        'info': "Show info and commands ℹ️",
    }
}
