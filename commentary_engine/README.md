# Advaitian Commentary Engine

This is the Streamlit interface for the Advaitian Commentary Engine, designed to process Minimum Viable Commentaries (MVC) into high-rigor Stage 2 Commentaries using the Google Gemini API and persisting to Firebase Firestore.

## Local Development

The app automatically inherits your API keys if you have placed them in the parent directory (`advaitian-philosophy`):
1. `AIzaSyCFoDs_OGzL65bacvVJzipZsxWx6YF.txt` (Gemini API Key)
2. `advaitian-commentary-engine-firebase-adminsdk-fbsvc-70e4298d89.json` (Firebase Admin SDK Key)

### To Run Locally:
```bash
# Navigate to the directory
cd commentary_engine

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## Deployment (Streamlit Cloud - Recommended)

To deploy exactly like the `vriddhi-core` repository:

1. **Push to GitHub / GitLab:**
   Commit this `commentary_engine` directory to your repository. **Note:** `.gitignore` ensures your local secret keys are NOT uploaded to source control.

2. **Deploy on Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Connect your repository and select the `commentary_engine` branch/folder.
   - Set **Main file path**: `commentary_engine/app.py`
   - Click "Deploy".

3. **Configure Secrets in Streamlit Cloud:**
   Since your local keys weren't uploaded, you must provide them securely on the server!
   - In your app dashboard (bottom right), click "Settings" → "Secrets"
   - Add your keys in TOML format:

   ```toml
   GEMINI_API_KEY = "your-actual-gemini-api-key"

   [firebase]
   type = "service_account"
   project_id = "advaitian-commentary-engine"
   private_key_id = "..."
   private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
   client_email = "..."
   client_id = "..."
   auth_uri = "https://accounts.google.com/o/oauth2/auth"
   token_uri = "https://oauth2.googleapis.com/token"
   auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
   client_x509_cert_url = "..."
   ```
   *(Hint: You can just copy the contents of your `advaitian-commentary-engine-firebase*.json` directly into the `[firebase]` block with exactly those keys).*

The engine will auto-detect the secrets on the cloud, just as it auto-detects the files on your local machine.
