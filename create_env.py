#!/usr/bin/env python3
"""
Script to help create the .env file with API key configuration.
"""

import os
from pathlib import Path

def create_env_file():
    """Create the .env file with proper configuration."""
    
    env_content = """# LLM Configuration for Resume Builder
# Get your FREE Hugging Face token from: https://huggingface.co/settings/tokens
# Get your Google Gemini API key from: https://makersuite.google.com/app/apikey

# GOOGLE GEMINI (RECOMMENDED - if you have API key)
# Get your API key from: https://makersuite.google.com/app/apikey
GOOGLE_API_KEY=your_gemini_api_key_here

# HUGGING FACE (FREE tier available)
# Get your FREE API key from: https://huggingface.co/settings/tokens
# No credit card required, completely free!
HUGGINGFACE_API_KEY=your_free_huggingface_api_key_here

# Application Configuration
USER_ID=demo_user_id
JOB_PROFILE=Software Engineer at TechCorp, focusing on backend development, Python, and cloud infrastructure.
CREW_TYPE=full

# PAID OPTIONS (only uncomment if you want premium quality)
# OpenAI (paid - but very fast)
# OPENAI_API_KEY=your_openai_api_key_here

# Anthropic Claude (paid - good quality)
# ANTHROPIC_API_KEY=your_anthropic_api_key_here
"""
    
    env_file = Path(".env")
    
    if env_file.exists():
        print("⚠️  .env file already exists!")
        print("📝 Please edit the existing .env file and add your API keys")
        print("🔑 Add your Gemini API key: GOOGLE_API_KEY=your_key_here")
        print("🔑 Add your Hugging Face token: HUGGINGFACE_API_KEY=your_token_here")
        return False
    else:
        with open(".env", "w") as f:
            f.write(env_content)
        print("✅ Created .env file successfully!")
        print("📝 Please edit the .env file and add your API keys")
        print("🔑 Add your Gemini API key: GOOGLE_API_KEY=your_key_here")
        print("🔑 Add your Hugging Face token: HUGGINGFACE_API_KEY=your_token_here")
        return True

def show_token_instructions():
    """Show instructions for getting API keys."""
    print("\n" + "="*60)
    print("🔑 HOW TO GET YOUR API KEYS")
    print("="*60)
    
    print("\n📋 STEP-BY-STEP INSTRUCTIONS:")
    
    print("\n1️⃣ GOOGLE GEMINI (RECOMMENDED)")
    print("   • Go to: https://makersuite.google.com/app/apikey")
    print("   • Sign in with your Google account")
    print("   • Click 'Create API Key'")
    print("   • Copy the API key")
    print("   • Add to .env: GOOGLE_API_KEY=your_key_here")
    print("   • ✅ Excellent for resume building")
    
    print("\n2️⃣ HUGGING FACE (FREE)")
    print("   • Go to: https://huggingface.co/settings/tokens")
    print("   • Create a FREE account (no credit card required)")
    print("   • Create a new token")
    print("   • Add to .env: HUGGINGFACE_API_KEY=your_token_here")
    print("   • ✅ Completely FREE")
    
    print("\n3️⃣ TEST YOUR SETUP")
    print("   • Run: python test_simple_models.py")
    print("   • Should show which API is being used")
    
    print("\n" + "="*60)
    print("💡 API KEY FORMATS:")
    print("   • Gemini: AIzaSyC... (starts with 'AIza')")
    print("   • Hugging Face: hf_abc123... (starts with 'hf_')")
    print("="*60)

def main():
    """Main function."""
    print("🔧 Resume Builder - Environment Setup")
    print("="*40)
    
    # Create .env file
    created = create_env_file()
    
    # Show instructions
    show_token_instructions()
    
    if created:
        print("\n🎉 Setup complete!")
        print("📝 Next: Edit .env file and add your API keys")
        print("🧪 Then: Run 'python test_simple_models.py' to test")
    else:
        print("\n📝 Please edit your existing .env file")
        print("🔑 Add your Gemini API key: GOOGLE_API_KEY=your_key_here")
        print("🔑 Add your Hugging Face token: HUGGINGFACE_API_KEY=your_token_here")

if __name__ == "__main__":
    main() 