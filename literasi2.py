import streamlit as st
from gtts import gTTS
import base64
import io
from streamlit.components.v1 import html


mengeja=['Ini ru-mah-ku.',
        'Di ru-mah a-da a-yah.',
        'A-yah ba-ca ko-ran.',
        'Di ru-mah a-da i-bu.',
        'I-bu ma-sak na-si.',
        'Di ru-mah a-da ka-ka.',
        'Ka-ka me-war-na-i ga-mbar.',

        'Di ru-mah a-da a-ku.',
        'A-ku ber-ma-in bo-la.',
        'A-ku se-nang di ru-mah.',
        'A-ku sa-yang ke-lu-arg-a-ku.'
        ]

if 'kondisi' not in st.session_state:
    st.session_state.kondisi={'kondisi1':True,'kondisi2':False,'kondisi3':False, 'kondisi4':False, 'kondisi5':False}
if 'halaman' not in st.session_state:
    st.session_state.halaman={'halaman1':True, 'halaman2':False, 'halaman3':False}


def halaman1():
    koding1='''
    <!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Keluargaku di Rumah</title>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&family=Dancing+Script:wght@700&family=Quicksand:wght@500;700&display=swap" rel="stylesheet">
    
    <!-- Font Awesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Poppins', sans-serif;
            overflow: hidden;
            height: 100vh;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            position: relative;
        }

        /* Animated Background */
        .bg-animation {
            position: absolute;
            width: 100%;
            height: 100%;
            overflow: hidden;
            z-index: 1;
        }

        .floating-shape {
            position: absolute;
            opacity: 0.1;
            animation: float 20s infinite ease-in-out;
        }

        .shape1 {
            width: 300px;
            height: 300px;
            background: white;
            border-radius: 50%;
            top: -150px;
            left: -150px;
            animation-delay: 0s;
        }

        .shape2 {
            width: 200px;
            height: 200px;
            background: white;
            border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%;
            bottom: -100px;
            right: -100px;
            animation-delay: 5s;
        }

        .shape3 {
            width: 150px;
            height: 150px;
            background: white;
            border-radius: 63% 37% 54% 46% / 55% 48% 52% 45%;
            top: 50%;
            left: 10%;
            animation-delay: 10s;
        }

        @keyframes float {
            0%, 100% {
                transform: translateY(0) rotate(0deg);
            }
            33% {
                transform: translateY(-30px) rotate(120deg);
            }
            66% {
                transform: translateY(30px) rotate(240deg);
            }
        }

        /* Main Container */
        .container {
            position: relative;
            z-index: 10;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 20px;
        }

        /* House Icon */
        .house-icon {
            font-size: 80px;
            color: rgba(255, 255, 255, 0.9);
            margin-bottom: 30px;
            animation: bounce 2s infinite;
        }

        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% {
                transform: translateY(0);
            }
            40% {
                transform: translateY(-20px);
            }
            60% {
                transform: translateY(-10px);
            }
        }

        /* Main Title */
        .main-title {
            font-family: 'Dancing Script', cursive;
            font-size: clamp(3rem, 8vw, 6rem);
            color: white;
            margin-bottom: 20px;
            text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3);
            animation: fadeInUp 1s ease-out;
        }

        /* Subtitle */
        .subtitle {
            font-family: 'Quicksand', sans-serif;
            font-size: clamp(1.2rem, 3vw, 1.8rem);
            color: rgba(255, 255, 255, 0.9);
            margin-bottom: 40px;
            animation: fadeInUp 1s ease-out 0.3s both;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Family Icons */
        .family-icons {
            display: flex;
            gap: 40px;
            margin-bottom: 50px;
            animation: fadeInUp 1s ease-out 0.6s both;
        }

        .family-member {
            display: flex;
            flex-direction: column;
            align-items: center;
            color: white;
            transition: transform 0.3s ease;
        }

        .family-member:hover {
            transform: translateY(-10px);
        }

        .family-member i {
            font-size: 40px;
            margin-bottom: 10px;
            color: rgba(255, 255, 255, 0.9);
        }

        .family-member span {
            font-size: 14px;
            font-weight: 500;
        }

        /* Decorative Elements */
        .decorative-line {
            width: 100px;
            height: 3px;
            background: rgba(255, 255, 255, 0.6);
            margin: 0 auto 30px;
            position: relative;
            animation: expandWidth 1.5s ease-out 0.9s both;
        }

        @keyframes expandWidth {
            from {
                width: 0;
            }
            to {
                width: 100px;
            }
        }

        /* Quote */
        .quote {
            font-family: 'Quicksand', sans-serif;
            font-size: clamp(1rem, 2vw, 1.3rem);
            color: rgba(255, 255, 255, 0.8);
            font-style: italic;
            max-width: 600px;
            animation: fadeInUp 1s ease-out 1.2s both;
        }

        /* Hearts Animation */
        .hearts {
            position: absolute;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 5;
        }

        .heart {
            position: absolute;
            color: rgba(255, 255, 255, 0.3);
            font-size: 20px;
            animation: floatHeart 15s infinite linear;
        }

        @keyframes floatHeart {
            0% {
                transform: translateY(100vh) rotate(0deg);
                opacity: 0;
            }
            10% {
                opacity: 1;
            }
            90% {
                opacity: 1;
            }
            100% {
                transform: translateY(-100px) rotate(360deg);
                opacity: 0;
            }
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .family-icons {
                gap: 30px;
            }
            
            .family-member i {
                font-size: 35px;
            }
            
            .family-member span {
                font-size: 12px;
            }
            
            .decorative-line {
                width: 80px;
            }
        }

        @media (max-width: 480px) {
            .family-icons {
                flex-wrap: wrap;
                gap: 20px;
                justify-content: center;
            }
            
            .house-icon {
                font-size: 60px;
            }
        }
    </style>
</head>
<body>
    <!-- Animated Background -->
    <div class="bg-animation">
        <div class="floating-shape shape1"></div>
        <div class="floating-shape shape2"></div>
        <div class="floating-shape shape3"></div>
    </div>

    <!-- Floating Hearts -->
    <div class="hearts" id="hearts"></div>

    <!-- Main Content -->
    <div class="container">
        <!-- House Icon -->
        <div class="house-icon">
            <i class="fas fa-home"></i>
        </div>

        <!-- Main Title -->
        <h1 class="main-title">Keluargaku di Rumah</h1>

        <!-- Subtitle -->
        <p class="subtitle">Tempat Paling Indah di Dunia</p>

        <!-- Decorative Line -->
        <div class="decorative-line"></div>

        <!-- Family Icons -->
        <div class="family-icons">
            <div class="family-member">
                <i class="fas fa-male"></i>
                <span>Ayah</span>
            </div>
            <div class="family-member">
                <i class="fas fa-female"></i>
                <span>Ibu</span>
            </div>
            <div class="family-member">
                <i class="fas fa-child"></i>
                <span>Anak</span>
            </div>
            <div class="family-member">
                <i class="fas fa-baby"></i>
                <span>Adik</span>
            </div>
        </div>

        <!-- Quote -->
        <p class="quote">
            "Rumah bukanlah tempat, tapi perasaan. Dan keluarga adalah hati dari rumah."
        </p>
    </div>

    <script>
        // Create floating hearts
        function createHeart() {
            const heart = document.createElement('div');
            heart.className = 'heart';
            heart.innerHTML = '❤️';
            heart.style.left = Math.random() * 100 + '%';
            heart.style.animationDuration = (Math.random() * 10 + 10) + 's';
            heart.style.fontSize = (Math.random() * 10 + 15) + 'px';
            document.getElementById('hearts').appendChild(heart);

            // Remove heart after animation
            setTimeout(() => {
                heart.remove();
            }, 20000);
        }

        // Create hearts periodically
        setInterval(createHeart, 2000);

        // Add interactive hover effect to family members
        document.querySelectorAll('.family-member').forEach(member => {
            member.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-10px) scale(1.1)';
            });
            
            member.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0) scale(1)';
            });
        });

        // Add click effect to main title
        document.querySelector('.main-title').addEventListener('click', function() {
            this.style.animation = 'none';
            setTimeout(() => {
                this.style.animation = 'bounce 1s ease-out';
            }, 10);
        });
    </script>
</body>
</html>
    '''
    st.components.v1.html(koding1,height=1000)


if 'selected_animation' not in st.session_state:
    st.session_state.selected_animation = 'fade-in-up'

# Fungsi untuk membuat audio
def text_to_speech(text):
    tts = gTTS(text=text, lang='id')
    audio_bytes = io.BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    b64 = base64.b64encode(audio_bytes.read()).decode()
    return f'<audio autoplay src="data:audio/mp3;base64,{b64}">'

st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@400;700&family=Fredoka+One&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: 'Comic Neue', cursive;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
        padding: 20px;
        position: relative;
        overflow-x: hidden;
    }

    /* Main Container */
    .container {
        max-width: 900px;
        margin: 0 auto;
        background: rgba(255, 255, 255, 0.95);
        border-radius: 30px;
        padding: 40px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        position: relative;
        overflow: hidden;
    }

    /* Header */
    .header {
        text-align: center;
        margin-bottom: 40px;
        position: relative;
    }

    .title {
        font-family: 'Fredoka One', cursive;
        font-size: clamp(2rem, 5vw, 3rem);
        color: black;
        margin-bottom: 10px;
        animation: bounceIn 1s ease-out;

    }

    .subtitle {
        font-size: clamp(1.2rem, 3vw, 1.5rem);
        color: #764ba2;
        font-weight: 700;
        animation: fadeInUp 1s ease-out 0.3s both;
    }

    @keyframes bounceIn {
        0% {
            transform: scale(0.3);
        }
        50% {
            transform: scale(1.05);
        }
        70% {
            transform: scale(0.9);
        }
        100% {
            transform: scale(1);
        }
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* Family Illustration */
    .family-illustration {
        display: flex;
        justify-content: center;
        gap: 30px;
        margin: 40px 0;
        flex-wrap: wrap;
        animation: slideIn 1s ease-out 0.6s both;
    }

    .family-member {
        text-align: center;
        transition: transform 0.3s ease;
        cursor: pointer;
    }

    .family-member:hover {
        transform: translateY(-10px);
    }

    .member-icon {
        width: 80px;
        height: 80px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 10px;
        font-size: 40px;
        color: white;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    }

    .member-name {
        font-weight: 700;
        color: #5a67d8;
        font-size: 1.1rem;
    }

    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    /* Reading Section */
    .reading-section {
        background: #f7fafc;
        border-radius: 20px;
        padding: 30px;
        margin: 30px 0;
        box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.1);
        animation: fadeIn 1s ease-out 0.9s both;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    .paragraph {
        font-size: clamp(1.3rem, 3vw, 1.6rem);
        line-height: 2;
        color: #2d3748;
        margin-bottom: 20px;
        text-align: justify;
    }

    .word {
        display: inline-block;
        margin: 0 3px;
        padding: 2px 6px;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s ease;
        position: relative;
    }

    .word:hover {
        background: #e6fffa;
        transform: scale(1.1);
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    }

    .word.clicked {
        animation: wordPulse 0.6s ease;
        background: #bee3f8;
    }

    @keyframes wordPulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); background: #90cdf4; }
        100% { transform: scale(1); }
    }

    /* Controls */
    .controls {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 30px;
        flex-wrap: wrap;
    }

    .control-btn {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        padding: 15px 30px;
        border-radius: 50px;
        font-size: 1.1rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .control-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
    }

    /* Highlight Box */
    .highlight-box {
        background: #fef3c7;
        border: 3px dashed #f59e0b;
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        text-align: center;
        animation: wiggle 2s ease-in-out infinite;
    }

    @keyframes wiggle {
        0%, 100% { transform: rotate(0deg); }
        25% { transform: rotate(-1deg); }
        75% { transform: rotate(1deg); }
    }

    .highlight-text {
        font-size: 1.4rem;
        color: #92400e;
        font-weight: 700;
    }

    /* Decorative Elements */
    .star {
        position: absolute;
        color: #fbbf24;
        animation: twinkle 3s ease-in-out infinite;
    }

    @keyframes twinkle {
        0%, 100% { opacity: 0.3; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.2); }
    }

    .star1 { top: 10%; left: 5%; font-size: 30px; animation-delay: 0s; }
    .star2 { top: 20%; right: 10%; font-size: 25px; animation-delay: 1s; }
    .star3 { bottom: 15%; left: 8%; font-size: 35px; animation-delay: 2s; }
    .star4 { bottom: 25%; right: 5%; font-size: 28px; animation-delay: 0.5s; }

    /* Responsive */
    @media (max-width: 768px) {
        .container {
            padding: 20px;
        }
        
        .family-illustration {
            gap: 20px;
        }
        
        .member-icon {
            width: 60px;
            height: 60px;
            font-size: 30px;
        }
        
        .controls {
            gap: 10px;
        }
        
        .control-btn {
            padding: 12px 20px;
            font-size: 1rem;
        }
    }
</style>

""", unsafe_allow_html=True)

css_code = """
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@400;700&family=Fredoka+One&family=Quicksand:wght@500;700&display=swap');
    
    /* Container utama */
    .main-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 20px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }
    
    /* Container untuk teks animasi */
    .text-display {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 40px;
        margin: 20px 0;
        text-align: center;
        min-height: 200px;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
    }
    
    /* Animasi 1: Fade In Up */
    .fade-in-up {
        font-family: 'Quicksand', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        color: #5a67d8;
        animation: fadeInUp 1s ease-out;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Animasi 2: Bounce In */
    .bounce-in {
        font-family: 'Fredoka One', cursive;
        font-size: 2.5rem;
        color: #e53e3e;
        animation: bounceIn 1s ease-out;
    }
    
    @keyframes bounceIn {
        0% {
            opacity: 0;
            transform: scale(0.3);
        }
        50% {
            transform: scale(1.05);
        }
        70% {
            transform: scale(0.9);
        }
        100% {
            opacity: 1;
            transform: scale(1);
        }
    }
    
    /* Animasi 3: Slide In Left */
    .slide-in-left {
        font-family: 'Comic Neue', cursive;
        font-size: 2.5rem;
        font-weight: 700;
        color: #38a169;
        animation: slideInLeft 1s ease-out;
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-100px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Animasi 4: Zoom In */
    .zoom-in {
        font-family: 'Quicksand', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        color: #805ad5;
        animation: zoomIn 1s ease-out;
    }
    
    @keyframes zoomIn {
        from {
            opacity: 0;
            transform: scale(0);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }
    
    /* Animasi 5: Rotate In */
    .rotate-in {
        font-family: 'Fredoka One', cursive;
        font-size: 2.5rem;
        color: #d69e2e;
        animation: rotateIn 1s ease-out;
    }
    
    @keyframes rotateIn {
        from {
            opacity: 0;
            transform: rotate(-180deg) scale(0);
        }
        to {
            opacity: 1;
            transform: rotate(0) scale(1);
        }
    }
    
    /* Animasi 6: Glow Effect */
    .glow-effect {
        font-family: 'Comic Neue', cursive;
        font-size: 2.5rem;
        font-weight: 700;
        color: #3182ce;
        text-shadow: 0 0 10px rgba(49, 130, 206, 0.5);
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { text-shadow: 0 0 10px rgba(49, 130, 206, 0.5); }
        to { text-shadow: 0 0 20px rgba(49, 130, 206, 0.8), 0 0 30px rgba(49, 130, 206, 0.6); }
    }
    
    /* Style untuk kata per kata */
    .word-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 10px;
        margin: 20px 0;
    }
    
    .word {
        font-family: 'Comic Neue', cursive;
        font-size: 1.8rem;
        font-weight: 700;
        color: #4a5568;
        padding: 10px 15px;
        background: #e6fffa;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
        border: 2px solid transparent;
    }
    
    .word:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        background: #bee3f8;
        border-color: #4299e1;
    }
    
    .word.clicked {
        animation: wordPulse 0.6s ease;
        background: #90cdf4;
        border-color: #3182ce;
    }
    
    @keyframes wordPulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    
    /* Style untuk tombol */
    .control-buttons {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin: 20px 0;
        flex-wrap: wrap;
    }
    
    .btn {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        padding: 12px 25px;
        border-radius: 25px;
        font-size: 1rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    
    .btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
    }
    
    /* Style untuk input */
    .input-container {
        background: rgba(255, 255, 255, 0.95);
        padding: 25px;
        border-radius: 15px;
        margin: 20px 0;
    }
    
    /* Style untuk pilihan animasi */
    .animation-options {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 15px;
        margin: 20px 0;
    }
    
    .animation-card {
        background: rgba(255, 255, 255, 0.9);
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        border: 2px solid transparent;
    }
    
    .animation-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        border-color: #667eea;
    }
    
    .animation-card.selected {
        background: #e6fffa;
        border-color: #4299e1;
    }
    
    .animation-title {
        font-family: 'Quicksand', sans-serif;
        font-weight: 700;
        color: #4a5568;
        margin-bottom: 5px;
    }
    
    .animation-preview {
        font-size: 0.9rem;
        color: #718096;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .fade-in-up, .bounce-in, .slide-in-left, .zoom-in, .rotate-in, .glow-effect {
            font-size: 1.8rem;
        }
        
        .word {
            font-size: 1.4rem;
            padding: 8px 12px;
        }
    }
</style>
"""
st.markdown(css_code,unsafe_allow_html=True)
def halaman2():
    # Konten HTML tanpa JavaScript
    html_content = """
    <div class="container" style='margin-bottom:10px;'>
        <!-- Decorative Stars -->
    <i class="fas fa-star star star1"></i>
    <i class="fas fa-star star star2"></i>
    <i class="fas fa-star star star3"></i>
    <i class="fas fa-star star star4"></i>

    <!-- Header -->
    <header class="header">
        <h1 class="title" style='color:black;'>Keluargaku di Rumah</h1>
        <p class="subtitle">Mari Belajar Membaca dan Mengeja!</p>
    </header>

    <!-- Family Illustration -->
    <div class="family-illustration">
        <div class="family-member" onclick="speakText('Ayah')">
            <div class="member-icon">
                <i class="fas fa-male"></i>
            </div>
            <div class="member-name">Ayah</div>
        </div>
        <div class="family-member" onclick="speakText('Ibu')">
            <div class="member-icon">
                <i class="fas fa-female"></i>
            </div>
            <div class="member-name">Ibu</div>
        </div>
        <div class="family-member" onclick="speakText('Naima')">
            <div class="member-icon">
                <i class="fas fa-child"></i>
            </div>
            <div class="member-name">Aku</div>
        </div>
        <div class="family-member" onclick="speakText('Rizki')">
            <div class="member-icon">
                <i class="fas fa-baby"></i>
            </div>
            <div class="member-name">Adik</div>
        </div>

    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)
    # Tambahkan kontrol Streamlit
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔊 Baca Semua"):
            full_text = "Ini adalah keluargaku. Namaku Naima. Aku punya ayah dan ibu. Ayahku bernama Bapak Rudi. Ibuku bernama Ibu Siti. Aku juga punya adik laki-laki. Namanya Rizki. Kami tinggal di rumah yang indah. Rumahku besar dan nyaman. Setiap hari, kami sarapan bersama. Ayah membaca koran. Ibu memasak di dapur. Aku dan Rizki bermain di ruang tamu. Kami sangat bahagia."
            st.markdown(text_to_speech(full_text), unsafe_allow_html=True)
        
    with col2:
        if st.button("⏹️ Berhenti"):
            st.experimental_rerun()
        
    with col3:
        if st.button("🔄 Ulangi"):
            st.experimental_rerun()

    # Tampilkan kata-kata dengan tombol terpisah
    words = ["Ini", "adalah", "keluargaku", "Namaku", "Naima", "Aku", "punya", "ayah", "dan", "ibu"]
    selected_word = st.selectbox("Pilih kata untuk dibaca:", mengeja)

    if st.button("Baca Kata"):
        st.markdown(text_to_speech(selected_word.replace("-","")), unsafe_allow_html=True)
    st.markdown("""
    <div class="main-container">
        <h3 style="font-family: 'Quicksand', sans-serif; color: white; text-align: center; margin-bottom: 20px;">
            📖 Kalimat untuk Dibaca
        </h3>
        <div class="text-display">
            <div class="{}">{}</div>
        </div>
    </div>
    """.format(st.session_state.selected_animation, selected_word), unsafe_allow_html=True)
    audio_value1 = st.audio_input("Baca Ejaan")
    if audio_value1:
        st.audio(audio_value1)

def halaman3():
    
    koding1='''
    <head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        .container {
            max-width: 800px;
            width: 100%;
            background-color: white;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            overflow: hidden;
        }

        .header {
            background: linear-gradient(45deg, #ff9a9e 0%, #fecfef 100%);
            color: white;
            text-align: center;
            padding: 25px 20px;
            position: relative;
        }

        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }

        .weather-icon {
            position: absolute;
            top: 15px;
            right: 20px;
            font-size: 2rem;
            animation: float 3s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        .content {
            padding: 40px 30px;
        }

        .reading-text {
            line-height: 1.8;
            font-size: 1.2rem;
            color: #333;
            margin-bottom: 30px;
        }

        .sentence {
            margin-bottom: 20px;
            opacity: 0;
            transform: translateX(-20px);
            transition: all 0.5s ease;
        }

        .sentence.active {
            opacity: 1;
            transform: translateX(0);
        }

        .controls {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 30px;
        }

        
        .family-icons {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 30px;
        }

        .icon-item {
            text-align: center;
            opacity: 0.6;
            transition: all 0.3s ease;
        }

        .icon-item.active {
            opacity: 1;
            transform: scale(1.2);
        }

        .icon-item i {
            font-size: 2.5rem;
            color: #667eea;
            margin-bottom: 10px;
        }

        .icon-label {
            font-size: 0.9rem;
            color: #555;
        }

        .footer {
            text-align: center;
            padding: 20px;
            background: #f8f0e3;
            color: #666;
            font-style: italic;
        }

        @media (max-width: 600px) {
            .header h1 {
                font-size: 2rem;
            }
            
            .controls {
                flex-direction: column;
                gap: 15px;
            }
            
            .progress-bar {
                width: 80%;
            }
        }
    </style>
    </head>
    <body>
    <div class="container">
        <div style="text-align:center;margin:10px;"><img src="https://img95.lovepik.com/photo/40103/4905.gif_wh860.gif" style="width:200px;margin:10px"></div>
        <div class="header">
            <h1>Keluargaku di Rumah</h1>
        </div>

    </body>
    '''
    st.markdown(koding1,unsafe_allow_html=True)
if st.session_state.kondisi['kondisi1']:
    halaman1()
if st.session_state.kondisi['kondisi2']:
    halaman2()
if st.session_state.kondisi['kondisi3']:
    halaman3()
with st.sidebar:
    if st.button("Halaman Depan"):
        st.session_state.kondisi={'kondisi1':True,'kondisi2':False,'kondisi3':False, 'kondisi4':False, 'kondisi5':False}
        st.rerun()
    if st.button("Mengeja Kalimat"):
        st.session_state.kondisi={'kondisi1':False,'kondisi2':True,'kondisi3':False, 'kondisi4':False, 'kondisi5':False}
        st.rerun()
    if st.button("Mambaca Kalimat"):
        st.session_state.kondisi={'kondisi1':False,'kondisi2':False,'kondisi3':True, 'kondisi4':False, 'kondisi5':False}
        st.rerun()
