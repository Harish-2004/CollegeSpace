#!/usr/bin/env python3
"""
Setup script for Hugging Face with DeepSeek inference provider.
"""

import os
from dotenv import load_dotenv

def create_huggingface_setup():
    """Create Hugging Face setup instructions."""
    
    print("🎯 Hugging Face with DeepSeek-V3 Setup Guide")
    print("="*50)
    
    print("\n📋 Step 1: Get FREE Hugging Face Token")
    print("1. Go to: https://huggingface.co/settings/tokens")
    print("2. Create a FREE account (no credit card required)")
    print("3. Click 'New token'")
    print("4. Name: 'resume-builder'")
    print("5. Role: 'Read' (FREE tier)")
    print("6. Click 'Generate token'")
    print("7. Copy the token (starts with 'hf_')")
    
    print("\n📋 Step 2: Update .env file")
    print("Add this line to your .env file:")
    print("HUGGINGFACE_API_KEY=hf_your_token_here")
    
    print("\n📋 Step 3: Test Configuration")
    print("Run: python test_cloud_api.py")
    
    print("\n✅ Benefits of DeepSeek-V3 via Hugging Face:")
    print("   • EXCELLENT for resume building")
    print("   • Professional writing quality")
    print("   • Great job analysis")
    print("   • Strong ATS optimization")
    print("   • FREE tier available")

def create_env_template():
    """Create .env template for Hugging Face."""
    env_content = """# HUGGING FACE WITH DEEPSEEK (RECOMMENDED)
HUGGINGFACE_API_KEY=hf_your_free_huggingface_token_here

# Application Configuration
USER_ID=demo_user_id
JOB_PROFILE=Software Engineer at TechCorp, focusing on backend development, Python, and cloud infrastructure.
CREW_TYPE=full
"""
    
    print("\n📝 .env Template for Hugging Face:")
    print("="*40)
    print(env_content)
    
    # Try to create/update .env file
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        print("\n✅ .env file updated with Hugging Face configuration")
    except Exception as e:
        print(f"\n⚠️  Could not update .env file: {e}")
        print("💡 Please manually add the configuration above to your .env file")

def check_current_setup():
    """Check current setup."""
    load_dotenv()
    
    print("\n🔍 Checking Current Setup:")
    
    api_key = os.getenv("HUGGINGFACE_API_KEY")
    if api_key and api_key != "hf_your_free_huggingface_token_here":
        print("✅ Hugging Face API key found")
        print(f"   Token: {api_key[:10]}...")
    else:
        print("❌ Hugging Face API key not found")
        print("💡 Get FREE token from: https://huggingface.co/settings/tokens")

def main():
    """Main setup function."""
    print("🚀 Hugging Face with DeepSeek Setup")
    print("="*50)
    
    # Show setup instructions
    create_huggingface_setup()
    
    # Create .env template
    create_env_template()
    
    # Check current setup
    check_current_setup()
    
    print("\n🎯 Next Steps:")
    print("1. Get your FREE Hugging Face token")
    print("2. Update your .env file with the token")
    print("3. Test: python test_cloud_api.py")
    print("4. Run resume builder: python main.py")

if __name__ == "__main__":
    main() 