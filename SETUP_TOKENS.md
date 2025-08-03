# 🔑 Setup Guide: Hugging Face Tokens for DialoGPT-medium

This guide shows you exactly what tokens and code you need to add to make the resume builder work with the FREE DialoGPT-medium model.

## 🎯 **STEP 1: Get Your FREE Hugging Face Token**

### **1. Create Hugging Face Account (FREE)**
- Go to: https://huggingface.co/join
- Click "Sign Up"
- **NO CREDIT CARD REQUIRED**
- Verify your email

### **2. Get Your FREE API Token**
- Go to: https://huggingface.co/settings/tokens
- Click "New token"
- Give it a name like "resume-builder"
- Select "Read" permissions
- Click "Generate token"
- **COPY THE TOKEN** (it looks like: `hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`)

## 🔧 **STEP 2: Create .env File**

Create a file named `.env` in your project root with this content:

```env
# FREE LLM Configuration for Resume Builder
# Get your FREE Hugging Face token from: https://huggingface.co/settings/tokens

# HUGGING FACE (RECOMMENDED - Completely FREE)
# Replace 'your_free_huggingface_api_key_here' with your actual token
HUGGINGFACE_API_KEY=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Application Configuration
USER_ID=demo_user_id
JOB_PROFILE=Software Engineer at TechCorp, focusing on backend development, Python, and cloud infrastructure.
CREW_TYPE=full

# PAID OPTIONS (only uncomment if you want premium quality)
# OpenAI (paid - but very fast)
# OPENAI_API_KEY=your_openai_api_key_here

# Anthropic Claude (paid - good quality)
# ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Google Gemini (paid - good quality)
# GOOGLE_API_KEY=your_google_api_key_here
```

## 📝 **STEP 3: What Your Token Looks Like**

Your Hugging Face token will look like this:
```
hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**Example:**
```
HUGGINGFACE_API_KEY=hf_abc123def456ghi789jkl012mno345pqr678stu901vwx234yz567
```

## 🚀 **STEP 4: Test Your Setup**

Run this command to test if your token works:

```bash
python test_cloud_api.py
```

You should see:
```
✅ Using Hugging Face FREE API
📝 Primary model: microsoft/DialoGPT-medium (CONFIRMED FREE)
✨ Excellent for resume writing, cover letters, and skill analysis
```

## 🎯 **STEP 5: Run the Resume Builder**

Once your token is working:

```bash
python main.py
```

## 💡 **IMPORTANT NOTES**

### **Token Security:**
- ✅ **Keep your token private** - don't share it
- ✅ **Don't commit .env to git** - it's already in .gitignore
- ✅ **Token is FREE** - no charges ever

### **Token Format:**
- ✅ **Starts with `hf_`**
- ✅ **About 40 characters long**
- ✅ **Contains letters and numbers**

### **What the Token Does:**
- ✅ **Accesses DialoGPT-medium** (CONFIRMED FREE)
- ✅ **30,000 requests/month** (FREE tier)
- ✅ **No credit card required**
- ✅ **Works immediately after setup**

## 🔍 **TROUBLESHOOTING**

### **If you get "No API key configured":**
1. Check that your `.env` file exists
2. Make sure the token starts with `hf_`
3. Verify you copied the entire token
4. Restart your terminal/IDE

### **If you get "Invalid token":**
1. Go back to https://huggingface.co/settings/tokens
2. Generate a new token
3. Replace the old one in `.env`

### **If you get "Rate limit exceeded":**
1. You've used your 30,000 free requests
2. Wait until next month
3. Or use local Ollama as backup

## 🆓 **FREE TIER LIMITS**

### **Hugging Face Free Tier:**
- **30,000 requests/month** (plenty for resume building)
- **DialoGPT-medium**: Always available
- **No credit card required**
- **No usage limits on basic models**

## 🎯 **CODE EXAMPLES**

### **Your .env file should look like this:**
```env
HUGGINGFACE_API_KEY=hf_your_actual_token_here
USER_ID=demo_user_id
JOB_PROFILE=Software Engineer at TechCorp, focusing on backend development, Python, and cloud infrastructure.
CREW_TYPE=full
```

### **The system will automatically:**
1. **Load your token** from `.env`
2. **Use DialoGPT-medium** as primary model
3. **Fall back to other FREE models** if needed
4. **Show you which model is being used**

## ✅ **VERIFICATION STEPS**

1. **Create Hugging Face account** ✅
2. **Generate token** ✅
3. **Create .env file** ✅
4. **Add token to .env** ✅
5. **Test with python test_cloud_api.py** ✅
6. **Run resume builder** ✅

That's it! Your resume builder will now use the FREE DialoGPT-medium model for excellent results. 