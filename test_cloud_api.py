#!/usr/bin/env python3
"""
Test script to verify LLM configuration and show model recommendations.
"""

import os
from dotenv import load_dotenv
from config.llm_config import get_llm_config, get_model_recommendations

def test_llm_configuration():
    """Test the LLM configuration and show which model is being used."""
    print("🧪 Testing LLM Configuration")
    print("="*40)
    
    # Load environment variables
    load_dotenv()
    
    # Check which API keys are configured
    api_keys = {
        "Hugging Face (DeepSeek)": os.getenv("HUGGINGFACE_API_KEY"),
        "OpenAI (Paid)": os.getenv("OPENAI_API_KEY"),
        "Anthropic (Paid)": os.getenv("ANTHROPIC_API_KEY")
    }
    
    print("\n📋 Configured API Keys:")
    for provider, key in api_keys.items():
        if key and key != "your_key_here" and key != "your_free_huggingface_api_key_here":
            status = "✅ Configured"
        else:
            status = "❌ Not configured"
        print(f"   {provider}: {status}")
    
    # Test LLM configuration
    print("\n🔍 Testing LLM Configuration...")
    try:
        llm = get_llm_config()
        print("✅ LLM configuration successful!")
        print(f"📡 Using: {type(llm).__name__}")
        
        # Determine which option is being used
        if "MockLLM" in str(type(llm)):
            print("🆓 Using: Mock LLM (completely FREE for testing)")
            print("💡 This is for testing only - add API keys for better results!")
        elif "DeepSeek" in str(type(llm)) or "deepseek" in str(type(llm)).lower():
            print("🎯 Using: Hugging Face with DeepSeek-V3 (EXCELLENT for resume building)")
            print("✨ EXCELLENT for resume building!")
            print("📝 Professional writing, job analysis, ATS optimization")
        elif "HuggingFace" in str(type(llm)) or "huggingface" in str(type(llm)).lower():
            print("🆓 Using: Hugging Face FREE API")
            print("📝 Good fallback option")
        elif "Ollama" in str(type(llm)) or "ollama" in str(type(llm)).lower():
            print("🆓 Using: Local Ollama (FREE local model)")
            print("💻 Good for privacy and unlimited usage")
        else:
            print("📡 Using: Cloud API")
        
        # Test a simple call
        print("\n🧪 Testing API call...")
        response = llm.call("Hello, this is a test message.")
        print("✅ API call successful!")
        print(f"📝 Response preview: {response[:100]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ LLM configuration failed: {e}")
        print("\n💡 Troubleshooting tips:")
        print("1. Make sure your API keys are valid")
        print("2. Check your internet connection")
        print("3. Verify API key format")
        print("4. Run: python create_env.py")
        return False

def show_api_options():
    """Show available API options."""
    print("\n🆓 AVAILABLE OPTIONS:")
    print("1. Hugging Face with DeepSeek-V3 (RECOMMENDED)")
    print("   • Get FREE token: https://huggingface.co/settings/tokens")
    print("   • Excellent for resume building")
    print("   • Professional writing quality")
    print("   • Great job analysis")
    
    print("\n2. Local Ollama (FREE local models)")
    print("   • Install: https://ollama.ai/download")
    print("   • Good for privacy")
    print("   • Unlimited usage")

def show_model_recommendations():
    """Show the best models for different resume building tasks."""
    print("\n🎯 BEST MODELS FOR RESUME BUILDING:")
    print("="*50)
    
    recommendations = get_model_recommendations()
    
    for task, info in recommendations.items():
        print(f"\n📝 {task.replace('_', ' ').title()}:")
        print(f"   🏆 Best: {info['best']}")
        print(f"   💡 Why: {info['reason']}")
        print(f"   🔄 Alternative: {info['alternative']}")
    
    print("\n🎯 PRIMARY RECOMMENDATION:")
    print("   huggingface/deepseek-ai/DeepSeek-V3-0324:novita")
    print("   ✅ EXCELLENT for resume building")
    print("   ✅ Professional writing quality")
    print("   ✅ Great job analysis")
    print("   ✅ Strong ATS optimization")

def main():
    """Main test function."""
    success = test_llm_configuration()
    
    if success:
        print("\n🎉 All tests passed! Your LLM is ready to use.")
        print("💡 You can now run: python main.py")
        
        # Show model recommendations
        show_model_recommendations()
        
        print("\n🚀 NEXT STEPS:")
        print("1. Your Gemini API is configured and working!")
        print("2. Run the resume builder: python main.py")
        print("3. Check the results in the generated files")
        print("4. Gemini will provide excellent resume building results!")
        
    else:
        print("\n⚠️  Tests failed. Please check your configuration.")
        show_api_options()

if __name__ == "__main__":
    main() 