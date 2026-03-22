"""测试智谱AI LLM配置"""

import os
import sys
from pathlib import Path

# 添加项目路径到 sys.path
sys.path.insert(0, str(Path(__file__).parent))

# 加载环境变量
from dotenv import load_dotenv
load_dotenv()

from hello_agents import HelloAgentsLLM


def test_llm_config():
    """测试LLM配置是否正确"""
    print("=" * 50)
    print("测试智谱AI LLM配置")
    print("=" * 50)

    # 显示当前环境变量配置
    print("\n📋 当前环境变量配置:")
    print(f"  LLM_MODEL_ID:  {os.getenv('LLM_MODEL_ID')}")
    print(f"  LLM_API_KEY:   {os.getenv('LLM_API_KEY', '')[:20]}...")
    print(f"  LLM_BASE_URL:  {os.getenv('LLM_BASE_URL')}")

    try:
        # 初始化LLM
        print("\n🔄 正在初始化LLM...")
        llm = HelloAgentsLLM()
        print(f"  ✅ 提供商: {llm.provider}")
        print(f"  ✅ 模型: {llm.model}")

        # 测试简单调用
        print("\n🔄 测试简单对话...")
        messages = [{"role": "user", "content": "请用一句话介绍你自己"}]
        response = llm.invoke(messages)
        print(f"  ✅ 响应: {response}")

        # 测试Agent能力
        print("\n🔄 测试Agent工具调用能力...")
        from hello_agents.agents.simple_agent import SimpleAgent

        agent = SimpleAgent(
            name="test_agent",
            llm=llm,
            system_prompt="你是一个帮助用户规划行程的助手，请简洁回答。"
        )

        # 测试简单任务
        result = agent.run("帮我推荐北京的两个著名景点")
        print(f"  ✅ Agent响应成功: {result[:100]}...")

        print("\n" + "=" * 50)
        print("✅ 所有测试通过！智谱AI配置可以正常使用")
        print("=" * 50)
        return True

    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = test_llm_config()
    sys.exit(0 if success else 1)
