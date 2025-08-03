import os
from crewai import LLM

def get_huggingface_deepseek_llm():
    """
    Configure LLM using Hugging Face router with DeepSeek-V3-0324 - EXCELLENT for resume building.
    """
    return LLM(
        model="huggingface/deepseek-ai/DeepSeek-V3-0324:novita",  # Add huggingface/ prefix for LiteLLM
        api_key=os.getenv("HUGGINGFACE_API_KEY"),
        base_url="https://router.huggingface.co/v1",
        temperature=0.7
    )

def get_huggingface_llm():
    """
    Configure LLM using Hugging Face Inference API - CONFIRMED FREE.
    """
    models = [
        "gpt2",
        "distilgpt2", 
        "microsoft/DialoGPT-small",
        "EleutherAI/gpt-neo-125M"
    ]
    
    return LLM(
        model=models[0],  # Use first model as primary
        api_key=os.getenv("HUGGINGFACE_API_KEY"),
        base_url="https://api-inference.huggingface.co/models/",
        temperature=0.7
    )

def get_huggingface_specialized():
    """
    Configure LLM using specialized FREE Hugging Face models for different tasks.
    """
    task_models = {
        "writing": "microsoft/DialoGPT-small",
        "general": "gpt2",
        "creative": "distilgpt2"
    }
    
    return LLM(
        model=task_models["writing"],  # Best for resume writing
        api_key=os.getenv("HUGGINGFACE_API_KEY"),
        base_url="https://api-inference.huggingface.co/models/",
        temperature=0.7
    )

def get_ollama_llm():
    """
    Configure LLM using local Ollama - FREE local models.
    """
    return LLM(
        model="ollama/mistral",
        base_url="http://localhost:11434",
        temperature=0.7
    )

def get_mock_llm():
    """
    Configure Mock LLM for testing - completely FREE.
    """
    return LLM(
        model="mock",
        temperature=0.7
    )

def get_llm_config():
    """
    Get the best available LLM configuration.
    Prioritizes Hugging Face with DeepSeek-V3, then other free options.
    """
    print("🔍 Looking for available LLM options...")
    
    # 1. Try Hugging Face with DeepSeek-V3 (EXCELLENT for resume building)
    if os.getenv("HUGGINGFACE_API_KEY"):
        try:
            print("✅ Using Hugging Face with DeepSeek-V3 (EXCELLENT for resume building)...")
            return get_huggingface_deepseek_llm()
        except Exception as e:
            print(f"⚠️  DeepSeek-V3 failed: {e}")
            try:
                print("🔄 Trying other Hugging Face models...")
                return get_huggingface_llm()
            except Exception as e2:
                print(f"⚠️  Hugging Face failed: {e2}")
                try:
                    print("🔄 Trying specialized FREE Hugging Face models...")
                    return get_huggingface_specialized()
                except Exception as e3:
                    print(f"⚠️  Specialized FREE Hugging Face models failed: {e3}")
    
    # 2. Try local Ollama with FREE models
    try:
        print("✅ Using local Ollama with FREE models...")
        return get_ollama_llm()
    except Exception as e:
        print(f"⚠️  Ollama failed: {e}")
    
    # 3. Fallback to Mock LLM (completely FREE)
    print("🆓 Using Mock LLM for testing (completely free)")
    return get_mock_llm()

def get_model_recommendations():
    """
    Get recommendations for different resume building tasks.
    """
    recommendations = {
        "resume_writing": {
            "best": "huggingface/deepseek-ai/DeepSeek-V3-0324:novita" if os.getenv("HUGGINGFACE_API_KEY") else "microsoft/DialoGPT-small",
            "reason": "Excellent for professional writing and content creation",
            "alternative": "gpt2"
        },
        "job_analysis": {
            "best": "huggingface/deepseek-ai/DeepSeek-V3-0324:novita" if os.getenv("HUGGINGFACE_API_KEY") else "gpt2",
            "reason": "Strong at understanding job requirements and matching skills",
            "alternative": "distilgpt2"
        },
        "ats_optimization": {
            "best": "huggingface/deepseek-ai/DeepSeek-V3-0324:novita" if os.getenv("HUGGINGFACE_API_KEY") else "microsoft/DialoGPT-small",
            "reason": "Good at keyword matching and ATS-friendly formatting",
            "alternative": "EleutherAI/gpt-neo-125M"
        },
        "skill_analysis": {
            "best": "huggingface/deepseek-ai/DeepSeek-V3-0324:novita" if os.getenv("HUGGINGFACE_API_KEY") else "gpt2",
            "reason": "Effective at analyzing and categorizing skills",
            "alternative": "distilgpt2"
        },
        "cover_letter_writing": {
            "best": "huggingface/deepseek-ai/DeepSeek-V3-0324:novita" if os.getenv("HUGGINGFACE_API_KEY") else "microsoft/DialoGPT-small",
            "reason": "Excellent for persuasive writing and professional tone",
            "alternative": "gpt2"
        }
    }
    
    return recommendations 