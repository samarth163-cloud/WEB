import sys

file_path = r'd:\Student\VS CODE project\website buy\new pro\buy.html'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    css_marker = '        nav ul li a:hover {\n            color: #ffffff;\n            transform: translateY(-1px);\n        }'
    
    new_css = '''        nav ul li a:hover {
            color: #ffffff;
            transform: translateY(-1px);
        }

        /* High-End Split Hero */
        .hero-split {
            display: flex;
            align-items: center;
            justify-content: space-between;
            max-width: 1200px;
            margin: 6rem auto 4rem auto;
            padding: 0 40px;
            gap: 60px;
            min-height: 50vh;
        }

        .hero-content {
            flex: 1;
            max-width: 550px;
            animation: slideUp 0.8s ease forwards;
            opacity: 0;
            transform: translateY(30px);
        }

        .hero-video-wrapper {
            flex: 1.2;
            animation: slideUp 0.8s ease forwards 0.2s;
            opacity: 0;
            transform: translateY(30px);
        }

        @keyframes slideUp {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .hero-badge {
            display: inline-block;
            background: rgba(255, 106, 0, 0.1);
            color: #ff6a00;
            border: 1px solid rgba(255, 106, 0, 0.3);
            padding: 8px 16px;
            border-radius: 100px;
            font-size: 0.9rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        .hero-title {
            font-size: 4rem;
            font-weight: 900;
            line-height: 1.1;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, #ffffff, #d1d1d1);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -2px;
        }

        .hero-subtitle {
            font-size: 1.8rem;
            color: #ffb3b3;
            font-weight: 500;
            margin-bottom: 2rem;
        }

        .hero-desc {
            font-size: 1.2rem;
            color: #a3a3a3;
            line-height: 1.6;
            margin-bottom: 2.5rem;
        }

        .price-box {
            display: flex;
            align-items: baseline;
            gap: 8px;
            margin-bottom: 2.5rem;
        }

        .price-currency {
            font-size: 1.5rem;
            color: #ffffff;
            font-weight: 600;
        }

        .price-amount {
            font-size: 3.5rem;
            color: #ffffff;
            font-weight: 800;
            letter-spacing: -1px;
        }

        .buy-action-btn {
            display: inline-flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            padding: 22px 30px;
            background: linear-gradient(135deg, #ff2a2a, #ff6a00);
            border-radius: 16px;
            color: #ffffff;
            font-size: 1.3rem;
            font-weight: 800;
            text-decoration: none;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            box-shadow: 0 15px 35px rgba(255, 42, 42, 0.3);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .buy-action-btn:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 45px rgba(255, 42, 42, 0.5);
        }

        .video-container-glass {
            position: relative;
            width: 100%;
            padding-bottom: 56.25%; /* 16:9 Aspect Ratio */
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 24px;
            box-shadow: 0 30px 60px rgba(0, 0, 0, 0.8);
            overflow: hidden;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            transform: perspective(1000px) rotateY(-5deg);
            transition: transform 0.5s ease;
        }
        
        .hero-video-wrapper:hover .video-container-glass {
             transform: perspective(1000px) rotateY(0deg);
        }

        .video-container-glass iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
        }

        @media (max-width: 992px) {
            .hero-split {
                flex-direction: column;
                text-align: center;
            }
            .hero-content {
                max-width: 100%;
            }
            .price-box {
                justify-content: center;
            }
            .video-container-glass {
                transform: none;
            }
            .hero-video-wrapper:hover .video-container-glass {
                transform: none;
            }
        }'''
        
    content = content.replace(css_marker, new_css)
    
    # Isolate and replace the target HTML block
    start_tag = '<!-- Main Hero Card (Glassmorphism) -->'
    end_tag = '<section class="bundle-section">'
    
    start_idx = content.find(start_tag)
    end_idx = content.find(end_tag)
    
    if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
        new_html = '''<!-- High-End Split Hero Section -->
    <main class="hero-split">
        <!-- Details & Buy Section -->
        <div class="hero-content">
            <div class="hero-badge">Premium Pack</div>
            <h1 class="hero-title">Creator Text Animations</h1>
            <h2 class="hero-subtitle">Pro-level text. One pack.</h2>
            
            <p class="hero-desc">
                Stop wasting hours animating text. Upgrade your content with 29 hand-crafted, drag & drop animations built for modern creators. 
            </p>

            <ul class="bundle-features" style="margin-bottom: 2rem;">
                <li>29 beautiful drag & drop text animations</li>
                <li>Fully customizable (fonts, colors, fps)</li>
                <li>Lifetime updates included</li>
            </ul>

            <div class="price-box">
                <span class="price-currency">$</span>
                <span class="price-amount">15</span>
                <span class="price-currency">USD</span>
            </div>

            <a href="#" class="buy-action-btn">Buy Now</a>
        </div>

        <!-- Video Section -->
        <div class="hero-video-wrapper">
            <div class="video-container-glass">
                <iframe src="https://www.youtube.com/embed/FuJMmRrjnQw?autoplay=1&mute=1&loop=1&playlist=FuJMmRrjnQw&controls=0" frameborder="0" allowfullscreen title="Creator Text Animations Preview"></iframe>
            </div>
        </div>
    </main>

    '''
        content = content[:start_idx] + new_html + content[end_idx:]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated buy.html!")
    else:
        print("Could not find HTML boundaries!")
except Exception as e:
    print(f"Error: {e}")
