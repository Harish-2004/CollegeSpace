#!/usr/bin/env python3
"""
Setup script for FREE cloud API configuration.
This will help you set up FREE API keys for cost-effective performance.
"""

import os
import sys
from pathlib import Path

def create_env_file():
    """Create a .env file with FREE API key placeholders."""
    env_content = """# FREE LLM Configuration for Resume Builder
# Uncomment and add your FREE API keys

# Option 1: Hugging Face (RECOMMENDED - FREE tier available)
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

# Google Gemini (paid - good quality)
# GOOGLE_API_KEY=your_google_api_key_here
"""
    
    env_file = Path(".env")
    if env_file.exists():
        print("⚠️  .env file already exists. Backing up to .env.backup")
        env_file.rename(".env.backup")
    
    with open(".env", "w") as f:
        f.write(env_content)
    
    print("✅ Created .env file with FREE API key placeholders")
    print("📝 Please edit .env file and add your FREE API keys")

def print_setup_instructions():
    """Print setup instructions for FREE API providers."""
    print("\n" + "="*60)
    print("🆓 FREE LLM SETUP INSTRUCTIONS")
    print("="*60)
    
    print("\n📋 FREE OPTIONS (in order of preference):")
    
    print("\n1️⃣ HUGGING FACE (RECOMMENDED - Completely FREE)")
    print("   • Go to: https://huggingface.co/settings/tokens")
    print("   • Create a FREE account (no credit card required)")
    print("   • Create a new token")
    print("   • Add to .env: HUGGINGFACE_API_KEY=your_token_here")
    print("   • ✅ Completely FREE, no limits, reliable")
    print("   • 🚀 Fast cloud-based inference")
    
    print("\n2️⃣ LOCAL OLLAMA (FREE - if you have enough RAM)")
    print("   • Install Ollama: https://ollama.ai/download")
    print("   • Run: ollama pull mistral")
    print("   • No API key needed - runs locally")
    print("   • ✅ Completely FREE, runs on your computer")
    print("   • ⚠️  Requires 8GB+ RAM for good performance")
    
    print("\n3️⃣ MOCK LLM (FREE - for testing)")
    print("   • No setup required")
    print("   • Used automatically if no other options available")
    print("   • ✅ Completely FREE, instant responses")
    print("   • ⚠️  Only for testing, not for production")
    
    print("\n" + "="*60)
    print("💰 PAID OPTIONS (only if you want premium quality):")
    print("• OpenAI: https://platform.openai.com/api-keys")
    print("• Anthropic: https://console.anthropic.com/")
    print("• Google: https://makersuite.google.com/app/apikey")
    print("="*60)
    
    print("\n💡 TIPS:")
    print("• Start with Hugging Face (completely FREE)")
    print("• You only need ONE API key to get started")
    print("• The system will automatically use the best FREE option")
    print("• Local Ollama will be used if you have it installed")
    print("• Mock LLM will be used as final fallback for testing")
    print("="*60)

def test_api_connection():
    """Test if any FREE API keys are configured and working."""
    print("\n🔍 TESTING FREE API CONNECTIONS...")
    
    from config.llm_config import get_llm_config
    
    try:
        llm = get_llm_config()
        print("✅ FREE API connection successful!")
        print(f"📡 Using: {type(llm).__name__}")
        
        # Test a simple call
        print("\n🧪 Testing FREE API call...")
        response = llm.call("Hello, this is a test message.")
        print("✅ FREE API call successful!")
        print(f"📝 Response preview: {response[:100]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ API connection failed: {e}")
        print("💡 Please configure at least one FREE API key in .env file")
        return False

def main():
    """Main setup function."""
    print("🤖 Resume Builder - FREE LLM Setup")
    print("="*40)
    
    # Create .env file
    create_env_file()
    
    # Print instructions
    print_setup_instructions()
    
    # Test connection
    if test_api_connection():
        print("\n🎉 Setup complete! You can now run the resume builder for FREE.")
        print("💡 Run: python main.py")
    else:
        print("\n⚠️  Please configure at least one FREE API key and run this script again.")

if __name__ == "__main__":
    main() 