## ⚠️ Security Notice

This repository contains a sample implementation of the project. Certain components, including cloud configuration files, credentials, and sensitive integration logic, have been intentionally excluded to protect security and prevent unauthorized access.

In particular:
- AWS credentials and access keys are not included  
- Environment configuration files (.env) are omitted  
- Some cloud deployment scripts and endpoints are removed  

These elements are critical for secure cloud operations and cannot be shared publicly.

If you would like to understand the complete implementation or discuss the architecture in detail, feel free to contact me.

Thank you for your understanding.


# FIC CLOUD - File Integrity Checker

FIC CLOUD is a full-stack web application designed to protect and verify the integrity of your digital files using AWS Cloud infrastructure.

## 🚀 Features
- **Secure Authentication**: AWS Cognito integrated for user management.
- **Cloud Storage**: Files are securely stored in AWS S3.
- **Integrity Verification**: blake3 hashing to detect tampering.
- **Metadata Management**: DynamoDB tracks file history and hashes.
- **Premium UI**: Modern, responsive React dashboard with glassmorphism.

---

## 🛠️ Backend Setup (FastAPI)

1. **Install Dependencies**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Configure Environment**:
   Update `backend/.env` with your AWS credentials:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `S3_BUCKET_NAME`
   - `COGNITO_USER_POOL_ID`
   - `COGNITO_APP_CLIENT_ID`

3. **Run Server**:
   ```bash
   python app/main.py
   ```
   API will be available at `http://localhost:8000`.

---

## 💻 Frontend Setup (React + Vite)

1. **Install Dependencies**:
   ```bash
   cd frontend
   npm install
   ```

2. **Run Development Server**:
   ```bash
   npm run dev
   ```
   App will be available at `http://localhost:3000`.

---

## ☁️ AWS Resource Setup Guide

### 1. AWS Cognito
- Create a **User Pool**.
- Create an **App Client** (Disable "Generate client secret" for frontend compatibility).
- Enable **Allow unauthenticated identities** (optional, based on IAM policy).
- Ensure `USER_PASSWORD_AUTH` is enabled in Authentication Flows.

### 2. AWS S3
- Create a bucket named `your-fic-bucket-name`.
- Enable **CORS** on the bucket to allow requests from your frontend:
  ```json
  [
    {
      "AllowedHeaders": ["*"],
      "AllowedMethods": ["GET", "PUT", "POST", "HEAD"],
      "AllowedOrigins": ["*"],
      "ExposedHeaders": ["ETag"]
    }
  ]
  ```

### 3. AWS DynamoDB
- Create a table named `fic_metadata`.
- Set `file_id` (String) as the **Partition Key**.
- (Optional) Add a GSI on `user_id` for efficient filtering (though the app uses a scan/filter for simplicity).

### 4. IAM Permissions
Ensure your AWS User has the following permissions:
- `AmazonS3FullAccess`
- `AmazonDynamoDBFullAccess`
- `AmazonCognitoPowerUser`

---

## 🛡️ Security Best Practices
- **JWT tokens** are used for every API call.
- Files are stored in user-specific S3 prefixes (`{user_id}/...`).
- Hashes are calculated on the server to prevent client-side spoofing.


To compile 
1. cd backend 
2. python -m uvicorn app.main:app --reload
3. cd frontend
4. npm run dev
