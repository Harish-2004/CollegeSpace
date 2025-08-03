#!/usr/bin/env python3
"""
Test script for DeepSeek-V3 with Hugging Face router API.
"""

import os
from dotenv import load_dotenv
from crewai import LLM

def test_deepseek_v3():
    """Test DeepSeek-V3 configuration."""
    load_dotenv()
    
    api_key = os.getenv("HUGGINGFACE_API_KEY")
    if not api_key:
        print("❌ HUGGINGFACE_API_KEY not found in .env file")
        return False
    
    print(f"🔑 API Key found: {api_key[:10]}...")
    
    try:
        # Test DeepSeek-V3 with Hugging Face router
        llm = LLM(
            model="huggingface/deepseek-ai/DeepSeek-V3-0324:novita",
            api_key=api_key,
            base_url="https://router.huggingface.co/v1",
            temperature=0.7
        )
        
        print("✅ DeepSeek-V3 LLM configured successfully")
        
        # Test a simple call
        response = llm.call("Hello, this is a test message for resume building.")
        print("✅ API call successful!")
        print(f"📝 Response: {response[:200]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ DeepSeek-V3 test failed: {e}")
        return False

def main():
    """Main test function."""
    print("🧪 Testing DeepSeek-V3 Configuration")
    print("="*50)
    
    if test_deepseek_v3():
        print("\n🎉 DeepSeek-V3 configuration successful!")
        print("✅ Your DeepSeek-V3 setup is working")
        print("🚀 You can now run: python main.py")
    else:
        print("\n❌ DeepSeek-V3 configuration failed")
        print("\n💡 Troubleshooting:")
        print("1. Make sure your Hugging Face token is valid")
        print("2. Check your internet connection")
        print("3. Verify the token has proper permissions")
        print("4. Run: python setup_huggingface.py")

if __name__ == "__main__":
    main() 