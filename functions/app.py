import os
import logging
from flask import Flask, render_template
from netlify_functions import handler  # Netlify helper to integrate Flask with serverless

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app, pointing to the correct template and static folders
# Ensure paths are correct in serverless environment
project_root = os.path.dirname(os.path.abspath(__file__))  # Get absolute path to the 'RDC-3.1' project root directory

# Create Flask app with correct template and static folder paths
app = Flask(__name__,
            template_folder=os.path.join(project_root, '..', 'templates'),  # Path to templates
            static_folder=os.path.join(project_root, '..', 'static'))      # Path to static files

# Set a secret key for sessions (if needed)
app.secret_key = os.environ.get("SESSION_SECRET", "your-secure-key")  # Add default if not set

# Routes (your routes remain the same)
@app.route('/')
def index():
    return render_template('index.html', active_page='home')

@app.route('/services')
def services():
    return render_template('services.html', active_page='services')

@app.route('/about')
def about():
    return render_template('about.html', active_page='about')

@app.route('/team')
def team():
    return render_template('team.html', active_page='team')

@app.route('/social-services')
def social_services():
    return render_template('social_services.html', active_page='about')

@app.route('/media')
def media():
    return render_template('media.html', active_page='about')

@app.route('/why-choose-us')
def why_choose_us():
    return render_template('why_choose_us.html', active_page='why_choose_us')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html', active_page='privacy')

@app.route('/terms')
def terms():
    return render_template('terms.html', active_page='terms')

@app.route('/services/dental-implants')
def dental_implants():
    return render_template('services/dental_implants.html', active_page='services')

@app.route('/services/full-mouth-rehabilitation')
def full_mouth_rehabilitation():
    return render_template('services/full_mouth_rehabilitation.html', active_page='services')

@app.route('/services/invisible-aligners')
def invisible_aligners():
    return render_template('services/invisible_aligners.html', active_page='services')

@app.route('/services/smile-makeover')
def smile_makeover():
    return render_template('services/smile_makeover.html', active_page='services')

@app.route('/services/crowns-bridges')
def crowns_bridges():
    return render_template('services/crowns_bridges.html', active_page='services')

@app.route('/services/teeth-whitening')
def teeth_whitening():
    return render_template('services/teeth_whitening.html', active_page='services')

@app.route('/services/braces-treatment')
def braces_treatment():
    return render_template('services/braces_treatment.html', active_page='services')

@app.route('/services/tooth-colored-fillings')
def tooth_colored_fillings():
    return render_template('services/tooth_colored_fillings.html', active_page='services')

@app.route('/services/wisdom-tooth-extraction')
def wisdom_tooth_extraction():
    return render_template('services/wisdom_tooth_extraction.html', active_page='services')

@app.route('/services/root-canal-treatment')
def root_canal_treatment():
    return render_template('services/root_canal-treatment.html', active_page='services')

@app.route('/contact')
def contact():
    return render_template('contact.html', active_page='contact')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', active_page='gallery')

# This tells Netlify to handle the Flask app as a serverless function
handler(app)
