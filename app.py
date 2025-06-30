import streamlit as st
from PIL import Image


def ocr_extract_text(image):
    
    return "Sodium Nitrate\nSugar\nMSG"

def analyze_ingredient(text):
    harmful = ['nitrate', 'msg']
    label = 'harmful' if any(h in text.lower() for h in harmful) else 'safe'
    return {
        "ingredient": text,
        "risk_level": "High" if label == 'harmful' else "Low",
        "side_effects": "May cause headaches or allergic reactions" if label == 'harmful' else "None",
        "alert_color": "Red" if label == 'harmful' else "Green"
    }

def create_alert(analysis):
    return analysis

def colored_label(text, color):
    return f"<span style='background-color:{color}; padding:5px 10px; border-radius:5px; color:white;'>{text}</span>"



st.set_page_config(page_title="Smart Ingredient Watchdog", layout="wide")
st.title("🛡️ Smart Ingredient Watchdog")


st.sidebar.title("ℹ️ About")
st.sidebar.info("""
Upload a product label image or enter ingredients manually.
The app detects harmful additives and warns you with color-coded alerts.
""")

col1, col2 = st.columns([1, 2])

with col1:
    uploaded_file = st.file_uploader("📷 Upload product label image", type=['png', 'jpg', 'jpeg'])
    manual_input = st.text_area("✍️ Or enter ingredients manually (comma separated)")

ingredients = []

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    text = ocr_extract_text(image)  # Replace with your OCR function
    ingredients = [line.strip() for line in text.split('\n') if line.strip()]

elif manual_input:
    ingredients = [ing.strip() for ing in manual_input.split(',') if ing.strip()]

if ingredients:
    with col2:
        st.header("🔎 Ingredient Analysis")

        status_emoji = {"Red": "🚨", "Green": "✅", "Yellow": "⚠️"}
        color_map = {"Red": "#e74c3c", "Green": "#27ae60", "Yellow": "#f39c12"}

        for ingredient in ingredients:
            analysis = analyze_ingredient(ingredient)
            alert = create_alert(analysis)

            color_hex = color_map.get(alert['alert_color'], "#95a5a6")
            emoji = status_emoji.get(alert['alert_color'], "")

            with st.expander(f"{emoji} {alert['ingredient']} - Risk: {alert['risk_level']}"):
                st.markdown(f"**Risk Level:** <span style='color:{color_hex}; font-weight:bold'>{alert['risk_level']}</span>", unsafe_allow_html=True)
                st.markdown(f"**Side Effects:** {alert['side_effects']}")
                st.markdown(f"**Alert Color:** {alert['alert_color']}")
else:
    st.info("Please upload an image or enter ingredients manually to get analysis.")
